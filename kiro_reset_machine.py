"""
Kiro Machine ID Reset
Adapted from Cursor Free VIP project
Resets machine identifiers to bypass trial limits
"""
import os
import json
import uuid
import hashlib
import shutil
import sqlite3
import re
from colorama import Fore, Style, init
from datetime import datetime
from kiro_config import get_kiro_paths, get_kiro_config

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

class KiroMachineIDResetter:
    def __init__(self):
        self.paths = get_kiro_paths()
        self.config = get_kiro_config()
        
    def backup_file(self, file_path):
        """Create timestamped backup"""
        if not os.path.exists(file_path):
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{file_path}.backup.{timestamp}"
        
        try:
            shutil.copy2(file_path, backup_path)
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} Backup: {backup_path}{Style.RESET_ALL}")
            return backup_path
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} Backup failed: {e}{Style.RESET_ALL}")
            return None
    
    def generate_new_ids(self):
        """Generate new machine identifiers"""
        # Generate new UUID
        dev_device_id = str(uuid.uuid4())
        
        # Generate new machineId (64 characters hex)
        machine_id = hashlib.sha256(os.urandom(32)).hexdigest()
        
        # Generate new macMachineId (128 characters hex)
        mac_machine_id = hashlib.sha512(os.urandom(64)).hexdigest()
        
        # Generate new sqmId
        sqm_id = "{" + str(uuid.uuid4()).upper() + "}"
        
        return {
            "telemetry.devDeviceId": dev_device_id,
            "telemetry.macMachineId": mac_machine_id,
            "telemetry.machineId": machine_id,
            "telemetry.sqmId": sqm_id,
            "storage.serviceMachineId": dev_device_id,
        }
    
    def update_storage_json(self, new_ids):
        """Update storage.json file"""
        storage_path = self.paths['storage_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['INFO']} Updating storage.json...{Style.RESET_ALL}")
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(storage_path), exist_ok=True)
            
            # Read existing data or create new
            if os.path.exists(storage_path):
                self.backup_file(storage_path)
                with open(storage_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            else:
                data = {}
            
            # Update IDs
            for key, value in new_ids.items():
                data[key] = value
                print(f"{Fore.CYAN}{EMOJI['INFO']} Set {key}{Style.RESET_ALL}")
            
            # Write back
            with open(storage_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} storage.json updated{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} storage.json update failed: {e}{Style.RESET_ALL}")
            return False
    
    def update_sqlite_db(self, new_ids):
        """Update SQLite database"""
        sqlite_path = self.paths['sqlite_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['INFO']} Updating SQLite database...{Style.RESET_ALL}")
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(sqlite_path), exist_ok=True)
            
            # Backup if exists
            if os.path.exists(sqlite_path):
                self.backup_file(sqlite_path)
            
            # Connect and update
            conn = sqlite3.connect(sqlite_path)
            cursor = conn.cursor()
            
            # Create table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ItemTable (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)
            
            # Update IDs
            for key, value in new_ids.items():
                cursor.execute("""
                    INSERT OR REPLACE INTO ItemTable (key, value) 
                    VALUES (?, ?)
                """, (key, value))
                print(f"{Fore.CYAN}{EMOJI['INFO']} Set {key}{Style.RESET_ALL}")
            
            conn.commit()
            conn.close()
            
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} SQLite database updated{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} SQLite update failed: {e}{Style.RESET_ALL}")
            return False
    
    def update_machine_id_file(self, machine_id):
        """Update machineId file"""
        machine_id_path = self.paths['machine_id_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['INFO']} Updating machineId file...{Style.RESET_ALL}")
            
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(machine_id_path), exist_ok=True)
            
            # Backup if exists
            if os.path.exists(machine_id_path):
                self.backup_file(machine_id_path)
            
            # Write new ID
            with open(machine_id_path, 'w', encoding='utf-8') as f:
                f.write(machine_id)
            
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} machineId file updated{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} machineId file update failed: {e}{Style.RESET_ALL}")
            return False
    
    def patch_main_js(self):
        """Patch main.js to bypass machine ID checks"""
        main_js_path = self.paths['main_js_path']
        
        try:
            print(f"{Fore.CYAN}{EMOJI['INFO']} Patching main.js...{Style.RESET_ALL}")
            
            if not os.path.exists(main_js_path):
                print(f"{Fore.YELLOW}{EMOJI['WARNING']} main.js not found, skipping patch{Style.RESET_ALL}")
                return True
            
            # Backup
            self.backup_file(main_js_path)
            
            # Read content
            with open(main_js_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply patches
            patterns = {
                r"async getMachineId\(\)\{return [^??]+\?\?([^}]+)\}": r"async getMachineId(){return \1}",
                r"async getMacMachineId\(\)\{return [^??]+\?\?([^}]+)\}": r"async getMacMachineId(){return \1}",
            }
            
            modified = False
            for pattern, replacement in patterns.items():
                if re.search(pattern, content):
                    content = re.sub(pattern, replacement, content)
                    modified = True
                    print(f"{Fore.CYAN}{EMOJI['INFO']} Applied patch: {pattern[:40]}...{Style.RESET_ALL}")
            
            if not modified:
                print(f"{Fore.YELLOW}{EMOJI['WARNING']} No patterns matched in main.js{Style.RESET_ALL}")
                return True
            
            # Write back
            with open(main_js_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"{Fore.GREEN}{EMOJI['SUCCESS']} main.js patched{Style.RESET_ALL}")
            return True
            
        except Exception as e:
            print(f"{Fore.RED}{EMOJI['ERROR']} main.js patch failed: {e}{Style.RESET_ALL}")
            return False
    
    def reset_all(self):
        """Perform complete machine ID reset"""
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{EMOJI['RESET']} Kiro Machine ID Reset{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
        
        # Generate new IDs
        print(f"{Fore.CYAN}{EMOJI['INFO']} Generating new machine IDs...{Style.RESET_ALL}")
        new_ids = self.generate_new_ids()
        
        print(f"\n{Fore.CYAN}New IDs:{Style.RESET_ALL}")
        for key, value in new_ids.items():
            print(f"  {key}: {value[:32]}...")
        
        print(f"\n{Fore.YELLOW}{EMOJI['WARNING']} This will reset your Kiro machine identity{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{EMOJI['WARNING']} Backups will be created automatically{Style.RESET_ALL}\n")
        
        response = input(f"{EMOJI['INFO']} Continue? (y/N): ").strip().lower()
        if response != 'y':
            print(f"{Fore.YELLOW}{EMOJI['INFO']} Operation cancelled{Style.RESET_ALL}")
            return False
        
        # Perform updates
        print(f"\n{Fore.CYAN}{EMOJI['RESET']} Resetting machine IDs...{Style.RESET_ALL}\n")
        
        success = True
        success &= self.update_storage_json(new_ids)
        success &= self.update_sqlite_db(new_ids)
        success &= self.update_machine_id_file(new_ids["telemetry.devDeviceId"])
        success &= self.patch_main_js()
        
        if success:
            print(f"\n{Fore.GREEN}{EMOJI['SUCCESS']} Machine ID reset completed successfully!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{EMOJI['INFO']} Please restart Kiro for changes to take effect{Style.RESET_ALL}")
        else:
            print(f"\n{Fore.YELLOW}{EMOJI['WARNING']} Machine ID reset completed with some errors{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{EMOJI['INFO']} Check the output above for details{Style.RESET_ALL}")
        
        print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        input(f"{EMOJI['INFO']} Press Enter to continue...")
        return success

def run():
    """Main execution function"""
    resetter = KiroMachineIDResetter()
    return resetter.reset_all()

if __name__ == "__main__":
    run()
