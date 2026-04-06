const fs = require('fs');
const path = 'second-brain-ai/frontend/src/store/useAppStore.ts';
let code = fs.readFileSync(path, 'utf8');

const target = `  quickCapture: async (content: string) => {
    try {
      const API_BASE = import.meta.env.VITE_API_BASE_URL || '/api';
      const response = await fetch(\`\${API_BASE}/notes/quick-capture\`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
        body: JSON.stringify({ content })
      });
      if (response.ok) {
        set({ toast: { id: Date.now(), tone: 'success', text: '灵感已捕获。' } });
        void get().loadInitialData();
      }
    } catch (error) {
      console.error('Quick capture failed:', error);
    }
  },`;

const replacement = `  quickCapture: async (content: string) => {
    try {
      const API_BASE = import.meta.env.VITE_API_BASE_URL || '/api';
      const response = await fetch(\`\${API_BASE}/notes/quick-capture\`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...getAuthHeaders() },
        body: JSON.stringify({ content })
      });
      if (response.ok) {
        const data = await response.json();
        
        set((state) => {
          const newNote = data.note;
          const updatedNotes = [newNote, ...state.notes];
          
          const updatedUserStats = state.userStats 
            ? { ...state.userStats, exp: data.current_exp, level: data.current_level }
            : null;

          // 缓存更新
          setCachedData(STORE_NOTES, updatedNotes);

          return { 
            notes: updatedNotes,
            userStats: updatedUserStats,
            recentNoteIds: [newNote.id, ...state.recentNoteIds].slice(0, 8),
            toast: { id: Date.now(), tone: 'success', text: \`灵感已捕获！+\${data.exp_gained} EXP\` }
          };
        });
      }
    } catch (error) {
      console.error('Quick capture failed:', error);
    }
  },`;

code = code.replace(target, replacement);
fs.writeFileSync(path, code);
