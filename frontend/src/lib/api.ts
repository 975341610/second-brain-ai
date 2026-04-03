import type { 
  AskResponse, 
  ModelConfig, 
  Note, 
  Notebook, 
  NoteProperty, 
  Task, 
  TrashState, 
  UserStats,
  UserAchievement,
} from './types';


declare global {
  interface Window {
    electron?: {
      ipcInvoke: (channel: string, ...args: any[]) => Promise<any>;
    };
  }
}

// Helper to call IPC or fallback to fetch
async function invoke<T>(channel: string, path: string, options?: any): Promise<T> {
  if (window.electron?.ipcInvoke) {
    // 📂 彻底切换到 Electron IPC 进行本地直接 CRUD
    // 坚决不使用 fetch 向本地 Python 后端发起 HTTP 请求
    try {
      const payload = options?.body ? JSON.parse(options.body) : options?.params || options;
      return await window.electron.ipcInvoke(channel, payload);
    } catch (e) {
      console.error(`IPC call to ${channel} failed:`, e);
      throw e; // 在 Electron 环境下，IPC 失败就不再回退到 fetch，防止违反离线优先原则
    }
  }
  
  // Fallback to FastAPI REST API (only if electron is not available, e.g. web preview)
  const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765/api';
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options?.headers as Record<string, string> || {}),
  };
  const response = await fetch(`${API_BASE}${path}`, {
    ...options,
    headers,
  });
  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || 'Request failed');
  }
  return response.json() as Promise<T>;
}

