// 用 Vercel AI SDK 调 cocodot(OpenAI 兼容 provider)。
//   npm i ai @ai-sdk/openai
//   export COCODOT_API_KEY=你的Key && node vercel-ai-sdk.mjs
import { createOpenAI } from "@ai-sdk/openai";
import { generateText } from "ai";

const cocodot = createOpenAI({
  baseURL: "https://cocodot.co/api/ai/v1",
  apiKey: process.env.COCODOT_API_KEY,
});

const { text } = await generateText({
  model: cocodot("mog-6"), // GPT-5.5;换 mco-6=Claude / mgg-8=Gemini / deepseek-v3.2
  prompt: "用一句话解释什么是 Vercel AI SDK",
});

console.log(text);
