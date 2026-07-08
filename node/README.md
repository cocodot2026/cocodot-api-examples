# Node.js 示例

需要 Node 18+(自带全局 `fetch`)。

```bash
npm install
export COCODOT_API_KEY=你的Key      # Windows: set COCODOT_API_KEY=...
node chat.mjs
```

| 文件 | 作用 |
|---|---|
| `chat.mjs` | 一次对话 |
| `stream.mjs` | 流式输出 |
| `multi-model.mjs` | 一个 Key 切多模型(省成本) |

`baseURL` 固定为 `https://cocodot.co/api/ai/v1`。在 [cocodot.co](https://cocodot.co) 注册 → 支付宝充值 → 控制台建 Key。模型代号见 [仓库主页](../README.md#模型调用代号)。
