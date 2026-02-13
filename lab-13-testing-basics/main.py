#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lab-13-testing-basics - 测试基础

print("=" * 60)
print("lab-13-testing-basics - 测试基础")
print("=" * 60)

# ========== 1. pytest 简介 ==========

print("\n1. pytest 简介")
print("-" * 60)

msg = "pytest 是 Python 生态中最流行的测试框架之一。\n\n特点：\n- 语法简洁，易于上手\n- 自动发现测试文件和测试函数\n- 丰富的插件生态\n- 强大的 fixture 系统\n- 优秀的错误报告\n\n测试文件命名规则：\n- test_*.py\n- *_test.py\n\n测试函数命名规则：\n- 以 test_ 开头\n"
print(msg)

print("\n安装 pytest:")
print("  pip install pytest")

print("\n运行测试:")
print("  pytest                    # 运行所有测试")
print("  pytest test_example.py    # 运行指定文件")
print("  pytest -v                 # 显示详细输出")
print("  pytest -s                 # 显示打印输出")


# ========== 2. 断言（assert）==========

print("\n\n2. 断言（assert）")
print("-" * 60)

msg2 = "pytest 直接使用 Python 的 assert 语句，不需要学习特殊的断言方法。\n\n基本断言：\n  assert x == y          # 相等\n  assert x != y          # 不相等\n  assert x > y           # 大于\n  assert x in y          # 包含\n  assert isinstance(x, y) # 类型判断\n\n复杂断言：\n  assert add(1, 2) == 3\n  assert 'hello' in greeting\n  assert len(items) > 0\n\n断言消息：\n  assert result == expected, f'期望 {expected}，实际 {result}'\n"
print(msg2)

# 示例：被测试的函数
def add(a: int, b: int) -> int:
    return a + b

def is_positive(num: int) -> bool:
    return num > 0

print("\n示例代码：")
print("")
print("def test_add():")
print("    assert add(1, 2) == 3")
print("    assert add(-1, 1) == 0")
print("")
print("def test_is_positive():")
print("    assert is_positive(5) == True")
print("    assert is_positive(-5) == False")
print("    assert is_positive(0) == False")


# ========== 3. Fixture ==========

print("\n\n3. Fixture")
print("-" * 60)

msg3 = "Fixture 是 pytest 提供的一种共享测试资源的方式。\n使用 @pytest.fixture 装饰器定义 fixture。\n\n示例：\n    @pytest.fixture\n    def sample_data():\n        return {'name': '张三', 'age': 20}\n\n    def test_use_fixture(sample_data):\n        assert sample_data['age'] == 20\n\n作用域：\n  - function（默认）：每个测试函数执行一次\n  - class：每个测试类执行一次\n  - module：每个模块执行一次\n  - session：整个测试会话执行一次\n"
print(msg3)

print("\n示例代码：")
print("")
print("@pytest.fixture")
print("def sample_data():")
print("    return {'name': '张三', 'age': 20}")
print("")
print("def test_use_fixture(sample_data):")
print("    assert sample_data['name'] == '张三'")
print("    assert sample_data['age'] == 20")


# ========== 4. 参数化测试 ==========

print("\n\n4. 参数化测试")
print("-" * 60)

msg4 = "参数化测试允许你使用不同的输入参数多次运行同一个测试。\n使用 @pytest.mark.parametrize 装饰器。\n\n语法：\n    @pytest.mark.parametrize('a,b,expected', [\n        (1, 2, 3),\n        (2, 3, 5),\n        (3, 4, 7),\n    ])\n    def test_add(a, b, expected):\n        assert add(a, b) == expected\n"
print(msg4)


# ========== 5. 测试异常 ==========

print("\n\n5. 测试异常")
print("-" * 60)

msg5 = "使用 pytest.raises 测试函数是否抛出预期的异常。\n\n示例：\n    def divide(a, b):\n        if b == 0:\n            raise ValueError('除数不能为 0')\n        return a / b\n\n    def test_divide_by_zero():\n        with pytest.raises(ValueError):\n            divide(1, 0)\n"
print(msg5)


# ========== 6. 运行 pytest 演示 ==========

print("\n\n6. 实际运行 pytest")
print("-" * 60)

print("本实验室包含一个测试文件 test_example.py，可以实际运行 pytest 查看效果。")

print("\n运行命令：")
print("  cd lab-13-testing-basics")
print("  pytest")

print("\n查看详细输出：")
print("  pytest -v")

print("\n查看打印输出：")
print("  pytest -s")

print("\n运行特定测试：")
print("  pytest test_example.py::test_add")


# ========== 7. 测试最佳实践 ==========

print("\n\n7. 测试最佳实践")
print("-" * 60)

msg7 = "1. 测试命名\n   - 使用描述性的测试名称\n   - 格式：test_功能_条件_期望结果\n\n2. 测试独立性\n   - 每个测试应该独立运行\n   - 不依赖其他测试的执行顺序或结果\n\n3. 测试覆盖率\n   - 测试正常情况\n   - 测试边界条件\n   - 测试异常情况\n\n4. 保持简单\n   - 每个测试只测试一个功能点\n   - 避免复杂的逻辑\n\n5. 可读性\n   - 测试代码应该清晰易懂\n   - 使用有意义的变量名\n"
print(msg7)

print("\n\n" + "=" * 60)
print("实验室演示完成！")
print("运行 'pytest test_example.py' 查看实际测试效果")
print("=" * 60)
