"""最简单的一次对话 —— 用 OpenAI SDK 通过 cocodot 调 Claude / GPT / Gemini。

运行前:
    pip install openai
    export COCODOT_API_KEY=你的Key
    python chat.py
"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)

resp = client.chat.completions.create(
    # mco-6 = Claude Opus 4.8;换成 mog-6=GPT-5.5 / mgg-8=Gemini 3.1 Pro / deepseek-v3.2=DeepSeek
    model="mco-6",
    messages=[{"role": "user", "content": "用一句话解释什么是向量数据库"}],
)

print(resp.choices[0].message.content)
