import { useState } from 'react';
import { Lock, ArrowRight } from 'lucide-react';

interface LoginPageProps {
  onLogin: (token: string) => void;
}

export function LoginPage({ onLogin }: LoginPageProps) {
  const [token, setToken] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!token.trim()) {
      setError('请输入访问密钥');
      return;
    }
    onLogin(token.trim());
  };

  return (
    <div className="min-h-screen bg-reflect-bg flex items-center justify-center p-6">
      <div className="w-full max-w-md rounded-[32px] border border-white/50 bg-[rgba(255,252,247,0.88)] p-8 shadow-soft-lg backdrop-blur animate-in fade-in slide-in-from-bottom-4 duration-500">
        <div className="mb-8 flex flex-col items-center text-center">
          <div className="mb-4 rounded-3xl bg-stone-900 p-4 text-white shadow-soft">
            <Lock size={28} />
          </div>
          <h1 className="text-2xl font-semibold text-stone-900">需要访问密钥</h1>
          <p className="mt-2 text-sm text-stone-500 leading-relaxed">
            为了保护您的第二大脑，请输入预设的访问密钥以继续。
          </p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          <div className="relative">
            <input
              type="password"
              value={token}
              onChange={(e) => {
                setToken(e.target.value);
                setError('');
              }}
              placeholder="输入密钥..."
              className={`w-full rounded-2xl border bg-white/50 px-5 py-4 text-sm transition-all focus:bg-white focus:outline-none focus:ring-2 ${
                error ? 'border-rose-300 focus:ring-rose-100' : 'border-stone-200 focus:ring-stone-100'
              }`}
              autoFocus
            />
            {error && (
              <p className="mt-2 text-xs text-rose-500 font-medium px-1">
                {error}
              </p>
            )}
          </div>

          <button
            type="submit"
            className="group w-full flex items-center justify-center gap-2 rounded-2xl bg-stone-900 py-4 text-sm font-semibold text-white transition-all hover:bg-stone-800 active:scale-[0.98] shadow-soft"
          >
            进入系统
            <ArrowRight size={16} className="transition-transform group-hover:translate-x-1" />
          </button>
        </form>

        <div className="mt-8 text-center">
          <p className="text-[11px] text-stone-400 italic">
            提示：您可以在后端配置文件或环境变量中设置 ACCESS_TOKEN
          </p>
        </div>
      </div>
    </div>
  );
}
