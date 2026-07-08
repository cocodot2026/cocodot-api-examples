// 最简单的一次对话 —— 用 OpenAI SDK 通过 cocodot 调 Claude / GPT / Gemini。
// 运行前: npm install  且  export COCODOT_API_KEY=你的Key  然后  node chat.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://cocodot.co/api/ai/v1",
  apiKey: process.env.COCODOT_API_KEY,
});

const resp = await client.chat.completions.create({
  // mco-6 = Claude Opus 4.8;换 mog-6=GPT-5.5 / mgg-8=Gemini 3.1 Pro / deepseek-v3.2=DeepSeek
  model: "mco-6",
  messages: [{ role: "user", content: "用一句话解释什么是向量数据库" }],
});

console.log(resp.choices[0].message.content);
