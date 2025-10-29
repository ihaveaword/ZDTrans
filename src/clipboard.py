"""
剪贴板操作模块
负责获取选中文本和剪贴板管理
"""

import pyperclip
import time
from pynput.keyboard import Key, Controller


class ClipboardManager:
    """剪贴板管理器"""
    
    def __init__(self):
        self.keyboard = Controller()
        
    def get_selected_text(self):
        """
        获取当前选中的文本
        
        通过模拟 Ctrl+C 来获取选中的文本
        会保存和恢复原剪贴板内容
        
        Returns:
            str: 选中的文本，如果没有选中或出错则返回空字符串
        """
        # 保存原剪贴板内容
        original_clipboard = pyperclip.paste()
        
        # 清空剪贴板
        pyperclip.copy('')
        
        # 短暂延迟，确保剪贴板已清空
        time.sleep(0.05)
        
        # 模拟 Ctrl+C
        try:
            # 按下 Ctrl
            self.keyboard.press(Key.ctrl if not self._is_mac() else Key.cmd)
            # 按下 C
            self.keyboard.press('c')
            # 释放 C
            self.keyboard.release('c')
            # 释放 Ctrl
            self.keyboard.release(Key.ctrl if not self._is_mac() else Key.cmd)
            
            # 等待剪贴板更新
            time.sleep(0.1)
            
            # 获取新的剪贴板内容
            selected_text = pyperclip.paste()
            
            # 恢复原剪贴板内容
            pyperclip.copy(original_clipboard)
            
            return selected_text
            
        except Exception as e:
            # 出错时恢复剪贴板
            pyperclip.copy(original_clipboard)
            print(f"Error getting selected text: {e}")
            return ""
            
    def set_clipboard(self, text):
        """设置剪贴板内容"""
        pyperclip.copy(text)
        
    def get_clipboard(self):
        """获取剪贴板内容"""
        return pyperclip.paste()
        
    def _is_mac(self):
        """检测是否为macOS系统"""
        import platform
        return platform.system() == 'Darwin'
