// 最简单的命令行聊天机器人(多轮对话,带上下文)。Ctrl+C 退出。
//   export COCODOT_API_KEY=你的Key && node chatbot.mjs
import OpenAI from "openai";
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const client = new OpenAI({
  baseURL: "https://cocodot.co/api/ai/v1",
  apiKey: process.env.COCODOT_API_KEY,
});
const MODEL = "mco-6"; // Claude Opus 4.8

const rl = readline.createInterface({ input, output });
const messages = [{ role: "system", content: "你是一个简洁、友好的助手。" }];

console.log(`cocodot 聊天机器人(${MODEL})—— 输入消息开始,Ctrl+C 退出\n`);

while (true) {
  const user = (await rl.question("你: ")).trim();
  if (!user) continue;
  messages.push({ role: "user", content: user });
  const reply = (await client.chat.completions.create({ model: MODEL, messages })).choices[0].message.content;
  console.log(`AI: ${reply}\n`);
  messages.push({ role: "assistant", content: reply });
}
