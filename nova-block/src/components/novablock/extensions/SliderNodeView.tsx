import React, { useState, useEffect, useCallback, useRef } from 'react';
import { NodeViewWrapper } from '@tiptap/react';
import { Settings, ChevronLeft, ChevronRight, Plus, X, Trash2, Upload, Image as ImageIcon, AlertCircle } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

const Toggle = ({ checked, onChange, label }: { checked: boolean; onChange: (v: boolean) => void; label: string }) => (
  <label className="flex items-center justify-between gap-4 cursor-pointer group">
    <span className="text-sm font-medium text-gray-600 group-hover:text-gray-900 transition-colors">{label}</span>
    <div
      onClick={() => onChange(!checked)}
      className={`relative w-10 h-5 rounded-full transition-colors duration-200 ease-in-out ${
        checked ? 'bg-blue-500' : 'bg-gray-200'
      }`}
    >
      <motion.div
        animate={{ x: checked ? 20 : 2 }}
        initial={false}
        className="absolute top-1 w-3 h-3 bg-white rounded-full shadow-sm"
      />
    </div>
  </label>
);

export const SliderNodeView: React.FC<any> = ({ node, updateAttributes }) => {
  const images = Array.isArray(node.attrs.images) ? node.attrs.images : [];
  const { autoPlay, showDots, showArrows, visibleCount = 5 } = node.attrs;
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [newImageUrl, setNewImageUrl] = useState('');
  const [failedImages, setFailedImages] = useState<Set<number>>(new Set());
  const wheelTimeout = useRef<any>(null);

  const nextSlide = useCallback(() => {
    if (images.length === 0) return;
    setCurrentIndex((prev) => (prev + 1) % images.length);
  }, [images.length]);

  const prevSlide = useCallback(() => {
    if (images.length === 0) return;
    setCurrentIndex((prev) => (prev - 1 + images.length) % images.length);
  }, [images.length]);

  useEffect(() => {
    if (autoPlay && images.length > 1 && !isSettingsOpen) {
      const interval = setInterval(nextSlide, 3000);
      return () => clearInterval(interval);
    }
  }, [autoPlay, images.length, nextSlide, isSettingsOpen]);

  const handleWheel = (e: React.WheelEvent) => {
    e.preventDefault();
    if (wheelTimeout.current) return;

    if (e.deltaY > 0) {
      nextSlide();
    } else if (e.deltaY < 0) {
      prevSlide();
    }

    wheelTimeout.current = setTimeout(() => {
      wheelTimeout.current = null;
    }, 300);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files) return;

    const newImages = [...images];
    let loadedCount = 0;

    Array.from(files).forEach((file) => {
      const reader = new FileReader();
      reader.onload = (event) => {
        if (event.target?.result) {
          newImages.push(event.target.result as string);
          loadedCount++;
          if (loadedCount === files.length) {
            updateAttributes({ images: newImages });
          }
        }
      };
      reader.readAsDataURL(file);
    });
  };

  const addImage = () => {
    if (newImageUrl.trim()) {
      updateAttributes({
        images: [...images, newImageUrl.trim()],
      });
      setNewImageUrl('');
    }
  };

  const removeImage = (index: number) => {
    const newImages = images.filter((_: any, i: number) => i !== index);
    updateAttributes({ images: newImages });
    setFailedImages((prev) => {
      const next = new Set(prev);
      next.delete(index);
      return next;
    });
    if (currentIndex >= newImages.length && newImages.length > 0) {
      setCurrentIndex(newImages.length - 1);
    } else if (newImages.length === 0) {
      setCurrentIndex(0);
    }
  };

  const renderCoverflow = () => {
    return (
      <div 
        className="relative w-full h-full flex items-center justify-center overflow-hidden"
        onWheel={handleWheel}
      >
        <AnimatePresence initial={false}>
          {images.map((url: string, index: number) => {
            let diff = index - currentIndex;
            
            // Handle wrap-around diff for smoother transitions
            if (diff > images.length / 2) diff -= images.length;
            if (diff < -images.length / 2) diff += images.length;

            const absDiff = Math.abs(diff);
            const isVisible = absDiff <= Math.floor(visibleCount / 2);

            if (!isVisible) return null;

            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, scale: 0.5, x: diff * 100 }}
                animate={{
                  opacity: 1,
                  scale: 1 - absDiff * 0.15,
                  x: `${diff * 40}%`,
                  zIndex: 50 - absDiff,
                  filter: `brightness(${1 - absDiff * 0.2}) blur(${absDiff * 1}px)`,
                }}
                exit={{ opacity: 0, scale: 0.5 }}
                transition={{ type: 'spring', stiffness: 300, damping: 30 }}
                className="absolute w-2/3 aspect-video rounded-xl shadow-2xl overflow-hidden bg-gray-200 border border-white/20 cursor-pointer"
                onClick={() => setCurrentIndex(index)}
              >
                {failedImages.has(index) ? (
                  <div className="w-full h-full flex flex-col items-center justify-center bg-gray-100 text-gray-400">
                    <AlertCircle size={48} className="mb-2" />
                    <span className="text-sm">图片加载失败</span>
                  </div>
                ) : (
                  <img
                    src={url}
                    alt={`Slide ${index + 1}`}
                    className="w-full h-full object-cover"
                    onError={() => setFailedImages((prev) => new Set(prev).add(index))}
                  />
                )}
              </motion.div>
            );
          })}
        </AnimatePresence>

        {showArrows && images.length > 1 && (
          <>
            <button
              onClick={(e) => { e.stopPropagation(); prevSlide(); }}
              className="absolute left-4 z-[100] p-3 bg-white/10 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-all border border-white/20"
            >
              <ChevronLeft size={24} />
            </button>
            <button
              onClick={(e) => { e.stopPropagation(); nextSlide(); }}
              className="absolute right-4 z-[100] p-3 bg-white/10 hover:bg-white/20 backdrop-blur-md rounded-full text-white transition-all border border-white/20"
            >
              <ChevronRight size={24} />
            </button>
          </>
        )}
      </div>
    );
  };

  return (
    <NodeViewWrapper className="slider-node my-8 relative group select-none">
      <div className="relative w-full aspect-[21/9] bg-slate-900 rounded-2xl overflow-hidden shadow-2xl border border-slate-800">
        {images.length > 0 ? (
          renderCoverflow()
        ) : (
          <div className="w-full h-full flex flex-col items-center justify-center text-slate-500 bg-slate-950 border-2 border-dashed border-slate-800 rounded-2xl m-1">
            <div className="p-4 bg-slate-900 rounded-full mb-4">
              <Plus size={48} className="text-slate-400" />
            </div>
            <p className="font-medium text-lg">开启 Coverflow 画廊之旅</p>
            <p className="text-sm opacity-60">点击右上角设置图标上传或添加图片</p>
          </div>
        )}

        <button
          onClick={() => setIsSettingsOpen(!isSettingsOpen)}
          className="absolute top-4 right-4 z-[110] p-2 bg-slate-800/80 hover:bg-slate-700 backdrop-blur-md rounded-xl shadow-lg text-slate-200 border border-slate-700 transition-all opacity-0 group-hover:opacity-100"
        >
          <Settings size={20} />
        </button>
      </div>

      <AnimatePresence>
        {isSettingsOpen && (
          <motion.div
            initial={{ opacity: 0, y: 10, scale: 0.95 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: 10, scale: 0.95 }}
            className="absolute top-full left-0 right-0 mt-4 z-[120] p-6 bg-white border border-gray-200 rounded-2xl shadow-2xl overflow-hidden"
          >
            <div className="flex justify-between items-center mb-6">
              <div>
                <h3 className="text-lg font-bold text-gray-900">Slider 设置面板</h3>
                <p className="text-sm text-gray-500">定制您的 2.5D Coverflow 画廊体验</p>
              </div>
              <button onClick={() => setIsSettingsOpen(false)} className="p-2 hover:bg-gray-100 rounded-full transition-colors">
                <X size={20} className="text-gray-400" />
              </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="space-y-6">
                <div className="space-y-4">
                  <h4 className="text-sm font-semibold text-gray-400 uppercase tracking-wider">交互配置</h4>
                  <div className="bg-gray-50 p-4 rounded-xl space-y-4">
                    <Toggle label="自动轮播" checked={autoPlay} onChange={(v) => updateAttributes({ autoPlay: v })} />
                    <Toggle label="显示分页指示器" checked={showDots} onChange={(v) => updateAttributes({ showDots: v })} />
                    <Toggle label="显示侧边导航" checked={showArrows} onChange={(v) => updateAttributes({ showArrows: v })} />
                  </div>
                </div>

                <div className="space-y-4">
                  <h4 className="text-sm font-semibold text-gray-400 uppercase tracking-wider">布局配置</h4>
                  <div className="bg-gray-50 p-4 rounded-xl">
                    <label className="block text-sm font-medium text-gray-600 mb-2">可见层级数量: {visibleCount}</label>
                    <input
                      type="range"
                      min="3"
                      max="9"
                      step="2"
                      value={visibleCount}
                      onChange={(e) => updateAttributes({ visibleCount: parseInt(e.target.value) })}
                      className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-blue-500"
                    />
                    <div className="flex justify-between text-[10px] text-gray-400 mt-2">
                      <span>精简 (3)</span>
                      <span>标准 (5)</span>
                      <span>丰富 (9)</span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="space-y-4">
                <h4 className="text-sm font-semibold text-gray-400 uppercase tracking-wider">媒体管理</h4>
                
                <div className="flex gap-2">
                  <div className="relative flex-1">
                    <input
                      type="text"
                      value={newImageUrl}
                      onChange={(e) => setNewImageUrl(e.target.value)}
                      placeholder="输入图片链接..."
                      className="w-full pl-4 pr-10 py-2.5 bg-gray-50 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all"
                      onKeyDown={(e) => e.key === 'Enter' && addImage()}
                    />
                    <ImageIcon size={16} className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400" />
                  </div>
                  <button
                    onClick={addImage}
                    className="px-4 py-2 bg-blue-600 text-white rounded-xl text-sm font-medium hover:bg-blue-700 shadow-lg shadow-blue-200 transition-all flex items-center gap-2"
                  >
                    <Plus size={18} />
                  </button>
                </div>

                <div className="relative">
                  <input
                    type="file"
                    multiple
                    accept="image/*"
                    onChange={handleFileUpload}
                    className="hidden"
                    id="slider-file-upload"
                  />
                  <label
                    htmlFor="slider-file-upload"
                    className="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-200 rounded-xl hover:border-blue-400 hover:bg-blue-50 cursor-pointer transition-all group"
                  >
                    <Upload size={24} className="text-gray-400 group-hover:text-blue-500 mb-2" />
                    <span className="text-sm font-medium text-gray-600 group-hover:text-blue-600">本地多选上传</span>
                    <span className="text-xs text-gray-400 mt-1">支持拖拽或点击</span>
                  </label>
                </div>

                {images.length > 0 && (
                  <div className="pt-2">
                    <div className="flex justify-between items-center mb-2">
                      <span className="text-sm font-medium text-gray-700">队列清单 ({images.length})</span>
                      <button 
                        onClick={() => updateAttributes({ images: [] })}
                        className="text-xs text-red-500 hover:underline"
                      >
                        清空全部
                      </button>
                    </div>
                    <div className="grid grid-cols-4 gap-2 max-h-[160px] overflow-y-auto p-1 pr-2">
                      {images.map((url: string, index: number) => (
                        <div key={index} className="relative aspect-square group/item rounded-lg overflow-hidden border border-gray-100 shadow-sm bg-gray-50">
                          <img src={url} alt="" className="w-full h-full object-cover" />
                          <button
                            onClick={() => removeImage(index)}
                            className="absolute inset-0 bg-black/40 flex items-center justify-center opacity-0 group-hover/item:opacity-100 transition-opacity"
                          >
                            <Trash2 size={16} className="text-white" />
                          </button>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </NodeViewWrapper>
  );
};

