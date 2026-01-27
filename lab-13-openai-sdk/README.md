# lab-13-openai-sdk

**流式输出（Streaming）与 Token 计算**

## 知识点

- OpenAI Python SDK：`openai.ChatCompletion` / `openai.chat.completions.create`
- 流式响应 `stream=True`，迭代 `response`
- Token 估算：`tiktoken` 或简单启发式（本 demo 含简化估算）

## 运行

```bash
pip install openai
# 设置环境变量 OPENAI_API_KEY，或代码中配置 base_url + api_key
python main.py
```

无 API Key 时，demo 使用**模拟流式输出**与**本地 token 估算**，可先跑通逻辑。
