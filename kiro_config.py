"""
Kiro IDE Configuration Module
Adapted from Cursor Free VIP project for Kiro IDE
"""
import os
import configparser
import platform
from colorama import Fore, Style

EMOJI = {
    "INFO": "ℹ️",
    "WARNING": "⚠️",
    "ERROR": "❌",
    "SUCCESS": "✅",
}

def get_user_documents_path():
    """Get user Documents folder path"""
    if platform.system() == "Windows":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                              "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders") as key:
                documents_path, _ = winreg.QueryValueEx(key, "Personal")
                return documents_path
        except Exception:
            return os.path.join(os.path.expanduser("~"), "Documents")
    elif platform.system() == "Darwin":
        return os.path.join(os.path.expanduser("~"), "Documents")
    else:  # Linux
        sudo_user = os.environ.get('SUDO_USER')
        if sudo_user:
            return os.path.join("/home", sudo_user, "Documents")
        return os.path.join(os.path.expanduser("~"), "Documents")

def get_kiro_paths():
    """Get Kiro IDE paths based on operating system"""
    system = platform.system()
    
    if system == "Windows":
        appdata = os.getenv("APPDATA")
        localappdata = os.getenv("LOCALAPPDATA")
        return {
            'storage_path': os.path.join(appdata, "Kiro", "User", "globalStorage", "storage.json"),
            'sqlite_path': os.path.join(appdata, "Kiro", "User", "globalStorage", "state.vscdb"),
            'machine_id_path': os.path.join(appdata, "Kiro", "machineId"),
            'app_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app"),
            'updater_path': os.path.join(localappdata, "kiro-updater"),
            'update_yml_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app-update.yml"),
            'product_json_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app", "product.json"),
            'main_js_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app", "out", "main.js"),
            'workbench_js_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app", "out", "vs", "workbench", "workbench.desktop.main.js"),
            'package_json_path': os.path.join(localappdata, "Programs", "Kiro", "resources", "app", "package.json")
        }
    
    elif system == "Darwin":  # macOS
        return {
            'storage_path': os.path.expanduser("~/Library/Application Support/Kiro/User/globalStorage/storage.json"),
            'sqlite_path': os.path.expanduser("~/Library/Application Support/Kiro/User/globalStorage/state.vscdb"),
            'machine_id_path': os.path.expanduser("~/Library/Application Support/Kiro/machineId"),
            'app_path': "/Applications/Kiro.app/Contents/Resources/app",
            'updater_path': os.path.expanduser("~/Library/Application Support/kiro-updater"),
            'update_yml_path': "/Applications/Kiro.app/Contents/Resources/app-update.yml",
            'product_json_path': "/Applications/Kiro.app/Contents/Resources/app/product.json",
            'main_js_path': "/Applications/Kiro.app/Contents/Resources/app/out/main.js",
            'workbench_js_path': "/Applications/Kiro.app/Contents/Resources/app/out/vs/workbench/workbench.desktop.main.js",
            'package_json_path': "/Applications/Kiro.app/Contents/Resources/app/package.json"
        }
    
    else:  # Linux
        return {
            'storage_path': os.path.expanduser("~/.config/kiro/User/globalStorage/storage.json"),
            'sqlite_path': os.path.expanduser("~/.config/kiro/User/globalStorage/state.vscdb"),
            'machine_id_path': os.path.expanduser("~/.config/kiro/machineid"),
            'app_path': "/opt/Kiro/resources/app",  # or /usr/share/kiro/resources/app
            'updater_path': os.path.expanduser("~/.config/kiro-updater"),
            'update_yml_path': os.path.expanduser("~/.config/kiro/resources/app-update.yml"),
            'product_json_path': os.path.expanduser("~/.config/kiro/resources/app/product.json"),
            'main_js_path': "/opt/Kiro/resources/app/out/main.js",
            'workbench_js_path': "/opt/Kiro/resources/app/out/vs/workbench/workbench.desktop.main.js",
            'package_json_path': "/opt/Kiro/resources/app/package.json"
        }

def setup_kiro_config():
    """Setup Kiro configuration file"""
    config_dir = os.path.join(get_user_documents_path(), ".kiro-bypass")
    config_file = os.path.join(config_dir, "config.ini")
    
    # Create config directory
    os.makedirs(config_dir, exist_ok=True)
    
    config = configparser.ConfigParser()
    paths = get_kiro_paths()
    system = platform.system()
    
    # Add paths to config
    section_name = f"{system}Paths"
    if not config.has_section(section_name):
        config.add_section(section_name)
    
    for key, value in paths.items():
        config.set(section_name, key, value)
    
    # Add utility settings
    if not config.has_section('Utils'):
        config.add_section('Utils')
        config.set('Utils', 'backup_enabled', 'True')
        config.set('Utils', 'backup_dir', os.path.join(config_dir, 'backups'))
        config.set('Utils', 'log_enabled', 'True')
    
    # Save config
    with open(config_file, 'w', encoding='utf-8') as f:
        config.write(f)
    
    print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Kiro config created: {config_file}{Style.RESET_ALL}")
    return config

def get_kiro_config():
    """Get existing Kiro config or create new one"""
    config_dir = os.path.join(get_user_documents_path(), ".kiro-bypass")
    config_file = os.path.join(config_dir, "config.ini")
    
    if not os.path.exists(config_file):
        return setup_kiro_config()
    
    config = configparser.ConfigParser()
    config.read(config_file, encoding='utf-8')
    return config

def verify_kiro_installation():
    """Verify Kiro is installed and paths exist"""
    paths = get_kiro_paths()
    system = platform.system()
    
    print(f"\n{Fore.CYAN}Verifying Kiro installation...{Style.RESET_ALL}")
    
    critical_paths = ['app_path', 'package_json_path', 'main_js_path', 'workbench_js_path']
    all_exist = True
    
    for path_key in critical_paths:
        path = paths[path_key]
        exists = os.path.exists(path)
        
        if exists:
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Found: {path}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}{EMOJI['ERROR']} Missing: {path}{Style.RESET_ALL}")
            all_exist = False
    
    if not all_exist:
        print(f"\n{Fore.YELLOW}{EMOJI['WARNING']} Some Kiro files are missing. Please ensure Kiro is properly installed.{Style.RESET_ALL}")
        return False
    
    print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} Kiro installation verified!{Style.RESET_ALL}")
    return True

if __name__ == "__main__":
    print("Kiro Configuration Module")
    print("=" * 50)
    
    # Setup config
    config = setup_kiro_config()
    
    # Verify installation
    verify_kiro_installation()
    
    # Display paths
    paths = get_kiro_paths()
    print(f"\n{Fore.CYAN}Kiro Paths:{Style.RESET_ALL}")
    for key, value in paths.items():
        print(f"  {key}: {value}")
