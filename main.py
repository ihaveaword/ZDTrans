"""
ZDTrans 主程序入口
一个轻量级桌面翻译和文本润色工具
"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from src.tray import TrayManager
from src.hotkey import HotkeyManager
from src.translator import TranslatorManager
from src.popup import PopupWindow
from src.settings import SettingsDialog
from src.clipboard import ClipboardManager
from src.utils import load_config, save_config, setup_logging, check_first_run
from src.permissions import request_accessibility_permission
from src.main_window import MainWindow


class ZDTransApp:
    """ZDTrans 应用程序主类"""
    
    def __init__(self):
        # 创建Qt应用
        self.app = QApplication(sys.argv)
        self.app.setQuitOnLastWindowClosed(False)  # 关闭窗口不退出程序
        
        # 设置日志
        setup_logging()
        
        # 检查 macOS 辅助功能权限
        if not request_accessibility_permission():
            print("\n⚠️  警告: 未授予辅助功能权限，全局快捷键可能无法工作！")
            print("程序将继续运行，但请尽快授予权限。\n")
        
        # 加载配置
        self.config = load_config()
        
        # 检查是否首次运行
        if check_first_run():
            self.show_first_run_dialog()
        
        # 初始化组件
        self.main_window = None
        self.tray_manager = None
        self.hotkey_manager = None
        self.translator_manager = None
        self.popup_window = None
        self.clipboard_manager = None
        self.settings_dialog = None
        
        self.init_components()
        
    def init_components(self):
        """初始化各个组件"""
        print("\n" + "="*50)
        print("正在初始化 ZDTrans 组件...")
        print("="*50)
        
        # 创建主窗口
        print("📱 创建主窗口...")
        self.main_window = MainWindow()
        self.main_window.show_settings_signal.connect(self.show_settings)
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()
        print(f"   ✅ 主窗口已显示 (可见性: {self.main_window.isVisible()})")
        
        # 更新主窗口的快捷键显示
        hotkey_config = self.config.get('hotkey', {})
        self.main_window.update_hotkeys(
            hotkey_config.get('translate', 'Ctrl+Q'),
            hotkey_config.get('polish', 'Ctrl+Shift+Q')
        )
        
        # 创建系统托盘
        print("🎨 创建系统托盘...")
        self.tray_manager = TrayManager(self.app)
        self.tray_manager.create_tray()
        self.tray_manager.show_settings_signal.connect(self.show_settings)
        
        # 添加托盘菜单项：显示主窗口
        from PySide6.QtGui import QAction
        show_window_action = QAction("📱 显示主窗口", self.tray_manager.menu)
        show_window_action.triggered.connect(self.show_main_window)
        # 插入到设置菜单之前
        actions = self.tray_manager.menu.actions()
        if actions:
            self.tray_manager.menu.insertAction(actions[0], show_window_action)
            self.tray_manager.menu.insertSeparator(actions[0])
        
        # 创建快捷键管理器
        print("⌨️  创建快捷键管理器...")
        self.hotkey_manager = HotkeyManager()
        # 从配置加载快捷键
        self.hotkey_manager.update_hotkeys(
            hotkey_config.get('translate', 'Ctrl+Q'),
            hotkey_config.get('polish', 'Ctrl+Shift+Q')
        )
        self.hotkey_manager.translate_triggered.connect(self.on_translate)
        self.hotkey_manager.polish_triggered.connect(self.on_polish)
        self.hotkey_manager.start_listening()
        print("   ✅ 快捷键监听已启动")
        
        # 创建翻译管理器
        print("🌐 创建翻译管理器...")
        self.translator_manager = TranslatorManager(self.config['api'])
        self.translator_manager.translation_ready.connect(self.on_translation_ready)
        self.translator_manager.translation_error.connect(self.on_translation_error)
        
        # 加载关键词配置
        trans_config = self.config.get('translation', {})
        keywords = trans_config.get('keywords', '')
        if keywords:
            self.translator_manager.set_keywords(keywords)
        
        # 创建弹出窗口
        self.popup_window = PopupWindow()
        
        # 创建剪贴板管理器
        self.clipboard_manager = ClipboardManager()
        
        print("\n" + "="*50)
        print("✅ ZDTrans 已启动，等待快捷键触发...")
        print("="*50)
        print(f"\n💡 主窗口应该已经显示在屏幕上")
        print(f"   如果看不到，请:")
        print(f"   1. 检查是否被其他窗口遮挡")
        print(f"   2. 按 Cmd+Tab 查看应用列表")
        print(f"   3. 检查是否在其他桌面/空间\n")
        
        self.tray_manager.show_message("ZDTrans", "程序已启动，使用 Ctrl+Q 快速翻译")
        self.main_window.update_status("程序已启动")
        
    def show_main_window(self):
        """显示主窗口"""
        print("显示主窗口")
        self.main_window.show()
        self.main_window.raise_()
        self.main_window.activateWindow()
        
    def show_first_run_dialog(self):
        """首次运行时显示欢迎信息"""
        # TODO: 实现首次运行向导
        pass
        
    def show_settings(self):
        """显示设置对话框"""
        if not self.settings_dialog:
            self.settings_dialog = SettingsDialog(self.config)
            self.settings_dialog.settings_saved.connect(self.on_settings_saved)
            
        self.settings_dialog.show()
        self.settings_dialog.raise_()
        self.settings_dialog.activateWindow()
        
    def on_settings_saved(self, new_config):
        """设置保存后的处理"""
        self.config = new_config
        save_config(new_config)
        
        # 更新翻译管理器的配置
        self.translator_manager.update_config(new_config['api'])
        
        # 更新快捷键配置
        hotkey_config = new_config.get('hotkey', {})
        self.hotkey_manager.update_hotkeys(
            hotkey_config.get('translate', 'Ctrl+Q'),
            hotkey_config.get('polish', 'Ctrl+Shift+Q')
        )
        
        self.tray_manager.show_message("ZDTrans", "设置已保存")
        
    def on_translate(self):
        """翻译快捷键触发"""
        print("翻译快捷键触发")
        
        # 获取选中的文本
        selected_text = self.clipboard_manager.get_selected_text()
        
        if not selected_text or not selected_text.strip():
            # 如果没有选中文本，显示主窗口
            print("未选中文本，显示主窗口")
            self.show_main_window()
            return
            
        print(f"选中的文本: {selected_text}")
        
        # 显示加载状态
        self.popup_window.show_loading('translate')
        
        # 开始翻译
        self.translator_manager.translate(selected_text)
        
    def on_polish(self):
        """润色快捷键触发"""
        print("润色快捷键触发")
        
        # 获取选中的文本
        selected_text = self.clipboard_manager.get_selected_text()
        
        if not selected_text or not selected_text.strip():
            self.tray_manager.show_message("ZDTrans", "未选中文本", duration=2000)
            return
            
        print(f"选中的文本: {selected_text}")
        
        # 显示加载状态
        self.popup_window.show_loading('polish')
        
        # 开始润色
        self.translator_manager.polish(selected_text)
        
    def on_translation_ready(self, result, action_type):
        """翻译/润色结果准备就绪"""
        print(f"翻译结果: {result}")
        self.popup_window.show_result(result, action_type)
        self.main_window.show_translation_result(result, action_type)
        self.main_window.show_translation_result(result, action_type)
        
    def on_translation_error(self, error_msg):
        """翻译/润色错误"""
        print(f"翻译错误: {error_msg}")
        self.popup_window.show_error(error_msg)
        self.main_window.show_translation_error(error_msg)
        
    def run(self):
        """运行应用程序"""
        return self.app.exec()
        

def main():
    """主函数"""
    # 在 macOS 上启用高 DPI 支持
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
        
    # 创建并运行应用
    app = ZDTransApp()
    sys.exit(app.run())


if __name__ == "__main__":
    main()
