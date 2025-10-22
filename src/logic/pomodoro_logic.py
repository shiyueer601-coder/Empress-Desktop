import threading
import time
from typing import Callable, Optional

class PomodoroTimer:
    """番茄钟计时器类"""
    def __init__(self):
        self.focus_time = 25 * 60  # 默认专注时间25分钟
        self.short_break = 5 * 60  # 默认短休息5分钟
        self.long_break = 15 * 60  # 默认长休息15分钟
        self.sessions_before_long_break = 4
        
        self.current_session = 0
        self.is_running = False
        self.is_paused = False
        self.timer_thread = None
        self.remaining_time = self.focus_time
        
        # 回调函数
        self.on_time_update: Optional[Callable[[int], None]] = None
        self.on_session_complete: Optional[Callable[[bool], None]] = None  # 参数为是否是长休息
        
    def set_time_settings(self, focus: int, short: int, long_rest: int, sessions: int):
        """设置时间参数
        
        Args:
            focus: 专注时间（分钟）
            short: 短休息时间（分钟）
            long_rest: 长休息时间（分钟）
            sessions: 长休息前的专注次数
        """
        self.focus_time = focus * 60
        self.short_break = short * 60
        self.long_break = long_rest * 60
        self.sessions_before_long_break = sessions
        
        if not self.is_running:
            self.remaining_time = self.focus_time
    
    def start(self):
        """开始或恢复计时器"""
        if self.is_running:
            return
        
        if self.is_paused:
            self.is_paused = False
        else:
            self.remaining_time = self.focus_time
        
        self.is_running = True
        self.timer_thread = threading.Thread(target=self._timer_loop)
        self.timer_thread.daemon = True
        self.timer_thread.start()
    
    def pause(self):
        """暂停计时器"""
        if not self.is_running:
            return
        
        self.is_paused = True
        self.is_running = False
    
    def stop(self):
        """停止计时器并重置"""
        self.is_running = False
        self.is_paused = False
        self.remaining_time = self.focus_time
        self.current_session = 0
        
        if self.on_time_update:
            self.on_time_update(self.remaining_time)
    
    def _timer_loop(self):
        """计时器循环"""
        while self.is_running:
            if self.remaining_time > 0:
                time.sleep(1)
                if not self.is_paused:
                    self.remaining_time -= 1
                    if self.on_time_update:
                        self.on_time_update(self.remaining_time)
            else:
                # 会话完成
                self.is_running = False
                self.current_session += 1
                
                # 检查是否需要长休息
                is_long_break = self.current_session % self.sessions_before_long_break == 0
                
                if self.on_session_complete:
                    self.on_session_complete(is_long_break)
                
                # 准备下一个会话
                if is_long_break:
                    self.remaining_time = self.long_break
                else:
                    self.remaining_time = self.focus_time
                break
    
    def get_time_string(self, seconds: Optional[int] = None) -> str:
        """将秒数转换为 mm:ss 格式的字符串
        
        Args:
            seconds: 秒数，如果为None则使用当前剩余时间
            
        Returns:
            格式化的时间字符串
        """
        if seconds is None:
            seconds = self.remaining_time
        
        minutes, secs = divmod(seconds, 60)
        return f"{minutes:02d}:{secs:02d}"
    
    def get_current_status(self) -> dict:
        """获取当前计时器状态
        
        Returns:
            包含状态信息的字典
        """
        return {
            'is_running': self.is_running,
            'is_paused': self.is_paused,
            'remaining_time': self.remaining_time,
            'current_session': self.current_session,
            'time_string': self.get_time_string()
        }
