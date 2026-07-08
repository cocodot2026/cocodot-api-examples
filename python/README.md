# Python 示例

```bash
pip install -r requirements.txt
export COCODOT_API_KEY=你的Key      # Windows: set COCODOT_API_KEY=...
python chat.py
```

| 文件 | 作用 |
|---|---|
| `chat.py` | 一次对话 |
| `stream.py` | 流式输出 |
| `multi_model.py` | 一个 Key 切多模型(省成本) |

`base_url` 固定为 `https://cocodot.co/api/ai/v1`。在 [cocodot.co](https://cocodot.co) 注册 → 支付宝充值 → 控制台建 Key。模型代号见 [仓库主页](../README.md#模型调用代号)。
