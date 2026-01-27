"""
lab-00-05-data-structures: 数据结构基础
"""

# ========== 列表 list ==========
print("=== 列表 list ===")
fruits = ["苹果", "香蕉", "橙子"]
print(f"fruits = {fruits}")

# 访问元素（索引从0开始）
print(f"第一个水果：{fruits[0]}")
print(f"最后一个水果：{fruits[-1]}")  # 负数索引从后往前

# 添加元素
fruits.append("葡萄")  # 在末尾添加
print(f"添加后：{fruits}")

fruits.insert(1, "草莓")  # 在索引1处插入
print(f"插入后：{fruits}")

# 删除元素
fruits.remove("香蕉")  # 删除指定值
print(f"删除后：{fruits}")

del fruits[0]  # 删除索引0的元素
print(f"删除索引0后：{fruits}")

# 列表长度
print(f"列表长度：{len(fruits)}")

# ========== 元组 tuple ==========
print("\n=== 元组 tuple ===")
point = (3, 4)  # 坐标点
print(f"point = {point}")

# 访问元素
print(f"x坐标：{point[0]}，y坐标：{point[1]}")

# 元组不可变（不能修改）
# point[0] = 5  # 这行会报错！

# 解包元组
x, y = point
print(f"x = {x}, y = {y}")

# ========== 字典 dict ==========
print("\n=== 字典 dict ===")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(f"student = {student}")

# 访问值
print(f"姓名：{student['name']}")
print(f"年龄：{student.get('age')}")  # 更安全的方式

# 添加/修改
student["city"] = "北京"  # 添加新键值对
student["age"] = 21  # 修改已有值
print(f"更新后：{student}")

# 删除
del student["grade"]
print(f"删除后：{student}")

# 遍历字典
print("遍历字典：")
for key, value in student.items():
    print(f"  {key}: {value}")

# ========== 集合 set ==========
print("\n=== 集合 set ===")
numbers = {1, 2, 3, 4, 5}
print(f"numbers = {numbers}")

# 添加元素
numbers.add(6)
print(f"添加6后：{numbers}")

# 集合自动去重
duplicates = {1, 2, 2, 3, 3, 3}
print(f"去重后：{duplicates}")

# 集合运算
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"交集：{set1 & set2}")  # {3, 4}
print(f"并集：{set1 | set2}")  # {1, 2, 3, 4, 5, 6}
print(f"差集：{set1 - set2}")  # {1, 2}
