"""
lab-05-magic-methods: __init__, __call__, __str__, __repr__, __len__, __getitem__
"""


class Greeter:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Greeter({self.name})"

    def __repr__(self):
        return f"Greeter(name={self.name!r})"

    def __call__(self, msg="Hello"):
        """实例可像函数一样调用"""
        return f"{msg}, {self.name}!"


class SimpleSeq:
    """实现 __len__ 和 __getitem__，即可被迭代、切片"""

    def __init__(self, data):
        self._data = list(data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key]


if __name__ == "__main__":
    print("=== __init__ / __str__ / __repr__ ===")
    g = Greeter("World")
    print(str(g))
    print(repr(g))

    print("\n=== __call__ ===")
    print(g())
    print(g("Hi"))

    print("\n=== __len__ / __getitem__ ===")
    s = SimpleSeq([10, 20, 30, 40])
    print(f"len(s) = {len(s)}")
    print(f"s[1] = {s[1]}, s[1:3] = {s[1:3]}")
    print(f"list(s) = {list(s)}")
