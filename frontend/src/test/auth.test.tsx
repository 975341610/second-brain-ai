import { describe, it, expect, beforeEach, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import App from '../pages/App';
import { ThemeProvider } from '../components/ThemeEngine';

// 模拟 API 和 Store
vi.mock('../lib/api', () => ({
  api: {
    getSystemVersion: vi.fn().mockResolvedValue({ version: '1.0.0' }),
    listNotes: vi.fn().mockResolvedValue([]),
    listNotebooks: vi.fn().mockResolvedValue([]),
    getTrash: vi.fn().mockResolvedValue({ notes: [], notebooks: [] }),
    listTasks: vi.fn().mockResolvedValue([]),
    getModelConfig: vi.fn().mockResolvedValue({}),
  }
}));

const renderWithTheme = (ui: React.ReactElement) => {
  return render(<ThemeProvider>{ui}</ThemeProvider>);
};

describe('Auth Integration', () => {
  beforeEach(() => {
    localStorage.clear();
    vi.clearAllMocks();
  });

  it('未认证时显示登录页面', () => {
    renderWithTheme(<App />);
    expect(screen.getByText('需要访问密钥')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('输入密钥...')).toBeInTheDocument();
  });

  it('输入密钥并登录后显示主界面', async () => {
    renderWithTheme(<App />);
    
    const input = screen.getByPlaceholderText('输入密钥...');
    const button = screen.getByText('进入系统');

    fireEvent.change(input, { target: { value: 'test-token' } });
    fireEvent.click(button);

    // 登录后 localStorage 应该有 token
    expect(localStorage.getItem('access_token')).toBe('test-token');
    
    // 应该显示主界面元素（例如 Sidebar 中的“搜索笔记”或类似内容）
    // 注意：由于异步加载，可能需要 waitFor，但 App 内部状态切换是同步的
    expect(screen.queryByText('需要访问密钥')).not.toBeInTheDocument();
  });

  it('已保存密钥时直接进入主界面', () => {
    localStorage.setItem('access_token', 'valid-token');
    renderWithTheme(<App />);
    expect(screen.queryByText('需要访问密钥')).not.toBeInTheDocument();
  });
});
