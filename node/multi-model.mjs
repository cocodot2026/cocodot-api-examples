// 一个 Key,按任务切不同模型 —— 便宜任务给国产、难任务给顶配,省成本。
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://cocodot.co/api/ai/v1",
  apiKey: process.env.COCODOT_API_KEY,
});

async function ask(model, prompt) {
  const r = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: prompt }],
  });
  return r.choices[0].message.content;
}

// 简单 / 批量任务 → 便宜的国产模型
console.log("[DeepSeek]      ", await ask("deepseek-v3.2", "把这句话翻译成英文:今天天气不错"));

// 难 / 关键任务 → 顶配模型
console.log("[Claude Opus 4.8]", await ask("mco-6", "用三步证明根号 2 是无理数"));
