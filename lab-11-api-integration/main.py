"""
lab-11-api-integration: httpx / requests 调用外部 API
"""
import httpx
import requests


def with_requests():
    """requests 同步调用"""
    r = requests.get("https://httpbin.org/get", params={"foo": "bar"}, timeout=10)
    r.raise_for_status()
    data = r.json()
    print("requests GET:", data.get("args"), data.get("url"))


def with_httpx_sync():
    """httpx 同步调用"""
    with httpx.Client(timeout=10) as client:
        r = client.get("https://httpbin.org/get", params={"baz": "qux"})
        r.raise_for_status()
        data = r.json()
        print("httpx GET:", data.get("args"), data.get("url"))


async def with_httpx_async():
    """httpx 异步调用"""
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get("https://httpbin.org/get", params={"async": "true"})
        r.raise_for_status()
        data = r.json()
        print("httpx async GET:", data.get("args"), data.get("url"))


if __name__ == "__main__":
    print("=== requests ===")
    with_requests()
    print("\n=== httpx sync ===")
    with_httpx_sync()
    print("\n=== httpx async ===")
    import asyncio
    asyncio.run(with_httpx_async())
