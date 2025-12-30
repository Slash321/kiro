"""
Kiro Bypass Tool - Main Menu
Adapted from Cursor Free VIP project for Kiro IDE
"""
import os
import sys
import platform
from colorama import Fore, Style, init

# Import bypass modules
try:
    import kiro_config
    import kiro_bypass_token_limit
    import kiro_reset_machine
    import kiro_disable_auto_update
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please ensure all kiro_*.py files are in the same directory")
    sys.exit(1)

init()

EMOJI = {
    "MENU": "📋",
    "ARROW": "➜",
    "SUCCESS": "✅",
    "ERROR": "❌",
    "INFO": "ℹ️",
    "RESET": "🔄",
    "SETTINGS": "⚙️",
    "EXIT": "🚪",
    "WARNING": "⚠️",
    "ROCKET": "🚀",
}

VERSION = "1.1.0"

def print_logo():
    """Print application logo"""
    logo = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║   {Fore.YELLOW}██╗  ██╗██╗██████╗  ██████╗     ██████╗ ██╗   ██╗{Fore.CYAN}      ║
║   {Fore.YELLOW}██║ ██╔╝██║██╔══██╗██╔═══██╗    ██╔══██╗╚██╗ ██╔╝{Fore.CYAN}      ║
║   {Fore.YELLOW}█████╔╝ ██║██████╔╝██║   ██║    ██████╔╝ ╚████╔╝{Fore.CYAN}       ║
║   {Fore.YELLOW}██╔═██╗ ██║██╔══██╗██║   ██║    ██╔══██╗  ╚██╔╝{Fore.CYAN}        ║
║   {Fore.YELLOW}██║  ██╗██║██║  ██║╚██████╔╝    ██████╔╝   ██║{Fore.CYAN}         ║
║   {Fore.YELLOW}╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝    ╚═╝{Fore.CYAN}         ║
║                                                           ║
║              {Fore.WHITE}Kiro IDE Bypass Tool v{VERSION}{Fore.CYAN}                ║
║        {Fore.YELLOW}Adapted from Cursor Free VIP Project{Fore.CYAN}              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(logo)

def print_menu():
    """Print main menu"""
    print(f"\n{Fore.CYAN}{EMOJI['MENU']} Main Menu:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'─' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}1{Style.RESET_ALL}. {EMOJI['RESET']} Reset Machine ID")
    print(f"{Fore.GREEN}2{Style.RESET_ALL}. {EMOJI['ROCKET']} Bypass Token Limit")
    print(f"{Fore.GREEN}3{Style.RESET_ALL}. {EMOJI['SETTINGS']} Disable Auto-Update")
    print(f"{Fore.GREEN}4{Style.RESET_ALL}. {EMOJI['INFO']} Verify Kiro Installation")
    print(f"{Fore.GREEN}5{Style.RESET_ALL}. {EMOJI['SETTINGS']} Show Configuration")
    print(f"{Fore.GREEN}0{Style.RESET_ALL}. {EMOJI['EXIT']} Exit")
    print(f"{Fore.YELLOW}{'─' * 60}{Style.RESET_ALL}")

def verify_installation():
    """Verify Kiro installation"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['INFO']} Verifying Kiro Installation{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    result = kiro_config.verify_kiro_installation()
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{EMOJI['INFO']} Press Enter to continue...")
    return result

def show_configuration():
    """Display current configuration"""
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{EMOJI['SETTINGS']} Kiro Configuration{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")
    
    paths = kiro_config.get_kiro_paths()
    
    print(f"{Fore.CYAN}System: {Fore.WHITE}{platform.system()}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Python: {Fore.WHITE}{sys.version.split()[0]}{Style.RESET_ALL}\n")
    
    print(f"{Fore.CYAN}Kiro Paths:{Style.RESET_ALL}")
    for key, value in paths.items():
        exists = os.path.exists(value)
        status = f"{Fore.GREEN}[OK]{Style.RESET_ALL}" if exists else f"{Fore.RED}[FAIL]{Style.RESET_ALL}"
        print(f"  {status} {key}: {value}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    input(f"{EMOJI['INFO']} Press Enter to continue...")

def show_disclaimer():
    """Show disclaimer and warnings"""
    disclaimer = f"""
{Fore.YELLOW}{'='*60}
                        ⚠️  DISCLAIMER ⚠️
{'='*60}{Style.RESET_ALL}

{Fore.RED}This tool modifies Kiro IDE's core files and may:{Style.RESET_ALL}

  • Violate Kiro's Terms of Service
  • Result in account suspension or ban
  • Cause instability or data loss
  • Break with future updates

{Fore.YELLOW}Use at your own risk. For educational purposes only.{Style.RESET_ALL}

{Fore.CYAN}Recommendations:{Style.RESET_ALL}
  • Backup your work before using
  • Test on non-production systems
  • Keep original files for restoration
  • Support the developers if you find value

{Fore.GREEN}This project is adapted from the Cursor Free VIP project:
https://github.com/yeongpin/cursor-free-vip{Style.RESET_ALL}

{Fore.YELLOW}{'='*60}{Style.RESET_ALL}
"""
    print(disclaimer)
    response = input(f"\n{EMOJI['WARNING']} Do you understand and accept the risks? (yes/no): ").strip().lower()
    return response == 'yes'

def main():
    """Main application loop"""
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Show logo
    print_logo()
    
    # Show disclaimer
    if not show_disclaimer():
        print(f"\n{Fore.YELLOW}{EMOJI['INFO']} Exiting...{Style.RESET_ALL}")
        return
    
    # Setup configuration
    print(f"\n{Fore.CYAN}{EMOJI['SETTINGS']} Initializing configuration...{Style.RESET_ALL}")
    try:
        config = kiro_config.setup_kiro_config()
    except Exception as e:
        print(f"{Fore.RED}{EMOJI['ERROR']} Configuration failed: {e}{Style.RESET_ALL}")
        input(f"\n{EMOJI['INFO']} Press Enter to exit...")
        return
    
    # Main loop
    while True:
        try:
            print_menu()
            choice = input(f"\n{EMOJI['ARROW']} {Fore.CYAN}Select option (0-5): {Style.RESET_ALL}").strip()
            
            if choice == "0":
                print(f"\n{Fore.YELLOW}{EMOJI['INFO']} Exiting...{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{'═' * 60}{Style.RESET_ALL}")
                break
                
            elif choice == "1":
                kiro_reset_machine.run()
                
            elif choice == "2":
                kiro_bypass_token_limit.run()
                
            elif choice == "3":
                kiro_disable_auto_update.run()
                
            elif choice == "4":
                verify_installation()
                
            elif choice == "5":
                show_configuration()
                
            else:
                print(f"{Fore.RED}{EMOJI['ERROR']} Invalid choice. Please select 0-5.{Style.RESET_ALL}")
                input(f"{EMOJI['INFO']} Press Enter to continue...")
                
        except KeyboardInterrupt:
            print(f"\n\n{Fore.YELLOW}{EMOJI['INFO']} Interrupted by user{Style.RESET_ALL}")
            print(f"{Fore.CYAN}{'═' * 60}{Style.RESET_ALL}")
            break
            
        except Exception as e:
            print(f"\n{Fore.RED}{EMOJI['ERROR']} Error: {e}{Style.RESET_ALL}")
            input(f"{EMOJI['INFO']} Press Enter to continue...")

if __name__ == "__main__":
    main()
