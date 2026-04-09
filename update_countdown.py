import re
import os

with open("nova_repo/nova-block/src/components/widgets/CountdownComponent.tsx", "r") as f:
    content = f.read()

# Replace FlipUnit
new_flip_unit = """
const FlipUnit: React.FC<{ value: string; label: string }> = ({ value, label }) => {
  const [currentValue, setCurrentValue] = useState(value);
  const [oldValue, setOldValue] = useState(value);
  const [flipKey, setFlipKey] = useState(0);

  useEffect(() => {
    if (value !== currentValue) {
      setOldValue(currentValue);
      setCurrentValue(value);
      setFlipKey(k => k + 1);
    }
  }, [value, currentValue]);

  return (
    <div className="flex flex-col items-center gap-3">
      <div className={`relative w-12 h-16 md:w-16 md:h-22 rounded-xl ${flipTheme.shadowOut} perspective-1000 select-none bg-[#F0F0F3]`}>
        
        {/* 层 1: 底板上半部 (静态，显示 New Value) */}
        <div className={`absolute top-0 left-0 right-0 bottom-1/2 overflow-hidden rounded-t-xl border-b border-stone-200/50 ${flipTheme.card} flex items-end justify-center pb-[1px]`}>
          <span className={`translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{currentValue}</span>
        </div>

        {/* 层 2: 底板下半部 (静态，显示 Old Value) */}
        <div className={`absolute top-1/2 left-0 right-0 bottom-0 overflow-hidden rounded-b-xl ${flipTheme.card} flex items-start justify-center pt-[1px]`}>
          <span className={`-translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{oldValue}</span>
        </div>

        {/* 动态翻页层 (仅在数字改变时播放一次动画，播放完毕停留在 -180度 并遮盖底板下半部) */}
        {flipKey > 0 && (
          <div
            key={flipKey}
            className="absolute top-0 left-0 right-0 bottom-1/2 z-10 flip-animation-card"
            style={{ transformOrigin: "bottom center", transformStyle: "preserve-3d" }}
          >
            {/* 翻页面正面: 显示 Old Value (上半部) */}
            <div 
              className={`absolute inset-0 w-full h-full overflow-hidden rounded-t-xl border-b border-stone-200/50 ${flipTheme.card} flex items-end justify-center pb-[1px] backface-hidden`}
            >
              <span className={`translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{oldValue}</span>
            </div>
            
            {/* 翻页面背面: 显示 New Value (下半部)，由于翻页到 -180度，本身颠倒了，所以用 rotateX(180deg) 扶正 */}
            <div 
              className={`absolute inset-0 w-full h-full overflow-hidden rounded-b-xl ${flipTheme.card} flex items-start justify-center pt-[1px] backface-hidden`}
              style={{ transform: "rotateX(180deg)" }}
            >
              <span className={`-translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{currentValue}</span>
            </div>
          </div>
        )}

        {/* 中间的那条缝隙阴影 */}
        <div className="absolute top-1/2 left-0 w-full h-[1px] bg-stone-300/30 z-20" />
      </div>
      <span className={`text-[9px] md:text-[10px] font-bold tracking-widest uppercase ${flipTheme.subtle}`}>{label}</span>
    </div>
  );
};
"""

content = re.sub(
    r"const FlipUnit: React\.FC<.*?> = \(\{ value, label \}\) => \{.*?(?=function safeParseISO)",
    new_flip_unit + "\n\n",
    content,
    flags=re.DOTALL
)

# Fix expiration alert
old_toggle = """<div className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        id="showBubble"
                        checked={showBubble}
                        onChange={(e) => setShowBubble(e.target.checked)}
                        className="sr-only peer"
                      />
                      <div className={`w-8 h-4 rounded-full ${flipTheme.shadowIn} peer-checked:bg-blue-400/20 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-3 after:w-3 after:transition-all peer-checked:after:translate-x-4 after:shadow-sm`}></div>
                    </div>"""

new_toggle = """<label className="relative inline-flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={showBubble}
                        onChange={(e) => setShowBubble(e.target.checked)}
                        className="sr-only peer"
                      />
                      <div className={`w-8 h-4 rounded-full ${flipTheme.shadowIn} peer-checked:bg-blue-400/20 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-3 after:w-3 after:transition-all peer-checked:after:translate-x-4 after:shadow-sm`}></div>
                    </label>"""

content = content.replace(old_toggle, new_toggle)

# Fix style block
old_style = """<style>{`
        .perspective-1000 {
          perspective: 1000px;
        }
        .backface-hidden {
          backface-visibility: hidden;
          -webkit-backface-visibility: hidden;
        }
      `}</style>"""

new_style = """<style>{`
        .perspective-1000 {
          perspective: 1000px;
        }
        .backface-hidden {
          backface-visibility: hidden;
          -webkit-backface-visibility: hidden;
        }
        @keyframes flipDown {
          0% { transform: rotateX(0deg); }
          100% { transform: rotateX(-180deg); }
        }
        .flip-animation-card {
          animation: flipDown 0.6s cubic-bezier(0.4, 0.0, 0.2, 1) forwards;
        }
      `}</style>"""

content = content.replace(old_style, new_style)

# Remove framer-motion from FlipUnit since we use pure CSS now (if it was still imported)
# Wait, AnimatePresence is used for the Settings panel, so we keep framer-motion import.

with open("nova_repo/nova-block/src/components/widgets/CountdownComponent.tsx", "w") as f:
    f.write(content)

