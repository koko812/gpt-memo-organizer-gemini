import google.generativeai as genai
import os
import re
from collections import defaultdict
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# ログ読み込み
with open("slack_log.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

# 日付ごとにまとめる
day_blocks = defaultdict(list)
for line in lines:
    m = re.match(r"\[(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}\] (.+)", line)
    if m:
        date, content = m.groups()
        day_blocks[date].append(content)

# 出力先
OUTPUT_DIR = "summarized_memos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# タグまとめファイル
tag_summary_path = os.path.join(OUTPUT_DIR, "tags_summary.md")
with open(tag_summary_path, "w") as tag_file:
    tag_file.write("# タグまとめ\n\n")

# 日付ごとにGPTに渡す
for date, contents in day_blocks.items():
    joined_content = "\n".join(contents)
    prompt = f"""
以下は {date} のメモ一覧です。これらを文脈として捉え、**300文字以内で簡潔に要約し、読みやすいようにMarkdown形式（箇条書きや段落などを活用）で記述**し、仮タグ（5個）と関連メモ候補を生成してください。

メモ一覧：
{joined_content}

フォーマット：
### ✨ 要約（300文字以内、Markdown形式）
- （箇条書き）

### 🔖 自動タグ
- #tag1
- #tag2
- #tag3
- #tag4
- #tag5

### 🔗 関連メモ候補
- タイトルだけでよい（仮でもOK、メモっぽい形で3つ）
"""

    response = model.generate_content(prompt)
    response_text = response.text


    # 要約の冒頭30文字をファイル名の一部に（安全な文字だけ）
    ##title_match = re.search(r"### ✨ 要約.*?\n(.+?)\n", response_text, re.DOTALL)
    ##if title_match:
        ##title_snippet = title_match.group(1)[:30].strip()
        ##title_snippet = re.sub(r"[^\w\-]", "_", title_snippet)
   ## else:
     ##   title_snippet = "memo"

    output_file = os.path.join(OUTPUT_DIR, f"{date}.md")

    with open(output_file, "w") as out:
        out.write(response_text)

    print(f"✅ {output_file} を生成しました！")

    # タグだけ抽出してまとめファイルにも追記
    tag_match = re.search(r"### 🔖 自動タグ\n(.+?)\n\n", response_text, re.DOTALL)
    if tag_match:
        tags = tag_match.group(1).strip()
        with open(tag_summary_path, "a") as tag_file:
            tag_file.write(f"## {date}\n{tags}\n\n")

print(f"✅ タグまとめを {tag_summary_path} に生成しました！")

