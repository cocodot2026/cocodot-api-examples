# 模型代号对照

调用时把 `model` 填成下面的**代号**(以 [cocodot 控制台模型列表](https://cocodot.co/api-access) 为准,代号可能随版本更新)。一个 Key 切换 `model` 即可调不同模型。

## 海外模型

| 模型 | 代号 | 适合 |
|---|---|---|
| Claude Opus 4.8 | `mco-6` | 复杂推理、长代码、关键输出(顶配) |
| Claude Sonnet 4.6 | `mcs-5` | 日常对话、写作,性价比高 |
| GPT-5.5 | `mog-6` | 通用、推理、工具调用 |
| Gemini 3.1 Pro | `mgg-8` | 多模态、超长上下文 |

## 国产模型(单价更低,适合高频 / 批量)

| 模型 | 代号 | 适合 |
|---|---|---|
| DeepSeek V3.2 | `deepseek-v3.2` | 中文、通用、代码辅助,便宜 |

> 省钱思路:**高频 / 简单 / 批量任务**用国产(如 `deepseek-v3.2`),**难 / 关键任务**用顶配(如 `mco-6`)。示例见 `python/multi_model.py` 与 `node/multi-model.mjs`。
