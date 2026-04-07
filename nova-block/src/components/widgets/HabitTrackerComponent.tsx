import React, { useMemo, useState, useEffect, useRef } from 'react';
import { NodeViewWrapper } from '@tiptap/react';
import {
  addMonths,
  eachDayOfInterval,
  endOfMonth,
  format,
  isSameMonth,
  startOfMonth,
  subMonths,
  isToday,
  startOfToday,
} from 'date-fns';
import { ChevronLeft, ChevronRight, Flame, Crown, Plus, Settings2, Trash2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import confetti from 'canvas-confetti';
import { useHabit } from '../../contexts/HabitContext';

const weekDays = ['一', '二', '三', '四', '五', '六', '日'];

export const HabitTrackerComponent: React.FC<any> = (props) => {
  const { node, updateAttributes, selected, editor } = props;
  const isEditable = editor?.isEditable;
  
  const { 
    habits, 
    activeHabitId, 
    setActiveHabitId, 
    logCheckIn, 
    getLogForDate, 
    getStreak,
    addHabit,
    deleteHabit 
  } = useHabit();

  const [cursor, setCursor] = useState(() => new Date());
  const [isSettingOpen, setIsSettingOpen] = useState(false);

  const activeHabit = habits.find(h => h.id === activeHabitId) || habits[0];
  const streak = activeHabit ? getStreak(activeHabit.id) : 0;

  const days = useMemo(() => {
    const start = startOfMonth(cursor);
    const end = endOfMonth(cursor);
    const list = eachDayOfInterval({ start, end });
    const firstDow = Number(format(start, 'i')); // 1 (Mon) to 7 (Sun)
    const pad = firstDow - 1;
    const padded: (Date | null)[] = [...Array.from({ length: pad }, () => null), ...list];
    const tail = (7 - (padded.length % 7)) % 7;
    return [...padded, ...Array.from({ length: tail }, () => null)];
  }, [cursor]);

  const handleCellClick = (date: Date, event: React.MouseEvent) => {
    if (!activeHabit || !isEditable) return;
    
    const dateStr = format(date, 'yyyy-MM-dd');
    const existingLog = getLogForDate(activeHabit.id, dateStr);
    const currentValue = existingLog ? existingLog.value : 0;
    const newValue = (currentValue + 1) % (activeHabit.targetValue + 1);
    
    logCheckIn(activeHabit.id, dateStr, newValue);

    // Trigger confetti if completed
    if (newValue === activeHabit.targetValue) {
      const rect = (event.currentTarget as HTMLElement).getBoundingClientRect();
      confetti({
        particleCount: 40,
        spread: 60,
        origin: { 
          x: (rect.left + rect.width / 2) / window.innerWidth, 
          y: (rect.top + rect.height / 2) / window.innerHeight 
        },
        colors: [activeHabit.color, '#ffffff', '#ffcc00'],
        ticks: 200,
        gravity: 1.2,
        scalar: 0.7,
      });
    }
  };

  return (
    <NodeViewWrapper className={`my-8 group relative ${selected ? 'ring-2 ring-primary/20 rounded-[2rem]' : ''}`}>
      <div className="max-w-md mx-auto">
        {/* Main Card */}
        <div className="relative overflow-hidden backdrop-blur-xl bg-white/40 dark:bg-black/20 border border-white/20 dark:border-white/10 rounded-[2rem] shadow-2xl shadow-primary/5 p-6 transition-all duration-500 hover:shadow-primary/10">
          
          {/* Header */}
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center gap-3">
              <div 
                className="w-12 h-12 rounded-2xl flex items-center justify-center text-2xl shadow-inner transition-transform hover:scale-110 active:scale-95 cursor-pointer"
                style={{ backgroundColor: activeHabit?.color + '44' }}
              >
                {activeHabit?.icon || '📅'}
              </div>
              <div>
                <div className="flex items-center gap-2">
                   <select 
                    value={activeHabitId || ''} 
                    onChange={(e) => setActiveHabitId(e.target.value)}
                    className="bg-transparent border-none font-bold text-lg focus:ring-0 cursor-pointer p-0 pr-6 appearance-none outline-none"
                  >
                    {habits.map(h => (
                      <option key={h.id} value={h.id}>{h.name}</option>
                    ))}
                  </select>
                </div>
                <div className="text-xs text-stone-500 font-medium tracking-wider uppercase">
                  {format(cursor, 'MMMM yyyy')}
                </div>
              </div>
            </div>

            <div className="flex items-center gap-2">
              <div className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/50 dark:bg-black/30 border border-white/20 shadow-sm">
                {streak >= 10 ? <Crown size={14} className="text-yellow-500 fill-yellow-500" /> : <Flame size={14} className="text-orange-500 fill-orange-500" />}
                <span className="text-sm font-bold tabular-nums">{streak}</span>
              </div>
              <button 
                onClick={() => setIsSettingOpen(!isSettingOpen)}
                className="p-2 rounded-xl hover:bg-white/60 transition-colors"
              >
                <Settings2 size={18} className="text-stone-400" />
              </button>
            </div>
          </div>

          {/* Controls */}
          <div className="flex items-center justify-between mb-4 px-1">
             <div className="flex gap-1">
               <button onClick={() => setCursor(subMonths(cursor, 1))} className="p-1.5 rounded-lg hover:bg-white/40 transition-colors"><ChevronLeft size={16}/></button>
               <button onClick={() => setCursor(addMonths(cursor, 1))} className="p-1.5 rounded-lg hover:bg-white/40 transition-colors"><ChevronRight size={16}/></button>
             </div>
             <button 
                onClick={() => setCursor(new Date())}
                className="text-[10px] font-bold text-stone-400 hover:text-primary transition-colors uppercase tracking-tighter"
             >
                Today
             </button>
          </div>

          {/* Calendar Grid */}
          <div className="grid grid-cols-7 gap-2">
            {weekDays.map(d => (
              <div key={d} className="text-[10px] font-bold text-stone-400 text-center pb-2">{d}</div>
            ))}
            
            {days.map((date, i) => {
              if (!date) return <div key={`empty-${i}`} className="aspect-square" />;
              
              const dateStr = format(date, 'yyyy-MM-dd');
              const isCurrMonth = isSameMonth(date, cursor);
              const log = getLogForDate(activeHabit?.id || '', dateStr);
              const val = log ? log.value : 0;
              const target = activeHabit?.targetValue || 1;
              const percent = Math.min(val / target, 1);
              const isCompleted = val >= target;
              const today = isToday(date);

              return (
                <motion.button
                  key={dateStr}
                  whileHover={{ scale: 1.1 }}
                  whileTap={{ scale: 0.9 }}
                  onClick={(e) => isCurrMonth && handleCellClick(date, e)}
                  disabled={!isCurrMonth || !isEditable}
                  className={`
                    relative aspect-square rounded-xl border flex items-center justify-center text-xs font-bold transition-all
                    ${isCurrMonth ? 'cursor-pointer' : 'opacity-0 pointer-events-none'}
                    ${today ? 'ring-2 ring-primary/40 ring-offset-2 ring-offset-transparent' : ''}
                  `}
                  style={{
                    backgroundColor: val > 0 ? (activeHabit?.color + Math.floor(percent * 255).toString(16).padStart(2, '0')) : 'rgba(255,255,255,0.3)',
                    borderColor: today ? activeHabit?.color : (val > 0 ? activeHabit?.color + '66' : 'rgba(0,0,0,0.05)'),
                    color: isCompleted ? 'white' : 'inherit',
                    textShadow: isCompleted ? '0 1px 2px rgba(0,0,0,0.1)' : 'none'
                  }}
                >
                  {format(date, 'd')}
                  
                  {/* Progress Fill */}
                  {val > 0 && val < target && (
                    <div 
                      className="absolute inset-0 rounded-xl pointer-events-none overflow-hidden opacity-30"
                      style={{ 
                        background: `linear-gradient(to top, ${activeHabit?.color} ${percent * 100}%, transparent 0%)` 
                      }}
                    />
                  )}
                </motion.button>
              );
            })}
          </div>

          {/* Quick Settings Panel */}
          <AnimatePresence>
            {isSettingOpen && (
              <motion.div 
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                className="overflow-hidden mt-6 pt-4 border-t border-white/20"
              >
                <div className="space-y-4">
                   <div className="flex items-center justify-between">
                     <span className="text-xs font-bold text-stone-500 uppercase">Manage Habits</span>
                     <button 
                        onClick={() => addHabit({ name: '新习惯', icon: '✨', color: '#b8c6db', targetValue: 1 })}
                        className="p-1 bg-primary/10 text-primary rounded-md hover:bg-primary/20 transition-colors"
                     >
                       <Plus size={14} />
                     </button>
                   </div>
                   <div className="max-h-32 overflow-y-auto space-y-2 pr-1">
                      {habits.map(h => (
                        <div key={h.id} className="flex items-center justify-between p-2 rounded-xl bg-white/40 dark:bg-black/20 group/item">
                          <div className="flex items-center gap-2">
                             <span>{h.icon}</span>
                             <span className="text-sm font-medium">{h.name}</span>
                          </div>
                          <button 
                            onClick={() => deleteHabit(h.id)}
                            className="p-1 opacity-0 group-hover/item:opacity-100 text-red-400 hover:text-red-500 transition-all"
                          >
                            <Trash2 size={14} />
                          </button>
                        </div>
                      ))}
                   </div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>
    </NodeViewWrapper>
  );
};
