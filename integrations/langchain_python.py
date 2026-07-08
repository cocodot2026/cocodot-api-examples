"""用 LangChain 调 cocodot —— 因为是 OpenAI 兼容,标准 ChatOpenAI 只改 base_url 即可。

    pip install langchain-openai
    export COCODOT_API_KEY=你的Key
    python langchain_python.py
"""
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="mco-6",  # Claude Opus 4.8;换 mog-6=GPT-5.5 / mgg-8=Gemini 3.1 Pro / deepseek-v3.2
    base_url="https://cocodot.co/api/ai/v1",
    api_key=os.environ["COCODOT_API_KEY"],
)

print(llm.invoke("用一句话解释什么是 LangChain").content)
