"""
Kiro Auto-Update Disabler
Adapted from Cursor Free VIP project
Prevents Kiro from auto-updating and detecting modifications
"""
import os
import shutil
import subprocess
import platform
import re
from colorama import Fore, Style, init
from kiro_config import get_kiro_paths

init()

EMOJI = {
    "PROCESS": "🔄",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "FOLDER": "📁",
    "FILE": "📄",
    "STOP": "🛑",
    "CHECK": "✔️",
    "WARNING": "⚠️",
}

class KiroAutoUpdateDisabler:
    def __init__(self):
        self.paths = get_kiro_paths()
        self.system = platform.system()
        
    def kill_kiro_processes(self):
        """Terminate all Kiro processes"""
        try:
            print(f"{Fore.CYAN}{EMOJI['PROCESS']} Terminating Kiro processes...{Style.RESET_ALL}")
            
            if self.system == "Windows":
                subprocess.run(['taskkill', '/F', '/IM', 'Kiro.exe', '/T'], 
                             capture_output=True, check=False)
            else:
                subprocess.run(['pkill', '-f', 'Kiro'], 
                             capture_output=True, check=False)
            
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Kiro processes terminated{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to terminate processes: {e}{Style.RESET_ALL}")
            return False
    
    def remove_updater_directory(self):
        """Remove updater directory"""
        updater_path = self.paths['updater_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['FOLDER']} Removing updater directory...{Style.RESET_ALL}")
            
            if os.path.exists(updater_path):
                try:
                    if os.path.isdir(updater_path):
                        shutil.rmtree(updater_path)
                    else:
                        os.remove(updater_path)
                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Updater directory removed{Style.RESET_ALL}")
                except PermissionError:
                    print(f"{Fore.YELLOW}{EMOJI['WARNING']} Updater directory locked, skipping{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{EMOJI['INFO']} Updater directory not found{Style.RESET_ALL}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to remove updater: {e}{Style.RESET_ALL}")
            return True  # Continue anyway
    
    def clear_update_yml(self):
        """Clear update.yml file"""
        update_yml_path = self.paths['update_yml_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['FILE']} Clearing update.yml...{Style.RESET_ALL}")
            
            if os.path.exists(update_yml_path):
                try:
                    with open(update_yml_path, 'w') as f:
                        f.write('')
                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} update.yml cleared{Style.RESET_ALL}")
                except PermissionError:
                    print(f"{Fore.YELLOW}{EMOJI['WARNING']} update.yml locked, skipping{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{EMOJI['INFO']} update.yml not found{Style.RESET_ALL}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to clear update.yml: {e}{Style.RESET_ALL}")
            return False
    
    def remove_update_urls(self):
        """Remove update URLs from product.json"""
        product_json_path = self.paths['product_json_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['FILE']} Removing update URLs from product.json...{Style.RESET_ALL}")
            
            if not os.path.exists(product_json_path):
                print(f"{Fore.YELLOW}{EMOJI['WARNING']} product.json not found{Style.RESET_ALL}")
                return True
            
            # Read file
            with open(product_json_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Backup
            backup_path = f"{product_json_path}.backup"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Remove update URLs
            patterns = {
                r'"updateUrl":\s*"[^"]*"': '"updateUrl": ""',
                r'"downloadUrl":\s*"[^"]*download[^"]*"': '"downloadUrl": ""',
            }
            
            modified = False
            for pattern, replacement in patterns.items():
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    modified = True
            
            if modified:
                # Write back
                with open(product_json_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Update URLs removed{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}{EMOJI['INFO']} No update URLs found{Style.RESET_ALL}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to modify product.json: {e}{Style.RESET_ALL}")
            return False
    
    def create_blocking_files(self):
        """Create blocking files to prevent updates"""
        updater_path = self.paths['updater_path']
        update_yml_path = self.paths['update_yml_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['FILE']} Creating blocking files...{Style.RESET_ALL}")
            
            # Create updater blocking file
            try:
                os.makedirs(os.path.dirname(updater_path), exist_ok=True)
                open(updater_path, 'w').close()
                
                # Set read-only
                if self.system == "Windows":
                    os.system(f'attrib +r "{updater_path}"')
                else:
                    os.chmod(updater_path, 0o444)
                
                print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Updater blocking file created{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.YELLOW}{EMOJI['WARNING']} Could not create updater block: {e}{Style.RESET_ALL}")
            
            # Create update.yml blocking file
            if os.path.exists(os.path.dirname(update_yml_path)):
                try:
                    with open(update_yml_path, 'w') as f:
                        f.write('# Locked to prevent auto-updates\nversion: 0.0.0\n')
                    
                    # Set read-only
                    if self.system == "Windows":
                        os.system(f'attrib +r "{update_yml_path}"')
                    else:
                        os.chmod(update_yml_path, 0o444)
                    
                    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} update.yml locked{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.YELLOW}{EMOJI['WARNING']} Could not lock update.yml: {e}{Style.RESET_ALL}")
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Failed to create blocking files: {e}{Style.RESET_ALL}")
            return True  # Continue anyway
    
    def disable_auto_update(self):
        """Perform complete auto-update disable"""
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{EMOJI['STOP']} Kiro Auto-Update Disabler{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        print(f"{Fore.YELLOW}{EMOJI['WARNING']} This will prevent Kiro from auto-updating{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{EMOJI['WARNING']} You'll need to manually update in the future{Style.RESET_ALL}\n")
        
        response = input(f"{EMOJI['INFO']} Continue? (y/N): ").strip().lower()
        if response != 'y':
            print(f"{Fore.YELLOW}{EMOJI['INFO']} Operation cancelled{Style.RESET_ALL}")
            return False
        
        print(f"\n{Fore.CYAN}{EMOJI['PROCESS']} Disabling auto-update...{Style.RESET_ALL}\n")
        
        # Execute steps
        success = True
        success &= self.kill_kiro_processes()
        success &= self.remove_updater_directory()
        success &= self.clear_update_yml()
        success &= self.remove_update_urls()
        success &= self.create_blocking_files()
        
        if success:
            print(f"\n{Fore.GREEN}{EMOJI['CHECK']} Auto-update disabled successfully!{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}{EMOJI['WARNING']} Auto-update disabled with some warnings{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}{EMOJI['INFO']} Kiro will no longer auto-update{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        input(f"{EMOJI['INFO']} Press Enter to continue...")
        return success

def run():
    """Main execution function"""
    disabler = KiroAutoUpdateDisabler()
    return disabler.disable_auto_update()

if __name__ == "__main__":
    run()
