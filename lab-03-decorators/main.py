"""
lab-03-decorators: 装饰器（Python 版 AOP）

运行时会展示：@deco 等价于 f = deco(f)、装饰器内外层执行顺序、叠放多个装饰器时的顺序。
"""
import functools
import time


def log_call(f):
    """简单装饰器：在函数调用前后打印，便于观察「何时进入、何时返回」"""
    @functools.wraps(f)  # 保留原函数的 __name__ 等元信息
    def wrapper(*args, **kwargs):
        print(f"  >>> [LOG 进入] 正在调用 {f.__name__}(args={args}, kwargs={kwargs})")
        result = f(*args, **kwargs)
        print(f"  >>> [LOG 返回] {f.__name__} 返回了 {result}")
        return result
    return wrapper


def timing(f):
    """计时装饰器：在函数执行前后打点，计算耗时"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        print(f"  >>> [TIMING 开始] 开始执行 {f.__name__}")
        result = f(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"  >>> [TIMING 结束] {f.__name__} 耗时 {elapsed:.4f}s，返回值 = {result}")
        return result
    return wrapper


# 等价于: add = log_call(add)，之后调用 add 实际调用的是 log_call(add) 返回的 wrapper
@log_call
def add(a, b):
    """被装饰后，每次调用 add 都会先经过 log_call 的 wrapper"""
    return a + b


@timing
def slow_demo():
    """用来观察计时效果"""
    time.sleep(0.1)
    return "done"


# 叠放顺序：下面的先应用，上面的后应用；执行时先进上面的 wrapper，再进下面的
# 即：both = log_call(timing(both))，调用时先进入 log_call 的 wrapper，再进入 timing 的 wrapper，再执行原函数
@log_call
@timing
def both(a, b):
    """叠放多个装饰器：从下往上包装，执行时从上往下进入"""
    time.sleep(0.05)
    return a * b


if __name__ == "__main__":
    print("=== 1. @log_call：观察进入与返回 ===\n")
    print("  调用: add(2, 3)")
    add(2, 3)

    print("\n=== 2. @timing：观察耗时 ===\n")
    print("  调用: slow_demo()")
    slow_demo()

    print("\n=== 3. 叠放 @log_call 和 @timing ===\n")
    print("  调用: both(4, 5)")
    print("  （顺序：先进 log_call -> 再进 timing -> 执行原函数 -> 先出 timing -> 再出 log_call）")
    both(4, 5)
