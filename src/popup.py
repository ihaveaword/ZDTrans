"""
弹出窗口UI模块
显示翻译和润色结果
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QTimer, QPoint
from PySide6.QtGui import QCursor, QFont
import pyperclip
from .theme import theme_manager


class PopupWindow(QWidget):
    """弹出窗口"""
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        # 连接主题变化信号
        theme_manager.theme_changed.connect(self.apply_theme)
        
    def init_ui(self):
        """初始化UI"""
        # 窗口设置
        self.setWindowFlags(
            Qt.FramelessWindowHint |  # 无边框
            Qt.WindowStaysOnTopHint |  # 置顶
            Qt.Tool  # 工具窗口（不显示在任务栏）
        )
        
        # 设置半透明背景
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # 应用初始主题
        self.apply_theme(theme_manager.get_theme())
        
        # 布局
        layout = QVBoxLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # 标题标签
        self.title_label = QLabel("正在处理...")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)
        
        # 结果文本框
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumSize(400, 200)
        layout.addWidget(self.result_text)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        
        self.copy_button = QPushButton("复制")
        self.copy_button.clicked.connect(self.copy_result)
        button_layout.addWidget(self.copy_button)
        
        self.close_button = QPushButton("关闭")
        self.close_button.clicked.connect(self.hide)
        button_layout.addWidget(self.close_button)
        
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # 设置窗口大小
        self.setFixedSize(450, 300)
        
    def apply_theme(self, theme):
        """应用主题"""
        self.setStyleSheet(theme_manager.get_popup_style(theme))
        
    def show_loading(self, action_type='translate'):
        """显示加载状态"""
        action_name = "翻译" if action_type == 'translate' else "润色"
        self.title_label.setText(f"正在{action_name}中...")
        self.result_text.setText("请稍候...")
        self.show_near_cursor()
        
    def show_result(self, result, action_type='translate'):
        """显示结果"""
        action_name = "翻译" if action_type == 'translate' else "润色"
        self.title_label.setText(f"{action_name}结果")
        self.result_text.setText(result)
        
    def show_error(self, error_msg):
        """显示错误信息"""
        self.title_label.setText("错误")
        self.result_text.setText(f"发生错误：\n{error_msg}")
        
    def show_near_cursor(self):
        """在鼠标附近显示窗口"""
        # 获取鼠标位置
        cursor_pos = QCursor.pos()
        
        # 计算窗口位置（鼠标右下方，留一些偏移）
        x = cursor_pos.x() + 20
        y = cursor_pos.y() + 20
        
        # 确保窗口不会超出屏幕
        screen = self.screen().geometry()
        if x + self.width() > screen.right():
            x = cursor_pos.x() - self.width() - 20
        if y + self.height() > screen.bottom():
            y = cursor_pos.y() - self.height() - 20
            
        self.move(x, y)
        self.show()
        self.raise_()
        self.activateWindow()
        
    def copy_result(self):
        """复制结果到剪贴板"""
        text = self.result_text.toPlainText()
        if text:
            pyperclip.copy(text)
            self.title_label.setText("已复制到剪贴板")
            
            # 1秒后恢复标题
            QTimer.singleShot(1000, lambda: self.title_label.setText("翻译结果"))
            
    def keyPressEvent(self, event):
        """按键事件"""
        if event.key() == Qt.Key_Escape:
            self.hide()
