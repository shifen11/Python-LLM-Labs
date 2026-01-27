"""
lab-13-openai-sdk: 流式输出与 Token 计算
"""
import os


def rough_token_count(text: str) -> int:
    """粗略 Token 估算：英文 ~4 字符/token，中文 ~1.5 字符/token"""
    en = sum(1 for c in text if ord(c) < 128)
    other = len(text) - en
    return max(1, en // 4 + int(other / 1.5))


def mock_streaming():
    """模拟流式输出（无 API Key 时用）"""
    chunks = ["Hello", ", ", "world", "!", " ", "This ", "is ", "streaming."]
    print("mock stream: ", end="", flush=True)
    for c in chunks:
        print(c, end="", flush=True)
    print()
    full = "".join(chunks)
    print(f"rough tokens: {rough_token_count(full)}")


def real_streaming():
    """真实 OpenAI 流式调用（需 OPENAI_API_KEY）"""
    try:
        from openai import OpenAI
        client = OpenAI()
        stream = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say 'Hi' in 5 words."}],
            stream=True,
        )
        print("openai stream: ", end="", flush=True)
        full = ""
        for chunk in stream:
            delta = chunk.choices[0].delta.content or ""
            full += delta
            print(delta, end="", flush=True)
        print()
        print(f"rough tokens: {rough_token_count(full)}")
    except Exception as e:
        print("OpenAI stream failed (missing key?):", e)


if __name__ == "__main__":
    print("=== 模拟流式 + Token 估算 ===")
    mock_streaming()
    print("\n=== 真实 OpenAI 流式（若有 KEY）===")
    real_streaming()
