# lab-00-07-file-operations

**文件操作：读写文本文件**

## 知识点

- 打开文件：`open(文件路径, 模式)`
- 文件模式：
  - `'r'`：只读（默认）
  - `'w'`：写入（覆盖）
  - `'a'`：追加
  - `'x'`：创建新文件
- 读取文件：`read()`, `readline()`, `readlines()`
- 写入文件：`write()`, `writelines()`
- 使用 `with` 语句自动关闭文件（推荐）

## 运行

```bash
python main.py
```

## 练习题

练习题见 [exercises.py](./exercises.py)，在 lab 目录下运行 `python exercises.py` 完成并自测。

## 学习目标

- 掌握文件的读写操作
- 理解文件模式的区别
- 学会使用 `with` 语句管理文件
