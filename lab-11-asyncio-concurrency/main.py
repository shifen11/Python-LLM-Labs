"""
lab-10-asyncio-concurrency: async/await 异步模型

运行时会展示：顺序 await 与 asyncio.gather 并发的耗时差异，理解「协程」与「事件循环」。
"""
import asyncio
import time


async def fetch(id: int, delay: float):
    """模拟 IO 操作（如请求 API）：等待 delay 秒后返回 id"""
    print(f"  >>> [协程 {id}] 开始等待 {delay}s")
    await asyncio.sleep(delay)
    print(f"  >>> [协程 {id}] 完成")
    return id


async def main():
    print("=== 1. 顺序 await（串行）===\n")
    print("  >>> [说明] 先 await fetch(1) 完成，再 await fetch(2)，总耗时约 0.2+0.2s")
    t0 = time.perf_counter()
    a = await fetch(1, 0.2)
    b = await fetch(2, 0.2)
    elapsed = time.perf_counter() - t0
    print(f"  结果: a={a}, b={b}, 总耗时: {elapsed:.2f}s\n")

    print("=== 2. asyncio.gather 并发（并行等待）===\n")
    print("  >>> [说明] 三个协程同时「挂起」等待，事件循环在它们之间切换，总耗时约 0.2s")
    t0 = time.perf_counter()
    results = await asyncio.gather(fetch(3, 0.2), fetch(4, 0.2), fetch(5, 0.2))
    elapsed = time.perf_counter() - t0
    print(f"  结果: {results}, 总耗时: {elapsed:.2f}s")
    print("  >>> [小结] 高 IO、低 CPU 场景用 async 可显著缩短总时间")


if __name__ == "__main__":
    asyncio.run(main())
