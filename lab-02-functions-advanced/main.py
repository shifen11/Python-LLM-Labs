"""
lab-02-functions-advanced: 解构赋值、*args、**kwargs
"""


def demo_unpacking():
    """解构赋值"""
    a, b = 1, 2
    print(f"a, b = 1, 2  -> a={a}, b={b}")
    first, *rest, last = [1, 2, 3, 4, 5]
    print(f"first, *rest, last = [1..5]  -> first={first}, rest={rest}, last={last}")
    d = {"x": 10, "y": 20}
    x, y = d.values()
    print(f"x, y = d.values()  -> x={x}, y={y}")


def greet(*names):
    """*args: 任意个 positional 参数 -> tuple"""
    print(f"greet(*names): names = {names}")
    for n in names:
        print(f"  Hello, {n}!")


def config(**kwargs):
    """**kwargs: 任意个 keyword 参数 -> dict"""
    print(f"config(**kwargs): kwargs = {kwargs}")
    for k, v in kwargs.items():
        print(f"  {k} = {v}")


def mixed(a, b, *args, **kwargs):
    """组合：固定参数 + *args + **kwargs"""
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")


if __name__ == "__main__":
    print("=== 解构赋值 ===")
    demo_unpacking()
    print("\n=== *args ===")
    greet("Alice", "Bob")
    print("\n=== **kwargs ===")
    config(host="localhost", port=8080, debug=True)
    print("\n=== 组合 ===")
    mixed(1, 2, 3, 4, foo="bar", baz=99)
