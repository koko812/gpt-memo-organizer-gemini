
# 🧠 GPTメモ整理システム（Gemini版）

ChatGPTやSlackで溜まったメモを、Google Gemini API（無料枠OK！）の力を借りて**自動要約・自動タグ付け・関連メモ探索**する、超シンプルなPythonスクリプト集です。

## 🚀 できること
- 手元のメモ（Slackログなど）を1行1メモで準備
- Gemini APIを使って、各メモを要約
- GPTが自動で仮タグを付与（タグ付け面倒問題を解決）
- 過去メモとの類似候補を自動で提案
- Markdownで保存 → ObsidianやVSCodeで快適整理

## 💡 特徴
- ✅ Gemini API（1.5 Flash / Pro）対応
- ✅ 超低コスト（Flashなら無料枠で爆速処理可能）
- ✅ Pythonだけで動くシンプル設計
- ✅ トークン数＆コスト見積もりもできる（予定）

## 📦 セットアップ

```bash
pip install google-generativeai
```

`.env` か直接スクリプト内で `GOOGLE_API_KEY` を設定してください。

## 📄 使い方

1. Slackログなどを `slack_log.txt` に1行1メモで保存
2. スクリプトを実行
3. `memo_1.md`, `memo_2.md` ... が生成される

```bash
python gemini_memo_summarizer.py
```

## 📊 コスト意識
- Gemini APIは**1.5 Flash推奨**
- Flashなら、**無料枠内で気にせず試せる**
- 必要なら、`CountTokens` APIで事前にトークン計算も可能

## 🚧 今後の予定
- SlackエクスポートJSONから直接処理
- Markdown出力にObsidianリンク対応
- 過去メモ自動検索＆リンク機能強化

## 🐣 注意
- まだ超シンプル版です
- 改良・Fork大歓迎！

---

## 🤝 クレジット
- Powered by [Google Generative AI](https://cloud.google.com/vertex-ai/generative-ai)
- アイデア by あなたとChatGPTの対話✨
