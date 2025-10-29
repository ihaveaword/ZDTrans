#!/usr/bin/env python3
"""测试快捷键解析功能"""

from src.hotkey import HotkeyManager

def test_parse_hotkey():
    manager = HotkeyManager()
    
    # 测试各种格式
    test_cases = [
        ('Ctrl+Q', {'ctrl', 'q'}),
        ('Ctrl+Shift+Q', {'ctrl', 'shift', 'q'}),
        ('Alt+X', {'alt', 'x'}),
        ('Ctrl+Alt+S', {'ctrl', 'alt', 's'}),
        ('Cmd+C', {'cmd', 'c'}),
    ]
    
    print("测试快捷键解析:")
    for hotkey_str, expected in test_cases:
        result = manager.parse_hotkey_string(hotkey_str)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{hotkey_str}' -> {result} (期望: {expected})")

if __name__ == "__main__":
    test_parse_hotkey()
