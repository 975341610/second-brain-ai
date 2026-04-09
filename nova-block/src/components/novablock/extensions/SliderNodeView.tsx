import React, { useState, useEffect, useCallback } from 'react';
import { NodeViewWrapper, NodeViewProps } from '@tiptap/react';
import { Settings, ChevronLeft, ChevronRight, Plus, X, Trash2 } from 'lucide-react';

export const SliderNodeView: React.FC<NodeViewProps> = ({ node, updateAttributes }) => {
  const { images, autoPlay, showDots, showArrows } = node.attrs;
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isSettingsOpen, setIsSettingsOpen] = useState(false);
  const [newImageUrl, setNewImageUrl] = useState('');

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
    if (currentIndex >= newImages.length && newImages.length > 0) {
      setCurrentIndex(newImages.length - 1);
    } else if (newImages.length === 0) {
      setCurrentIndex(0);
    }
  };

  return (
    <NodeViewWrapper className="slider-node my-4 relative group">
      <div className="relative w-full aspect-video bg-gray-100 rounded-lg overflow-hidden border border-gray-200 shadow-sm">
        {images.length > 0 ? (
          <div className="w-full h-full relative">
            <img
              src={images[currentIndex]}
              alt={`Slide ${currentIndex + 1}`}
              className="w-full h-full object-cover transition-opacity duration-500"
            />
            
            {showArrows && images.length > 1 && (
              <>
                <button
                  onClick={prevSlide}
                  className="absolute left-2 top-1/2 -translate-y-1/2 p-2 bg-white/80 hover:bg-white rounded-full shadow-md text-gray-800 transition-colors opacity-0 group-hover:opacity-100"
                >
                  <ChevronLeft size={20} />
                </button>
                <button
                  onClick={nextSlide}
                  className="absolute right-2 top-1/2 -translate-y-1/2 p-2 bg-white/80 hover:bg-white rounded-full shadow-md text-gray-800 transition-colors opacity-0 group-hover:opacity-100"
                >
                  <ChevronRight size={20} />
                </button>
              </>
            )}

            {showDots && images.length > 1 && (
              <div className="absolute bottom-4 left-1/2 -translate-x-1/2 flex gap-2">
                {images.map((_: any, i: number) => (
                  <button
                    key={i}
                    onClick={() => setCurrentIndex(i)}
                    className={`w-2 h-2 rounded-full transition-all ${
                      i === currentIndex ? 'bg-white w-4' : 'bg-white/50 hover:bg-white/80'
                    }`}
                  />
                ))}
              </div>
            )}
          </div>
        ) : (
          <div className="w-full h-full flex flex-col items-center justify-center text-gray-400 bg-gray-50 border-2 border-dashed border-gray-200">
            <Plus size={48} className="mb-2 opacity-50" />
            <p>点击设置图标添加图片轮播内容</p>
          </div>
        )}

        {/* 浮动设置图标 */}
        <button
          onClick={() => setIsSettingsOpen(!isSettingsOpen)}
          className="absolute top-2 right-2 p-1.5 bg-white/90 hover:bg-white rounded-md shadow-sm text-gray-600 border border-gray-200 transition-all opacity-0 group-hover:opacity-100"
        >
          <Settings size={18} />
        </button>
      </div>

      {/* 设置面板 */}
      {isSettingsOpen && (
        <div className="mt-3 p-4 bg-white border border-gray-200 rounded-lg shadow-lg animate-in fade-in slide-in-from-top-2">
          <div className="flex justify-between items-center mb-4">
            <h3 className="font-semibold text-gray-800">轮播图设置</h3>
            <button onClick={() => setIsSettingsOpen(false)} className="text-gray-400 hover:text-gray-600">
              <X size={18} />
            </button>
          </div>

          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">添加图片 URL</label>
              <div className="flex gap-2">
                <input
                  type="text"
                  value={newImageUrl}
                  onChange={(e) => setNewImageUrl(e.target.value)}
                  placeholder="粘贴图片链接..."
                  className="flex-1 px-3 py-1.5 border border-gray-300 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                  onKeyDown={(e) => e.key === 'Enter' && addImage()}
                />
                <button
                  onClick={addImage}
                  className="px-3 py-1.5 bg-blue-600 text-white rounded-md text-sm hover:bg-blue-700 transition-colors flex items-center gap-1"
                >
                  <Plus size={16} /> 添加
                </button>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <label className="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={autoPlay}
                  onChange={(e) => updateAttributes({ autoPlay: e.target.checked })}
                  className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <span className="text-sm text-gray-600">自动播放</span>
              </label>
              <label className="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={showDots}
                  onChange={(e) => updateAttributes({ showDots: e.target.checked })}
                  className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <span className="text-sm text-gray-600">显示分页点</span>
              </label>
              <label className="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={showArrows}
                  onChange={(e) => updateAttributes({ showArrows: e.target.checked })}
                  className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                />
                <span className="text-sm text-gray-600">显示左右箭头</span>
              </label>
            </div>

            {images.length > 0 && (
              <div className="border-t pt-3">
                <label className="block text-sm font-medium text-gray-700 mb-2">已添加图片 ({images.length})</label>
                <div className="space-y-2 max-h-40 overflow-y-auto">
                  {images.map((url: string, index: number) => (
                    <div key={index} className="flex items-center gap-2 p-2 bg-gray-50 rounded-md">
                      <img src={url} alt="" className="w-10 h-10 object-cover rounded" />
                      <span className="flex-1 text-xs truncate text-gray-500">{url}</span>
                      <button
                        onClick={() => removeImage(index)}
                        className="p-1 text-red-400 hover:text-red-600"
                      >
                        <Trash2 size={14} />
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </NodeViewWrapper>
  );
};
