"""一个最简单的命令行聊天机器人(多轮对话,带上下文)。Ctrl+C 退出。

    export COCODOT_API_KEY=你的Key
    python chatbot.py
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)
MODEL = "mco-6"  # Claude Opus 4.8

messages = [{"role": "system", "content": "你是一个简洁、友好的助手。"}]
print(f"cocodot 聊天机器人({MODEL})—— 输入消息开始,Ctrl+C 退出\n")

try:
    while True:
        user = input("你: ").strip()
        if not user:
            continue
        messages.append({"role": "user", "content": user})
        reply = client.chat.completions.create(model=MODEL, messages=messages).choices[0].message.content
        print(f"AI: {reply}\n")
        messages.append({"role": "assistant", "content": reply})
except (KeyboardInterrupt, EOFError):
    print("\n再见!")
