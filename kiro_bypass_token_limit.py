"""
Kiro Token Limit Bypass
Adapted from Cursor Free VIP project
Modifies workbench.desktop.main.js to bypass token limits
"""
import os
import shutil
import tempfile
from colorama import Fore, Style, init
from datetime import datetime
from kiro_config import get_kiro_paths

init()

EMOJI = {
    "FILE": "📄",
    "BACKUP": "💾",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "RESET": "🔄",
    "WARNING": "⚠️",
}


def backup_file(file_path):
    """Create timestamped backup of file"""
    if not os.path.exists(file_path):
        print(f"{Fore.RED}{EMOJI['ERROR']} File not found: {file_path}{Style.RESET_ALL}")
        return None
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{file_path}.backup.{timestamp}"
    
    try:
        shutil.copy2(file_path, backup_path)
        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Backup created: {backup_path}{Style.RESET_ALL}")
        return backup_path
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Backup failed: {e}{Style.RESET_ALL}")
        return None


def modify_workbench_js(file_path):
    """Modify workbench.desktop.main.js to bypass token limits"""
    try:
        # Save original file permissions
        original_stat = os.stat(file_path)
        original_mode = original_stat.st_mode
        original_uid = original_stat.st_uid
        original_gid = original_stat.st_gid

        # Create temporary file
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", errors="ignore", delete=False) as tmp_file:
            # Read original content
            with open(file_path, "r", encoding="utf-8", errors="ignore") as main_file:
                content = main_file.read()

            # Define replacement patterns
            patterns = {
                # Token limit bypass - increase from 200k to 9M
                r'async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;': 
                    r'async getEffectiveTokenLimit(e){return 9000000;const n=e.modelName;if(!n)return 9e5;',
                
                # UI modifications - change upgrade buttons
                r'B(k,D(Ln,{title:"Upgrade to Pro",size:"small",get codicon(){return A.rocket},get onClick(){return t.pay}}),null)': 
                    r'B(k,D(Ln,{title:"Kiro Bypass Active",size:"small",get codicon(){return A.github},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
                
                r'M(x,I(as,{title:"Upgrade to Pro",size:"small",get codicon(){return $.rocket},get onClick(){return t.pay}}),null)': 
                    r'M(x,I(as,{title:"Kiro Bypass Active",size:"small",get codicon(){return $.github},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
                
                r'$(k,E(Ks,{title:"Upgrade to Pro",size:"small",get codicon(){return F.rocket},get onClick(){return t.pay}}),null)': 
                    r'$(k,E(Ks,{title:"Kiro Bypass Active",size:"small",get codicon(){return F.rocket},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}),null)',
                
                # Badge replacement
                r'<div>Pro Trial': r'<div>Pro',
                
                # Auto-select text replacement
                r'py-1">Auto-select': r'py-1">Bypass-Active',
                
                # Pro status display
                r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>.");': 
                    r'var DWr=ne("<div class=settings__item_description>You are currently signed in with <strong></strong>. <h1>Pro (Bypassed)</h1>");',
                
                # Hide notification toasts
                r'notifications-toasts': r'notifications-toasts hidden'
            }

            # Apply all replacements
            modifications_made = 0
            for old_pattern, new_pattern in patterns.items():
                if old_pattern in content:
                    content = content.replace(old_pattern, new_pattern)
                    modifications_made += 1
                    print(f"{Fore.CYAN}{EMOJI['INFO']} Applied pattern: {old_pattern[:50]}...{Style.RESET_ALL}")

            if modifications_made == 0:
                print(f"{Fore.YELLOW}{EMOJI['WARNING']} No patterns matched. File may already be modified or version mismatch.{Style.RESET_ALL}")
                return False

            # Write to temporary file
            tmp_file.write(content)
            tmp_path = tmp_file.name

        # Backup original file
        backup_path = backup_file(file_path)
        if not backup_path:
            print(f"{Fore.RED}{EMOJI['ERROR']} Cannot proceed without backup{Style.RESET_ALL}")
            os.unlink(tmp_path)
            return False
        
        # Move temporary file to original position
        if os.path.exists(file_path):
            os.remove(file_path)
        shutil.move(tmp_path, file_path)

        # Restore original permissions
        os.chmod(file_path, original_mode)
        if os.name != "nt":  # Not Windows
            try:
                os.chown(file_path, original_uid, original_gid)
            except:
                pass

        print(f"{Fore.GREEN}{EMOJI['SUCCESS']} File modified successfully ({modifications_made} patterns applied){Style.RESET_ALL}")
        return True

    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Modification failed: {e}{Style.RESET_ALL}")
        if "tmp_path" in locals():
            try:
                os.unlink(tmp_path)
            except:
                pass
        return False

def run():
    """Main execution function"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['RESET']} Kiro Token Limit Bypass{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    # Get Kiro paths
    paths = get_kiro_paths()
    workbench_path = paths['workbench_js_path']
    
    # Verify file exists
    if not os.path.exists(workbench_path):
        print(f"{Fore.RED}{EMOJI['ERROR']} Workbench file not found: {workbench_path}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{EMOJI['INFO']} Please ensure Kiro is properly installed{Style.RESET_ALL}")
        input(f"\n{EMOJI['INFO']} Press Enter to exit...")
        return False
    
    print(f"{Fore.CYAN}{EMOJI['INFO']} Target file: {workbench_path}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{EMOJI['WARNING']} This will modify Kiro's core files{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{EMOJI['WARNING']} A backup will be created automatically{Style.RESET_ALL}\n")
    
    # Confirm action
    response = input(f"{EMOJI['INFO']} Continue? (y/N): ").strip().lower()
    if response != 'y':
        print(f"{Fore.YELLOW}{EMOJI['INFO']} Operation cancelled{Style.RESET_ALL}")
        return False
    
    # Perform modification
    print(f"\n{Fore.CYAN}{EMOJI['RESET']} Modifying workbench file...{Style.RESET_ALL}\n")
    success = modify_workbench_js(workbench_path)
    
    if success:
        print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} Token limit bypass applied successfully!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{EMOJI['INFO']} Please restart Kiro for changes to take effect{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.RED}{EMOJI['ERROR']} Token limit bypass failed{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{EMOJI['INFO']} Press Enter to continue...")
    return success

if __name__ == "__main__":
    run()
