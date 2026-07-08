// 流式输出示例 —— 和官方 OpenAI 的 stream 用法完全一致。
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://cocodot.co/api/ai/v1",
  apiKey: process.env.COCODOT_API_KEY,
});

const stream = await client.chat.completions.create({
  model: "mog-6", // GPT-5.5
  messages: [{ role: "user", content: "写一首关于代码的四行小诗" }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
process.stdout.write("\n");
