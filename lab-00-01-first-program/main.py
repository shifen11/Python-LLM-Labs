"""
lab-00-01-first-program: 第一个 Python 程序

运行时会展示：print 的用法、注释写法、缩进规则，以及「代码块」如何用缩进表示。
这是多行注释，用三个双引号或单引号包裹。
"""

# 这是单行注释，用 # 开头

print("=== 1. 最简输出 ===\n")
print("Hello, World!")
print("欢迎来到 Python 学习之旅！")

print("\n=== 2. print 多参数（逗号分隔，中间会加空格）===\n")
print("  >>> [说明] print 可以接多个值，用逗号分隔，输出时自动用空格连接")
print("我的名字是", "Python", "，版本是", 3.11)

print("\n=== 3. f-string 格式化（Python 3.6+，推荐）===\n")
print("  >>> [说明] f'...{变量}...' 会在运行时把变量值填进去")
name = "Python"
version = 3.11
print(f"语言：{name}，版本：{version}")

print("\n=== 4. 缩进表示代码块（与 Java 的 {} 不同）===\n")
print("  >>> [说明] Python 用缩进（通常 4 个空格）表示「属于同一块」")
print("  >>> [触发] 下面进入 if True: 的代码块")
if True:
    print("这是 if 语句块内的代码")
    print("注意缩进！")
print("  >>> [触发] 这里已离开 if 块，缩进恢复")
print("这是 if 语句块外的代码")
