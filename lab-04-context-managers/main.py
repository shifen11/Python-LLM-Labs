"""
lab-04-context-managers: with 与上下文管理器
"""
from contextlib import contextmanager


class Timer:
    """类形式：__enter__ / __exit__"""

    def __enter__(self):
        import time
        self.start = time.perf_counter()
        print("[Timer] start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        elapsed = time.perf_counter() - self.start
        print(f"[Timer] elapsed {elapsed:.4f}s")
        return False  # 不吞掉异常


@contextmanager
def managed_list():
    """生成器形式：@contextmanager + yield"""
    data = []
    print("[managed_list] setup")
    try:
        yield data
    finally:
        print(f"[managed_list] teardown, len={len(data)}")


if __name__ == "__main__":
    print("=== 类实现 ===")
    with Timer() as t:
        pass

    print("\n=== @contextmanager ===")
    with managed_list() as lst:
        lst.append(1)
        lst.append(2)
        print(f"  lst = {lst}")

    print("\n=== 内置 with：打开文件 ===")
    with open(__file__, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"  read {len(lines)} lines from main.py")
