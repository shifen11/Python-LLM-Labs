"""
lab-11 练习题：调用外部 API
运行: python exercises.py（需网络）
需安装: pip install requests httpx
"""


# ========== 练习 1 ==========
# 用 requests.get("https://httpbin.org/get", params={"key": "value"}, timeout=5) 发 GET，打印 response.status_code 和 response.json() 的 "args"
# 期望输出: 200 和 {'key': 'value'}
def exercise_1():
    pass


# ========== 练习 2 ==========
# 用 httpx 同步：with httpx.Client(timeout=5) as client: r = client.get("https://httpbin.org/get", params={"foo": "bar"})，打印 r.json()["args"]
# 期望输出: {'foo': 'bar'}
def exercise_2():
    pass


# ========== 练习 3 ==========
# 用 httpx 异步：async with httpx.AsyncClient(timeout=5) as client: r = await client.get(...)，在 asyncio.run 里调用并打印
# 期望输出: 与同步类似的 args（需网络）
def exercise_3():
    pass


if __name__ == "__main__":
    print("=== 练习 1 ===")
    exercise_1()
    print("  [期望] 200 和 args 含传入的 params（需网络）")
    print("\n=== 练习 2 ===")
    exercise_2()
    print("  [期望] args 含 foo=bar（需网络）")
    print("\n=== 练习 3 ===")
    exercise_3()
    print("  [期望] 同上（异步，需网络）")
