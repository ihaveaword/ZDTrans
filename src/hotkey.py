"""
全局快捷键监听模块
负责注册和监听全局快捷键
"""

from pynput import keyboard
from PySide6.QtCore import QObject, Signal
import threading


class HotkeyManager(QObject):
    """全局快捷键管理器"""
    
    # 信号定义
    translate_triggered = Signal()
    polish_triggered = Signal()
    
    def __init__(self):
        super().__init__()
        self.listener = None
        self.current_keys = set()
        self.hotkeys = {
            'translate': {'ctrl', 'q'},  # Ctrl+Q for translate
            'polish': {'ctrl', 'shift', 'q'}  # Ctrl+Shift+Q for polish
        }
        
    def parse_hotkey_string(self, hotkey_str):
        """
        解析快捷键字符串为按键集合
        例如: 'Ctrl+Q' -> {'ctrl', 'q'}
              'Ctrl+Shift+Q' -> {'ctrl', 'shift', 'q'}
        """
        if not hotkey_str:
            return set()
            
        keys = set()
        parts = hotkey_str.lower().split('+')
        
        for part in parts:
            part = part.strip()
            # 标准化某些按键名称
            if part in ['control', 'ctl']:
                part = 'ctrl'
            elif part == 'command' or part == 'cmd':
                part = 'cmd'
            elif part == 'option':
                part = 'alt'
                
            keys.add(part)
            
        return keys
        
    def update_hotkeys(self, translate_hotkey, polish_hotkey):
        """
        更新快捷键配置
        
        Args:
            translate_hotkey: 翻译快捷键字符串，如 'Ctrl+Q'
            polish_hotkey: 润色快捷键字符串，如 'Ctrl+Shift+Q'
        """
        self.hotkeys['translate'] = self.parse_hotkey_string(translate_hotkey)
        self.hotkeys['polish'] = self.parse_hotkey_string(polish_hotkey)
        print(f"快捷键已更新: 翻译={translate_hotkey}, 润色={polish_hotkey}")
        
    def start_listening(self):
        """开始监听快捷键"""
        self.listener = keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        )
        self.listener.start()
        
    def stop_listening(self):
        """停止监听快捷键"""
        if self.listener:
            self.listener.stop()
            
    def _normalize_key(self, key):
        """标准化按键名称"""
        try:
            # 处理特殊键
            if hasattr(key, 'name'):
                return key.name.lower()
            # 处理字符键
            elif hasattr(key, 'char') and key.char:
                return key.char.lower()
        except AttributeError:
            pass
        return str(key).lower()
        
    def _on_press(self, key):
        """按键按下事件"""
        normalized = self._normalize_key(key)
        
        # 将ctrl_l/ctrl_r统一为ctrl
        if normalized in ['ctrl_l', 'ctrl_r']:
            normalized = 'ctrl'
        elif normalized in ['shift_l', 'shift_r']:
            normalized = 'shift'
        elif normalized in ['alt_l', 'alt_r']:
            normalized = 'alt'
            
        self.current_keys.add(normalized)
        
        # 检查是否匹配快捷键
        self._check_hotkeys()
        
    def _on_release(self, key):
        """按键释放事件"""
        normalized = self._normalize_key(key)
        
        # 将ctrl_l/ctrl_r统一为ctrl
        if normalized in ['ctrl_l', 'ctrl_r']:
            normalized = 'ctrl'
        elif normalized in ['shift_l', 'shift_r']:
            normalized = 'shift'
        elif normalized in ['alt_l', 'alt_r']:
            normalized = 'alt'
            
        self.current_keys.discard(normalized)
        
    def _check_hotkeys(self):
        """检查当前按键组合是否匹配预设的快捷键"""
        # 使用一个标志避免重复触发
        if not hasattr(self, '_last_triggered'):
            self._last_triggered = None
            
        # 检查翻译快捷键
        if self.current_keys == self.hotkeys['translate']:
            if self._last_triggered != 'translate':
                self._last_triggered = 'translate'
                self.translate_triggered.emit()
            
        # 检查润色快捷键
        elif self.current_keys == self.hotkeys['polish']:
            if self._last_triggered != 'polish':
                self._last_triggered = 'polish'
                self.polish_triggered.emit()
        else:
            # 如果当前按键不匹配任何快捷键，重置标志
            self._last_triggered = None
            
    def set_hotkey(self, action, keys):
        """
        设置快捷键
        
        Args:
            action: 'translate' or 'polish'
            keys: set of key names, e.g., {'ctrl', 'q'}
        """
        if action in self.hotkeys:
            self.hotkeys[action] = keys
            
    def get_hotkey(self, action):
        """获取快捷键配置"""
        return self.hotkeys.get(action, set())
