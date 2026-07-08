"""一个 Key,按任务切不同模型 —— 便宜任务给国产、难任务给顶配,省成本。"""
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)


def ask(model: str, prompt: str) -> str:
    r = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return r.choices[0].message.content


# 简单 / 批量任务 → 便宜的国产模型
print("[DeepSeek]      ", ask("deepseek-v3.2", "把这句话翻译成英文:今天天气不错"))

# 难 / 关键任务 → 顶配模型
print("[Claude Opus 4.8]", ask("mco-6", "用三步证明根号 2 是无理数"))
