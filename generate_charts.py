import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter

# Load analysis results
with open("analysis_results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# Font configuration
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC'] + plt.rcParams['font.sans-serif']

def save_chart(name):
    plt.savefig(f"{name}.png", bbox_inches="tight", dpi=200)
    plt.close()

# 1. Problem Category Distribution (Initial Review)
# We need to re-calculate this from the original records or assume based on sample size
# Let's count from the records directly for accuracy
file_path = "/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/lark_bitable_large_output/lark_bitable_resp_1774255050_409bbf44.json"
with open(file_path, "r") as f:
    raw_data = json.load(f)
records = raw_data.get("data", {}).get("items", [])

cat_counts = Counter()
for r in records:
    cats = r.get("fields", {}).get("初审-问题类别", [])
    if not cats:
        cat_counts["未填报"] += 1
    else:
        for c in cats:
            cat_counts[c] += 1

labels = list(cat_counts.keys())
sizes = list(cat_counts.values())

fig, ax = plt.subplots(figsize=(8, 6), constrained_layout=True)
wedges, texts, autotexts = ax.pie(sizes, labels=None, autopct='%1.1f%%', shadow=False, startangle=140)
ax.legend(wedges, labels, loc="lower center", bbox_to_anchor=(0.5, -0.1), ncol=len(labels), frameon=False)
ax.set_title("初审问题类别分布", fontsize=14, pad=20)
save_chart("problem_category_dist")

# 2. Annotation Security Top Labels
sec_df = pd.DataFrame(results["security_stats"]).head(10)
if not sec_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    sns.barplot(x="Count", y="Label", data=sec_df, ax=ax, palette="Reds_r")
    ax.set_title("标注侧-安全维度Top 10标签", fontsize=14)
    ax.set_xlabel("出现次数")
    ax.set_ylabel("标签名称")
    # Add counts
    for i, v in enumerate(sec_df["Count"]):
        ax.text(v + 0.1, i, str(v), color='black', va='center')
    save_chart("security_top_labels")

# 3. Annotation Quality Top Labels
qual_df = pd.DataFrame(results["quality_stats"]).head(10)
if not qual_df.empty:
    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    sns.barplot(x="Count", y="Label", data=qual_df, ax=ax, palette="Blues_r")
    ax.set_title("标注侧-质量维度Top 10标签", fontsize=14)
    ax.set_xlabel("出现次数")
    ax.set_ylabel("标签名称")
    # Add counts
    for i, v in enumerate(qual_df["Count"]):
        ax.text(v + 0.1, i, str(v), color='black', va='center')
    save_chart("quality_top_labels")

# 4. Execution vs Standard Problem Labels (Top 5 each)
exec_df = pd.DataFrame(results["execution_stats"]).head(5)
std_df = pd.DataFrame(results["standard_stats"]).head(5)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

if not exec_df.empty:
    sns.barplot(x="Count", y="Label", data=exec_df, ax=ax1, palette="Oranges_r")
    ax1.set_title("执行问题-Top 5标签", fontsize=12)
    ax1.set_xlabel("次数")
    ax1.set_ylabel("")

if not std_df.empty:
    sns.barplot(x="Count", y="Label", data=std_df, ax=ax2, palette="Greens_r")
    ax2.set_title("标准问题-Top 5标签", fontsize=12)
    ax2.set_xlabel("次数")
    ax2.set_ylabel("")

fig.suptitle("问题归因细分统计", fontsize=16)
save_chart("execution_vs_standard")
