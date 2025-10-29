"""
快捷键编辑器组件
允许用户通过按键来设置快捷键
"""

from PySide6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import Qt, Signal
from pynput import keyboard


class HotkeyEditor(QWidget):
    """快捷键编辑器"""
    
    # 当快捷键改变时发出信号
    hotkey_changed = Signal(str)  # 新的快捷键字符串
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.current_hotkey = ""
        self.is_recording = False
        self.pressed_keys = set()
        self.listener = None
        
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 显示当前快捷键的输入框
        self.hotkey_display = QLineEdit()
        self.hotkey_display.setReadOnly(True)
        self.hotkey_display.setPlaceholderText("点击'录制'按钮设置快捷键")
        layout.addWidget(self.hotkey_display)
        
        # 录制按钮
        self.record_button = QPushButton("录制")
        self.record_button.setFixedWidth(80)
        self.record_button.clicked.connect(self.toggle_recording)
        layout.addWidget(self.record_button)
        
        # 清除按钮
        self.clear_button = QPushButton("清除")
        self.clear_button.setFixedWidth(60)
        self.clear_button.clicked.connect(self.clear_hotkey)
        layout.addWidget(self.clear_button)
        
        self.setLayout(layout)
        
    def set_hotkey(self, hotkey_str):
        """设置快捷键显示"""
        self.current_hotkey = hotkey_str
        self.hotkey_display.setText(hotkey_str)
        
    def get_hotkey(self):
        """获取当前快捷键"""
        return self.current_hotkey
        
    def toggle_recording(self):
        """切换录制状态"""
        if self.is_recording:
            self.stop_recording()
        else:
            self.start_recording()
            
    def start_recording(self):
        """开始录制快捷键"""
        self.is_recording = True
        self.pressed_keys.clear()
        self.record_button.setText("按下快捷键...")
        self.record_button.setStyleSheet("background-color: #ff6b6b; color: white;")
        self.hotkey_display.setText("等待输入...")
        
        # 启动键盘监听
        self.listener = keyboard.Listener(
            on_press=self._on_key_press,
            on_release=self._on_key_release
        )
        self.listener.start()
        
    def stop_recording(self):
        """停止录制快捷键"""
        self.is_recording = False
        self.record_button.setText("录制")
        self.record_button.setStyleSheet("")
        
        # 停止键盘监听
        if self.listener:
            self.listener.stop()
            self.listener = None
            
    def _normalize_key(self, key):
        """标准化按键名称"""
        try:
            # 处理特殊键
            if hasattr(key, 'name'):
                name = key.name.lower()
                # 统一左右修饰键
                if name in ['ctrl_l', 'ctrl_r']:
                    return 'ctrl'
                elif name in ['shift_l', 'shift_r']:
                    return 'shift'
                elif name in ['alt_l', 'alt_r', 'alt_gr']:
                    return 'alt'
                elif name in ['cmd', 'cmd_l', 'cmd_r']:
                    return 'cmd'
                return name
            # 处理字符键
            elif hasattr(key, 'char') and key.char:
                return key.char.lower()
        except AttributeError:
            pass
        return str(key).lower()
        
    def _on_key_press(self, key):
        """按键按下事件"""
        if not self.is_recording:
            return
            
        normalized = self._normalize_key(key)
        self.pressed_keys.add(normalized)
        
        # 实时显示当前按下的键
        self._update_display()
        
    def _on_key_release(self, key):
        """按键释放事件"""
        if not self.is_recording:
            return
            
        # 当释放任意键时，如果已经有组合键，则完成录制
        if len(self.pressed_keys) > 0:
            # 确保至少有一个修饰键（Ctrl/Shift/Alt/Cmd）
            modifiers = {'ctrl', 'shift', 'alt', 'cmd'}
            if self.pressed_keys & modifiers:
                self._finish_recording()
            else:
                # 如果只是普通键，继续等待
                self.hotkey_display.setText("请使用修饰键组合（Ctrl/Shift/Alt）")
                self.pressed_keys.clear()
                
    def _update_display(self):
        """更新显示"""
        if not self.pressed_keys:
            return
            
        # 排序键以保证一致性：修饰键在前，普通键在后
        modifier_order = ['ctrl', 'alt', 'shift', 'cmd']
        modifiers = []
        normal_keys = []
        
        for key in self.pressed_keys:
            if key in modifier_order:
                modifiers.append(key)
            else:
                normal_keys.append(key)
                
        # 按预定义顺序排序修饰键
        modifiers.sort(key=lambda x: modifier_order.index(x))
        
        # 组合显示
        all_keys = modifiers + sorted(normal_keys)
        display_text = '+'.join(k.capitalize() for k in all_keys)
        self.hotkey_display.setText(display_text)
        
    def _finish_recording(self):
        """完成录制"""
        # 生成快捷键字符串
        modifier_order = ['ctrl', 'alt', 'shift', 'cmd']
        modifiers = []
        normal_keys = []
        
        for key in self.pressed_keys:
            if key in modifier_order:
                modifiers.append(key)
            else:
                normal_keys.append(key)
                
        modifiers.sort(key=lambda x: modifier_order.index(x))
        all_keys = modifiers + sorted(normal_keys)
        
        # 转换为标准格式（首字母大写，用+连接）
        hotkey_str = '+'.join(k.capitalize() for k in all_keys)
        
        self.current_hotkey = hotkey_str
        self.hotkey_display.setText(hotkey_str)
        
        # 发出信号
        self.hotkey_changed.emit(hotkey_str)
        
        # 停止录制
        self.stop_recording()
        
    def clear_hotkey(self):
        """清除快捷键"""
        self.current_hotkey = ""
        self.hotkey_display.clear()
        self.hotkey_changed.emit("")
