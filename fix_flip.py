import re

with open("nova_repo/nova-block/src/components/widgets/CountdownComponent.tsx", "r") as f:
    content = f.read()

new_flip_unit = """
const FlipUnit: React.FC<{ value: string; label: string }> = ({ value, label }) => {
  const [currentValue, setCurrentValue] = useState(value);
  const [oldValue, setOldValue] = useState(value);

  useEffect(() => {
    if (value !== currentValue) {
      setOldValue(currentValue);
      setCurrentValue(value);
    }
  }, [value, currentValue]);

  return (
    <div className="flex flex-col items-center gap-3">
      <div className={`relative w-12 h-16 md:w-16 md:h-22 rounded-xl ${flipTheme.shadowOut} perspective-1000 select-none bg-[#F0F0F3]`}>
        
        {/* 层 1: 底板上半部 (静态，显示 currentValue) */}
        <div className={`absolute top-0 left-0 right-0 bottom-1/2 overflow-hidden rounded-t-xl border-b border-stone-200/50 ${flipTheme.card} flex items-end justify-center pb-[1px]`}>
          <span className={`translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{currentValue}</span>
        </div>

        {/* 层 2: 底板下半部 (静态，显示 oldValue) */}
        <div className={`absolute top-1/2 left-0 right-0 bottom-0 overflow-hidden rounded-b-xl ${flipTheme.card} flex items-start justify-center pt-[1px]`}>
          <span className={`-translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{oldValue}</span>
        </div>

        {/* 动态翻页层: key 绑定 currentValue，数字改变时重新创建该 DOM，触发完整 CSS 动画 */}
        {currentValue !== oldValue && (
          <div
            key={currentValue}
            className="absolute top-0 left-0 right-0 bottom-1/2 z-10 flip-animation-card"
            style={{ transformOrigin: "bottom center", transformStyle: "preserve-3d" }}
          >
            {/* 翻页面正面: 显示 oldValue (上半部) */}
            <div 
              className={`absolute inset-0 w-full h-full overflow-hidden rounded-t-xl border-b border-stone-200/50 ${flipTheme.card} flex items-end justify-center pb-[1px] backface-hidden`}
            >
              <span className={`translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{oldValue}</span>
            </div>
            
            {/* 翻页面背面: 显示 currentValue (下半部)，由于翻到-180度，本身颠倒，需 rotateX(180deg) 扶正 */}
            <div 
              className={`absolute inset-0 w-full h-full overflow-hidden rounded-b-xl ${flipTheme.card} flex items-start justify-center pt-[1px] backface-hidden`}
              style={{ transform: "rotateX(180deg)" }}
            >
              <span className={`-translate-y-1/2 ${flipTheme.text} font-bold text-3xl md:text-5xl tabular-nums`}>{currentValue}</span>
            </div>
          </div>
        )}

        {/* 中缝阴影 */}
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

with open("nova_repo/nova-block/src/components/widgets/CountdownComponent.tsx", "w") as f:
    f.write(content)

