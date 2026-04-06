import sys
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Add skill path to sys.path
SKILL_ROOT = "/workspace/sensitive/skill/managing-lark-bitable-data"
if SKILL_ROOT not in sys.path:
    sys.path.append(SKILL_ROOT)

from scripts.search_records import search_records

def analyze_and_report():
    app_token = "ZPW6baVfxaNfdjsgdv0cqe2Vnyh"
    table_id = "tblY78NFYYN4OZpX"
    view_id = "vewMtsOxkB"
    
    total_rows = 0
    non_empty_rows = 0
    correct_count = 0
    inconsistent_count = 0
    execution_count = 0
    standard_count = 0
    
    label_counts = {}
    
    page_token = ""
    while True:
        resp = search_records(
            app_token,
            table_id,
            view_id=view_id,
            automatic_fields=True,
            page_token=page_token,
            page_size=500
        )
        
        data = resp.get("data", {})
        items = data.get("items", [])
        
        for item in items:
            fields = item.get("fields", {})
            total_rows += 1
            
            cats = fields.get("初审-问题类别", [])
            if not isinstance(cats, list):
                cats = [cats] if cats else []
            
            if not cats:
                continue
                
            non_empty_rows += 1
            
            if "无问题" in cats:
                correct_count += 1
            else:
                inconsistent_count += 1
                if "执行问题" in cats:
                    execution_count += 1
                if "标准问题" in cats:
                    standard_count += 1
                
                # Labels
                label_fields = [
                    "标注【封面】安全一级policy",
                    "标注【封面】安全二级policy",
                    "标注【书名简介】安全一级policy",
                    "标注【书名简介】安全二级policy",
                    "标注【封面】质量policy",
                    "标注【书名简介】质量policy"
                ]
                item_labels = set()
                for f in label_fields:
                    val = fields.get(f, [])
                    if isinstance(val, list):
                        for v in val: item_labels.add(v)
                    elif val: item_labels.add(str(val))
                
                for label in item_labels:
                    label_counts[label] = label_counts.get(label, 0) + 1
        
        if not data.get("has_more"):
            break
        page_token = data.get("page_token")

    # Metrics
    correct_pct = (correct_count / non_empty_rows * 100) if non_empty_rows > 0 else 0
    inconsistent_pct = (inconsistent_count / non_empty_rows * 100) if non_empty_rows > 0 else 0
    execution_pct = (execution_count / non_empty_rows * 100) if non_empty_rows > 0 else 0
    standard_pct = (standard_count / non_empty_rows * 100) if non_empty_rows > 0 else 0
    
    # 1. Output directory
    os.makedirs("output", exist_ok=True)
    
    # 2. Charts
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC'] + plt.rcParams['font.sans-serif']
    
    # Pie 1: Accuracy
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.pie([correct_count, inconsistent_count], labels=[f"正确\n{correct_count} ({correct_pct:.1f}%)", f"不一致\n{inconsistent_count} ({inconsistent_pct:.1f}%)"], 
           colors=['#4CAF50', '#FF5252'], startangle=140, shadow=False, autopct='%1.1f%%')
    ax.set_title("初审准确性统计", fontsize=14)
    plt.tight_layout()
    plt.savefig("output/accuracy_pie.png")
    plt.close()

    # Bar: Label Breakdown
    sorted_labels = sorted(label_counts.items(), key=lambda x: x[1], reverse=True)
    if sorted_labels:
        labels_names = [x[0] for x in sorted_labels]
        counts = [x[1] for x in sorted_labels]
        pcts = [(c / inconsistent_count * 100) for c in counts]
        
        # Display up to top 15 labels to keep chart readable
        display_labels = labels_names[:15]
        display_counts = counts[:15]
        display_pcts = pcts[:15]
        
        # Shorten very long labels
        display_labels_short = [ (l[:20] + '...') if len(l) > 23 else l for l in display_labels ]

        fig, ax = plt.subplots(figsize=(10, 8))
        sns.barplot(x=display_counts, y=display_labels_short, palette="viridis", ax=ax)
        ax.set_xlabel("出现次数")
        ax.set_title(f"标签细分统计 (Top {len(display_labels)}, 总不一致样本={inconsistent_count})")
        
        # Add text labels
        for i, (v, p) in enumerate(zip(display_counts, display_pcts)):
            ax.text(v + 0.1, i, f"{v} ({p:.1f}%)", va='center')
        
        plt.tight_layout()
        plt.savefig("output/label_breakdown.png")
        plt.close()

    # 3. Markdown Report
    report = f"""
# 多维表格数据统计分析报告

## 1. 总样本量统计
- **总记录数**：{total_rows}
- **有效样本量**（“初审-问题类别”非空）：**{non_empty_rows}**
- **待处理/为空样本**：{total_rows - non_empty_rows}

## 2. 准确性统计
分析基于有效样本量 ({non_empty_rows})。

<table>
  <tr>
    <td>统计项</td>
    <td>数量</td>
    <td>占比</td>
  </tr>
  <tr>
    <td>**初审与标注正确** (无问题)</td>
    <td>{correct_count}</td>
    <td>{correct_pct:.2f}%</td>
  </tr>
  <tr>
    <td>**初审与标注不一致** (有问题)</td>
    <td>{inconsistent_count}</td>
    <td>{inconsistent_pct:.2f}%</td>
  </tr>
</table>

![Accuracy Pie Chart](accuracy_pie.png)

## 3. 问题归因统计 (相对于总有效样本)
<table>
  <tr>
    <td>问题类型</td>
    <td>数量</td>
    <td>相对于总样本占比</td>
  </tr>
  <tr>
    <td>**执行问题**</td>
    <td>{execution_count}</td>
    <td>{execution_pct:.2f}%</td>
  </tr>
  <tr>
    <td>**标准问题**</td>
    <td>{standard_count}</td>
    <td>{standard_pct:.2f}%</td>
  </tr>
</table>

## 4. 标签细分统计
在 **{inconsistent_count}** 个“不一致”样本中，各标签的分布如下：

<table>
  <tr>
    <td>安全/质量标签</td>
    <td>数量</td>
    <td>在“有问题”样本中占比</td>
  </tr>
"""
    for label, count, pct in [(x['label'], x['count'], x['percentage']) for x in sorted([{'label': l, 'count': c, 'percentage': (c/inconsistent_count*100) if inconsistent_count>0 else 0} for l,c in label_counts.items()], key=lambda x: x['count'], reverse=True)]:
        report += f"""  <tr>
    <td>{label}</td>
    <td>{count}</td>
    <td>{pct:.2f}%</td>
  </tr>
"""
    report += """</table>

![Label Breakdown Chart](label_breakdown.png)

---
*报告生成时间：2026-03-23*
"""
    with open("output/report.lark.md", "w") as f:
        f.write(report)
    
    print("Report generated successfully in output/ directory.")

if __name__ == "__main__":
    analyze_and_report()
