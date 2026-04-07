import React, { useEffect, useMemo, useState } from 'react';
import { NodeViewWrapper } from '@tiptap/react';
import { differenceInSeconds, isValid, parseISO, addDays, addHours, addMinutes, addSeconds, format } from 'date-fns';
import { Settings, Calendar, X, Check } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const morandi = {
  bg: 'bg-[#F6F3EF]',
  card: 'bg-white/70',
  text: 'text-[#3F3A3A]',
  subtle: 'text-[#6E6868]',
  border: 'border-[#E6DFD8]',
  accent: 'bg-[#B7C0C7]',
  accent2: 'bg-[#C7B7BE]',
};

function pad2(n: number) {
  return String(Math.max(0, n)).padStart(2, '0');
}

function safeParseISO(v: string | undefined): Date | null {
  if (!v) return null;
  try {
    const d = parseISO(v);
    return isValid(d) ? d : null;
  } catch {
    return null;
  }
}

export const CountdownComponent: React.FC<any> = (props) => {
  const { editor, node, updateAttributes, selected } = props;
  const isEditable = editor?.isEditable;

  const [now, setNow] = useState(() => Date.now());
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);

  // Settings Temp State
  const [mode, setMode] = useState<'duration' | 'date'>('duration');
  const [duration, setDuration] = useState({ days: '0', hours: '0', minutes: '0', seconds: '0' });
  const [targetDateTime, setTargetDateTime] = useState('');
  const [showBubble, setShowBubble] = useState(node?.attrs?.showBubble ?? false);

  const target = useMemo(() => safeParseISO(node?.attrs?.targetDate), [node?.attrs?.targetDate]);

  useEffect(() => {
    const t = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(t);
  }, []);

  const diff = useMemo(() => {
    if (!target) return 0;
    return differenceInSeconds(target, new Date(now));
  }, [target, now]);

  const { days, hours, minutes, seconds, isOver } = useMemo(() => {
    const s = Math.max(0, diff);
    const d = Math.floor(s / 86400);
    const h = Math.floor((s % 86400) / 3600);
    const m = Math.floor((s % 3600) / 60);
    const sec = s % 60;
    return { days: d, hours: h, minutes: m, seconds: sec, isOver: diff <= 0 };
  }, [diff]);

  const title = node?.attrs?.title ?? '倒计时';

  const handleOpenSettings = () => {
    setIsSettingsOpen(true);
    if (target) {
      setTargetDateTime(format(target, "yyyy-MM-dd'T'HH:mm"));
    } else {
      setTargetDateTime(format(new Date(), "yyyy-MM-dd'T'HH:mm"));
    }
    setDuration({ days: '0', hours: '0', minutes: '0', seconds: '0' });
    setShowBubble(node?.attrs?.showBubble ?? false);
  };

  const handleConfirm = () => {
    let nextDate: Date;
    if (mode === 'duration') {
      nextDate = new Date();
      nextDate = addDays(nextDate, parseInt(duration.days) || 0);
      nextDate = addHours(nextDate, parseInt(duration.hours) || 0);
      nextDate = addMinutes(nextDate, parseInt(duration.minutes) || 0);
      nextDate = addSeconds(nextDate, parseInt(duration.seconds) || 0);
    } else {
      nextDate = parseISO(targetDateTime);
    }

    if (isValid(nextDate)) {
      updateAttributes({
        targetDate: nextDate.toISOString(),
        showBubble: showBubble,
      });
    }
    setIsSettingsOpen(false);
  };

  return (
    <NodeViewWrapper
      className={`my-4 rounded-3xl border ${morandi.border} ${morandi.bg} shadow-soft overflow-hidden select-none ${selected ? 'ring-2 ring-black/10' : ''}`}
      data-drag-handle
    >
      <div className="p-5 md:p-6 relative min-h-[160px]">
        {/* Main Interface */}
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <div className={`text-sm font-black tracking-wide ${morandi.text}`}>{title}</div>
            <div className={`mt-1 text-xs ${morandi.subtle} font-medium opacity-70`}>
              {target ? (
                <>目标：{format(target, 'yyyy-MM-dd HH:mm')}</>
              ) : (
                <>设置一个目标日期或时长</>
              )}
            </div>
          </div>

          <div className="flex items-center gap-3">
            <span className={`px-2.5 py-1 rounded-full text-[10px] font-black border ${morandi.border} ${morandi.card} ${morandi.subtle}`}>
              {isOver ? '已到达' : '进行中'}
            </span>
            {isEditable && (
              <button
                onClick={handleOpenSettings}
                className={`p-1.5 rounded-xl border ${morandi.border} ${morandi.card} hover:bg-white active:scale-95 transition-all shadow-sm cursor-pointer`}
              >
                <Settings size={14} className={morandi.subtle} />
              </button>
            )}
          </div>
        </div>

        <div className="mt-6 grid grid-cols-4 gap-2 md:gap-3">
          {[
            { label: '天', value: String(days) },
            { label: '小时', value: pad2(hours) },
            { label: '分', value: pad2(minutes) },
            { label: '秒', value: pad2(seconds) },
          ].map((it) => (
            <div
              key={it.label}
              className={`rounded-2xl border ${morandi.border} ${morandi.card} backdrop-blur-xl px-2 py-3 md:px-4 md:py-4 flex flex-col items-center justify-center`}
            >
              <div className={`text-2xl md:text-3xl font-black tabular-nums ${morandi.text}`}>{it.value}</div>
              <div className={`mt-1 text-[10px] font-bold tracking-widest ${morandi.subtle} opacity-50 uppercase`}>{it.label}</div>
            </div>
          ))}
        </div>

        {/* Settings Panel Overlay */}
        <AnimatePresence>
          {isSettingsOpen && (
            <motion.div
              initial={{ opacity: 0, y: 10, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 10, scale: 0.98 }}
              className={`absolute inset-0 z-30 p-4 md:p-5 ${morandi.bg} flex flex-col gap-3 rounded-3xl`}
            >
              <div className="flex-1 flex flex-col gap-5 overflow-y-auto">
                <div className="flex flex-col gap-3">
                  {/* Mode Selector */}
                  <div className="flex p-1 bg-black/5 rounded-xl">
                    <button
                      onClick={() => setMode('duration')}
                      className={`flex-1 py-1 rounded-md text-[10px] font-bold transition-all ${mode === 'duration' ? 'bg-white shadow-sm text-[#3F3A3A]' : 'text-[#6E6868]'}`}
                    >
                      输入时长
                    </button>
                    <button
                      onClick={() => setMode('date')}
                      className={`flex-1 py-1 rounded-md text-[10px] font-bold transition-all ${mode === 'date' ? 'bg-white shadow-sm text-[#3F3A3A]' : 'text-[#6E6868]'}`}
                    >
                      具体日期
                    </button>
                  </div>

                  {mode === 'duration' ? (
                    <div className="grid grid-cols-4 gap-2">
                      {[
                        { label: '天', key: 'days' },
                        { label: '时', key: 'hours' },
                        { label: '分', key: 'minutes' },
                        { label: '秒', key: 'seconds' },
                      ].map((f) => (
                        <div key={f.key} className="flex flex-col items-center gap-1">
                          <input
                            type="number"
                            min="0"
                            value={duration[f.key as keyof typeof duration]}
                            onChange={(e) => setDuration({ ...duration, [f.key]: e.target.value })}
                            className={`w-full py-1.5 rounded-xl border-none ${morandi.card} text-center font-black text-sm focus:ring-2 ring-[#B7C0C7] ${morandi.text}`}
                          />
                          <span className={`text-[9px] font-bold ${morandi.subtle}`}>{f.label}</span>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <div className={`flex items-center gap-2 p-2 rounded-xl ${morandi.card} border ${morandi.border}`}>
                      <Calendar size={14} className={morandi.subtle} />
                      <input
                        type="datetime-local"
                        value={targetDateTime}
                        onChange={(e) => setTargetDateTime(e.target.value)}
                        className="flex-1 bg-transparent border-none outline-none text-xs font-bold text-[#3F3A3A] focus:ring-0 px-1 py-0.5"
                      />
                    </div>
                  )}
                </div>

                <div className="flex items-center gap-2 p-2 rounded-xl bg-white/40 mt-1 border border-dashed border-black/10">
                  <input
                    type="checkbox"
                    id="showBubble"
                    checked={showBubble}
                    onChange={(e) => setShowBubble(e.target.checked)}
                    className="w-4 h-4 rounded border-[#E6DFD8] text-[#B7C0C7] focus:ring-[#B7C0C7] cursor-pointer"
                  />
                  <label htmlFor="showBubble" className={`text-[10px] font-bold ${morandi.subtle} cursor-pointer select-none`}>
                    倒计时结束时显示气泡提醒
                  </label>
                </div>
              </div>

              <div className="flex gap-2 justify-end mt-1">
                <button
                  onClick={() => setIsSettingsOpen(false)}
                  title="取消"
                  className="p-2 rounded-xl bg-white border border-[#E6DFD8] text-[#6E6868] hover:bg-gray-50 active:scale-95 transition-all shadow-sm flex items-center justify-center group relative"
                >
                  <X size={14} strokeWidth={3} />
                </button>
                <button
                  onClick={handleConfirm}
                  title="保存"
                  className="p-2 rounded-xl bg-[#B7C0C7] text-white shadow-md shadow-[#B7C0C7]/30 hover:opacity-90 active:scale-95 transition-all flex items-center justify-center group relative"
                >
                  <Check size={14} strokeWidth={3} />
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </NodeViewWrapper>
  );
};
