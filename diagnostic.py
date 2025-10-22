import tkinter as tk
from tkinter import messagebox
import os
import sys

# 诊断脚本 - 用于检查女帝启示录应用的基本功能
print("开始诊断...")
print(f"Python版本: {sys.version}")
print(f"当前工作目录: {os.getcwd()}")

# 1. 检查tkinter是否正常工作
print("\n检查tkinter...")
try:
    # 创建一个简单的测试窗口
    root = tk.Tk()
    root.title("诊断测试")
    root.geometry("300x200")
    
    label = tk.Label(root, text="测试窗口显示成功")
    label.pack(pady=20)
    
    button = tk.Button(root, text="关闭", command=root.destroy)
    button.pack(pady=10)
    
    # 设置一个定时器在3秒后自动关闭窗口
    root.after(3000, root.destroy)
    
    print("tkinter窗口已创建，正在显示...")
    root.mainloop()
    print("tkinter测试通过")
except Exception as e:
    print(f"tkinter测试失败: {e}")

# 2. 检查模块导入
print("\n检查模块导入...")
try:
    # 尝试导入项目的关键模块
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    from src.logic.pomodoro_logic import PomodoroTimer
    from src.ai.ai_companion import AICompanion
    
    print("模块导入成功")
    
    # 测试模块功能
    print("\n测试番茄钟模块...")
    pomodoro = PomodoroTimer()
    print(f"番茄钟初始化成功，默认时间: {pomodoro.get_time_string()}")
    
    print("\n测试AI伴侣模块...")
    companion = AICompanion()
    print(f"AI伴侣初始化成功，问候语: {companion.get_greeting()}")
    
    print("\n所有测试通过！")
except Exception as e:
    print(f"模块测试失败: {e}")

print("\n诊断完成")
