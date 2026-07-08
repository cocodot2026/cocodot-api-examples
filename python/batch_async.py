"""并发批量调用 —— 适合批处理 / Agent 场景。用 AsyncOpenAI + asyncio.gather 同时发多个请求。

    export COCODOT_API_KEY=你的Key
    python batch_async.py
"""
import asyncio
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)

PROMPTS = [
    "把'今天天气不错'翻译成英文",
    "把'我喜欢编程'翻译成英文",
    "把'人工智能很有趣'翻译成英文",
]


async def one(prompt: str) -> str:
    r = await client.chat.completions.create(
        model="deepseek-v3.2",  # 批量任务用便宜的国产模型省成本
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content


async def main():
    results = await asyncio.gather(*(one(p) for p in PROMPTS))
    for prompt, result in zip(PROMPTS, results):
        print(f"- {prompt}  →  {result}")


asyncio.run(main())
