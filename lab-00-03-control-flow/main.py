"""
lab-00-03-control-flow: 控制流（条件判断与循环）
"""

# ========== if / elif / else ==========
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# ========== for 循环 ==========
print("\n=== for 循环：遍历列表 ===")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢 {fruit}")

print("\n=== for 循环：遍历字符串 ===")
for char in "Python":
    print(char, end=" ")
print()

print("\n=== for 循环：使用 range() ===")
# range(5) 生成 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=" ")
print()

# range(2, 6) 生成 2, 3, 4, 5
for i in range(2, 6):
    print(i, end=" ")
print()

# range(0, 10, 2) 生成 0, 2, 4, 6, 8（步长为2）
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# ========== while 循环 ==========
print("\n=== while 循环 ===")
count = 0
while count < 5:
    print(f"count = {count}")
    count += 1  # count = count + 1

# ========== break：跳出循环 ==========
print("\n=== break：找到目标后停止 ===")
for i in range(10):
    if i == 5:
        print(f"找到 {i}，停止循环")
        break
    print(i, end=" ")
print()

# ========== continue：跳过本次循环 ==========
print("\n=== continue：跳过偶数 ===")
for i in range(10):
    if i % 2 == 0:  # 如果是偶数
        continue  # 跳过本次循环，继续下一次
    print(i, end=" ")  # 只打印奇数
print()

# ========== 嵌套循环 ==========
print("\n=== 嵌套循环：打印乘法表（部分）===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="  ")
    print()  # 换行