export const api = {
  listNotes: () => invoke<Note[]>('notes:list', '/notes'),
  listNotebooks: () => invoke<Notebook[]>('notebooks:list', '/notebooks'),
  createNotebook: (payload: { name: string; icon?: string }) => 
    invoke<Notebook>('notebooks:create', '/notebooks', { method: 'POST', body: JSON.stringify(payload) }),
  updateNotebook: (notebookId: number, payload: { name?: string; icon?: string }) =>
    invoke<Notebook>('notebooks:update', `/notebooks/${notebookId}`, { params: { id: notebookId, ...payload } }),
  deleteNotebook: (notebookId: number) => invoke('notebooks:delete', `/notebooks/${notebookId}`, { params: { id: notebookId } }),
  restoreNotebook: (notebookId: number) => invoke<Notebook>('notebooks:restore', `/notebooks/${notebookId}/restore`, { params: { id: notebookId } }),
  purgeNotebook: (notebookId: number) => invoke('notebooks:purge', `/notebooks/${notebookId}/purge`, { params: { id: notebookId } }),
  createNote: (payload: { title: string; content: string; notebook_id?: number | null; icon?: string; parent_id?: number | null; is_title_manually_edited?: boolean; tags?: string[] }) =>
    invoke<Note>('notes:create', '/notes', { method: 'POST', body: JSON.stringify(payload) }),
  updateNote: (noteId: number, payload: { title?: string; content?: string; icon?: string; parent_id?: number | null; is_title_manually_edited?: boolean; tags?: string[] }) =>
    invoke<Note>('notes:update', `/notes/${noteId}`, { params: { id: noteId, ...payload } }),
  updateNoteTags: (noteId: number, tags: string[]) =>
    invoke<Note>('notes:update-tags', `/notes/${noteId}/tags`, { params: { id: noteId, tags } }),
  moveNote: (noteId: number, payload: { notebook_id?: number | null; position: number; parent_id?: number | null }) =>
    invoke<Note>('notes:move', `/notes/${noteId}/move`, { params: { id: noteId, ...payload } }),
  bulkMoveNotes: (payload: { note_ids: number[]; notebook_id?: number | null; position: number; parent_id?: number | null }) =>
    invoke<{ notes: Note[] }>('notes:bulk-move', '/notes/bulk-move', { method: 'POST', body: JSON.stringify(payload) }),
  bulkDeleteNotes: (payload: { note_ids: number[]; position?: number }) =>
    invoke<{ notes: Note[] }>('notes:bulk-delete', '/notes/bulk-delete', { method: 'POST', body: JSON.stringify(payload) }),
  deleteNote: (noteId: number) => invoke('notes:delete', `/notes/${noteId}`, { params: { id: noteId } }),
  listNotesFiltered: (propertyName: string, propertyValue: string) => 
    invoke<Note[]>('notes:list-filtered', `/notes?property_name=${encodeURIComponent(propertyName)}&property_value=${encodeURIComponent(propertyValue)}`, { params: { propertyName, propertyValue } }),
  restoreNote: (noteId: number) => invoke<Note>('notes:restore', `/notes/${noteId}/restore`, { params: { id: noteId } }),
  purgeNote: (noteId: number) => invoke('notes:purge', `/notes/${noteId}/purge`, { params: { id: noteId } }),
  purgeTrash: () => invoke('trash:purge', '/trash/purge'),
  getTrash: () => invoke<TrashState>('trash:get', '/trash'),
  listTasks: () => invoke<Task[]>('tasks:list', '/tasks'),
  createTask: (payload: { title: string; status?: string; priority?: string; task_type?: string; deadline?: string | null }) =>
    invoke<Task>('tasks:create', '/tasks', { method: 'POST', body: JSON.stringify(payload) }),
  updateTask: (taskId: number, payload: { title?: string; status?: string; priority?: string; task_type?: string; deadline?: string | null }) =>
    invoke<Task>('tasks:update', `/tasks/${taskId}`, { params: { id: taskId, ...payload } }),
  deleteTask: (taskId: number) => invoke('tasks:delete', `/tasks/${taskId}`, { params: { id: taskId } }),
  clearCompletedTasks: () => invoke('tasks:clear-completed', '/tasks/clear-completed'),
  ask: (payload: { question: string; mode: 'chat' | 'rag' | 'agent' }) =>
    invoke<AskResponse>('ai:ask', '/ask', { method: 'POST', body: JSON.stringify(payload) }),
  streamInlineAI: async (payload: { prompt: string; context: string; action: string }, onChunk: (chunk: string) => void) => {
    if (window.electron?.ipcInvoke) {
      return window.electron.ipcInvoke('ai:stream-inline', payload, (chunk: string) => onChunk(chunk));
    }
    const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765/api';
    const response = await fetch(`${API_BASE}/inline-ai`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error(await response.text());
    const reader = response.body?.getReader();
    if (!reader) return;
    const decoder = new TextDecoder();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      onChunk(decoder.decode(value, { stream: true }));
    }
  },
  getModelConfig: () => invoke<ModelConfig>('config:get-model', '/model-config'),
  updateModelConfig: (payload: ModelConfig) =>
    invoke<ModelConfig>('config:update-model', '/model-config', { method: 'POST', body: JSON.stringify(payload) }),
  
  // Streaming AI and File uploads still use network requests (or we can wrap them later)
  // For now, these are less critical than CRUD saving
  streamChat: async (payload: { question: string; mode: string }, onChunk: (chunk: string) => void) => {
    if (window.electron?.ipcInvoke) {
      // Use IPC for streaming if implemented
      try {
        await window.electron.ipcInvoke('ai:stream-chat', payload, (chunk: string) => onChunk(chunk));
        return;
      } catch (e) {
        console.warn('IPC streaming failed, falling back to fetch', e);
      }
    }
    const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765/api';
    const response = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    });
    if (!response.ok) throw new Error(await response.text());
    const reader = response.body?.getReader();
    if (!reader) return;
    const decoder = new TextDecoder();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      onChunk(decoder.decode(value, { stream: true }));
    }
  },
  upload: async (files: File[]) => {
    // Upload is complex via IPC without proper encoding, keep it for now or implement as FS copy
    const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765/api';
    const formData = new FormData();
    files.forEach((file) => formData.append('files', file));
    const response = await fetch(`${API_BASE}/upload`, { method: 'POST', body: formData });
    if (!response.ok) throw new Error(await response.text());
    return response.json();
  },
  getUserStats: () => invoke<UserStats>('user:get-stats', '/user/stats'),
  listUserAchievements: () => invoke<UserAchievement[]>('user:list-achievements', '/user/achievements'),
  updateUserTheme: (theme: string) => invoke<UserStats>('user:update-theme', '/user/theme', { params: { theme } }),
  updateUserWallpaper: (wallpaperUrl: string) => invoke<UserStats>('user:update-wallpaper', '/user/wallpaper', { params: { wallpaper_url: wallpaperUrl } }),
  listBgm: () => invoke<string[]>('bgm:list', '/bgm/list'),
  getBgmStreamUrl: (filename: string) => {
    const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8765/api';
    return `${API_BASE}/bgm/stream/${encodeURIComponent(filename)}`;
  },
  getSystemVersion: () => invoke<{ version: string; git_commit?: string; build_time?: string; executable?: string }>('system:version', '/system/version'),
};
