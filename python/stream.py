"""流式输出示例 —— 和官方 OpenAI 的 stream 用法完全一致。"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)

stream = client.chat.completions.create(
    model="mog-6",  # GPT-5.5
    messages=[{"role": "user", "content": "写一首关于代码的四行小诗"}],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
print()
