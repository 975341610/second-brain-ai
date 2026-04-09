import React, { useState, useEffect, useCallback, useRef } from 'react';
import { NodeViewWrapper, NodeViewProps } from '@tiptap/react';
import { Settings, ChevronLeft, ChevronRight, Plus, X, Trash2, Upload, Image as ImageIcon, AlertCircle } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

// 高级 Switch 组件
const Switch: React.FC<{ checked: boolean; onChange: (checked: boolean) => void; label: string }> = ({ checked, onChange, label }) => {
  return (
    <div className="flex items-center justify-between gap-3 cursor-pointer group" onClick={() => onChange(!checked)}>
      <span className="text-sm font-medium text-zinc-600 group-hover:text-zinc-900 transition-colors">{label}</span>
      <div 
        className={`relative w-10 h-5.5 rounded-full transition-colors duration-200 flex items-center px-0.5 ${
          checked ? 'bg-zinc-900' : 'bg-zinc-200'
        }`}
      >
        <motion.div
          animate={{ x: checked ? 18 : 0 }}
          transition={{ type: "spring", stiffness: 500, damping: 30 }}
          className="w-4.5 h-4.5 bg-white rounded-full shadow-sm"
        />
      </div>
    </div>
  );
};

export const SliderNodeView: React.FC<NodeViewProps> = ({ node, updateAttributes }) => {
  const { images, autoPlay, showDots, showArrows, visibleCount = 5 } = node.attrs;
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [newImageUrl, setNewImageUrl] = useState('');
  const [failedImages, setFailedImages] = useState<Record<number, boolean>>({});
  const fileInputRef = useRef<HTMLInputElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const wheelTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const nextSlide = useCallback(() => {
    if (images.length === 0) return;
    setCurrentIndex((prev) => (prev + 1) % images.length);
  }, [images.length]);

  const prevSlide = useCallback(() => {
    if (images.length === 0) return;
    setCurrentIndex((prev) => (prev - 1 + images.length) % images.length);
  }, [images.length]);

  // 处理滚轮事件
  useEffect(() => {
    const handleWheel = (e: WheelEvent) => {
      e.preventDefault();
      
      if (wheelTimeoutRef.current) return;

      if (e.deltaY > 0) {
        nextSlide();
      } else if (e.deltaY < 0) {
        prevSlide();
      }

      wheelTimeoutRef.current = setTimeout(() => {
        wheelTimeoutRef.current = null;
      }, 300); // 300ms 节流锁
    };

    const container = containerRef.current;
    if (container) {
      container.addEventListener('wheel', handleWheel, { passive: false });
    }

    return () => {
      if (container) {
        container.removeEventListener('wheel', handleWheel);
      }
      if (wheelTimeoutRef.current) {
        clearTimeout(wheelTimeoutRef.current);
      }
    };
  }, [nextSlide, prevSlide]);

  useEffect(() => {
    if (autoPlay && images.length > 1 && !isSettingsOpen) {
      const interval = setInterval(nextSlide, 3000);
      return () => clearInterval(interval);
    }
  }, [autoPlay, images.length, nextSlide, isSettingsOpen]);

  const addImage = () => {
    if (newImageUrl.trim()) {
      updateAttributes({
        images: [...images, newImageUrl.trim()],
      });
      setNewImageUrl('');
    }
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files) return;

    Array.from(files).forEach(file => {
      const reader = new FileReader();
      reader.onload = (event) => {
        const base64 = event.target?.result as string;
        if (base64) {
          updateAttributes({
            images: [...(node.attrs.images || []), base64]
          });
        }
      };
      reader.readAsDataURL(file);
    });
    
    // 清空 input 方便下次选择
    if (fileInputRef.current) fileInputRef.current.value = '';
  };

  const removeImage = (index: number) => {
    const newImages = images.filter((_: any, i: number) => i !== index);
    updateAttributes({ images: newImages });
    
    // 清除该索引的错误标记（由于索引变化，简单处理为重新加载时重新判断）
    setFailedImages({});
    
    if (currentIndex >= newImages.length && newImages.length > 0) {
      setCurrentIndex(newImages.length - 1);
    } else if (newImages.length === 0) {
      setCurrentIndex(0);
    }
  };

  return (
    <NodeViewWrapper className="slider-node my-10 relative group">
      <div 
        ref={containerRef}
        className="relative w-full aspect-[21/9] flex items-center justify-center overflow-hidden"
      >
        {images.length > 0 ? (
          <div className="relative w-full h-full flex items-center justify-center">
            {images.map((url: string, index: number) => {
              // 处理环形逻辑的 diff
              let diff = index - currentIndex;
              const len = images.length;
              
              // 寻找最短路径
              if (diff > len / 2) diff -= len;
              if (diff < -len / 2) diff += len;

              const isVisible = Math.abs(diff) <= Math.floor(visibleCount / 2);
              
              return (
                <motion.div
                  key={index}
                  style={{
                    zIndex: 50 - Math.abs(diff),
                    position: 'absolute',
                  }}
                  initial={false}
                  animate={{
                    x: diff * 45 + '%', // 平移量
                    scale: 1 - Math.abs(diff) * 0.15, // 缩放
                    opacity: isVisible ? 1 : 0,
                    pointerEvents: index === currentIndex ? 'auto' : 'none',
                  }}
                  transition={{
                    type: "spring",
                    stiffness: 260,
                    damping: 20
                  }}
                  className="w-1/2 aspect-video rounded-2xl overflow-hidden shadow-2xl border border-white/20"
                >
                  {failedImages[index] ? (
                    <div className="w-full h-full flex flex-col items-center justify-center bg-zinc-100 text-zinc-400 gap-2">
                      <AlertCircle size={40} className="stroke-[1.5]" />
                      <span className="text-sm font-medium">图片加载失败</span>
                    </div>
                  ) : (
                    <img
                      src={url}
                      alt={`Slide ${index + 1}`}
                      className="w-full h-full object-cover select-none"
                      onError={() => setFailedImages(prev => ({ ...prev, [index]: true }))}
                    />
                  )}
                  {/* 倒影或遮罩效果增强景深 */}
                  {index !== currentIndex && (
                    <div className="absolute inset-0 bg-black/20 transition-opacity duration-300" />
                  )}
                </motion.div>
              );
            })}
            
            {showArrows && images.length > 1 && (
              <>
                <button
                  onClick={prevSlide}
                  className="absolute left-8 z-[100] p-3 bg-white/90 hover:bg-white rounded-full shadow-xl text-zinc-800 transition-all opacity-0 group-hover:opacity-100 border border-zinc-100 hover:scale-110 active:scale-90"
                >
                  <ChevronLeft size={24} />
                </button>
                <button
                  onClick={nextSlide}
                  className="absolute right-8 z-[100] p-3 bg-white/90 hover:bg-white rounded-full shadow-xl text-zinc-800 transition-all opacity-0 group-hover:opacity-100 border border-zinc-100 hover:scale-110 active:scale-90"
                >
                  <ChevronRight size={24} />
                </button>
              </>
            )}

            {showDots && images.length > 1 && (
              <div className="absolute -bottom-10 left-1/2 -translate-x-1/2 flex gap-2 px-4 py-2 bg-zinc-100/50 backdrop-blur-md rounded-full border border-zinc-200/50">
                {images.map((_: any, i: number) => (
                  <button
                    key={i}
                    onClick={() => setCurrentIndex(i)}
                    className={`h-1.5 rounded-full transition-all duration-300 ${
                      i === currentIndex ? 'bg-zinc-800 w-6' : 'bg-zinc-300 hover:bg-zinc-400 w-1.5'
                    }`}
                  />
                ))}
              </div>
            )}
          </div>
        ) : (
          <div className="w-full h-full flex flex-col items-center justify-center text-zinc-400 bg-zinc-50 border-2 border-dashed border-zinc-200/80 m-0 rounded-xl">
            <div className="p-4 bg-white rounded-2xl shadow-sm border border-zinc-100 mb-3">
              <ImageIcon size={40} className="text-zinc-300 stroke-[1.5]" />
            </div>
            <p className="text-sm font-medium text-zinc-500">点击右侧齿轮添加图片轮播 🖼️</p>
          </div>
        )}

        {/* 浮动设置图标 */}
        <button
          onClick={() => setIsSettingsOpen(!isSettingsOpen)}
          className={`absolute top-4 right-4 z-[101] p-2 rounded-lg shadow-sm transition-all border opacity-0 group-hover:opacity-100 ${
            isSettingsOpen 
              ? 'bg-zinc-900 text-white border-zinc-800 scale-100 opacity-100' 
              : 'bg-white/90 text-zinc-600 border-zinc-200 hover:bg-white scale-95 hover:scale-100'
          }`}
        >
          <Settings size={18} />
        </button>
      </div>

      {/* 设置面板 */}
      <AnimatePresence>
        {isSettingsOpen && (
          <motion.div
            initial={{ opacity: 0, y: 10, scale: 0.98 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 10, scale: 0.98 }}
            className="mt-4 p-5 bg-white border border-zinc-200 rounded-xl shadow-[0_20px_50px_rgba(0,0,0,0.1)] z-10"
          >
            <div className="flex justify-between items-center mb-5">
              <div className="flex items-center gap-2">
                <div className="w-1.5 h-1.5 bg-blue-500 rounded-full" />
                <h3 className="font-bold text-zinc-800 tracking-tight">轮播图高级设置</h3>
              </div>
              <button 
                onClick={() => setIsSettingsOpen(false)} 
                className="p-1 text-zinc-400 hover:text-zinc-600 hover:bg-zinc-100 rounded-md transition-colors"
              >
                <X size={18} />
              </button>
            </div>

            <div className="space-y-6">
              {/* 可见数量配置 */}
              <div className="bg-zinc-50/50 p-4 rounded-xl border border-zinc-100">
                <div className="flex justify-between items-center mb-3">
                  <label className="text-xs font-bold text-zinc-400 uppercase tracking-wider">可见图片数量</label>
                  <span className="text-xs font-bold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">{visibleCount} 张</span>
                </div>
                <input
                  type="range"
                  min="3"
                  max="9"
                  step="2"
                  value={visibleCount}
                  onChange={(e) => updateAttributes({ visibleCount: parseInt(e.target.value) })}
                  className="w-full h-1.5 bg-zinc-200 rounded-lg appearance-none cursor-pointer accent-zinc-900"
                />
                <div className="flex justify-between mt-2 px-0.5">
                  <span className="text-[10px] text-zinc-400 font-medium">精简 (3)</span>
                  <span className="text-[10px] text-zinc-400 font-medium">标准 (5)</span>
                  <span className="text-[10px] text-zinc-400 font-medium">宽幅 (9)</span>
                </div>
              </div>

              {/* 图片添加区域 */}
              <div className="space-y-3">
                <label className="block text-xs font-bold text-zinc-400 uppercase tracking-wider">素材添加</label>
                <div className="flex flex-col gap-2">
                  <div className="flex gap-2">
                    <input
                      type="text"
                      value={newImageUrl}
                      onChange={(e) => setNewImageUrl(e.target.value)}
                      placeholder="粘贴图片直链 (URL)..."
                      className="flex-1 px-3 py-2 bg-zinc-50 border border-zinc-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500/50 transition-all"
                      onKeyDown={(e) => e.key === 'Enter' && addImage()}
                    />
                    <button
                      onClick={addImage}
                      className="px-4 py-2 bg-zinc-900 text-white rounded-lg text-sm font-medium hover:bg-zinc-800 transition-all flex items-center gap-1.5 shadow-sm active:scale-95"
                    >
                      <Plus size={16} /> 添加
                    </button>
                  </div>
                  
                  <div className="relative">
                    <input 
                      type="file" 
                      ref={fileInputRef}
                      onChange={handleFileUpload}
                      multiple 
                      accept="image/*" 
                      className="hidden" 
                    />
                    <button
                      onClick={() => fileInputRef.current?.click()}
                      className="w-full py-2.5 bg-white border-2 border-dashed border-zinc-200 rounded-lg text-sm font-medium text-zinc-600 hover:border-zinc-300 hover:bg-zinc-50 transition-all flex items-center justify-center gap-2 group"
                    >
                      <Upload size={16} className="text-zinc-400 group-hover:text-zinc-600 transition-colors" />
                      本地多选上传
                    </button>
                  </div>
                </div>
              </div>

              {/* 交互配置区域 */}
              <div className="bg-zinc-50/50 p-4 rounded-xl border border-zinc-100">
                <label className="block text-xs font-bold text-zinc-400 uppercase tracking-wider mb-3">交互配置</label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-8 gap-y-3">
                  <Switch 
                    checked={autoPlay} 
                    onChange={(val) => updateAttributes({ autoPlay: val })} 
                    label="自动轮播" 
                  />
                  <Switch 
                    checked={showDots} 
                    onChange={(val) => updateAttributes({ showDots: val })} 
                    label="分页导航" 
                  />
                  <Switch 
                    checked={showArrows} 
                    onChange={(val) => updateAttributes({ showArrows: val })} 
                    label="左右箭头" 
                  />
                </div>
              </div>

              {/* 图片列表预览 */}
              {images.length > 0 && (
                <div className="border-t border-zinc-100 pt-4">
                  <div className="flex justify-between items-center mb-3">
                    <label className="text-xs font-bold text-zinc-400 uppercase tracking-wider">图片库 ({images.length})</label>
                  </div>
                  <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 max-h-48 overflow-y-auto pr-1 custom-scrollbar">
                    {images.map((url: string, index: number) => (
                      <div key={index} className="group/item relative aspect-video bg-zinc-100 rounded-lg overflow-hidden border border-zinc-200">
                        <img src={url} alt="" className="w-full h-full object-cover transition-transform group-hover/item:scale-105" />
                        <div className="absolute inset-0 bg-black/20 opacity-0 group-hover/item:opacity-100 transition-opacity flex items-center justify-center">
                          <button
                            onClick={() => removeImage(index)}
                            className="p-1.5 bg-red-500 text-white rounded-full shadow-lg hover:bg-red-600 transform scale-75 group-hover/item:scale-100 transition-all"
                          >
                            <Trash2 size={14} />
                          </button>
                        </div>
                        {url.startsWith('data:') && (
                          <div className="absolute bottom-1 left-1 px-1 bg-white/80 backdrop-blur-sm rounded text-[8px] font-bold text-zinc-500 uppercase">Local</div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </NodeViewWrapper>
  );
};
