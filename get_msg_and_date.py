import os
from slack_sdk import WebClient
from datetime import datetime
from dotenv import load_dotenv

# .envを読み込み
load_dotenv()

SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID")

client = WebClient(token=SLACK_USER_TOKEN)

response = client.conversations_history(channel=CHANNEL_ID, limit=100)

with open("slack_log.txt", "w") as f:
    for msg in reversed(response["messages"]):  # 古い順に並べる
        ts = float(msg["ts"])
        dt = datetime.fromtimestamp(ts)
        dt_str = dt.strftime("%Y-%m-%d %H:%M")
        text = msg.get("text", "").replace("\n", " ").strip()
        f.write(f"[{dt_str}] {text}\n")

