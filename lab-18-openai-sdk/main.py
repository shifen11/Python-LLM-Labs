"""
lab-13-openai-sdk: 流式输出与 Token 计算

运行时会展示：模拟流式输出（无 KEY 时）、粗略 Token 估算、以及真实 OpenAI 流式调用（需 OPENAI_API_KEY）。
"""


def rough_token_count(text: str) -> int:
    """粗略 Token 估算：英文约 4 字符/token，中文约 1.5 字符/token"""
    en = sum(1 for c in text if ord(c) < 128)
    other = len(text) - en
    return max(1, en // 4 + int(other / 1.5))


print("=== 1. 模拟流式输出（无 API Key 时用）===\n")
print("  >>> [说明] 流式：服务端边生成边推送，客户端边收边显示，降低首字延迟")
chunks = ["Hello", ", ", "world", "!", " ", "This ", "is ", "streaming."]
print("  mock stream: ", end="", flush=True)
for c in chunks:
    print(c, end="", flush=True)
print()
full = "".join(chunks)
print(f"  >>> [触发] 粗略 token 数: {rough_token_count(full)}\n")

print("=== 2. 真实 OpenAI 流式调用（需 OPENAI_API_KEY）===\n")
print("  >>> [说明] client.chat.completions.create(..., stream=True) 返回迭代器，逐块取 delta")


def real_streaming():
    try:
        from openai import OpenAI
        client = OpenAI()
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hi' in 5 words."}],
            stream=True,
        )
        print("  openai stream: ", end="", flush=True)
        full = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            full += delta
            print(delta, end="", flush=True)
        print()
        print(f"  >>> [触发] 粗略 token 数: {rough_token_count(full)}")
    except Exception as e:
        print(f"  OpenAI 流式失败（未设置 KEY 或网络）: {e}")


real_streaming()
