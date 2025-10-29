"""
macOS 权限检查模块
"""

import platform
import subprocess


def is_macos():
    """检查是否为 macOS 系统"""
    return platform.system() == 'Darwin'


def check_accessibility_permission():
    """
    检查是否已授予辅助功能权限
    
    Returns:
        bool: True if has permission, False otherwise
    """
    if not is_macos():
        return True
        
    try:
        # 在 macOS 上，尝试使用 AppleScript 检查权限
        script = '''
        tell application "System Events"
            return enabled of accessibility features
        end tell
        '''
        result = subprocess.run(
            ['osascript', '-e', script],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0 and 'true' in result.stdout.lower()
    except Exception as e:
        print(f"权限检查失败: {e}")
        return False


def show_accessibility_instructions():
    """显示如何授予辅助功能权限的说明"""
    print("\n" + "=" * 60)
    print("⚠️  需要辅助功能权限")
    print("=" * 60)
    print("\nmacOS 需要辅助功能权限才能监听全局快捷键。")
    print("\n请按照以下步骤授予权限：")
    print("\n1. 打开 '系统偏好设置' (System Preferences)")
    print("2. 进入 '安全性与隐私' (Security & Privacy)")
    print("3. 选择 '隐私' (Privacy) 标签")
    print("4. 在左侧列表中选择 '辅助功能' (Accessibility)")
    print("5. 点击左下角的锁图标解锁（需要输入密码）")
    print("6. 勾选以下应用程序：")
    print("   - Terminal (如果从终端运行)")
    print("   - Python (或 Python 3.x)")
    print("   - 或您的 IDE (如 VS Code, PyCharm)")
    print("7. 关闭并重新启动本程序")
    print("\n" + "=" * 60 + "\n")
    
    # 尝试打开系统偏好设置
    try:
        subprocess.run([
            'open',
            'x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility'
        ])
        print("✅ 已尝试打开系统偏好设置...")
    except:
        pass


def request_accessibility_permission():
    """请求辅助功能权限（如果需要）"""
    if not is_macos():
        return True
        
    if not check_accessibility_permission():
        show_accessibility_instructions()
        return False
    
    return True
