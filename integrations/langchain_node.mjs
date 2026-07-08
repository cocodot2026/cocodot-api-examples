// 用 LangChain.js 调 cocodot(OpenAI 兼容)。
//   npm i @langchain/openai @langchain/core
//   export COCODOT_API_KEY=你的Key && node langchain_node.mjs
import { ChatOpenAI } from "@langchain/openai";

const llm = new ChatOpenAI({
  model: "mco-6", // Claude Opus 4.8
  apiKey: process.env.COCODOT_API_KEY,
  configuration: { baseURL: "https://cocodot.co/api/ai/v1" },
});

const res = await llm.invoke("用一句话解释什么是 LangChain");
console.log(res.content);
