"""
lab-03-decorators: 装饰器（Python 版 AOP）
"""
import functools
import time


def log_call(f):
    """简单装饰器：在调用前后打印"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        print(f"[LOG] calling {f.__name__}({args}, {kwargs})")
        result = f(*args, **kwargs)
        print(f"[LOG] {f.__name__} returned {result}")
        return result
    return wrapper


def timing(f):
    """计时装饰器"""
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = f(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(f"[TIMING] {f.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


@log_call
def add(a, b):
    return a + b


@timing
def slow_demo():
    time.sleep(0.1)
    return "done"


@log_call
@timing
def both(a, b):
    """叠加多个装饰器：先 timing 再 log_call（从下往上执行）"""
    time.sleep(0.05)
    return a * b


if __name__ == "__main__":
    print("=== @log_call ===")
    add(2, 3)
    print("\n=== @timing ===")
    slow_demo()
    print("\n=== 叠放 @log_call @timing ===")
    both(4, 5)
