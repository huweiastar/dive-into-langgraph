# -*- coding: utf-8 -*-
# 指定文件编码为UTF-8，保证中文和特殊字符能正常识别

# 从**当前包目录**中导入 server 模块
# . 代表当前文件夹，适用于包内部的相对导入
from . import server


# 定义包的公开导出列表
# __all__ 是Python固定语法，作用是：
# 当其他代码使用 from 包名 import * 时
# 只会导入这里列出的内容（server），避免导出内部无用变量
__all__ = ['server']