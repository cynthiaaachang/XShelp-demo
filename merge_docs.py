import os
import yaml
import datetime
from pathlib import Path

# --- 設定區 ---
MKDOCS_CONFIG = "mkdocs.yml"      # 設定檔
SOURCE_DIR = "docs"               # 原始資料夾
OUTPUT_DIR = "merged_final_level" # 輸出資料夾
IGNORE_FILES = ["index.md", "view.md", "README.md", "search-history/view.md", "search-records/view.md"]

def load_yaml_config(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"❌ 錯誤: 找不到 {filepath}")
        return None

def flatten_nav_structure(nav_item, parent_category=""):
    """
    遞迴將巢狀的目錄結構「攤平」
    """
    files_to_process = []

    if isinstance(nav_item, str):
        if Path(nav_item).name not in IGNORE_FILES:
            category = parent_category if parent_category else "其他"
            files_to_process.append((category, nav_item))

    elif isinstance(nav_item, list):
        for sub_item in nav_item:
            files_to_process.extend(flatten_nav_structure(sub_item, parent_category))

    elif isinstance(nav_item, dict):
        for category, content in nav_item.items():
            current_category = category 
            files_to_process.extend(flatten_nav_structure(content, current_category))
            
    return files_to_process

def process_file_content(file_path, sub_category):
    """
    讀取檔案內容並調整標題層級 (修正版：支援無 YAML 檔頭的檔案)
    """
    full_path = Path(file_path)
    if not full_path.exists():
        full_path = Path(SOURCE_DIR) / file_path
    
    if not full_path.exists():
        return None

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        processed_lines = []
        filename_title = full_path.stem

        # 1. 加上三級標題 (### 函數名稱)
        processed_lines.append(f"\n### {filename_title}\n")
        
        # --- 修正邏輯開始 ---
        # 檢查第一行是否為 ---，只有在有 header 時才執行跳過邏輯
        has_yaml = False
        if len(lines) > 0 and lines[0].strip() == "---":
            has_yaml = True
            
        yaml_ended = False
        yaml_count = 0

        for line in lines:
            stripped = line.strip()

            # 如果檔案有 YAML 檔頭，執行過濾
            if has_yaml:
                if stripped == "---":
                    yaml_count += 1
                    if yaml_count == 2: # 遇到第二個 ---，代表檔頭結束
                        yaml_ended = True
                    continue # 跳過分隔線本身
                
                if not yaml_ended:
                    continue # 跳過檔頭內容

            # 2. 標題降級處理 (H1 -> H4, H2 -> H5)
            # 這樣可以確保內容結構不會打亂大文件的層級
            if line.startswith("# "):
                processed_lines.append("####" + line[1:]) 
            elif line.startswith("##"):
                processed_lines.append("#####" + line[2:])
            else:
                processed_lines.append(line)
        
        return "".join(processed_lines)

    except Exception as e:
        print(f"讀取失敗: {file_path} - {e}")
        return None

def generate_front_matter(title, file_count, sub_categories):
    """生成 AI 讀取的檔頭"""
    today = datetime.date.today().strftime("%Y-%m-%d")
    sub_cats_str = ", ".join(set(sub_categories)) 
    
    header = "---\n"
    header += f"title: XS完整手冊 - {title}\n"
    header += f"category: {title}\n"
    header += f"tags: [XS語法, {title}, {sub_cats_str}]\n" 
    header += f"last_updated: {today}\n"
    header += f"total_functions: {file_count}\n"
    header += "---\n\n"
    header += f"# {title} (完整收錄)\n\n"
    header += f"> 本文件收錄了 [{title}] 下的所有子分類與函數說明，共 {file_count} 筆。\n"
    header += f"> 包含子分類：{sub_cats_str}\n\n"
    header += "---\n"
    return header

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    config = load_yaml_config(MKDOCS_CONFIG)
    if not config: return

    nav = config.get('nav', [])
    print(f"🚀 開始執行「頂層合併」(修正版)...")

    for item in nav:
        if isinstance(item, dict):
            for top_level_name, content in item.items():
                
                if top_level_name in ["首頁", "檢視紀錄", "搜尋記錄", "教學網站"]:
                    continue

                print(f"📂 正在處理: [{top_level_name}] ...")

                all_files = flatten_nav_structure(content)

                if not all_files:
                    continue

                merged_body = ""
                current_sub_category = None
                valid_count = 0
                sub_categories_list = []

                for sub_cat, file_path in all_files:
                    if sub_cat != current_sub_category:
                        merged_body += f"\n\n## {sub_cat}\n"
                        merged_body += "--- \n"
                        current_sub_category = sub_cat
                        sub_categories_list.append(sub_cat)

                    file_content = process_file_content(file_path, sub_cat)
                    
                    if file_content:
                        merged_body += file_content
                        merged_body += "\n___\n"
                        valid_count += 1

                if valid_count > 0:
                    front_matter = generate_front_matter(top_level_name, valid_count, sub_categories_list)
                    final_content = front_matter + merged_body
                    
                    filename = f"{top_level_name}.md".replace("/", "_")
                    output_path = Path(OUTPUT_DIR) / filename
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(final_content)
                    
                    print(f"   ✅ 成功合併 {valid_count} 個檔案 -> {filename}")

    print(f"\n🎉 完成！檔案已修正，內容應該都回來了。請查看 {OUTPUT_DIR}")

if __name__ == "__main__":
    main()