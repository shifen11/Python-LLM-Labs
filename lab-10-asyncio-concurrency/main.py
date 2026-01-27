"""
lab-10-asyncio-concurrency: async/await 异步模型
"""
import asyncio
import time


async def fetch(id: int, delay: float):
    """模拟 IO 操作"""
    print(f"  fetch({id}) start")
    await asyncio.sleep(delay)
    print(f"  fetch({id}) done")
    return id


async def main():
    print("=== 顺序 await ===")
    t0 = time.perf_counter()
    a = await fetch(1, 0.2)
    b = await fetch(2, 0.2)
    print(f"  result: {a}, {b}, elapsed: {time.perf_counter() - t0:.2f}s\n")

    print("=== asyncio.gather 并发 ===")
    t0 = time.perf_counter()
    results = await asyncio.gather(fetch(3, 0.2), fetch(4, 0.2), fetch(5, 0.2))
    print(f"  result: {results}, elapsed: {time.perf_counter() - t0:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
