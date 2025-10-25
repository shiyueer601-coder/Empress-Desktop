import tkinter as tk
from tkinter import ttk, messagebox
import os
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入项目模块
from logic.pomodoro_logic import PomodoroTimer
from ai.ai_companion import companion

class EmpressApp:
    """女帝启示录主应用类"""

    def __init__(self, root):
        self.root = root
        self.root.title("女帝启示录")
        self.root.geometry("800x600")
        self.root.configure(bg="#2b1f16")
        
        # 设置中文字体支持
        self._setup_fonts()
        # 设置古风样式
        self._setup_styles()
        
        # 初始化番茄钟
        self.pomodoro = PomodoroTimer()
        self.pomodoro.on_time_update = self._on_time_update
        self.pomodoro.on_session_complete = self._on_session_complete
        
        # 创建主界面
        self._create_main_frame()
        
        # 显示初始欢迎界面
        self._show_welcome_screen()
    
    def _setup_fonts(self):
        """设置中文字体"""
        # 在Windows上使用系统字体
        # 优先楷体，回退到黑体
        self.font_large = ("KaiTi", 26, "bold")
        self.font_medium = ("KaiTi", 16)
        self.font_small = ("KaiTi", 12)

    def _setup_styles(self):
        """配置ttk古风主题样式"""
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except Exception:
            pass
        imperial_bg = "#2b1f16"      # 深胡桃木色
        imperial_panel = "#3a2a1a"   # 面板底色
        imperial_border = "#c8a86b"  # 金色描边
        imperial_text = "#f3e6c2"    # 纸色文字
        accent = "#d4b15f"

        # Frame / Label / Labelframe
        style.configure("Imperial.TFrame", background=imperial_bg)
        style.configure("ImperialPanel.TFrame", background=imperial_panel)
        style.configure("Imperial.TLabel", background=imperial_panel, foreground=imperial_text, font=self.font_medium)
        style.configure("ImperialTitle.TLabel", background=imperial_panel, foreground=accent, font=self.font_large)
        style.configure("Imperial.TLabelframe", background=imperial_panel, foreground=accent, bordercolor=imperial_border, relief="solid")
        style.configure("Imperial.TLabelframe.Label", background=imperial_panel, foreground=accent, font=self.font_medium)

        # Buttons
        style.configure("Imperial.TButton", font=self.font_small, foreground="#1b140c", background=accent, bordercolor=imperial_border, focusthickness=3, focuscolor=imperial_border, padding=(12, 6))
        style.map(
            "Imperial.TButton",
            background=[("active", "#e5c773"), ("disabled", "#8a7a4c")],
            foreground=[("disabled", "#3f3a2c")]
        )
        style.configure("Accent.TButton", font=self.font_medium, background="#b88a2a", foreground="#1b140c")
    
    def _create_main_frame(self):
        """创建主框架"""
        # 创建一个主框架来容纳所有内容
        self.main_frame = ttk.Frame(self.root, style="Imperial.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 创建一个容器来切换不同的页面
        self.content_container = ttk.Frame(self.main_frame, style="ImperialPanel.TFrame")
        self.content_container.pack(fill=tk.BOTH, expand=True)
    
    def _show_welcome_screen(self):
        """显示欢迎界面"""
        # 清空内容容器
        for widget in self.content_container.winfo_children():
            widget.destroy()
        
        # 创建欢迎界面元素
        welcome_frame = ttk.Frame(self.content_container, style="ImperialPanel.TFrame")
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # 欢迎标题
        title_label = ttk.Label(welcome_frame, text="女帝启示录", style="ImperialTitle.TLabel")
        title_label.pack(pady=50)
        
        # 欢迎信息
        welcome_text = "奉天承运，皇帝诏曰：兹有天命之子，身负紫微星辰，\n然元神未定，朝纲待兴。今特赐下《女帝启示录》\n助尔重整河山，修心明性。钦此！"
        info_label = ttk.Label(welcome_frame, text=welcome_text, style="Imperial.TLabel", justify=tk.CENTER)
        info_label.pack(pady=20)
        
        # 开始按钮
        start_button = ttk.Button(
            welcome_frame, 
            text="开始你的帝王之旅", 
            command=self._show_main_interface,
            style="Imperial.TButton"
        )
        start_button.pack(pady=30, ipady=10, ipadx=20)
        
        # 设置按钮样式
        style = ttk.Style()
        style.configure("Accent.TButton", font=self.font_medium)
    
    def _show_main_interface(self):
        """显示主界面"""
        # 清空内容容器
        for widget in self.content_container.winfo_children():
            widget.destroy()
        
        # 创建主界面布局
        main_interface = ttk.Frame(self.content_container, style="ImperialPanel.TFrame")
        main_interface.pack(fill=tk.BOTH, expand=True)
        
        # 顶部区域 - 角色对话
        chat_frame = ttk.LabelFrame(main_interface, text="宫廷对话", padding=10, style="Imperial.TLabelframe")
        chat_frame.pack(fill=tk.BOTH, expand=False, pady=10)
        
        # 角色图像占位符
        character_frame = ttk.Frame(chat_frame, width=100, height=100, style="ImperialPanel.TFrame")
        character_frame.pack(side=tk.LEFT, padx=10)
        
        character_label = ttk.Label(character_frame, text="云瑾", style="Imperial.TLabel")
        character_label.pack(expand=True)
        
        # 对话区域
        self.dialog_text = tk.Text(chat_frame, height=5, width=60, font=self.font_small, bg="#3a2a1a", fg="#f3e6c2", insertbackground="#f3e6c2", highlightthickness=1, highlightbackground="#c8a86b")
        self.dialog_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        self.dialog_text.insert(tk.END, companion.get_greeting())
        self.dialog_text.config(state=tk.DISABLED)
        
        # 输入区域
        input_frame = ttk.Frame(chat_frame, style="ImperialPanel.TFrame")
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        self.user_input = ttk.Entry(input_frame, font=self.font_small)
        self.user_input.pack(fill=tk.X, expand=True, side=tk.LEFT, padx=(0, 5))
        
        send_button = ttk.Button(input_frame, text="发送", command=self._send_message, style="Imperial.TButton")
        send_button.pack(side=tk.LEFT)
        
        # 中部区域 - 番茄钟
        pomodoro_frame = ttk.LabelFrame(main_interface, text="朝政时间", padding=10, style="Imperial.TLabelframe")
        pomodoro_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 计时器显示
        self.timer_label = ttk.Label(pomodoro_frame, text="25:00", foreground="#f6f1dc", background="#3a2a1a", font=("KaiTi", 48, "bold"))
        self.timer_label.pack(pady=20)
        
        # 控制按钮
        control_frame = ttk.Frame(pomodoro_frame, style="ImperialPanel.TFrame")
        control_frame.pack(pady=20)
        
        self.start_button = ttk.Button(control_frame, text="开始朝政", command=self._start_pomodoro, style="Imperial.TButton")
        self.start_button.pack(side=tk.LEFT, padx=10, ipady=5, ipadx=15)
        
        self.pause_button = ttk.Button(control_frame, text="暂停", command=self._pause_pomodoro, state=tk.DISABLED, style="Imperial.TButton")
        self.pause_button.pack(side=tk.LEFT, padx=10, ipady=5, ipadx=15)
        
        self.stop_button = ttk.Button(control_frame, text="停止", command=self._stop_pomodoro, state=tk.DISABLED, style="Imperial.TButton")
        self.stop_button.pack(side=tk.LEFT, padx=10, ipady=5, ipadx=15)
        
        # 设置按钮
        settings_button = ttk.Button(control_frame, text="设置", command=self._show_settings, style="Imperial.TButton")
        settings_button.pack(side=tk.LEFT, padx=10, ipady=5, ipadx=15)
        
        # 底部区域 - 状态信息
        status_frame = ttk.Frame(main_interface, style="ImperialPanel.TFrame")
        status_frame.pack(fill=tk.X, pady=10)
        
        self.status_label = ttk.Label(status_frame, text="准备就绪，陛下请指示", style="Imperial.TLabel")
        self.status_label.pack(anchor=tk.W)
    
    def _send_message(self):
        """发送消息给AI伴侣"""
        message = self.user_input.get().strip()
        if not message:
            return
        
        # 清空输入框
        self.user_input.delete(0, tk.END)
        
        # 添加用户消息到对话区域
        self.dialog_text.config(state=tk.NORMAL)
        self.dialog_text.insert(tk.END, f"\n\n陛下：{message}")
        
        # 获取AI回复
        response = companion.generate_response(message)
        self.dialog_text.insert(tk.END, f"\n\n{response}")
        
        # 滚动到底部
        self.dialog_text.see(tk.END)
        self.dialog_text.config(state=tk.DISABLED)
    
    def _start_pomodoro(self):
        """开始番茄钟"""
        self.pomodoro.start()
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="朝政时间开始，陛下请专注")
        
        # 发送开始消息给AI伴侣
        self.dialog_text.config(state=tk.NORMAL)
        self.dialog_text.insert(tk.END, f"\n\n{companion.generate_response('番茄钟开始')}")
        self.dialog_text.see(tk.END)
        self.dialog_text.config(state=tk.DISABLED)
    
    def _pause_pomodoro(self):
        """暂停番茄钟"""
        self.pomodoro.pause()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.status_label.config(text="朝政暂停，陛下请稍息")
    
    def _stop_pomodoro(self):
        """停止番茄钟"""
        self.pomodoro.stop()
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        self.timer_label.config(text="25:00")
        self.status_label.config(text="朝政已结束，准备就绪")
    
    def _on_time_update(self, remaining_time):
        """番茄钟时间更新回调"""
        time_str = self.pomodoro.get_time_string(remaining_time)
        self.timer_label.config(text=time_str)
    
    def _on_session_complete(self, is_long_break):
        """番茄钟会话完成回调"""
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)
        
        # 显示完成消息
        if is_long_break:
            message = "长休息时间到了，陛下请好好放松"
            self.timer_label.config(text="15:00")
        else:
            message = "短休息时间，陛下请稍作休息"
            self.timer_label.config(text="05:00")
        
        self.status_label.config(text=message)
        
        # 显示通知
        messagebox.showinfo("时间到", message)
        
        # 发送完成消息给AI伴侣
        self.dialog_text.config(state=tk.NORMAL)
        self.dialog_text.insert(tk.END, f"\n\n{companion.generate_response('番茄钟结束')}")
        self.dialog_text.see(tk.END)
        self.dialog_text.config(state=tk.DISABLED)
    
    def _show_settings(self):
        """显示设置对话框"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("朝政设置")
        settings_window.geometry("400x300")
        settings_window.transient(self.root)
        settings_window.grab_set()
        
        # 创建设置界面
        settings_frame = ttk.Frame(settings_window, padding=20, style="ImperialPanel.TFrame")
        settings_frame.pack(fill=tk.BOTH, expand=True)
        
        # 专注时间设置
        ttk.Label(settings_frame, text="专注时间（分钟）", style="Imperial.TLabel").grid(row=0, column=0, sticky=tk.W, pady=5)
        focus_var = tk.StringVar(value=str(self.pomodoro.focus_time // 60))
        focus_entry = ttk.Entry(settings_frame, textvariable=focus_var, width=10)
        focus_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # 短休息设置
        ttk.Label(settings_frame, text="短休息时间（分钟）", style="Imperial.TLabel").grid(row=1, column=0, sticky=tk.W, pady=5)
        short_var = tk.StringVar(value=str(self.pomodoro.short_break // 60))
        short_entry = ttk.Entry(settings_frame, textvariable=short_var, width=10)
        short_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # 长休息设置
        ttk.Label(settings_frame, text="长休息时间（分钟）", style="Imperial.TLabel").grid(row=2, column=0, sticky=tk.W, pady=5)
        long_var = tk.StringVar(value=str(self.pomodoro.long_break // 60))
        long_entry = ttk.Entry(settings_frame, textvariable=long_var, width=10)
        long_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # 会话次数设置
        ttk.Label(settings_frame, text="长休息前的会话次数", style="Imperial.TLabel").grid(row=3, column=0, sticky=tk.W, pady=5)
        sessions_var = tk.StringVar(value=str(self.pomodoro.sessions_before_long_break))
        sessions_entry = ttk.Entry(settings_frame, textvariable=sessions_var, width=10)
        sessions_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # 保存按钮
        def save_settings():
            try:
                focus = int(focus_var.get())
                short = int(short_var.get())
                long_rest = int(long_var.get())
                sessions = int(sessions_var.get())
                
                if focus <= 0 or short <= 0 or long_rest <= 0 or sessions <= 0:
                    messagebox.showerror("错误", "所有时间必须为正数")
                    return
                
                self.pomodoro.set_time_settings(focus, short, long_rest, sessions)
                self.timer_label.config(text=self.pomodoro.get_time_string())
                settings_window.destroy()
            except ValueError:
                messagebox.showerror("错误", "请输入有效的数字")
        
        save_button = ttk.Button(settings_frame, text="保存", command=save_settings, style="Imperial.TButton")
        save_button.grid(row=4, column=0, columnspan=2, pady=20)

def main():
    """主函数"""
    root = tk.Tk()
    app = EmpressApp(root)
    
    # 添加中文字体支持
    root.option_add("*Font", "KaiTi 10")
    
    # 启动应用
    root.mainloop()

if __name__ == "__main__":
    main()
