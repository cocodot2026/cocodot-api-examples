# cocodot AI API 示例 · 用 OpenAI SDK 在国内调 Claude / GPT / Gemini

> 在中国大陆,用你熟悉的 **OpenAI SDK**、改两个参数,就能调用 **Claude、GPT、Gemini、DeepSeek** —— 人民币(支付宝)付费,不用海外信用卡。
>
> 本仓库是 [cocodot](https://cocodot.co) AI API 中转的**极简示例**(Python + Node.js),复制即可跑。

[English below ↓](#english)

---

## 为什么需要它

国内直接用 Claude、OpenAI 官方 API 有三道坎:

1. **支付** —— 官方只收海外信用卡,支付宝 / 微信付不进;
2. **网络** —— 官方端点在海外,国内直连高延迟、易超时;
3. **风控** —— 非常规手段调用容易触发封号。

cocodot 提供一个 **OpenAI 兼容**的接入:支付宝充值、一个 Key 调多家模型、把 `base_url` 一换就能用,现有 OpenAI 代码几乎不动。

## 60 秒上手

1. 注册 [cocodot.co](https://cocodot.co),用**支付宝小额充值**(余额 > 0 才能调用,按量计费)
2. 在控制台创建一个 **API Key**
3. 把这两个参数填进任意 OpenAI SDK 代码:
   - `base_url` = `https://cocodot.co/api/ai/v1`
   - `api_key` = 你的 Key
4. `model` 填**调用代号**(见下表),其余和官方 OpenAI 用法完全一样

### Python
```bash
pip install openai
export COCODOT_API_KEY=你的Key      # Windows: set COCODOT_API_KEY=...
python python/chat.py
```

### Node.js
```bash
cd node && npm install
export COCODOT_API_KEY=你的Key
node chat.mjs
```

## 模型调用代号

| 模型 | `model` 代号 |
|---|---|
| Claude Opus 4.8 | `mco-6` |
| Claude Sonnet 4.6 | `mcs-5` |
| GPT-5.5 | `mog-6` |
| Gemini 3.1 Pro | `mgg-8` |
| DeepSeek V3.2 | `deepseek-v3.2` |

> 完整型号与价格以 [控制台模型列表](https://cocodot.co/api-access) 为准。**一个 Key 切换 `model` 即可调不同模型**,方便做对比和容灾。

## 示例

| 文件 | 作用 |
|---|---|
| `python/chat.py` · `node/chat.mjs` | 最简单的一次对话 |
| `python/stream.py` · `node/stream.mjs` | 流式输出 |
| `python/multi_model.py` · `node/multi-model.mjs` | 一个 Key,按任务切 Claude / GPT / DeepSeek（省成本） |
| `python/chatbot.py` · `node/chatbot.mjs` | 命令行多轮聊天机器人 |
| `python/batch_async.py` | 并发批量调用（适合批处理 / Agent） |

完整模型代号见 [MODELS.md](./MODELS.md)。

## 整合 LangChain / Vercel AI SDK / Cursor / Cline

因为是 OpenAI 兼容,主流框架和工具都能接,通常只改 `base_url` + `api_key`(详见 [`integrations/`](./integrations/)):

| 框架 / 工具 | 示例 |
|---|---|
| LangChain · Python | [`integrations/langchain_python.py`](./integrations/langchain_python.py) |
| LangChain · Node | [`integrations/langchain_node.mjs`](./integrations/langchain_node.mjs) |
| Vercel AI SDK | [`integrations/vercel-ai-sdk.mjs`](./integrations/vercel-ai-sdk.mjs) |
| Cursor / Cline / Roo Code | [配置说明](./integrations/README.md) |

## 说明

- 接口是 **OpenAI 格式**,适配 OpenAI SDK,以及 **Cursor / Cline** 等支持自定义 OpenAI 端点的工具。
- **Claude Code** 走 Anthropic 专有格式,不吃本 OpenAI 接口 —— 但 cocodot 另有 **Anthropic 兼容端点**(BETA),设 `ANTHROPIC_BASE_URL=https://cocodot.co/api/ai` 即可让 Claude Code 直连,见 [Claude Code 国内直连教程](https://cocodot.co/hub/claude-code-china-direct)。官方 Claude.ai 网页版不适用。
- 需先充值(余额 > 0)才能调用;**注册后验证邮箱送 $0.5 体验额度**,可先免费跑通验证,再小额充值加量。

## 常见问题

**用什么付费?** 支付宝人民币充值,不用海外信用卡。需先充值(余额 > 0)才能调用,无免费额度。

**和官方 OpenAI / Claude 用法一样吗?** 一样 —— OpenAI 兼容,改 `base_url` + `api_key` 即可,现有代码几乎不动。

**能用 Claude Code 吗?** 能(BETA)。Claude Code 走 Anthropic 专有格式(`/v1/messages`),本仓库的 OpenAI 接口不适用,但 cocodot 提供了 Anthropic 兼容端点:`export ANTHROPIC_BASE_URL=https://cocodot.co/api/ai` + `export ANTHROPIC_AUTH_TOKEN=你的Key` 即可直连,详见 [教程](https://cocodot.co/hub/claude-code-china-direct)。Cursor / Cline 这类 OpenAI 兼容工具走本仓库的方式。

**支持哪些模型?** Claude、GPT、Gemini、DeepSeek 等,见 [MODELS.md](./MODELS.md),一个 Key 切换 `model` 调用。

## 延伸阅读

- [2026 国内接入 Claude / ChatGPT API 完全指南](https://cocodot.co/hub/claude-gpt-api-china-guide)
- [Claude / OpenAI API 人民币充值:支付宝直充,不用海外卡](https://cocodot.co/hub/ai-api-alipay-cny-recharge)
- [Cursor / Cline 接入国内中转 API](https://cocodot.co/hub/cursor-cline-openai-relay-china)

---

## English

Minimal examples for calling **Claude / GPT / Gemini / DeepSeek via the OpenAI SDK from mainland China**, using [cocodot](https://cocodot.co)'s OpenAI-compatible API — pay in CNY (Alipay), no overseas credit card needed.

Set `base_url` to `https://cocodot.co/api/ai/v1`, use your cocodot API key, and pick a model code (`mco-6` = Claude Opus 4.8, `mog-6` = GPT-5.5, `mgg-8` = Gemini 3.1 Pro, `deepseek-v3.2` = DeepSeek). Everything else is standard OpenAI SDK.

```python
from openai import OpenAI

client = OpenAI(base_url="https://cocodot.co/api/ai/v1", api_key="YOUR_KEY")
r = client.chat.completions.create(
    model="mco-6",  # Claude Opus 4.8
    messages=[{"role": "user", "content": "Hello"}],
)
print(r.choices[0].message.content)
```

**Notes:** OpenAI-compatible (works with OpenAI SDK, Cursor, Cline). **Claude Code** is also supported via cocodot's Anthropic-compatible endpoint (beta): set `ANTHROPIC_BASE_URL=https://cocodot.co/api/ai` — see the [guide](https://cocodot.co/claude-code). Verify your email after signup for $0.5 free credit, then top up as needed.

## License

[MIT](./LICENSE)
