import React, { useState, useEffect, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { cn } from '../lib/utils'; // Assuming this exists for class merging, or I'll define a simple one

interface OutlineItem {
  id: string;
  text: string;
  level: number;
}

interface TableOfContentsProps {
  outline: OutlineItem[];
  activeId?: string;
}

/**
 * TableOfContents Component
 * A minimalist TOC that appears as lines on the right side and expands on hover.
 */
export const TableOfContents: React.FC<TableOfContentsProps> = ({ outline, activeId: propActiveId }) => {
  const [isHovered, setIsHovered] = useState(false);
  const [activeId, setActiveId] = useState<string | undefined>(propActiveId);

  // Sync scroll position with active heading
  useEffect(() => {
    if (propActiveId) {
      setActiveId(propActiveId);
    }
  }, [propActiveId]);

  // Handle click to scroll
  const handleClick = useCallback((id: string) => {
    const element = document.getElementById(id);
    if (element) {
      const headerOffset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth',
      });
    }
  }, []);

  // Use IntersectionObserver to track which heading is currently visible if propActiveId isn't provided or updated frequently
  useEffect(() => {
    if (!outline.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      {
        rootMargin: '-10% 0px -70% 0px', // Trigger when heading is near the top
        threshold: 1.0,
      }
    );

    outline.forEach((item) => {
      const element = document.getElementById(item.id);
      if (element) observer.observe(element);
    });

    return () => observer.disconnect();
  }, [outline]);

  if (!outline || outline.length === 0) return null;

  return (
    <motion.aside
      className="fixed right-0 top-1/2 -translate-y-1/2 z-40 flex flex-col items-end py-10 pr-1 select-none"
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      initial={false}
      animate={{
        width: isHovered ? '240px' : '32px',
        backgroundColor: isHovered ? 'rgba(255, 255, 255, 0.05)' : 'rgba(255, 255, 255, 0)',
        backdropFilter: isHovered ? 'blur(8px)' : 'blur(0px)',
      }}
      transition={{
        duration: 0.4,
        ease: [0.4, 0, 0.2, 1], // Advanced cubic-bezier
      }}
    >
      <div className="absolute right-0 top-0 bottom-0 w-[1px] bg-stone-200/20" />
      
      <nav className="flex flex-col gap-2 items-end w-full px-3">
        {outline.map((item) => {
          const isActive = activeId === item.id;
          
          return (
            <button
              key={item.id}
              onClick={() => handleClick(item.id)}
              className="group relative flex items-center justify-end h-5 w-full outline-none transition-all duration-300"
              data-active={isActive}
            >
              <div className="flex items-center gap-2.5 w-full justify-end">
                {/* Heading Text - Only visible on hover */}
                <AnimatePresence>
                  {isHovered && (
                    <motion.span
                      initial={{ opacity: 0, x: 10, filter: 'blur(4px)' }}
                      animate={{ opacity: 1, x: 0, filter: 'blur(0px)' }}
                      exit={{ opacity: 0, x: 5, filter: 'blur(2px)' }}
                      transition={{ duration: 0.3, delay: 0.05 }}
                      className={cn(
                        "text-[11px] font-medium tracking-wide whitespace-nowrap transition-colors duration-300 flex-1 text-right truncate",
                        isActive ? "text-reflect-text" : "text-stone-400 group-hover:text-reflect-text"
                      )}
                    >
                      {item.text}
                    </motion.span>
                  )}
                </AnimatePresence>

                {/* Horizontal Lines (TOC visual signature) */}
                <motion.div
                  layout
                  className={cn(
                    "h-[1.5px] rounded-full transition-all duration-300 transform shrink-0",
                    // Line length based on heading level: H1 > H2 > H3
                    item.level === 1 ? "w-5" : item.level === 2 ? "w-3.5" : "w-2",
                    isActive ? "bg-reflect-text w-6 shadow-[0_0_8px_rgba(0,0,0,0.1)]" : "bg-stone-300/60 group-hover:bg-stone-400"
                  )}
                />
              </div>
            </button>
          );
        })}
      </nav>
    </motion.aside>
  );
};
