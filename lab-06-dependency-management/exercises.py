"""
lab-06 练习题：虚拟环境与包管理
本 lab 无 main.py，练习题以「在终端执行」为主。
运行: python exercises.py 会打印题目与参考答案命令，你在终端自行执行并核对。
"""


import sys


def check_venv():
    """练习 4：判断当前是否在虚拟环境中"""
    if sys.prefix != sys.base_prefix:
        print("当前在虚拟环境中")
    else:
        print("当前不在虚拟环境中")


def print_exercises():
    print("""
=== 练习 1（在终端执行）===
在项目根目录创建虚拟环境 .venv，并激活（Mac/Linux: source .venv/bin/activate；Windows: .venv\\Scripts\\activate）
参考答案: python -m venv .venv
          source .venv/bin/activate
期望: 命令行前出现 (.venv)，且当前目录下出现 .venv 文件夹

=== 练习 2（在终端执行）===
在已激活的虚拟环境中，用 pip 安装根目录 requirements.txt 中的依赖。
参考答案: pip install -r requirements.txt
期望: 依赖安装成功，无报错

=== 练习 3（在终端执行）===
将当前环境已安装的包导出到 my_requirements.txt。
参考答案: pip freeze > my_requirements.txt
期望: 当前目录生成 my_requirements.txt，内容为包列表

=== 练习 4（编程）===
见本文件 check_venv()：若 sys.prefix != sys.base_prefix 打印「当前在虚拟环境中」，否则「当前不在虚拟环境中」。下方会调用。
期望输出: 当前不在虚拟环境中（未激活时）或 当前在虚拟环境中（已激活时）
""")
    print("=== 练习 4 自测 ===")
    check_venv()


if __name__ == "__main__":
    print_exercises()
