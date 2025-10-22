import tkinter as tk
from tkinter import ttk
import os

# 创建一个简单的测试窗口来确认GUI是否正常显示
root = tk.Tk()
root.title("女帝启示录 - 测试窗口")
root.geometry("600x400")
root.configure(bg="#3a2a1a")
root.attributes("-topmost", True)  # 窗口置顶确保可见

# 创建主框架
main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# 标题标签 - 确保中文显示
print("创建标题标签...")
title_label = ttk.Label(main_frame, text="女帝启示录", font=("SimHei", 24, "bold"))
title_label.pack(pady=30)

# 测试信息
info_text = "这是一个测试窗口，确认GUI系统正常工作。\n\n"
info_text += "如果您能看到这个窗口，说明：\n"
info_text += "1. Python和tkinter安装正常\n"
info_text += "2. 中文字体可以正常显示\n"
info_text += "3. 窗口系统工作正常"

info_label = ttk.Label(main_frame, text=info_text, font=("SimHei", 12), justify=tk.CENTER)
info_label.pack(pady=20)

# 创建一个简单的按钮
def on_click():
    status_var.set("按钮点击成功！GUI交互正常。")
    print("按钮被点击，交互正常！")

button = ttk.Button(main_frame, text="点击测试", command=on_click)
button.pack(pady=20)

# 状态显示
status_var = tk.StringVar(value="测试窗口正常运行中...")
status_label = ttk.Label(main_frame, textvariable=status_var, font=("SimHei", 10))
status_label.pack(pady=10)

# 显示窗口信息
window_info = f"窗口ID: {root.winfo_id()}\n屏幕尺寸: {root.winfo_screenwidth()}x{root.winfo_screenheight()}\n"
window_info += f"当前路径: {os.getcwd()}"
info_label = ttk.Label(main_frame, text=window_info, font=("SimHei", 8), justify=tk.LEFT)
info_label.pack(pady=10, anchor="w")

print("测试窗口创建完成！")
print(f"窗口状态: {root.winfo_exists()}")
print(f"窗口位置: {root.winfo_x()}, {root.winfo_y()}")

# 启动主循环
root.mainloop()