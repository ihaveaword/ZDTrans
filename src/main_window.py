"""
主窗口界面模块
提供可视化的程序控制界面
"""

from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QPushButton, QTextEdit, QGroupBox, 
                               QStatusBar, QFrame)
from PySide6.QtCore import Qt, Signal, QTimer
from PySide6.QtGui import QFont, QIcon


class MainWindow(QMainWindow):
    """主窗口"""
    
    # 信号定义
    show_settings_signal = Signal()
    
    def __init__(self):
        super().__init__()
        self.translation_count = 0
        self.init_ui()
        
    def init_ui(self):
        """初始化UI"""
        self.setWindowTitle("ZDTrans - 智能翻译助手")
        self.setMinimumSize(600, 500)
        
        # 强制窗口居中显示
        from PySide6.QtGui import QScreen
        screen = QScreen.availableGeometry(self.screen())
        x = (screen.width() - 600) // 2
        y = (screen.height() - 500) // 2
        self.move(x, y)
        
        # 设置窗口属性，确保可见
        # 不使用置顶，避免 showEvent 问题
        self.setWindowFlags(Qt.Window)
        
        # 设置默认字体（macOS 兼容）
        from PySide6.QtGui import QFont
        default_font = QFont()
        default_font.setFamily("PingFang SC")  # macOS 中文字体
        default_font.setPointSize(13)
        self.setFont(default_font)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # 标题区域
        title_label = QLabel("ZDTrans 翻译助手")
        title_font = QFont("PingFang SC", 24, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 副标题
        subtitle = QLabel("全局快捷键翻译 · 专业术语优化")
        subtitle_font = QFont("PingFang SC", 14)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #666;")
        layout.addWidget(subtitle)
        
        layout.addSpacing(10)
        
        # 状态信息组
        status_group = QGroupBox("运行状态")
        status_layout = QVBoxLayout()
        
        self.status_label = QLabel("程序运行中，等待快捷键触发...")
        status_label_font = QFont("PingFang SC", 13)
        self.status_label.setFont(status_label_font)
        self.status_label.setStyleSheet("color: #0078d4; padding: 5px;")
        status_layout.addWidget(self.status_label)
        
        self.count_label = QLabel(f"已翻译: {self.translation_count} 次")
        count_label_font = QFont("PingFang SC", 12)
        self.count_label.setFont(count_label_font)
        self.count_label.setStyleSheet("color: #666; padding: 5px;")
        status_layout.addWidget(self.count_label)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # 快捷键说明组
        hotkey_group = QGroupBox("快捷键")
        hotkey_layout = QVBoxLayout()
        
        self.translate_hotkey_label = QLabel("翻译: Ctrl+Q")
        translate_font = QFont("PingFang SC", 13)
        self.translate_hotkey_label.setFont(translate_font)
        self.translate_hotkey_label.setStyleSheet("padding: 3px;")
        hotkey_layout.addWidget(self.translate_hotkey_label)
        
        self.polish_hotkey_label = QLabel("润色: Ctrl+Shift+Q")
        polish_font = QFont("PingFang SC", 13)
        self.polish_hotkey_label.setFont(polish_font)
        self.polish_hotkey_label.setStyleSheet("padding: 3px;")
        hotkey_layout.addWidget(self.polish_hotkey_label)
        
        hotkey_tip = QLabel("在任何应用中选中文字，按快捷键即可翻译\n未选中文字时，按翻译快捷键可显示本窗口")
        tip_font = QFont("PingFang SC", 11)
        hotkey_tip.setFont(tip_font)
        hotkey_tip.setWordWrap(True)
        hotkey_tip.setStyleSheet("color: #888; padding: 5px;")
        hotkey_layout.addWidget(hotkey_tip)
        
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        # 最近翻译结果
        result_group = QGroupBox("最近翻译")
        result_layout = QVBoxLayout()
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("翻译结果将显示在这里...")
        self.result_text.setMaximumHeight(150)
        # 设置字体
        result_font = QFont("PingFang SC", 12)
        self.result_text.setFont(result_font)
        result_layout.addWidget(self.result_text)
        
        result_group.setLayout(result_layout)
        layout.addWidget(result_group)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.settings_button = QPushButton("设置")
        settings_font = QFont("PingFang SC", 14, QFont.Bold)
        self.settings_button.setFont(settings_font)
        self.settings_button.setMinimumHeight(40)
        self.settings_button.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #106ebe;
            }
            QPushButton:pressed {
                background-color: #005a9e;
            }
        """)
        self.settings_button.clicked.connect(self.on_settings_clicked)
        button_layout.addWidget(self.settings_button)
        
        self.minimize_button = QPushButton("最小化")
        minimize_font = QFont("PingFang SC", 14)
        self.minimize_button.setFont(minimize_font)
        self.minimize_button.setMinimumHeight(40)
        self.minimize_button.setStyleSheet("""
            QPushButton {
                background-color: #5c5c5c;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #6c6c6c;
            }
            QPushButton:pressed {
                background-color: #4c4c4c;
            }
        """)
        self.minimize_button.clicked.connect(self.hide)
        button_layout.addWidget(self.minimize_button)
        
        layout.addLayout(button_layout)
        
        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)
        
        # 提示信息
        tip_label = QLabel("提示: 关闭此窗口不会退出程序，程序将继续在后台运行")
        tip_font = QFont("PingFang SC", 11)
        tip_label.setFont(tip_font)
        tip_label.setWordWrap(True)
        tip_label.setStyleSheet("color: #888;")
        layout.addWidget(tip_label)
        
        central_widget.setLayout(layout)
        
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
        
        # 设置窗口样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QGroupBox {
                font-weight: bold;
                font-family: 'PingFang SC';
                border: 2px solid #ddd;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                font-family: 'PingFang SC';
            }
        """)
        
    def on_settings_clicked(self):
        """设置按钮点击"""
        self.show_settings_signal.emit()
        
    def update_status(self, message, duration=3000):
        """更新状态消息"""
        self.status_label.setText(message)
        self.statusBar.showMessage(message, duration)
        
        # 3秒后恢复默认状态
        QTimer.singleShot(duration, lambda: self.status_label.setText("程序运行中，等待快捷键触发..."))
        
    def update_hotkeys(self, translate_hotkey, polish_hotkey):
        """更新快捷键显示"""
        self.translate_hotkey_label.setText(f"翻译: {translate_hotkey}")
        self.polish_hotkey_label.setText(f"润色: {polish_hotkey}")
        
    def show_translation_result(self, result, action_type):
        """显示翻译结果"""
        self.translation_count += 1
        self.count_label.setText(f"已翻译: {self.translation_count} 次")
        
        action_name = "翻译" if action_type == "translate" else "润色"
        timestamp = QTimer().singleShot(0, lambda: None)  # 简单时间戳
        
        # 在结果区显示
        current_text = self.result_text.toPlainText()
        new_text = f"[{action_name}]\n{result}\n\n{current_text}"
        
        # 限制显示最近3条结果
        lines = new_text.split('\n\n')
        if len(lines) > 3:
            new_text = '\n\n'.join(lines[:3])
            
        self.result_text.setPlainText(new_text)
        
        # 更新状态
        self.update_status(f"{action_name}完成")
        
    def show_translation_error(self, error_msg):
        """显示翻译错误"""
        self.status_label.setText(f"错误: {error_msg}")
        self.statusBar.showMessage(f"错误: {error_msg}", 5000)
        
        QTimer.singleShot(5000, lambda: self.status_label.setText("程序运行中，等待快捷键触发..."))
        
    def closeEvent(self, event):
        """关闭事件 - 隐藏窗口而不是退出"""
        event.ignore()
        self.hide()
        self.update_status("窗口已最小化")
        
    def showEvent(self, event):
        """显示事件"""
        super().showEvent(event)
