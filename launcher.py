#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
女帝启示录启动器
Windows系统专用启动脚本
"""

import os
import sys
import subprocess
import platform
import time
from pathlib import Path

class EmpressLauncher:
    """女帝启示录启动器类"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.main_script = self.project_root / "src" / "main.py"
        self.simple_script = self.project_root / "src" / "empress_simple.py"
        self.test_script = self.project_root / "src" / "simple_test.py"
        
    def print_banner(self):
        """打印启动横幅"""
        print("=" * 50)
        print("           女帝启示录启动器")
        print("=" * 50)
        print()
    
    def check_system(self):
        """检查系统环境"""
        print("[信息] 检查系统环境...")
        
        # 检查操作系统
        if platform.system() != "Windows":
            print("[警告] 此启动器专为Windows系统设计")
            print(f"当前系统: {platform.system()}")
        
        # 检查Python版本
        python_version = sys.version_info
        print(f"[信息] Python版本: {python_version.major}.{python_version.minor}.{python_version.micro}")
        
        if python_version < (3, 6):
            print("[错误] 需要Python 3.6或更高版本")
            return False
        
        return True
    
    def check_dependencies(self):
        """检查依赖包"""
        print("[信息] 检查依赖包...")
        
        required_modules = ['tkinter', 'threading', 'time']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
                print(f"  ✓ {module}")
            except ImportError:
                print(f"  ✗ {module} (缺失)")
                missing_modules.append(module)
        
        if missing_modules:
            print(f"[错误] 缺少必要的模块: {', '.join(missing_modules)}")
            return False
        
        return True
    
    def check_files(self):
        """检查必要文件"""
        print("[信息] 检查项目文件...")
        
        files_to_check = [
            (self.main_script, "主程序"),
            (self.simple_script, "简化版程序"),
            (self.test_script, "测试程序")
        ]
        
        available_scripts = []
        
        for file_path, description in files_to_check:
            if file_path.exists():
                print(f"  ✓ {description}: {file_path}")
                available_scripts.append((file_path, description))
            else:
                print(f"  ✗ {description}: {file_path} (不存在)")
        
        return available_scripts
    
    def show_menu(self, available_scripts):
        """显示启动菜单"""
        print("\n" + "=" * 30)
        print("        启动选项")
        print("=" * 30)
        
        for i, (script_path, description) in enumerate(available_scripts, 1):
            print(f"{i}. {description}")
        
        print("0. 退出")
        print()
        
        while True:
            try:
                choice = input("请选择要启动的程序 (输入数字): ").strip()
                
                if choice == "0":
                    print("退出启动器")
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(available_scripts):
                    return available_scripts[choice_num - 1]
                else:
                    print("无效选择，请重新输入")
                    
            except ValueError:
                print("请输入有效的数字")
            except KeyboardInterrupt:
                print("\n用户取消操作")
                return None
    
    def run_script(self, script_path, description):
        """运行选定的脚本"""
        print(f"\n[信息] 正在启动 {description}...")
        print(f"脚本路径: {script_path}")
        print("-" * 50)
        
        try:
            # 切换到项目目录
            os.chdir(self.project_root)
            
            # 运行脚本
            result = subprocess.run([
                sys.executable, str(script_path)
            ], check=True)
            
            print(f"\n[信息] {description} 正常退出")
            
        except subprocess.CalledProcessError as e:
            print(f"\n[错误] {description} 异常退出，错误代码: {e.returncode}")
            return False
        except FileNotFoundError:
            print(f"\n[错误] 找不到Python解释器")
            return False
        except KeyboardInterrupt:
            print(f"\n[信息] 用户中断了 {description}")
            return True
        except Exception as e:
            print(f"\n[错误] 启动失败: {e}")
            return False
        
        return True
    
    def run(self):
        """主运行方法"""
        self.print_banner()
        
        # 检查系统环境
        if not self.check_system():
            input("\n按回车键退出...")
            return False
        
        # 检查依赖
        if not self.check_dependencies():
            input("\n按回车键退出...")
            return False
        
        # 检查文件
        available_scripts = self.check_files()
        if not available_scripts:
            print("[错误] 没有找到可运行的程序")
            input("\n按回车键退出...")
            return False
        
        # 显示菜单并获取选择
        selected_script = self.show_menu(available_scripts)
        if selected_script is None:
            return True
        
        # 运行选定的脚本
        script_path, description = selected_script
        success = self.run_script(script_path, description)
        
        if success:
            print("\n" + "=" * 50)
            print("感谢使用女帝启示录！")
            print("=" * 50)
        
        input("\n按回车键退出...")
        return success

def main():
    """主函数"""
    try:
        launcher = EmpressLauncher()
        launcher.run()
    except KeyboardInterrupt:
        print("\n\n用户中断操作")
    except Exception as e:
        print(f"\n[错误] 启动器异常: {e}")
        input("\n按回车键退出...")

if __name__ == "__main__":
    main()
