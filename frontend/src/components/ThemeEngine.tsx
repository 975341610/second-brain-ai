import React, { createContext, useContext, useEffect, ReactNode } from 'react';
import { useAppStore } from '../store/useAppStore';

interface ThemeContextType {
  theme: string;
  setTheme: (theme: string) => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const { userStats, updateUserTheme, panelSettings } = useAppStore();
  const currentTheme = userStats?.current_theme || 'default';

  useEffect(() => {
    // 动态应用主题属性到 body
    document.body.setAttribute('data-theme', currentTheme);
    
    // 如果是默认主题，移除属性以便使用 :root 变量
    if (currentTheme === 'default') {
      document.body.removeAttribute('data-theme');
    }
  }, [currentTheme]);

  useEffect(() => {
    // 动态应用面板设置到 CSS 变量
    const root = document.documentElement;
    
    // Slash Menu
    root.style.setProperty('--slash-menu-bg', panelSettings.slashMenu.background);
    root.style.setProperty('--slash-menu-blur', `${panelSettings.slashMenu.blur}px`);
    root.style.setProperty('--slash-menu-border', panelSettings.slashMenu.border);
    root.style.setProperty('--slash-menu-opacity', panelSettings.slashMenu.opacity.toString());

    // Text Menu
    root.style.setProperty('--text-menu-bg', panelSettings.textMenu.background);
    root.style.setProperty('--text-menu-blur', `${panelSettings.textMenu.blur}px`);
    root.style.setProperty('--text-menu-border', panelSettings.textMenu.border);
    root.style.setProperty('--text-menu-opacity', panelSettings.textMenu.opacity.toString());

    // Block Menu
    root.style.setProperty('--block-menu-bg', panelSettings.blockMenu.background);
    root.style.setProperty('--block-menu-blur', `${panelSettings.blockMenu.blur}px`);
    root.style.setProperty('--block-menu-border', panelSettings.blockMenu.border);
    root.style.setProperty('--block-menu-opacity', panelSettings.blockMenu.opacity.toString());
  }, [panelSettings]);

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
