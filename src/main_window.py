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
        self.setFixedSize(700, 750)
        
        # 强制窗口居中显示
        from PySide6.QtGui import QScreen
        screen = QScreen.availableGeometry(self.screen())
        x = (screen.width() - 700) // 2
        y = (screen.height() - 750) // 2
        self.move(x, y)
        
        # 设置窗口属性
        self.setWindowFlags(Qt.Window)
        
        # 设置默认字体
        default_font = QFont("PingFang SC", 12)
        self.setFont(default_font)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # 标题
        title_label = QLabel("ZDTrans 翻译助手")
        title_font = QFont("PingFang SC", 20, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 副标题
        subtitle = QLabel("全局快捷键翻译 · 专业术语优化")
        subtitle_font = QFont("PingFang SC", 12)
        subtitle.setFont(subtitle_font)
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #666; margin-bottom: 10px;")
        layout.addWidget(subtitle)
        
        # 状态信息组
        status_group = QGroupBox("运行状态")
        status_layout = QVBoxLayout()
        status_layout.setContentsMargins(15, 15, 15, 15)
        status_layout.setSpacing(10)
        
        self.status_label = QLabel("程序运行中")
        status_font = QFont("PingFang SC", 12)
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet("color: #0078d4;")
        status_layout.addWidget(self.status_label)
        
        self.count_label = QLabel(f"已翻译: {self.translation_count} 次")
        count_font = QFont("PingFang SC", 11)
        self.count_label.setFont(count_font)
        self.count_label.setStyleSheet("color: #666;")
        status_layout.addWidget(self.count_label)
        
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)
        
        # 快捷键组
        hotkey_group = QGroupBox("快捷键")
        hotkey_layout = QVBoxLayout()
        hotkey_layout.setContentsMargins(15, 15, 15, 15)
        hotkey_layout.setSpacing(10)
        
        translate_label = QLabel("翻译: Ctrl+Q")
        translate_font = QFont("PingFang SC", 12)
        translate_label.setFont(translate_font)
        hotkey_layout.addWidget(translate_label)
        
        polish_label = QLabel("润色: Ctrl+Shift+Q")
        polish_font = QFont("PingFang SC", 12)
        polish_label.setFont(polish_font)
        hotkey_layout.addWidget(polish_label)
        
        tip = QLabel("选中文字后按快捷键翻译\n无选中时按 Ctrl+Q 显示此窗口")
        tip_font = QFont("PingFang SC", 10)
        tip.setFont(tip_font)
        tip.setStyleSheet("color: #888;")
        tip.setWordWrap(True)
        hotkey_layout.addWidget(tip)
        
        # 保存引用用于更新
        self.translate_hotkey_label = translate_label
        self.polish_hotkey_label = polish_label
        
        hotkey_group.setLayout(hotkey_layout)
        layout.addWidget(hotkey_group)
        
        # 翻译结果组
        result_group = QGroupBox("最近翻译")
        result_layout = QVBoxLayout()
        result_layout.setContentsMargins(15, 15, 15, 15)
        
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("翻译结果将显示在这里...")
        self.result_text.setFixedHeight(120)
        result_font = QFont("PingFang SC", 11)
        self.result_text.setFont(result_font)
        result_layout.addWidget(self.result_text)
        
        result_group.setLayout(result_layout)
        layout.addWidget(result_group)
        
        # 按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        settings_btn = QPushButton("设置")
        settings_btn.setFixedHeight(40)
        settings_font = QFont("PingFang SC", 13, QFont.Bold)
        settings_btn.setFont(settings_font)
        settings_btn.setStyleSheet("""
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #106ebe; }
            QPushButton:pressed { background-color: #005a9e; }
        """)
        settings_btn.clicked.connect(self.on_settings_clicked)
        button_layout.addWidget(settings_btn)
        
        minimize_btn = QPushButton("最小化")
        minimize_btn.setFixedHeight(40)
        minimize_font = QFont("PingFang SC", 13)
        minimize_btn.setFont(minimize_font)
        minimize_btn.setStyleSheet("""
            QPushButton {
                background-color: #5c5c5c;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #6c6c6c; }
            QPushButton:pressed { background-color: #4c4c4c; }
        """)
        minimize_btn.clicked.connect(self.hide)
        button_layout.addWidget(minimize_btn)
        
        self.settings_button = settings_btn
        self.minimize_button = minimize_btn
        
        layout.addLayout(button_layout)
        
        # 提示信息
        tip_label = QLabel("提示: 关闭窗口不会退出程序")
        tip_label.setAlignment(Qt.AlignCenter)
        tip_font = QFont("PingFang SC", 10)
        tip_label.setFont(tip_font)
        tip_label.setStyleSheet("color: #888; margin-top: 10px;")
        layout.addWidget(tip_label)
        
        # 弹性空间
        layout.addStretch()
        
        # 状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("就绪")
        
        # 窗口样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QGroupBox {
                font-family: 'PingFang SC';
                font-size: 13px;
                font-weight: bold;
                border: 2px solid #ddd;
                border-radius: 6px;
                margin-top: 10px;
                padding: 15px 10px 10px 10px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
            }
        """)
        
    def on_settings_clicked(self):
        """设置按钮点击"""
        self.show_settings_signal.emit()
        
    def update_status(self, message, duration=3000):
        """更新状态消息"""
        self.status_label.setText(message)
        self.statusBar.showMessage(message, duration)
        QTimer.singleShot(duration, lambda: self.status_label.setText("程序运行中"))
        
    def update_hotkeys(self, translate_hotkey, polish_hotkey):
        """更新快捷键显示"""
        self.translate_hotkey_label.setText(f"翻译: {translate_hotkey}")
        self.polish_hotkey_label.setText(f"润色: {polish_hotkey}")
        
    def show_translation_result(self, result, action_type):
        """显示翻译结果"""
        self.translation_count += 1
        self.count_label.setText(f"已翻译: {self.translation_count} 次")
        
        action_name = "翻译" if action_type == "translate" else "润色"
        
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
        QTimer.singleShot(5000, lambda: self.status_label.setText("程序运行中"))
        
    def closeEvent(self, event):
        """关闭事件 - 隐藏窗口而不是退出"""
        event.ignore()
        self.hide()
        self.update_status("窗口已最小化")
        
    def showEvent(self, event):
        """显示事件"""
        super().showEvent(event)

