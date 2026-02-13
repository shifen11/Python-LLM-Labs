#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-06-typing-hints - 类型注解

本脚本演示 Python 的类型注解功能。
"""

# >>> [说明] Python 3.5+ 引入了类型注解功能
# 类型注解不会影响程序运行，但可以帮助 IDE 和类型检查工具提供更好的支持

from typing import List, Dict, Set, Tuple, Optional, Union


# ========== 1. 基本类型注解 ==========

print("=" * 50)
print("1. 基本类型注解")
print("=" * 50)

# >>> [说明] 为函数参数和返回值添加类型注解
def add(a: int, b: int) -> int:
    """两个整数相加"""
    return a + b


def greet(name: str) -> str:
    """返回问候语"""
    return f"你好，{name}！"


def calculate_area(radius: float) -> float:
    """计算圆的面积"""
    return 3.14 * radius * radius


def is_adult(age: int) -> bool:
    """判断是否成年"""
    return age >= 18


# >>> [触发] 调用函数
result = add(3, 5)
print(f"add(3, 5) = {result}, 类型是 {type(result).__name__}")
# >>> [预期输出] add(3, 5) = 8, 类型是 int

message = greet("张三")
print(f"{message}, 类型是 {type(message).__name__}")
# >>> [预期输出] 你好，张三！, 类型是 str

area = calculate_area(2.0)
print(f"area(2.0) = {area:.2f}, 类型是 {type(area).__name__}")
# >>> [预期输出] area(2.0) = 12.56, 类型是 float

adult = is_adult(20)
print(f"is_adult(20) = {adult}, 类型是 {type(adult).__name__}")
# >>> [预期输出] is_adult(20) = True, 类型是 bool


# >>> [说明] 变量类型注解（Python 3.6+）
username: str = "alice"
score: int = 95
price: float = 9.99
is_active: bool = True

print(f"\n变量类型注解:")
print(f"  username: {username} ({type(username).__name__})")
print(f"  score: {score} ({type(score).__name__})")
print(f"  price: {price} ({type(price).__name__})")
print(f"  is_active: {is_active} ({type(is_active).__name__})")


# ========== 2. Optional 类型 ==========

print("\n" + "=" * 50)
print("2. Optional 类型")
print("=" * 50)

# >>> [说明] Optional 表示值可能是指定类型或 None
def find_user(user_id: int) -> Optional[str]:
    """根据用户 ID 查找用户名，找不到返回 None"""
    users = {
        1: "alice",
        2: "bob",
        3: "charlie",
    }
    return users.get(user_id)  # 如果找不到返回 None


def divide(a: float, b: Optional[float] = None) -> Optional[float]:
    """除法，如果除数为 None 则返回 None"""
    if b is None or b == 0:
        return None
    return a / b


# >>> [触发] 测试 Optional
result1 = find_user(1)
print(f"find_user(1) = {result1}")
# >>> [预期输出] find_user(1) = alice

result2 = find_user(999)
print(f"find_user(999) = {result2}")
# >>> [预期输出] find_user(999) = None

div1 = divide(10, 2)
print(f"divide(10, 2) = {div1}")
# >>> [预期输出] divide(10, 2) = 5.0

div2 = divide(10, 0)
print(f"divide(10, 0) = {div2}")
# >>> [预期输出] divide(10, 0) = None

div3 = divide(10)
print(f"divide(10) = {div3}")
# >>> [预期输出] divide(10) = None


# ========== 3. Union 类型 ==========

print("\n" + "=" * 50)
print("3. Union 类型")
print("=" * 50)

# >>> [说明] Union 表示值可以是多种类型之一
def process_data(data: Union[int, str]) -> str:
    """处理数据，返回字符串"""
    return str(data)


def get_value(key: str, data: Union[Dict[str, int], Dict[str, str]]) -> Union[int, str, None]:
    """从字典中获取值，值可能是 int 或 str"""
    return data.get(key)


# >>> [说明] Union 也可以有多个类型
def process_any(data: Union[int, float, str, bool]) -> str:
    """处理任意基本类型"""
    if isinstance(data, bool):
        return "布尔值: " + str(data)
    elif isinstance(data, (int, float)):
        return f"数字: {data}"
    else:
        return f"字符串: {data}"


# >>> [触发] 测试 Union
print(f"process_data(123) = {process_data(123)}")
# >>> [预期输出] process_data(123) = 123

print(f"process_data('hello') = {process_data('hello')}")
# >>> [预期输出] process_data('hello') = hello

data1 = {"name": "张三", "score": 90}
print(f"get_value('name', data) = {get_value('name', data1)}")
# >>> [预期输出] get_value('name', data) = 张三

print(f"get_value('score', data) = {get_value('score', data1)}")
# >>> [预期输出] get_value('score', data) = 90

print(f"process_any(True) = {process_any(True)}")
# >>> [预期输出] process_any(True) = 布尔值: True

print(f"process_any(3.14) = {process_any(3.14)}")
# >>> [预期输出] process_any(3.14) = 数字: 3.14


# ========== 4. 泛型类型 ==========

print("\n" + "=" * 50)
print("4. 泛型类型（List, Dict, Set, Tuple）")
print("=" * 50)

# >>> [说明] List 类型注解
def get_scores() -> List[int]:
    """返回成绩列表"""
    return [85, 90, 78, 92, 88]


def filter_even(numbers: List[int]) -> List[int]:
    """过滤出偶数"""
    return [n for n in numbers if n % 2 == 0]


# >>> [说明] Dict 类型注解
def get_user_info() -> Dict[str, str]:
    """返回用户信息字典"""
    return {
        "name": "张三",
        "email": "zhangsan@example.com",
        "city": "北京"
    }


def update_counts(counts: Dict[str, int], key: str, increment: int = 1) -> None:
    """更新计数字典"""
    counts[key] = counts.get(key, 0) + increment


# >>> [说明] Set 类型注解
def get_unique_tags() -> Set[str]:
    """返回唯一的标签集合"""
    return {"python", "ai", "machine-learning"}


# >>> [说明] Tuple 类型注解
def get_coordinates() -> Tuple[float, float]:
    """返回坐标（x, y）"""
    return (3.14, 2.71)


def get_person() -> Tuple[str, int, str]:
    """返回人（姓名, 年龄, 城市）"""
    return ("李四", 25, "上海")


# >>> [说明] 嵌套泛型类型
def get_user_list() -> List[Dict[str, Union[str, int]]]:
    """返回用户列表，每个用户是字典"""
    return [
        {"name": "张三", "age": 20, "city": "北京"},
        {"name": "李四", "age": 25, "city": "上海"},
    ]


# >>> [触发] 测试泛型类型
scores = get_scores()
print(f"scores = {scores}")
# >>> [预期输出] scores = [85, 90, 78, 92, 88]

evens = filter_even([1, 2, 3, 4, 5, 6])
print(f"filter_even([1,2,3,4,5,6]) = {evens}")
# >>> [预期输出] filter_even([1,2,3,4,5,6]) = [2, 4, 6]

user_info = get_user_info()
print(f"user_info = {user_info}")
# >>> [预期输出] user_info = {'name': '张三', 'email': 'zhangsan@example.com', 'city': '北京'}

tags = get_unique_tags()
print(f"tags = {tags}")
# >>> [预期输出] tags = {'python', 'ai', 'machine-learning'}

coords = get_coordinates()
print(f"coordinates = {coords}")
# >>> [预期输出] coordinates = (3.14, 2.71)

person = get_person()
print(f"person = {person}")
# >>> [预期输出] person = ('李四', 25, '上海')

users = get_user_list()
print(f"users = {users}")
# >>> [预期输出] users = [{'name': '张三', 'age': 20, 'city': '北京'}, {'name': '李四', 'age': 25, 'city': '上海'}]


# ========== 5. Python 3.10+ 新语法 ==========

print("\n" + "=" * 50)
print("5. Python 3.10+ 新语法")
print("=" * 50)

# >>> [说明] Python 3.10+ 可以使用内置类型作为泛型
# 不需要从 typing 导入 List、Dict 等，直接用 list、dict 等

def get_scores_310() -> list[int]:
    """Python 3.10+ 写法"""
    return [85, 90, 78]


def get_user_info_310() -> dict[str, str]:
    """Python 3.10+ 写法"""
    return {"name": "张三", "email": "zhangsan@example.com"}


def get_coordinates_310() -> tuple[float, float]:
    """Python 3.10+ 写法"""
    return (3.14, 2.71)


# >>> [说明] 类型联合的新语法（Python 3.10+）
def process_data_310(data: int | str) -> str:
    """Python 3.10+ 使用 | 代替 Union[int, str]"""
    return str(data)


# >>> [触发] 测试新语法
print(f"Python 3.10+ list[int]: {get_scores_310()}")
# >>> [预期输出] Python 3.10+ list[int]: [85, 90, 78]

print(f"Python 3.10+ dict[str, str]: {get_user_info_310()}")
# >>> [预期输出] Python 3.10+ dict[str, str]: {'name': '张三', 'email': 'zhangsan@example.com'}

print(f"Python 3.10+ tuple[float, float]: {get_coordinates_310()}")
# >>> [预期输出] Python 3.10+ tuple[float, float]: (3.14, 2.71)

print(f"Python 3.10+ int | str: {process_data_310('hello')}")
# >>> [预期输出] Python 3.10+ int | str: hello


# ========== 6. 类型别名 ==========

print("\n" + "=" * 50)
print("6. 类型别名")
print("=" * 50)

# >>> [说明] 为复杂类型定义别名，提高代码可读性
UserId = int
UserName = str
Score = int

UserInfo = Dict[str, Union[str, int]]
UserList = List[Dict[str, Union[str, int]]]


def get_username_by_id(user_id: UserId) -> Optional[UserName]:
    """根据用户 ID 获取用户名"""
    users = {1: "张三", 2: "李四"}
    return users.get(user_id)


def calculate_average_score(scores: list[Score]) -> float:
    """计算平均分"""
    return sum(scores) / len(scores)


def filter_adults(users: UserList) -> UserList:
    """过滤出成年用户（年龄 >= 18）"""
    return [user for user in users if user.get("age", 0) >= 18]


# >>> [触发] 测试类型别名
username = get_username_by_id(1)
print(f"username = {username}")
# >>> [预期输出] username = 张三

avg_score = calculate_average_score([85, 90, 78])
print(f"average score = {avg_score:.2f}")
# >>> [预期输出] average score = 84.33

adults = filter_adults([
    {"name": "张三", "age": 20, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 15, "city": "广州"},
])
print(f"adults = {adults}")
# >>> [预期输出] adults = [{'name': '张三', 'age': 20, 'city': '北京'}, {'name': '李四', 'age': 25, 'city': '上海'}]


print("\n" + "=" * 50)
print("实验室演示完成！")
print("=" * 50)
print("\n提示：可以使用 mypy 工具进行类型检查：")
print("  pip install mypy")
print("  mypy main.py")
