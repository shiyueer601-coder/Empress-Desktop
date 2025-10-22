import tkinter as tk
from tkinter import ttk
import time

class SimpleEmpressApp:
    def __init__(self, root):
        """简化版女帝启示录应用"""
        self.root = root
        self.root.title("女帝启示录")
        self.root.geometry("800x600")
        
        # 确保窗口显示在最前面
        self.root.attributes("-topmost", True)
        self.root.lift()
        self.root.focus_force()
        
        # 使用简单的背景色
        self.root.configure(bg="#f0e6d2")
        
        print("初始化简化版女帝启示录应用...")
        
        # 创建主框架
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # 显示欢迎界面
        self._show_welcome_screen()
        
        print("应用初始化完成！")
    
    def _show_welcome_screen(self):
        """显示欢迎界面"""
        print("显示欢迎界面...")
        
        # 清空主框架
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # 标题 - 大字体确保醒目
        title_label = ttk.Label(
            self.main_frame, 
            text="女帝启示录", 
            font=("SimHei", 36, "bold")
        )
        title_label.pack(pady=60)
        
        # 欢迎信息
        welcome_text = """
        欢迎来到女帝启示录！
        
        这是一个专为您打造的古风宫廷体验。
        点击下方按钮开始您的女帝之旅。
        """
        info_label = ttk.Label(
            self.main_frame, 
            text=welcome_text, 
            font=("SimHei", 14), 
            justify=tk.CENTER
        )
        info_label.pack(pady=40)
        
        # 状态指示器
        self.status_var = tk.StringVar(value="准备就绪")
        status_label = ttk.Label(
            self.main_frame, 
            textvariable=self.status_var, 
            font=("SimHei", 12)
        )
        status_label.pack(pady=20)
        
        # 开始按钮
        start_button = ttk.Button(
            self.main_frame, 
            text="开始女帝之旅", 
            command=self._show_main_interface,
            width=20
        )
        start_button.pack(pady=30)
        
        # 确保按钮获取焦点
        start_button.focus_set()
        
        print("欢迎界面创建完成！")
    
    def _show_main_interface(self):
        """显示主界面"""
        print("显示主界面...")
        
        # 清空主框架
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # 主界面标题
        title_label = ttk.Label(
            self.main_frame, 
            text="女帝朝政", 
            font=("SimHei", 28, "bold")
        )
        title_label.pack(pady=30)
        
        # 朝政区域
        court_frame = ttk.LabelFrame(self.main_frame, text="朝政区域", padding=20)
        court_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # 对话显示区域
        dialogue_text = """
        众爱卿平身！
        
        今日朝政，有何事启奏？
        """
        dialogue_label = ttk.Label(
            court_frame, 
            text=dialogue_text, 
            font=("SimHei", 12), 
            justify=tk.LEFT,
            wraplength=600
        )
        dialogue_label.pack(pady=20, anchor="w")
        
        # 返回按钮
        back_button = ttk.Button(
            self.main_frame, 
            text="返回", 
            command=self._show_welcome_screen,
            width=10
        )
        back_button.pack(pady=20, side=tk.BOTTOM)
        
        print("主界面创建完成！")
        self.status_var.set("主界面已加载")

def main():
    """应用入口"""
    print("启动女帝启示录简化版...")
    
    # 创建主窗口
    root = tk.Tk()
    
    # 确保中文显示
    print("检查系统字体支持...")
    
    # 创建应用实例
    app = SimpleEmpressApp(root)
    
    # 确保窗口可见性
    root.update_idletasks()
    root.deiconify()
    root.focus_force()
    
    print("应用启动完成，请查看窗口是否显示！")
    
    # 启动主循环
    root.mainloop()

if __name__ == "__main__":
    main()