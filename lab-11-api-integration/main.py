"""
lab-11-api-integration: 调用外部 API（requests / httpx）

运行时会展示：requests 同步 GET、httpx 同步/异步 GET，以及 response.json()、raise_for_status()。
"""
import asyncio

print("=== 1. requests 同步调用 ===\n")
print("  >>> [说明] requests.get(url, params=..., timeout=...) 发 GET；.json() 解析 JSON")
try:
    import requests
    r = requests.get("https://httpbin.org/get", params={"foo": "bar"}, timeout=10)
    r.raise_for_status()
    data = r.json()
    print(f"  >>> [触发] 收到 args: {data.get('args')}, url: {data.get('url')}")
except Exception as e:
    print(f"  请求失败（需网络）: {e}\n")

print("=== 2. httpx 同步调用 ===\n")
print("  >>> [说明] with httpx.Client() 可复用连接；接口与 requests 类似")
try:
    import httpx
    with httpx.Client(timeout=10) as client:
        r = client.get("https://httpbin.org/get", params={"baz": "qux"})
        r.raise_for_status()
        data = r.json()
        print(f"  >>> [触发] 收到 args: {data.get('args')}")
except Exception as e:
    print(f"  请求失败: {e}\n")

print("=== 3. httpx 异步调用 ===\n")
print("  >>> [说明] async with httpx.AsyncClient() 与 await client.get()，适合与 asyncio 配合")


async def with_httpx_async():
    try:
        import httpx
        async with httpx.AsyncClient(timeout=10) as client:
            r = await client.get("https://httpbin.org/get", params={"async": "true"})
            r.raise_for_status()
            data = r.json()
            print(f"  >>> [触发] 收到 args: {data.get('args')}")
    except Exception as e:
        print(f"  请求失败: {e}")


asyncio.run(with_httpx_async())
print("\n  >>> [小结] FastAPI 生态常用 httpx；需要并发请求时用异步更高效")
