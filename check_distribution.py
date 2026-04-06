import sys
import json
import os

SKILL_ROOT = "/workspace/sensitive/skill/managing-lark-bitable-data"
if SKILL_ROOT not in sys.path:
    sys.path.append(SKILL_ROOT)

from scripts.search_records import search_records

def analyze_distribution():
    app_token = "ZPW6baVfxaNfdjsgdv0cqe2Vnyh"
    table_id = "tblY78NFYYN4OZpX"
    view_id = "vewMtsOxkB"
    
    category_distribution = {}
    empty_category_count = 0
    empty_category_with_labels = 0
    
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
            
            # Check "初审-问题类别"
            cats = fields.get("初审-问题类别", [])
            if not isinstance(cats, list):
                cats = [cats] if cats else []
            
            cat_key = str(sorted(cats))
            category_distribution[cat_key] = category_distribution.get(cat_key, 0) + 1
            
            if not cats:
                empty_category_count += 1
                # Check if it has labels
                label_fields = [
                    "标注【封面】安全一级policy",
                    "标注【封面】安全二级policy",
                    "标注【书名简介】安全一级policy",
                    "标注【书名简介】安全二级policy",
                    "标注【封面】质量policy",
                    "标注【书名简介】质量policy"
                ]
                has_label = False
                for f in label_fields:
                    if fields.get(f):
                        has_label = True
                        break
                if has_label:
                    empty_category_with_labels += 1
        
        if not data.get("has_more"):
            break
        page_token = data.get("page_token")

    print(json.dumps({
        "category_distribution": category_distribution,
        "empty_category_count": empty_category_count,
        "empty_category_with_labels": empty_category_with_labels
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    analyze_distribution()
