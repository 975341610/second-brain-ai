import React, { useEffect, useMemo, useRef, useState } from 'react';
import { NodeViewWrapper } from '@tiptap/react';
import { motion, useAnimation } from 'framer-motion';
import { Upload, Link2, Play, Pause, Volume2 } from 'lucide-react';

const palette = {
  bg: 'bg-[#F6F3EF]',
  card: 'bg-white/70',
  text: 'text-[#2E2A2A]',
  subtle: 'text-[#6E6868]',
  border: 'border-[#E6DFD8]',
};

function formatTime(sec: number) {
  if (!Number.isFinite(sec) || sec < 0) return '0:00';
  const m = Math.floor(sec / 60);
  const s = Math.floor(sec % 60);
  return `${m}:${String(s).padStart(2, '0')}`;
}

export const MusicPlayerComponent: React.FC<any> = (props) => {
  const { editor, node, updateAttributes, selected } = props;
  const isEditable = editor?.isEditable;

  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [duration, setDuration] = useState(0);
  const [current, setCurrent] = useState(0);
  const [volume, setVolume] = useState(0.9);

  const controls = useAnimation();

  const src = node?.attrs?.src || '';
  const title = node?.attrs?.title || '未命名歌曲';
  const artist = node?.attrs?.artist || '未知艺术家';
  const cover = node?.attrs?.cover || '';

  useEffect(() => {
    const a = audioRef.current;
    if (!a) return;

    const onTime = () => setCurrent(a.currentTime || 0);
    const onMeta = () => setDuration(a.duration || 0);
    const onEnd = () => setIsPlaying(false);

    a.addEventListener('timeupdate', onTime);
    a.addEventListener('loadedmetadata', onMeta);
    a.addEventListener('ended', onEnd);
    return () => {
      a.removeEventListener('timeupdate', onTime);
      a.removeEventListener('loadedmetadata', onMeta);
      a.removeEventListener('ended', onEnd);
    };
  }, [src]);

  useEffect(() => {
    const a = audioRef.current;
    if (a) a.volume = volume;
  }, [volume]);

  useEffect(() => {
    if (isPlaying) {
      controls.start({ rotate: 360, transition: { duration: 2.2, ease: 'linear', repeat: Infinity } });
    } else {
      controls.stop();
    }
  }, [isPlaying, controls]);

  const toggle = async () => {
    const a = audioRef.current;
    if (!a) return;

    if (!src) {
      if (isEditable) window.alert('请先设置音频链接或上传音频文件');
      return;
    }

    if (a.paused) {
      try {
        await a.play();
        setIsPlaying(true);
      } catch (e) {
        console.error(e);
        setIsPlaying(false);
      }
    } else {
      a.pause();
      setIsPlaying(false);
    }
  };

  const progress = useMemo(() => {
    if (!duration) return 0;
    return Math.min(1, Math.max(0, current / duration));
  }, [current, duration]);

  return (
    <NodeViewWrapper
      className={`my-5 rounded-3xl border ${palette.border} ${palette.bg} shadow-soft overflow-hidden ${selected ? 'ring-2 ring-black/10' : ''}`}
      data-drag-handle
    >
      <div className="p-5 md:p-6">
        <div className="flex items-start gap-5">
          {/* Vinyl */}
          <div className="relative w-28 h-28 md:w-32 md:h-32 shrink-0">
            <div className="absolute inset-0 rounded-full bg-black/80 shadow-[0_18px_45px_rgba(0,0,0,0.28)]" />
            <motion.div
              animate={controls}
              className="absolute inset-2 rounded-full overflow-hidden"
              style={{
                backgroundImage: cover ? `url(${cover})` : undefined,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
              }}
            >
              <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(0,0,0,0)_0%,rgba(0,0,0,0.25)_45%,rgba(0,0,0,0.65)_100%)]" />
              {/* grooves */}
              <div className="absolute inset-0 opacity-40" style={{
                backgroundImage:
                  'repeating-radial-gradient(circle at center, rgba(255,255,255,0.08) 0px, rgba(255,255,255,0.08) 1px, rgba(0,0,0,0) 5px, rgba(0,0,0,0) 8px)',
              }} />
            </motion.div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-7 h-7 rounded-full bg-[#F6F3EF] border border-black/10" />
            </div>
          </div>

          {/* Info */}
          <div className="flex-1 min-w-0">
            <div className={`text-base md:text-lg font-black tracking-tight ${palette.text} truncate`}>{title}</div>
            <div className={`mt-1 text-sm font-semibold ${palette.subtle} truncate`}>{artist}</div>

            {/* Controls */}
            <div className="mt-4 flex items-center gap-3">
              <button
                type="button"
                onClick={toggle}
                className="h-10 px-4 rounded-full bg-black text-white text-sm font-bold flex items-center gap-2 hover:bg-black/90 transition-colors"
              >
                {isPlaying ? <Pause size={16} /> : <Play size={16} />}
                {isPlaying ? '暂停' : '播放'}
              </button>

              <div className={`flex-1 rounded-full border ${palette.border} ${palette.card} px-3 py-2`}
                onClick={(e) => {
                  const a = audioRef.current;
                  if (!a || !duration) return;
                  const rect = (e.currentTarget as HTMLDivElement).getBoundingClientRect();
                  const x = e.clientX - rect.left;
                  const ratio = Math.min(1, Math.max(0, x / rect.width));
                  a.currentTime = ratio * duration;
                }}
              >
                <div className="relative h-2 rounded-full bg-black/10 overflow-hidden">
                  <div className="absolute inset-y-0 left-0 bg-black/70" style={{ width: `${progress * 100}%` }} />
                </div>
                <div className="mt-1 flex justify-between text-[11px] font-semibold text-black/40 tabular-nums">
                  <span>{formatTime(current)}</span>
                  <span>{formatTime(duration)}</span>
                </div>
              </div>

              <div className="hidden md:flex items-center gap-2">
                <Volume2 size={16} className="text-black/40" />
                <input
                  type="range"
                  min={0}
                  max={1}
                  step={0.01}
                  value={volume}
                  onChange={(e) => setVolume(Number(e.target.value))}
                />
              </div>
            </div>

            {isEditable && (
              <div className="mt-4 rounded-2xl border border-dashed border-black/10 bg-white/40 px-4 py-3">
                <div className="text-[11px] font-semibold text-black/40 tracking-widest">配置</div>
                <div className="mt-2 grid grid-cols-1 md:grid-cols-2 gap-2">
                  <button
                    type="button"
                    className="px-3 py-2 rounded-xl border border-black/10 bg-white/60 hover:bg-white transition-colors text-xs font-semibold flex items-center gap-2"
                    onClick={() => {
                      const v = window.prompt('音频直链 URL（mp3/ogg/wav）：', src);
                      if (v !== null) updateAttributes({ src: v.trim() });
                    }}
                  >
                    <Link2 size={14} /> 设置音频直链
                  </button>

                  <button
                    type="button"
                    className="px-3 py-2 rounded-xl border border-black/10 bg-white/60 hover:bg-white transition-colors text-xs font-semibold flex items-center gap-2"
                    onClick={() => {
                      const v = window.prompt('封面图片 URL：', cover);
                      if (v !== null) updateAttributes({ cover: v.trim() });
                    }}
                  >
                    <Link2 size={14} /> 设置封面
                  </button>

                  <button
                    type="button"
                    className="px-3 py-2 rounded-xl border border-black/10 bg-white/60 hover:bg-white transition-colors text-xs font-semibold flex items-center gap-2"
                    onClick={() => {
                      const v = window.prompt('歌曲名：', title);
                      if (v !== null) updateAttributes({ title: v.trim() || '未命名歌曲' });
                    }}
                  >
                    <Link2 size={14} /> 设置歌曲名
                  </button>

                  <button
                    type="button"
                    className="px-3 py-2 rounded-xl border border-black/10 bg-white/60 hover:bg-white transition-colors text-xs font-semibold flex items-center gap-2"
                    onClick={() => {
                      const v = window.prompt('艺术家：', artist);
                      if (v !== null) updateAttributes({ artist: v.trim() || '未知艺术家' });
                    }}
                  >
                    <Link2 size={14} /> 设置艺术家
                  </button>

                  <label className="md:col-span-2 px-3 py-2 rounded-xl border border-black/10 bg-white/60 text-xs font-semibold flex items-center gap-2 cursor-pointer hover:bg-white transition-colors">
                    <Upload size={14} /> 上传音频文件（本地）
                    <input
                      type="file"
                      accept="audio/*"
                      className="hidden"
                      onChange={(e) => {
                        const f = e.target.files?.[0];
                        if (!f) return;
                        const url = URL.createObjectURL(f);
                        updateAttributes({ src: url, title: node?.attrs?.title || f.name });
                        // note: objectURL 在页面生命周期内有效；如需持久化请走后端 upload（项目已有 FileUpload 扩展）
                      }}
                    />
                  </label>
                </div>

                <div className="mt-2 text-[11px] text-black/40">
                  Tip：直链建议用已上传到可访问的 URL；本地上传仅用于当前页面临时播放。
                </div>
              </div>
            )}
          </div>
        </div>

        <audio ref={audioRef} src={src || undefined} preload="metadata" />
      </div>
    </NodeViewWrapper>
  );
};
