# 框架与工具整合

cocodot 是 **OpenAI 兼容**接口,所以几乎所有支持"自定义 OpenAI 端点"的框架/工具都能接 —— 通常只改 `base_url`(或 `baseURL`)+ `api_key` 两个值。

接入地址:`https://cocodot.co/api/ai/v1` · 在 [cocodot.co](https://cocodot.co) 注册 → 支付宝充值 → 控制台建 Key。

## LangChain
- Python:`langchain_python.py`(`pip install langchain-openai`)
- Node:`langchain_node.mjs`(`npm i @langchain/openai`)

关键:把 `ChatOpenAI` 的 `base_url`/`configuration.baseURL` 指向 cocodot,`model` 填代号(如 `mco-6`)。

## Vercel AI SDK
- `vercel-ai-sdk.mjs`(`npm i ai @ai-sdk/openai`)

用 `createOpenAI({ baseURL, apiKey })` 造一个 provider,再 `generateText({ model: cocodot("mog-6"), ... })`。

## Cursor
设置 → **Models** → 勾选 **Override OpenAI Base URL**:
- Base URL:`https://cocodot.co/api/ai/v1`
- API Key:你的 cocodot Key
- 模型名填代号(如 `mog-6` = GPT-5.5)

详见教程:[Cursor / Cline 接入国内中转 API](https://cocodot.co/hub/cursor-cline-openai-relay-china)

## Cline / Roo Code(VS Code 插件)
设置里 API Provider 选 **OpenAI Compatible**:
- Base URL:`https://cocodot.co/api/ai/v1`
- API Key:你的 cocodot Key
- Model:代号(如 `mco-6`)

## ⚠️ 不兼容
**Claude Code、官方 Claude.ai** 用的是 Anthropic 专有格式(`/v1/messages`),与 OpenAI 格式不通用,**不能**用本接口接。
