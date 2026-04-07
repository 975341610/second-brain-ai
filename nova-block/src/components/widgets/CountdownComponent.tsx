import React, { useEffect, useMemo, useState } from 'react';
import { NodeViewWrapper } from '@tiptap/react';
import { differenceInSeconds, isValid, parseISO } from 'date-fns';

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

function safeParseISO(v: string): Date | null {
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

  const target = useMemo(() => safeParseISO(node?.attrs?.targetDate), [node?.attrs?.targetDate]);
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    const t = window.setInterval(() => setNow(Date.now()), 250);
    return () => window.clearInterval(t);
  }, []);

  const diff = useMemo(() => {
    if (!target) return 0;
    return differenceInSeconds(target, new Date(now));
  }, [target, now]);

  const { days, hours, minutes, seconds, isOver } = useMemo(() => {
    const s = Math.max(0, diff);
    const days = Math.floor(s / 86400);
    const hours = Math.floor((s % 86400) / 3600);
    const minutes = Math.floor((s % 3600) / 60);
    const seconds = s % 60;
    return { days, hours, minutes, seconds, isOver: diff <= 0 };
  }, [diff]);

  const title = node?.attrs?.title ?? '倒计时';

  return (
    <NodeViewWrapper
      className={`my-4 rounded-3xl border ${morandi.border} ${morandi.bg} shadow-soft overflow-hidden select-none ${selected ? 'ring-2 ring-black/10' : ''}`}
      data-drag-handle
    >
      <div className="p-5 md:p-6">
        <div className="flex items-start justify-between gap-4">
          <div className="min-w-0">
            <div className={`text-sm font-semibold tracking-wide ${morandi.text}`}>{title}</div>
            <div className={`mt-1 text-xs ${morandi.subtle}`}>
              {target ? (
                <>目标：{target.toLocaleString()}</>
              ) : (
                <>目标日期无效，请在右侧面板重新设置</>
              )}
            </div>
          </div>

          <div className="flex items-center gap-2">
            <span className={`px-2.5 py-1 rounded-full text-[11px] font-semibold border ${morandi.border} ${morandi.card} ${morandi.subtle}`}>
              {isOver ? '已到达' : '进行中'}
            </span>
            <span className={`w-2.5 h-2.5 rounded-full ${isOver ? morandi.accent2 : morandi.accent}`} />
          </div>
        </div>

        <div className="mt-5 grid grid-cols-4 gap-2 md:gap-3">
          {[
            { label: '天', value: String(days) },
            { label: '小时', value: pad2(hours) },
            { label: '分', value: pad2(minutes) },
            { label: '秒', value: pad2(seconds) },
          ].map((it) => (
            <div
              key={it.label}
              className={`rounded-2xl border ${morandi.border} ${morandi.card} backdrop-blur-xl px-3 py-3 md:px-4 md:py-4 flex flex-col items-center justify-center`}
            >
              <div className={`text-2xl md:text-3xl font-black tabular-nums ${morandi.text}`}>{it.value}</div>
              <div className={`mt-1 text-[11px] font-semibold tracking-widest ${morandi.subtle}`}>{it.label}</div>
            </div>
          ))}
        </div>

        {isEditable && (
          <div className="mt-4 rounded-2xl border border-dashed border-black/10 bg-white/40 px-4 py-3">
            <div className="text-[11px] font-semibold text-black/40 tracking-widest">快速设置</div>
            <div className="mt-2 flex flex-wrap gap-2">
              {[1, 3, 7, 30].map((d) => (
                <button
                  key={d}
                  onClick={() => {
                    const next = new Date(Date.now() + d * 86400 * 1000).toISOString();
                    updateAttributes({ targetDate: next });
                  }}
                  className="px-3 py-1.5 rounded-full text-xs font-semibold border border-black/10 bg-white/60 hover:bg-white transition-colors"
                  type="button"
                >
                  {d} 天后
                </button>
              ))}
              <button
                onClick={() => {
                  const v = window.prompt('请输入目标日期（ISO 或 YYYY-MM-DDTHH:mm:ss）：', node?.attrs?.targetDate);
                  if (v) {
                    const next = safeParseISO(v) ? parseISO(v).toISOString() : v;
                    updateAttributes({ targetDate: next });
                  }
                }}
                className="px-3 py-1.5 rounded-full text-xs font-semibold border border-black/10 bg-white/60 hover:bg-white transition-colors"
                type="button"
              >
                输入…
              </button>
            </div>
          </div>
        )}
      </div>
    </NodeViewWrapper>
  );
};
