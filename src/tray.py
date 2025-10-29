"""
系统托盘管理模块
负责创建和管理系统托盘图标及其菜单
"""

from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon, QAction
from PySide6.QtCore import QObject, Signal
import sys
import os


class TrayManager(QObject):
    """系统托盘管理器"""
    
    # 信号定义
    show_settings_signal = Signal()
    exit_signal = Signal()
    
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.tray_icon = None
        self.menu = None
        
    def create_tray(self):
        """创建系统托盘图标和菜单"""
        # 创建托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        
        # 设置图标（使用更明显的图标）
        from PySide6.QtWidgets import QApplication
        from PySide6.QtGui import QPixmap, QPainter, QColor
        
        # 创建一个简单的彩色图标
        pixmap = QPixmap(64, 64)
        pixmap.fill(QColor(0, 0, 0, 0))  # 透明背景
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制一个蓝色圆形
        painter.setBrush(QColor(0, 120, 215))  # 蓝色
        painter.setPen(QColor(255, 255, 255))
        painter.drawEllipse(8, 8, 48, 48)
        
        # 绘制 'T' 字母
        painter.setPen(QColor(255, 255, 255))
        from PySide6.QtGui import QFont
        font = QFont("Arial", 32, QFont.Bold)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), 0x84, "T")  # Qt.AlignCenter
        
        painter.end()
        
        icon = QIcon(pixmap)
        self.tray_icon.setIcon(icon)
        
        print("🎨 托盘图标已创建")
        
        # 创建菜单
        self.menu = QMenu()
        
        # 添加菜单项
        settings_action = QAction("⚙️ 设置", self)
        settings_action.triggered.connect(self.show_settings)
        self.menu.addAction(settings_action)
        
        self.menu.addSeparator()
        
        about_action = QAction("ℹ️ 关于", self)
        about_action.triggered.connect(self.show_about)
        self.menu.addAction(about_action)
        
        self.menu.addSeparator()
        
        exit_action = QAction("🚪 退出", self)
        exit_action.triggered.connect(self.exit_app)
        self.menu.addAction(exit_action)
        
        # 设置托盘菜单
        self.tray_icon.setContextMenu(self.menu)
        
        # macOS: 添加左键点击事件
        self.tray_icon.activated.connect(self._on_tray_activated)
        
        # 设置提示信息
        self.tray_icon.setToolTip("ZDTrans - 翻译助手\n左键点击打开菜单")
        
        # 显示托盘图标
        self.tray_icon.show()
        
        # 检查托盘是否真的显示了
        if self.tray_icon.isVisible():
            print("✅ 托盘图标已显示")
            print("💡 请在屏幕右上角状态栏查找蓝色圆形图标")
        else:
            print("⚠️  托盘图标可能未显示，请检查系统设置")
        
    def _on_tray_activated(self, reason):
        """托盘图标激活事件（macOS兼容）"""
        # 在macOS上，左键点击也显示菜单
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            if self.menu:
                # 获取托盘图标位置并显示菜单
                from PySide6.QtGui import QCursor
                self.menu.popup(QCursor.pos())
        
    def show_settings(self):
        """显示设置窗口"""
        self.show_settings_signal.emit()
        
    def show_about(self):
        """显示关于信息"""
        # TODO: 实现关于对话框
        pass
        
    def exit_app(self):
        """退出应用程序"""
        self.tray_icon.hide()
        self.exit_signal.emit()
        self.app.quit()
        
    def show_message(self, title, message, icon=QSystemTrayIcon.Information, duration=3000):
        """显示托盘消息通知"""
        if self.tray_icon:
            self.tray_icon.showMessage(title, message, icon, duration)
