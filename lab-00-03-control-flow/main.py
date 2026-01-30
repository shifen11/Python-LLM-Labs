"""
lab-00-03-control-flow: 控制流（条件判断与循环）

运行时会展示：if/elif/else、for、while、range()、break、continue 及嵌套循环的用法。
"""

print("=== 1. if / elif / else ===\n")
print("  >>> [说明] 条件后加冒号，下一行缩进即「属于该分支」")
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
print(f"  (当前 score = {score}，故输出「良好」)\n")

print("=== 2. for 循环：遍历列表 ===\n")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"  我喜欢 {fruit}")
print("  >>> [小结] for 变量 in 可迭代对象: 依次绑定\n")

print("=== 3. for 循环：遍历字符串 ===\n")
for char in "Python":
    print(char, end=" ")
print("\n  >>> [小结] 字符串也是可迭代对象，逐个字符\n")

print("=== 4. for + range() ===\n")
print("  >>> [说明] range(n) 生成 0..n-1；range(start, stop) 左闭右开；range(start, stop, step)")
print("  range(5) -> ", end="")
for i in range(5):
    print(i, end=" ")
print("\n  range(2, 6) -> ", end="")
for i in range(2, 6):
    print(i, end=" ")
print("\n  range(0, 10, 2) -> ", end="")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

print("=== 5. while 循环 ===\n")
print("  >>> [说明] 先判断条件，为 True 则执行块内代码，再重复")
count = 0
while count < 5:
    print(f"  count = {count}")
    count += 1
print("  >>> [触发] 条件 count < 5 变为 False，退出 while\n")

print("=== 6. break：跳出当前循环 ===\n")
print("  >>> [说明] 遇到 break 立即退出本层 for/while")
for i in range(10):
    if i == 5:
        print(f"  找到 {i}，停止循环")
        break
    print(i, end=" ")
print("\n")

print("=== 7. continue：跳过本次，进入下一轮 ===\n")
print("  >>> [说明] 遇到 continue 不执行后面代码，直接下一轮")
print("  只打印奇数: ", end="")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\n")

print("=== 8. 嵌套循环（乘法表局部）===\n")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()
