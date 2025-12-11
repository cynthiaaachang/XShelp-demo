import argparse
import re
from pathlib import Path

import yaml


def read_title(md_path: Path) -> str:
    """讀取 md 檔第一個 H1(# ) 作為標題，沒有就用檔名。"""
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return md_path.stem

    for line in text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip() or md_path.stem
    return md_path.stem

def shorten_title(raw_title: str) -> str:
    """
    把像「估計量 – （報價欄位） <kbd>常用</kbd> <kbd>量能</kbd>」這種標題，
    截成「估計量」即可。

    規則：
    1. 如果有「 空格 + -/–/— + 空格 」後面接任何東西 → 只取前面
    2. 如果有 <kbd ...> → 只取 <kbd 之前的文字
    3. 都沒有就原樣返回
    """
    raw = raw_title.strip()
    if not raw:
        return raw

    # 1) 先處理 "名稱 – 後面一大串"
    m = re.match(r"^(.*?)(?:\s[–\-—]\s.*)$", raw)
    if m:
        raw = m.group(1).strip()

    # 2) 再處理 <kbd> 的情況
    if "<kbd" in raw:
        raw = raw.split("<kbd", 1)[0].strip()

    return raw or raw_title



def build_nav_tree_for_root(root: Path, docs_dir: Path) -> list[dict]:
    """
    root: 例如 docs/quote-fields
    回傳 nav 用的結構：

    [
      {"常用": [ { "委比": "quote-fields/常用/委比.md" }, ... ]},
      {"價格": [...]},
      ...
    ]
    """

    # 🔽 這裡定義你要的資料夾順序（沒有出現在列表裡的，會排在最後、照名稱排序）
    preferred_order = [
        "常用",
        "價格",
        "量能",
        "財務",
        "籌碼",        
        "基本",
        "事件",
        "市場統計",
        "期權",
        "五檔統計",                
        "其他",
    ]
    order_index = {name: i for i, name in enumerate(preferred_order)}

    def folder_sort_key(p: Path):
        # 先看有沒有在 preferred_order 裡，有的照順序；其他的排在後面
        return (order_index.get(p.name, 9999), p.name)

    sections: list[dict] = []

    # ✅ 使用自訂排序，而不是單純 sorted(root.iterdir())
    for sub in sorted(root.iterdir(), key=folder_sort_key):
        if not sub.is_dir():
            continue

        sub_title = sub.name  # 例如 "五檔統計"
        items: list[dict] = []

        for md in sorted(sub.glob("*.md")):
            if md.name.lower() == "readme.md":
                continue

            raw_title = read_title(md)
            title = shorten_title(raw_title)

            rel_path = md.relative_to(docs_dir).as_posix()
            items.append({title: rel_path})



        if items:
            sections.append({sub_title: items})

    return sections



def update_nav_section(nav: list, section_title: str, section_items: list[dict]) -> list:
    """
    在 nav 裡更新 / 新增某個區塊 (例如 section_title='報價欄位')：

    - 如果 nav 中有多個同名區塊，會被「合併成一個」，
      避免每次執行都多長出一個。
    - 會保留原本區塊裡的 README / index 連結
      （例如 '總覽: quote-fields/README.md'），
      其它舊項目一律視為「舊的自動產生內容」，會被新的覆蓋掉。
    - 如果 nav 中沒有這個區塊，就直接在最後新增一段。
    """
    if nav is None:
        return [{section_title: section_items}]

    first_idx = None
    existing_keep_items = []
    new_nav = []

    for entry in nav:
        if isinstance(entry, dict) and section_title in entry:
            items = entry.get(section_title) or []

            # 第一次遇到這個區塊 → 保留 README / index 類型的項目
            if first_idx is None:
                first_idx = len(new_nav)

                for it in items:
                    if isinstance(it, dict):
                        label, path = next(iter(it.items()))
                        if isinstance(path, str) and (
                            path.endswith("README.md") or path.endswith("index.md")
                        ):
                            existing_keep_items.append(it)
                    else:
                        # 非 dict 的特殊項目，一律保留
                        existing_keep_items.append(it)

                # 先放一個 placeholder，待會再覆蓋
                new_nav.append({section_title: []})
            else:
                # 之後再遇到同名區塊，一律略過（視為重複）
                continue
        else:
            new_nav.append(entry)

    # nav 中原本沒有這個區塊 → 直接新增
    if first_idx is None:
        new_nav.append({section_title: section_items})
    else:
        # 用「保留的項目 + 新生成的 items」覆蓋原本區塊
        new_nav[first_idx] = {section_title: existing_keep_items + section_items}

    return new_nav




def main():
    parser = argparse.ArgumentParser(
        description="依 docs/quote-fields 子資料夾自動更新 mkdocs.yml nav 區塊"
    )
    parser.add_argument("mkdocs_yml", help="mkdocs.yml 路徑，例如 mkdocs.yml")
    parser.add_argument(
        "root_folder",
        help="quote-fields 根目錄，例如 docs/quote-fields",
    )
    parser.add_argument(
        "--section-title",
        help="nav 裡顯示的區塊名稱（例如 報價欄位）；預設用資料夾名稱。",
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="MkDocs 的 docs_dir，預設為 docs",
    )

    args = parser.parse_args()

    mkdocs_path = Path(args.mkdocs_yml)
    root = Path(args.root_folder)
    docs_dir = Path(args.docs_dir)

    if not mkdocs_path.exists():
        raise FileNotFoundError(f"找不到 mkdocs.yml：{mkdocs_path}")
    if not root.exists() or not root.is_dir():
        raise NotADirectoryError(f"資料夾不存在或不是資料夾：{root}")

    section_title = args.section_title or root.name  # 例如 "quote-fields"

    # 1) 讀 mkdocs.yml
    config = yaml.safe_load(mkdocs_path.read_text(encoding="utf-8")) or {}
    nav = config.get("nav", [])

    # 2) 生成 nav 結構
    section_items = build_nav_tree_for_root(root, docs_dir)
    if not section_items:
        print(f"⚠️ {root} 底下沒有子資料夾或 md 檔，未更新 nav。")
        return

    # 3) 更新 nav
    nav = update_nav_section(nav, section_title, section_items)
    config["nav"] = nav

    # 4) 寫回 mkdocs.yml
    mkdocs_path.write_text(
        yaml.safe_dump(
            config,
            allow_unicode=True,  # 重要：支援中文
            sort_keys=False,
            width=1000,
        ),
        encoding="utf-8",
    )

    print(f"✅ 已更新 mkdocs.yml nav 區塊：{section_title}")
    print(f"   來源資料夾：{root}")


if __name__ == "__main__":
    main()
