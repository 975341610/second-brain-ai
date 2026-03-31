import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electron', {
  minimize: () => ipcRenderer.send('window-minimize'),
  maximize: () => ipcRenderer.send('window-maximize'),
  unmaximize: () => ipcRenderer.send('window-unmaximize'),
  close: () => ipcRenderer.send('window-close'),
  isMaximized: () => ipcRenderer.invoke('window-is-maximized'),
  checkForUpdate: () => ipcRenderer.invoke('check-for-update'),
  downloadUpdate: () => ipcRenderer.invoke('download-update'),
  installUpdate: () => ipcRenderer.invoke('install-update'),
  installLocalUpdate: () => ipcRenderer.invoke('install-local-update'),
  // Generic IPC invoke for all local operations
  ipcInvoke: (channel: string, ...args: any[]) => ipcRenderer.invoke(channel, ...args),
  // --- SSOT API ---
  watchNote: (noteId: number, path: string) => ipcRenderer.send('ssot:watch-note', { noteId, path }),
  unwatchNote: (noteId: number) => ipcRenderer.send('ssot:unwatch-note', { noteId }),
  on: (channel: string, callback: (...args: any[]) => void) => {
    const subscription = (_event: any, ...args: any[]) => callback(...args);
    ipcRenderer.on(channel, subscription);
    return () => ipcRenderer.removeListener(channel, subscription);
  }
});
