#!/usr/bin/env python3
"""
主题功能演示脚本
展示日间/夜间模式切换效果
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Qt
from src.theme import theme_manager


class ThemeDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZDTrans 主题演示")
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # 标题
        title = QLabel("主题切换演示")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin: 20px;")
        layout.addWidget(title)
        
        # 当前主题显示
        self.theme_label = QLabel(f"当前主题: {theme_manager.get_theme()}")
        self.theme_label.setAlignment(Qt.AlignCenter)
        self.theme_label.setStyleSheet("font-size: 14px; margin: 10px;")
        layout.addWidget(self.theme_label)
        
        # 切换按钮
        self.toggle_btn = QPushButton("🌙 切换到夜间模式")
        self.toggle_btn.setFixedHeight(50)
        self.toggle_btn.clicked.connect(self.toggle_theme)
        layout.addWidget(self.toggle_btn)
        
        # 说明文字
        info = QLabel("点击按钮体验主题切换效果\n所有窗口会同步更新")
        info.setAlignment(Qt.AlignCenter)
        info.setStyleSheet("margin: 20px;")
        layout.addWidget(info)
        
        self.setLayout(layout)
        
        # 连接主题变化信号
        theme_manager.theme_changed.connect(self.on_theme_changed)
        
        # 应用初始主题
        self.apply_theme(theme_manager.get_theme())
        
    def toggle_theme(self):
        """切换主题"""
        theme_manager.toggle_theme()
        
    def on_theme_changed(self, theme):
        """主题改变回调"""
        self.theme_label.setText(f"当前主题: {theme}")
        self.toggle_btn.setText("☀️ 切换到日间模式" if theme == 'dark' else "🌙 切换到夜间模式")
        self.apply_theme(theme)
        
    def apply_theme(self, theme):
        """应用主题"""
        if theme == 'dark':
            self.setStyleSheet("""
                QWidget {
                    background-color: #1e1e1e;
                    color: #e0e0e0;
                }
                QPushButton {
                    background-color: #0078d4;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #106ebe;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #f5f5f5;
                    color: #000000;
                }
                QPushButton {
                    background-color: #0078d4;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #106ebe;
                }
            """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ThemeDemo()
    demo.show()
    sys.exit(app.exec())
