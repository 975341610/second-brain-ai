import json
import pandas as pd
from collections import Counter

# Load data
file_path = "/workspace/iris_4313d091-e484-4384-8564-8ce91e478bc4/lark_bitable_large_output/lark_bitable_resp_1774255050_409bbf44.json"
with open(file_path, "r") as f:
    raw_data = json.load(f)

records = raw_data.get("data", {}).get("items", [])

# Initial Review Problem Category: "初审-问题类别"
FIELD_PROBLEM_CATEGORY = "初审-问题类别"
# Attribution: "问题归因"
FIELD_PROBLEM_ATTRIBUTION = "问题归因"

# Policy fields for Initial Review
POLICY_FIELDS_INITIAL = [
    "初审【封面】安全一级policy",
    "初审【封面】安全二级policy",
    "初审【书名简介】安全一级policy",
    "初审【书名简介】安全二级policy",
    "初审【封面】质量policy",
    "初审【书名简介】质量policy"
]

# Policy fields for Annotation (Label)
POLICY_FIELDS_ANNOTATION_SECURITY = [
    "标注【封面】安全一级policy",
    "标注【封面】安全二级policy",
    "标注【书名简介】安全一级policy",
    "标注【书名简介】安全二级policy"
]
POLICY_FIELDS_ANNOTATION_QUALITY = [
    "标注【封面】质量policy",
    "标注【书名简介】质量policy"
]

# 1. Total Sample Size
sample_records = [r for r in records if r.get("fields", {}).get(FIELD_PROBLEM_CATEGORY)]
total_sample_size = len(sample_records)
print(f"Total Sample Size (records with {FIELD_PROBLEM_CATEGORY} non-empty): {total_sample_size}")

# 2. Problem Attribution Breakdown
execution_problems = []
standard_problems = []

for r in sample_records:
    problem_cats = r.get("fields", {}).get(FIELD_PROBLEM_CATEGORY, [])
    # Flatten the labels for this record
    labels = []
    for field in POLICY_FIELDS_INITIAL:
        val = r.get("fields", {}).get(field)
        if isinstance(val, list):
            labels.extend(val)
        elif val:
            labels.append(val)
    
    if "执行问题" in problem_cats:
        execution_problems.append({"id": r.get("record_id"), "labels": labels})
    if "标准问题" in problem_cats:
        standard_problems.append({"id": r.get("record_id"), "labels": labels})

def get_stats(records_list):
    total_count = len(records_list)
    label_counts = Counter()
    for item in records_list:
        # Avoid double counting if a record has multiple labels (though requested as counts/shares)
        # Assuming we want to count each occurrence of a label across all records
        for label in item["labels"]:
            label_counts[label] += 1
    
    stats = []
    for label, count in label_counts.most_common():
        stats.append({"Label": label, "Count": count, "Percentage": round(count / total_count * 100, 2) if total_count > 0 else 0})
    return stats

execution_stats = get_stats(execution_problems)
standard_stats = get_stats(standard_problems)

print("\n--- Execution Problem Labels ---")
print(pd.DataFrame(execution_stats[:10]))
print("\n--- Standard Problem Labels ---")
print(pd.DataFrame(standard_stats[:10]))

# 3. Label Multi-dimensional Statistics (Annotation side)
# We count each label's occurrence in the annotation fields, separated by Security and Quality.

security_labels = Counter()
quality_labels = Counter()

# Records with "标注" (Annotation) labels
annotation_sample_count = 0
for r in records:
    fields = r.get("fields", {})
    has_annotation = False
    
    # Security side
    for field in POLICY_FIELDS_ANNOTATION_SECURITY:
        val = fields.get(field)
        if val:
            has_annotation = True
            if isinstance(val, list):
                for v in val:
                    security_labels[v] += 1
            else:
                security_labels[val] += 1
    
    # Quality side
    for field in POLICY_FIELDS_ANNOTATION_QUALITY:
        val = fields.get(field)
        if val:
            has_annotation = True
            if isinstance(val, list):
                for v in val:
                    quality_labels[v] += 1
            else:
                quality_labels[val] += 1
    
    if has_annotation:
        annotation_sample_count += 1

def counter_to_df(counter):
    data = [{"Label": label, "Count": count} for label, count in counter.most_common()]
    return pd.DataFrame(data)

security_stats_df = counter_to_df(security_labels)
quality_stats_df = counter_to_df(quality_labels)

print(f"\nAnnotation Sample Size: {annotation_sample_count}")
print("\n--- Annotation Security Labels ---")
print(security_stats_df.head(10))
print("\n--- Annotation Quality Labels ---")
print(quality_stats_df.head(10))

# Result Export for Report
analysis_results = {
    "total_sample_size": total_sample_size,
    "execution_stats": execution_stats,
    "standard_stats": standard_stats,
    "annotation_sample_count": annotation_sample_count,
    "security_stats": security_stats_df.to_dict(orient="records"),
    "quality_stats": quality_stats_df.to_dict(orient="records"),
}

with open("analysis_results.json", "w", encoding="utf-8") as f:
    json.dump(analysis_results, f, ensure_ascii=False, indent=2)
