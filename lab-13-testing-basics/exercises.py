#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lab-13-testing-basics - 练习题验证脚本

请完成 test_exercises.py 中的练习题，然后运行本文件验证你的答案。
"""

import sys
import os

# 添加当前目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 50)
print("练习题验证")
print("=" * 50)
print("\n请先完成 test_exercises.py 中的练习题，然后运行：")
print("  pytest test_exercises.py")
print("\n或者运行：")
print("  pytest test_exercises.py -v")
print("  pytest test_exercises.py -s")
print("\n" + "=" * 50)
