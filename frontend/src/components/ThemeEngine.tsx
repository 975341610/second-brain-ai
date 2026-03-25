import React, { createContext, useContext, useEffect, ReactNode } from 'react';
import { useAppStore } from '../store/useAppStore';

interface ThemeContextType {
  theme: string;
  setTheme: (theme: string) => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const { userStats, updateUserTheme } = useAppStore();
  const currentTheme = userStats?.current_theme || 'default';

  useEffect(() => {
    // 动态应用主题属性到 body
    document.body.setAttribute('data-theme', currentTheme);
    
    // 如果是默认主题，移除属性以便使用 :root 变量
    if (currentTheme === 'default') {
      document.body.removeAttribute('data-theme');
    }
  }, [currentTheme]);

  const setTheme = (theme: string) => {
    void updateUserTheme(theme);
  };

  return (
    <ThemeContext.Provider value={{ theme: currentTheme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};
