#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
女帝启示录 - 入口文件
用于启动女帝启示录应用
"""

import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """启动应用"""
    print("正在启动女帝启示录...")
    
    try:
        # 导入并运行主应用
        import main
        main.main()
    except ImportError as e:
        print(f"导入错误: {e}")
        print("请确保所有依赖已安装，运行: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"应用启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
