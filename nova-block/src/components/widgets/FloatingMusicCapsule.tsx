import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Play, Pause, SkipBack, SkipForward, X, ListMusic } from 'lucide-react';
import { useMusic } from '../../contexts/MusicContext';
import { PlaylistPopover } from './PlaylistPopover';

export const FloatingMusicCapsule: React.FC = () => {
  const { currentTrack, isPlaying, toggle, next, prev, stop } = useMusic();
  const [isSnapped, setIsSnapped] = useState(false);
  const [snapSide, setSnapSide] = useState<'left' | 'right'>('right');
  const [showPlaylist, setShowPlaylist] = useState(false);
  const [isHovered, setIsHovered] = useState(false);

  if (!currentTrack) return null;

  const handleDragEnd = (_: any, info: any) => {
    const threshold = 150;
    const windowWidth = window.innerWidth;
    const x = info.point.x;

    if (x < threshold) {
      setIsSnapped(true);
      setSnapSide('left');
    } else if (x > windowWidth - threshold) {
      setIsSnapped(true);
      setSnapSide('right');
    } else {
      setIsSnapped(false);
    }
  };

  const isSemiHidden = isSnapped && !isHovered;

  return (
    <AnimatePresence>
      <motion.div
        drag
        dragMomentum={false}
        onDragEnd={handleDragEnd}
        initial={{ opacity: 0, y: 50, scale: 0.9 }}
        animate={{ 
          opacity: 1, 
          scale: 1,
          x: isSemiHidden ? (snapSide === 'left' ? -60 : 60) : 0,
        }}
        exit={{ opacity: 0, y: 50, scale: 0.9 }}
        onMouseEnter={() => setIsHovered(true)}
        onMouseLeave={() => setIsHovered(false)}
        className={`fixed bottom-10 right-10 z-[100] flex items-center gap-2 bg-white/70 backdrop-blur-xl border border-white/40 shadow-2xl rounded-full p-1.5 transition-all duration-300 hover:shadow-pink-200/50 ${isSnapped ? '' : 'cursor-move'}`}
        style={{
           left: isSnapped && snapSide === 'left' ? '0' : 'auto',
           right: isSnapped && snapSide === 'right' ? '0' : (isSnapped ? 'auto' : '40px'),
        }}
      >
        {/* Vinyl Disc */}
        <div className="relative w-10 h-10 shrink-0">
          <div className="absolute inset-0 rounded-full bg-black/90 shadow-md ring-1 ring-white/20" />
          <motion.div
            animate={{ rotate: isPlaying ? 360 : 0 }}
            transition={{ duration: 4, ease: 'linear', repeat: isPlaying ? Infinity : 0 }}
            className="absolute inset-1 rounded-full overflow-hidden"
            style={{
              backgroundImage: currentTrack.cover ? `url(${currentTrack.cover})` : 'linear-gradient(45deg, #FF9A9E 0%, #FAD0C4 99%, #FAD0C4 100%)',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
            }}
          >
            <div className="absolute inset-0 bg-black/20" />
          </motion.div>
          <div className="absolute inset-0 flex items-center justify-center">
            <div className="w-1.5 h-1.5 rounded-full bg-white/90 border border-black/10" />
          </div>
        </div>

        {/* Info & Controls */}
        <AnimatePresence>
          {!isSemiHidden && (
            <motion.div 
              initial={{ opacity: 0, width: 0 }}
              animate={{ opacity: 1, width: 'auto' }}
              exit={{ opacity: 0, width: 0 }}
              className="flex items-center gap-3 pr-2 overflow-hidden whitespace-nowrap"
            >
              <div className="flex flex-col min-w-0 max-w-[120px]">
                <div className="text-[11px] font-bold text-gray-800 truncate">
                  {currentTrack.title}
                </div>
                <div className="flex items-center gap-0.5 mt-0.5">
                  <button onClick={prev} className="p-1 hover:bg-black/5 rounded-full transition-colors text-gray-600">
                    <SkipBack size={12} fill="currentColor" />
                  </button>
                  <button onClick={toggle} className="p-1 bg-black text-white rounded-full hover:scale-110 transition-transform">
                    {isPlaying ? <Pause size={10} fill="currentColor" /> : <Play size={10} fill="currentColor" />}
                  </button>
                  <button onClick={next} className="p-1 hover:bg-black/5 rounded-full transition-colors text-gray-600">
                    <SkipForward size={12} fill="currentColor" />
                  </button>
                </div>
              </div>

              <div className="flex items-center gap-1 border-l border-black/5 pl-2">
                <button 
                  onClick={() => setShowPlaylist(!showPlaylist)} 
                  className={`p-1.5 rounded-full transition-colors ${showPlaylist ? 'bg-pink-100 text-pink-500' : 'hover:bg-black/5 text-gray-500'}`}
                >
                  <ListMusic size={14} />
                </button>
                <button onClick={stop} className="p-1.5 rounded-full hover:bg-red-50 text-gray-400 hover:text-red-500 transition-colors">
                  <X size={14} />
                </button>
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {showPlaylist && <PlaylistPopover onClose={() => setShowPlaylist(false)} />}
      </motion.div>
    </AnimatePresence>
  );
};
