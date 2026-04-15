import { Database, Settings2, Folder, RefreshCw, Terminal, CheckCircle2, AlertTriangle, ShieldCheck, Image as ImageIcon, Upload, Palette, Trash2, Check, Cpu, Sliders, Blinds } from 'lucide-react';
import { useEffect, useState, useRef, ChangeEvent } from 'react';
import type { ModelConfig } from '../lib/types';
import { api } from '../lib/api';
import { useAppStore } from '../store/useAppStore';
import { wallpaperStore } from '../lib/wallpaperStore';

type SettingsPanelProps = {
  modelConfig: ModelConfig;
  onUpdateModelConfig: (payload: ModelConfig) => Promise<void>;
};

export function SettingsPanel({ modelConfig, onUpdateModelConfig }: SettingsPanelProps) {
  const { userStats, updateUserWallpaper, updateUserTheme, aiPluginEnabled, setAIPluginEnabled, panelSettings, updatePanelSettings } = useAppStore();
  const [config, setConfig] = useState(modelConfig);
  const [isCheckingHardware, setIsCheckingHardware] = useState(false);
  const [hwInfo, setHwInfo] = useState<{ compatible: boolean; memory_gb: number; cpu_count: number; os: string; message: string } | null>(null);
  const [dataPath, setDataPath] = useState('');
  const [accessToken, setAccessToken] = useState(() => localStorage.getItem('access_token') || '');
  const [logs, setLogs] = useState<string[]>([]);
  const [isUpdating, setIsUpdating] = useState(false);
  const [updateStatus, setUpdateStatus] = useState<'idle' | 'checking' | 'up-to-date' | 'pending' | 'updating' | 'success' | 'error'>('idle');
  const [updateOutput, setUpdateOutput] = useState('');
  const [isUploadingWallpaper, setIsUploadingWallpaper] = useState(false);
  const [savedWallpapers, setSavedWallpapers] = useState<any[]>([]);
  const [wallpaperPreviews, setWallpaperPreviews] = useState<Record<string, string>>({});
  const logContainerRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const checkHardware = async () => {
    setIsCheckingHardware(true);
    try {
      const res = await api.checkHardware();
      setHwInfo(res);
      return res;
    } catch (e: any) {
      alert('硬件检测失败: ' + e.message);
      return null;
    } finally {
      setIsCheckingHardware(false);
    }
  };

  const handleToggleAIPlugin = async () => {
    const nextState = !aiPluginEnabled;
    if (nextState) {
      const hw = await checkHardware();
      if (!hw || !hw.compatible) {
        return; // 不开启
      }
    }
    try {
      await setAIPluginEnabled(nextState);
    } catch (e) {
      // Error handled by store toast
    }
  };

  const themes = [
    { id: 'default', name: '默认 (Reflect)', color: 'bg-[#fcfbf9]' },
    { id: 'dark', name: '深色模式', color: 'bg-[#1a1a1a]' },
  ];

  // 加载已保存壁纸列表
  const loadWallpapers = async () => {
    try {
      const list = await wallpaperStore.listWallpapers();
      setSavedWallpapers(list);
      
      // 生成预览
      const previews: Record<string, string> = {};
      for (const wp of list) {
        const result = await wallpaperStore.resolveIdbUrl(`idb://${wp.id}`);
        if (result) {
          previews[wp.id] = typeof result === 'object' ? result.url : result;
        }
      }
      setWallpaperPreviews(previews);
    } catch (e) {
      console.error('Failed to load wallpapers', e);
    }
  };

  useEffect(() => {
    loadWallpapers();
  }, []);

  useEffect(() => {
    setConfig(modelConfig);
  }, [modelConfig]);

  // 定期拉取日志
  useEffect(() => {
    const fetchLogs = async () => {
      try {
        const res = await api.getSystemLogs();
        if (res.logs.length > 0) {
          setLogs(prev => [...prev, ...res.logs].slice(-500));
        }
      } catch (e) {
        console.error('Failed to fetch logs', e);
      }
    };
    const timer = setInterval(fetchLogs, 2000);
    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    if (logContainerRef.current) {
      logContainerRef.current.scrollTop = logContainerRef.current.scrollHeight;
    }
  }, [logs]);

  const handleCheck = async () => {
    setIsUpdating(true);
    setUpdateStatus('checking');
    setUpdateOutput('');
    try {
      const res = await api.checkUpdate();
      setUpdateOutput(res.output);
      setUpdateStatus(res.status as any);
    } catch (e: any) {
      setUpdateOutput(e.message);
      setUpdateStatus('error');
    } finally {
      setIsUpdating(false);
    }
  };

  const handlePerformUpdate = async () => {
    setIsUpdating(true);
    setUpdateStatus('updating');
    try {
      const res = await api.performUpdate();
      setUpdateOutput(res.output);
      setUpdateStatus(res.status === 'ok' ? 'success' : 'error');
    } catch (e: any) {
      setUpdateOutput(e.message);
      setUpdateStatus('error');
    } finally {
      setIsUpdating(false);
    }
  };

  const handleRestart = async () => {
    try {
      await api.restartApp();
      alert('应用正在通过 fast_update.bat 重启并更新，请稍候...');
    } catch (e: any) {
      alert('重启失败: ' + e.message);
    }
  };

  const handleSwitchDataPath = async () => {
    if (!dataPath) return;
    try {
      const res = await api.switchDataPath(dataPath);
      alert(res.message);
    } catch (e: any) {
      alert('切换路径失败: ' + e.message);
    }
  };

  const handleUpdateAccessToken = () => {
    localStorage.setItem('access_token', accessToken);
    alert('本地访问密钥已更新。请确保它与后端配置一致。');
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    window.dispatchEvent(new CustomEvent('unauthorized'));
  };

  const handleWallpaperChange = async (e: ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsUploadingWallpaper(true);
    try {
      const id = `wp-${Date.now()}`;
      const buffer = await file.arrayBuffer();
      const idbUrl = await wallpaperStore.setWallpaper(id, buffer, file.type, file.name);
      await updateUserWallpaper(idbUrl);
      await loadWallpapers();
    } catch (err: any) {
      alert('壁纸上传失败: ' + err.message);
    } finally {
      setIsUploadingWallpaper(false);
    }
  };

  const clearWallpaper = async () => {
    await updateUserWallpaper('');
  };

  const deleteWallpaper = async (id: string) => {
    if (!confirm('确定要删除这张壁纸吗？')) return;
    try {
      await wallpaperStore.deleteWallpaper(id);
      if (userStats?.wallpaper_url === `idb://${id}`) {
        await updateUserWallpaper('');
      }
      await loadWallpapers();
    } catch (e: any) {
      alert('删除失败: ' + e.message);
    }
  };

  return (
    <section className="space-y-6">
      <div className="rounded-[28px] border border-white/50 bg-[rgba(255,252,247,0.88)] p-6 shadow-soft backdrop-blur">
        <div className="mb-6 flex items-center gap-3">
          <div className="rounded-2xl bg-stone-900 p-3 text-white"><Settings2 size={18} /></div>
          <div>
            <div className="text-lg font-medium text-stone-900">设置</div>
            <div className="text-sm text-stone-500">在这里统一管理模型、导入和工作区设置。</div>
          </div>
        </div>
        
        <div className="grid gap-6 xl:grid-cols-2">
          {/* 模型设置 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center gap-2 text-sm font-medium text-stone-500"><Database size={16} /> 模型设置</div>
            <div className="space-y-3">
              <input value={config.provider} onChange={(e) => setConfig({ ...config, provider: e.target.value })} className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" placeholder="服务商" />
              <input value={config.model_name} onChange={(e) => setConfig({ ...config, model_name: e.target.value })} className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" placeholder="模型名称" />
              <input value={config.base_url} onChange={(e) => setConfig({ ...config, base_url: e.target.value })} className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" placeholder="接口地址 (需包含 /v1)" />
              <input value={config.api_key} onChange={(e) => setConfig({ ...config, api_key: e.target.value })} className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" placeholder="API Key" />
              <button onClick={() => onUpdateModelConfig(config)} className="w-full rounded-2xl bg-stone-900 px-4 py-3 text-sm font-medium text-white hover:bg-stone-800 transition-colors">保存设置</button>
            </div>
          </div>

          {/* 本地 AI 引擎 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center justify-between">
              <div className="flex items-center gap-2 text-sm font-medium text-stone-500"><Cpu size={16} /> 本地 AI 引擎</div>
              <div className={`text-[10px] px-2 py-0.5 rounded-full font-bold ${aiPluginEnabled ? 'bg-green-100 text-green-700' : 'bg-stone-100 text-stone-400'}`}>
                {aiPluginEnabled ? 'RUNNING' : 'OFF'}
              </div>
            </div>
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div className="pr-4">
                  <div className="text-sm font-medium text-stone-700">启用本地 Llama 引擎</div>
                  <div className="text-[11px] text-stone-400 leading-tight mt-0.5">使用本地硬件推理，保护隐私且无需联网。</div>
                </div>
                <button
                  onClick={handleToggleAIPlugin}
                  disabled={isCheckingHardware}
                  className={`relative inline-flex h-6 w-11 flex-shrink-0 items-center rounded-full transition-colors focus:outline-none ${
                    aiPluginEnabled ? 'bg-stone-900' : 'bg-stone-200'
                  }`}
                >
                  <span
                    className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                      aiPluginEnabled ? 'translate-x-6' : 'translate-x-1'
                    }`}
                  />
                </button>
              </div>
              
              {hwInfo && (
                <div className="rounded-xl bg-stone-50 p-3 text-[11px] text-stone-500 space-y-1 border border-stone-100">
                   <div className="flex justify-between"><span>系统架构:</span> <span className="font-mono text-stone-700">{hwInfo.os} ({hwInfo.cpu_count} Cores)</span></div>
                   <div className="flex justify-between"><span>可用内存:</span> <span className="font-mono text-stone-700">{hwInfo.memory_gb} GB</span></div>
                   <div className="flex justify-between"><span>硬件兼容:</span> <span className={hwInfo.compatible ? 'text-green-600 font-bold' : 'text-rose-600 font-bold'}>{hwInfo.compatible ? '通过' : '未通过'}</span></div>
                   {!hwInfo.compatible && <div className="text-rose-500 mt-1 font-medium">{hwInfo.message}</div>}
                </div>
              )}
              
              {!hwInfo && (
                 <button 
                   onClick={checkHardware}
                   disabled={isCheckingHardware}
                   className="w-full py-2 border border-dashed border-stone-300 rounded-xl text-xs text-stone-500 hover:bg-stone-50 transition-colors flex items-center justify-center gap-2"
                 >
                   {isCheckingHardware ? <RefreshCw size={12} className="animate-spin" /> : null}
                   {isCheckingHardware ? '正在检测...' : '检查硬件兼容性'}
                 </button>
              )}
            </div>
          </div>

          {/* 外观与主题 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center gap-2 text-sm font-medium text-stone-500"><Palette size={16} /> 主题与外观</div>
            <div className="space-y-4">
              <div className="grid grid-cols-2 gap-2">
                {themes.map((t) => (
                  <button
                    key={t.id}
                    onClick={() => updateUserTheme(t.id)}
                    className={`flex items-center gap-3 rounded-2xl border p-3 transition-all ${
                      userStats?.current_theme === t.id
                        ? 'border-stone-900 bg-stone-50 ring-1 ring-stone-900'
                        : 'border-stone-100 hover:border-stone-300'
                    }`}
                  >
                    <div className={`h-4 w-4 rounded-full ${t.color}`} />
                    <span className="text-xs font-medium text-stone-700">{t.name}</span>
                  </button>
                ))}
              </div>
              
              <div className="h-px bg-stone-100 my-2" />
              
              <div className="space-y-3">
                <div className="text-xs text-stone-400 mb-1 flex items-center gap-2">
                  <ImageIcon size={14} /> 壁纸库 (Gallery)
                </div>
                
                {savedWallpapers.length > 0 && (
                  <div className="grid grid-cols-3 gap-2 mb-3">
                    {savedWallpapers.map((wp) => (
                      <div key={wp.id} className="group relative aspect-video rounded-xl overflow-hidden border border-stone-100 hover:border-stone-300 transition-all">
                        {wp.type.startsWith('video') ? (
                          <video src={wallpaperPreviews[wp.id]} className="w-full h-full object-cover" />
                        ) : (
                          <img src={wallpaperPreviews[wp.id]} className="w-full h-full object-cover" />
                        )}
                        <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-2">
                          <button 
                            onClick={() => updateUserWallpaper(`idb://${wp.id}`)}
                            className="p-1.5 bg-white rounded-full text-stone-900 hover:scale-110 transition-transform"
                            title="应用"
                          >
                            <Check size={14} />
                          </button>
                          <button 
                            onClick={() => deleteWallpaper(wp.id)}
                            className="p-1.5 bg-white rounded-full text-rose-600 hover:scale-110 transition-transform"
                            title="删除"
                          >
                            <Trash2 size={14} />
                          </button>
                        </div>
                        {userStats?.wallpaper_url === `idb://${wp.id}` && (
                          <div className="absolute top-1 right-1 bg-stone-900 text-white rounded-full p-0.5">
                            <Check size={8} />
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                )}

                <input 
                  type="file" 
                  ref={fileInputRef} 
                  onChange={handleWallpaperChange} 
                  className="hidden" 
                  accept="image/*,video/*"
                />
                <div className="flex gap-2">
                  <button 
                    onClick={() => fileInputRef.current?.click()} 
                    disabled={isUploadingWallpaper}
                    className="flex-1 flex items-center justify-center gap-2 rounded-2xl bg-stone-900 px-4 py-3 text-sm font-medium text-white hover:bg-stone-800 transition-colors disabled:opacity-50"
                  >
                    <Upload size={14} />
                    {isUploadingWallpaper ? '上传中...' : '上传壁纸'}
                  </button>
                  {userStats?.wallpaper_url && (
                    <button 
                      onClick={clearWallpaper}
                      className="rounded-2xl border border-rose-200 px-4 py-3 text-sm font-medium text-rose-600 hover:bg-rose-50 transition-colors"
                    >
                      清除当前壁纸
                    </button>
                  )}
                </div>
                <div className="text-[11px] text-stone-400 leading-relaxed italic">
                  * 壁纸支持 MP4, WEBP, PNG。大视频将保存在本地。
                </div>
              </div>
            </div>
          </div>

          {/* 面板外观自定义 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center gap-2 text-sm font-medium text-stone-500"><Sliders size={16} /> 面板外观自定义</div>
            <div className="space-y-6">
              {[
                { id: 'slashMenu', name: 'Slash 菜单 (/)' },
                { id: 'textMenu', name: '文字菜单 (Bubble)' },
                { id: 'blockMenu', name: '块菜单 (DragHandle)' }
              ].map((panel) => (
                <div key={panel.id} className="space-y-3">
                  <div className="text-xs font-bold text-stone-400 uppercase tracking-wider">{panel.name}</div>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="space-y-1">
                      <label className="text-[10px] text-stone-500">背景颜色</label>
                      <div className="flex items-center gap-2">
                        <input 
                          type="color" 
                          value={panelSettings[panel.id as keyof typeof panelSettings].background} 
                          onChange={(e) => updatePanelSettings({ [panel.id]: { background: e.target.value } })}
                          className="h-8 w-8 rounded cursor-pointer border-none bg-transparent"
                        />
                        <input 
                          type="text" 
                          value={panelSettings[panel.id as keyof typeof panelSettings].background} 
                          onChange={(e) => updatePanelSettings({ [panel.id]: { background: e.target.value } })}
                          className="flex-1 text-[10px] font-mono border border-stone-100 rounded px-2 py-1"
                        />
                      </div>
                    </div>
                    <div className="space-y-1">
                      <label className="text-[10px] text-stone-500">边框颜色</label>
                      <div className="flex items-center gap-2">
                        <input 
                          type="color" 
                          value={panelSettings[panel.id as keyof typeof panelSettings].border} 
                          onChange={(e) => updatePanelSettings({ [panel.id]: { border: e.target.value } })}
                          className="h-8 w-8 rounded cursor-pointer border-none bg-transparent"
                        />
                        <input 
                          type="text" 
                          value={panelSettings[panel.id as keyof typeof panelSettings].border} 
                          onChange={(e) => updatePanelSettings({ [panel.id]: { border: e.target.value } })}
                          className="flex-1 text-[10px] font-mono border border-stone-100 rounded px-2 py-1"
                        />
                      </div>
                    </div>
                  </div>
                  <div className="grid grid-cols-2 gap-4">
                    <div className="space-y-1">
                      <div className="flex justify-between">
                        <label className="text-[10px] text-stone-500">透明度</label>
                        <span className="text-[10px] font-mono text-stone-400">{Math.round(panelSettings[panel.id as keyof typeof panelSettings].opacity * 100)}%</span>
                      </div>
                      <input 
                        type="range" min="0" max="1" step="0.01"
                        value={panelSettings[panel.id as keyof typeof panelSettings].opacity} 
                        onChange={(e) => updatePanelSettings({ [panel.id]: { opacity: parseFloat(e.target.value) } })}
                        className="w-full h-1 bg-stone-100 rounded-lg appearance-none cursor-pointer accent-stone-900"
                      />
                    </div>
                    <div className="space-y-1">
                      <div className="flex justify-between">
                        <label className="text-[10px] text-stone-500">模糊度 (Blur)</label>
                        <span className="text-[10px] font-mono text-stone-400">{panelSettings[panel.id as keyof typeof panelSettings].blur}px</span>
                      </div>
                      <input 
                        type="range" min="0" max="40" step="1"
                        value={panelSettings[panel.id as keyof typeof panelSettings].blur} 
                        onChange={(e) => updatePanelSettings({ [panel.id]: { blur: parseInt(e.target.value) } })}
                        className="w-full h-1 bg-stone-100 rounded-lg appearance-none cursor-pointer accent-stone-900"
                      />
                    </div>
                  </div>
                </div>
              ))}
              <div className="text-[11px] text-stone-400 leading-relaxed italic mt-2 border-t border-stone-50 pt-3">
                * 设置将实时预览并自动保存。毛玻璃效果在深色模式或有背景图时更明显。
              </div>
            </div>
          </div>

          {/* 数据存储设置 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center gap-2 text-sm font-medium text-stone-500"><Folder size={16} /> 数据存储</div>
            <div className="space-y-3">
              <div className="text-xs text-stone-400 mb-1">选择数据存储路径</div>
              <input 
                value={dataPath} 
                onChange={(e) => setDataPath(e.target.value)} 
                className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" 
                placeholder="例如: D:\SecondBrainData" 
              />
              <button 
                onClick={handleSwitchDataPath} 
                className="w-full rounded-2xl border border-stone-900 px-4 py-3 text-sm font-medium text-stone-900 hover:bg-stone-50 transition-colors"
              >
                应用
              </button>
              <div className="text-[11px] text-stone-400 leading-relaxed italic">
                * 切换成功后请重启软件生效。
              </div>
            </div>
          </div>

          {/* 访问密钥设置 */}
          <div className="rounded-[24px] bg-white/85 p-5">
            <div className="mb-3 flex items-center gap-2 text-sm font-medium text-stone-500"><ShieldCheck size={16} /> 访问控制</div>
            <div className="space-y-3">
              <div className="text-xs text-stone-400 mb-1">本地 Access Token</div>
              <input 
                type="password"
                value={accessToken} 
                onChange={(e) => setAccessToken(e.target.value)} 
                className="w-full rounded-2xl border border-stone-200 px-3 py-2 text-sm" 
                placeholder="输入密钥" 
              />
              <div className="flex gap-2">
                <button 
                  onClick={handleUpdateAccessToken} 
                  className="flex-1 rounded-2xl bg-stone-900 px-4 py-3 text-sm font-medium text-white hover:bg-stone-800 transition-colors"
                >
                  更新密钥
                </button>
                <button 
                  onClick={handleLogout} 
                  className="rounded-2xl border border-rose-200 px-4 py-3 text-sm font-medium text-rose-600 hover:bg-rose-50 transition-colors"
                >
                  退出登录
                </button>
              </div>
              <div className="text-[11px] text-stone-400 leading-relaxed italic">
                * 修改此处仅更新浏览器存储的密钥，后端验证密钥需在 .env 或 backend/config.py 中配置。
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* 系统日志与更新 */}
      <div className="rounded-[28px] border border-white/50 bg-[rgba(255,252,247,0.88)] p-6 shadow-soft backdrop-blur">
        <div className="mb-6 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="rounded-2xl bg-stone-900 p-3 text-white"><Terminal size={18} /></div>
            <div>
              <div className="text-lg font-medium text-stone-900">系统日志与更新</div>
              <div className="text-sm text-stone-500">查看运行状态并获取最新功能。</div>
            </div>
          </div>
          
          <div className="flex gap-2">
            <button 
              onClick={handleCheck} 
              disabled={isUpdating}
              className="flex items-center gap-2 rounded-2xl bg-stone-100 px-4 py-2 text-sm font-medium text-stone-700 hover:bg-stone-200 transition-all disabled:opacity-50"
            >
              <RefreshCw size={14} className={isUpdating && updateStatus === 'checking' ? 'animate-spin' : ''} />
              {isUpdating && updateStatus === 'checking' ? '检查中...' : '检查更新'}
            </button>
            
            {/* 发现新版本 → 显示确认更新按钮 */}
            {updateStatus === 'pending' && (
              <button 
                onClick={handlePerformUpdate} 
                disabled={isUpdating}
                className="flex items-center gap-2 rounded-2xl bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 transition-all disabled:opacity-50"
              >
                <RefreshCw size={14} className={isUpdating ? 'animate-spin' : ''} />
                {isUpdating ? '更新中...' : '确认更新'}
              </button>
            )}
            
            {/* 更新成功 → 显示重启按钮 */}
            {updateStatus === 'success' && (
              <button 
                onClick={handleRestart} 
                className="flex items-center gap-2 rounded-2xl bg-green-600 px-4 py-2 text-sm font-medium text-white hover:bg-green-700 transition-all"
              >
                <CheckCircle2 size={14} />
                重启并应用
              </button>
            )}
          </div>
        </div>

        <div className="space-y-4">
          {updateStatus !== 'idle' && updateOutput && (
            <div className={`rounded-2xl p-4 text-xs font-mono whitespace-pre-wrap ${
              updateStatus === 'error' ? 'bg-red-50 text-red-600' : 
              updateStatus === 'up-to-date' ? 'bg-green-50 text-green-700' :
              updateStatus === 'pending' ? 'bg-blue-50 text-blue-700' :
              'bg-stone-50 text-stone-600'
            }`}>
              <div className="mb-2 font-bold flex items-center gap-2">
                {updateStatus === 'error' ? <AlertTriangle size={12} /> : <CheckCircle2 size={12} />}
                {updateStatus === 'up-to-date' ? '已是最新版本' : 
                 updateStatus === 'pending' ? '发现新版本' :
                 updateStatus === 'success' ? '更新成功' : 
                 updateStatus === 'error' ? '操作失败' : 'Update Result:'}
              </div>
              {updateOutput}
            </div>
          )}

          <div 
            ref={logContainerRef}
            className="h-64 overflow-y-auto rounded-[24px] bg-stone-900 p-4 font-mono text-xs text-stone-300 shadow-inner scroll-smooth"
          >
            <div className="space-y-1">
              {logs.map((log, i) => (
                <div key={i} className="opacity-90">{log}</div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
