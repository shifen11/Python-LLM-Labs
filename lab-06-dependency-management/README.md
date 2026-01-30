# lab-06-dependency-management

**虚拟环境与包管理**

## 知识点

- `python -m venv .venv`：创建虚拟环境
- `pip install -r requirements.txt`：从依赖文件安装
- `pip freeze > requirements.txt`：导出当前环境
- Conda：`conda create -n myenv python=3.11`、`conda activate myenv`

## 运行

本 lab 为操作指引，无 `main.py`。按 README 在项目根执行：

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 练习题

练习题见 [exercises.py](./exercises.py)，在 lab 目录下运行 `python exercises.py` 查看题目与自测（练习 1～3 需在终端执行命令）。
