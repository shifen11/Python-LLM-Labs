"""
lab-04-context-managers: with 与上下文管理器

运行时会展示：进入 with 时触发 __enter__，退出时触发 __exit__；
以及 @contextmanager + yield 的「前半段 = 进入，后半段 = 退出」。
"""
import time
from contextlib import contextmanager


class Timer:
    """类形式：实现 __enter__ 和 __exit__，即可用于 with 语句（类似 Java try-with-resources）"""

    def __enter__(self):
        print("  >>> [触发 __enter__] 进入 with 块，开始计时")
        self.start = time.perf_counter()
        return self  # 返回值会赋给 as 后面的变量

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start
        print(f"  >>> [触发 __exit__] 离开 with 块，耗时 {elapsed:.4f}s")
        print(f"       (若发生异常: exc_type={exc_type}, exc_val={exc_val})")
        return False  # False 表示不吞掉异常，异常会继续向外抛


@contextmanager
def managed_list():
    """生成器形式：yield 之前的代码 = 进入时执行，yield 之后的在 finally 里 = 退出时执行"""
    data = []
    print("  >>> [contextmanager 进入] 相当于 __enter__，初始化 data = []")
    try:
        yield data  # 这里把 data 传给 as 后面的变量
        print("  >>> [contextmanager 正常退出] with 块内没有异常，会执行到这里")
    finally:
        print(f"  >>> [contextmanager finally] 相当于 __exit__，收尾时 len(data) = {len(data)}")


if __name__ == "__main__":
    print("=== 1. 类实现：Timer（__enter__ / __exit__）===\n")
    print("  执行: with Timer() as t: ...")
    with Timer() as t:
        print("  执行中...")

    print("\n=== 2. @contextmanager：managed_list ===\n")
    print("  执行: with managed_list() as lst: lst.append(1); lst.append(2)")
    with managed_list() as lst:
        lst.append(1)
        lst.append(2)
        print(f"  lst = {lst}")

    print("\n=== 3. 内置 with：打开文件 ===\n")
    print("  执行: with open(__file__, 'r', encoding='utf-8') as f: f.readlines()")
    with open(__file__, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"  读取到 {len(lines)} 行（本文件 main.py）")
