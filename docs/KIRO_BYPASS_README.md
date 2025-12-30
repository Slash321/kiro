# Kiro IDE Bypass Tool

> **Adapted from [Cursor Free VIP](https://github.com/yeongpin/cursor-free-vip) project**

A comprehensive tool to bypass Kiro IDE's token limits and trial restrictions. This project adapts the proven Cursor bypass mechanisms for Kiro IDE.

## ⚠️ DISCLAIMER

**FOR EDUCATIONAL PURPOSES ONLY**

This tool modifies Kiro IDE's core files and may:
- Violate Kiro's Terms of Service
- Result in account suspension or ban
- Cause instability or data loss
- Break with future updates

**Use at your own risk. Always backup your work before using.**

## ✨ Features

### 1. Machine ID Reset
- Generates new device identifiers
- Bypasses trial limitations
- Modifies storage.json and SQLite database
- Patches main.js for machine ID validation

### 2. Token Limit Bypass
- Increases token limit from 200,000 to 9,000,000
- Modifies workbench.desktop.main.js
- Changes UI elements to show "Pro" status

### 3. Auto-Update Disabler
- Prevents Kiro from auto-updating
- Protects modifications from being overwritten
- Removes update URLs and blocks update mechanisms

## 💻 System Requirements

- **Operating Systems**: Windows, macOS, Linux
- **Python**: 3.8 or higher
- **Kiro IDE**: Installed and accessible

### Required Python Packages

```bash
pip install colorama
```

## 📦 Installation

1. **Clone or download this repository**

```bash
git clone <repository-url>
cd kiro-bypass
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install colorama
```

3. **Verify Kiro installation**

```bash
python kiro_config.py
```

## 🚀 Usage

### Quick Start

Run the main menu:

```bash
python kiro_main.py
```

### Individual Tools

#### 1. Reset Machine ID

```bash
python kiro_reset_machine.py
```

This will:
- Generate new UUIDs and machine identifiers
- Update storage.json
- Update SQLite database (state.vscdb)
- Update machineId file
- Patch main.js

#### 2. Bypass Token Limit

```bash
python kiro_bypass_token_limit.py
```

This will:
- Modify workbench.desktop.main.js
- Increase token limit to 9,000,000
- Change UI elements

#### 3. Disable Auto-Update

```bash
python kiro_disable_auto_update.py
```

This will:
- Kill Kiro processes
- Remove updater directory
- Clear update.yml
- Remove update URLs from product.json
- Create blocking files

#### 4. Verify Installation

```bash
python kiro_config.py
```

This will check if all Kiro files are accessible.

## 📁 File Structure

```
kiro-bypass/
├── kiro_main.py                  # Main menu interface
├── kiro_config.py                # Configuration and path management
├── kiro_reset_machine.py         # Machine ID reset tool
├── kiro_bypass_token_limit.py    # Token limit bypass tool
├── kiro_disable_auto_update.py   # Auto-update disabler
├── ANALYSIS.md                   # Comprehensive technical analysis
├── KIRO_BYPASS_README.md         # This file
└── requirements.txt              # Python dependencies
```

## 🔧 Configuration

The tool automatically detects your system and Kiro installation paths. Configuration is stored in:

- **Windows**: `%USERPROFILE%\Documents\.kiro-bypass\config.ini`
- **macOS**: `~/Documents/.kiro-bypass/config.ini`
- **Linux**: `~/Documents/.kiro-bypass/config.ini`

### Default Kiro Paths

#### Windows
- Storage: `%APPDATA%\Kiro\User\globalStorage\storage.json`
- SQLite: `%APPDATA%\Kiro\User\globalStorage\state.vscdb`
- Machine ID: `%APPDATA%\Kiro\machineId`
- App: `%LOCALAPPDATA%\Programs\Kiro\resources\app`

#### macOS
- Storage: `~/Library/Application Support/Kiro/User/globalStorage/storage.json`
- SQLite: `~/Library/Application Support/Kiro/User/globalStorage/state.vscdb`
- Machine ID: `~/Library/Application Support/Kiro/machineId`
- App: `/Applications/Kiro.app/Contents/Resources/app`

#### Linux
- Storage: `~/.config/kiro/User/globalStorage/storage.json`
- SQLite: `~/.config/kiro/User/globalStorage/state.vscdb`
- Machine ID: `~/.config/kiro/machineid`
- App: `/opt/Kiro/resources/app`

## 🛡️ Safety Features

### Automatic Backups

All tools create timestamped backups before modifying files:

```
file.json.backup.20250117_143022
```

### Verification

The tool verifies:
- File existence before modification
- Successful backup creation
- File permissions
- Pattern matching in code

### Restore

To restore from backup:

1. Locate backup files (they have `.backup.TIMESTAMP` extension)
2. Remove the current file
3. Rename backup file to original name

Example:
```bash
# Windows
del "%APPDATA%\Kiro\User\globalStorage\storage.json"
ren "%APPDATA%\Kiro\User\globalStorage\storage.json.backup.20250117_143022" storage.json

# Linux/macOS
rm ~/.config/kiro/User/globalStorage/storage.json
mv ~/.config/kiro/User/globalStorage/storage.json.backup.20250117_143022 storage.json
```

## 🐛 Troubleshooting

### "File not found" errors

**Solution**: Verify Kiro is installed and run:
```bash
python kiro_config.py
```

### "Permission denied" errors

**Solution**: Run with administrator/sudo privileges:

```bash
# Windows (Run as Administrator)
python kiro_main.py

# Linux/macOS
sudo python kiro_main.py
```

### "No patterns matched" warnings

**Solution**: Your Kiro version may be different. Check:
1. Kiro version in `package.json`
2. File structure matches expected paths
3. Files haven't been previously modified

### Kiro won't start after modifications

**Solution**: Restore from backups:

1. Find backup files with `.backup.TIMESTAMP` extension
2. Restore each modified file
3. Restart Kiro

## 📊 Technical Details

### Machine IDs Modified

- `telemetry.devDeviceId` - Device UUID
- `telemetry.machineId` - 64-character hex hash
- `telemetry.macMachineId` - 128-character hex hash
- `telemetry.sqmId` - Software Quality Metrics ID
- `storage.serviceMachineId` - Service machine identifier

### Code Patterns Modified

#### Token Limit (workbench.desktop.main.js)
```javascript
// Before
async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;

// After
async getEffectiveTokenLimit(e){return 9000000;const n=e.modelName;if(!n)return 9e5;
```

#### Machine ID Validation (main.js)
```javascript
// Before
async getMachineId(){return [cached]??[generated]}

// After
async getMachineId(){return [generated]}
```

## 🤝 Contributing

This project is adapted from the Cursor Free VIP project. Contributions are welcome:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📜 License

This project is for educational purposes only. Use at your own risk.

Original Cursor Free VIP project: [yeongpin/cursor-free-vip](https://github.com/yeongpin/cursor-free-vip)

## 🙏 Credits

- **Original Project**: [Cursor Free VIP](https://github.com/yeongpin/cursor-free-vip) by yeongpin
- **Adaptation**: Kiro IDE Bypass Tool
- **Contributors**: See original project for full credits

## ⚖️ Legal Notice

This tool is provided "as is" without warranty of any kind. The authors are not responsible for any damages or legal issues arising from its use. Always respect software licenses and terms of service.

## 📞 Support

For issues specific to Kiro bypass:
- Check the troubleshooting section
- Review ANALYSIS.md for technical details
- Ensure backups are created before modifications

For general bypass concepts:
- Refer to the original [Cursor Free VIP](https://github.com/yeongpin/cursor-free-vip) project

---

**Remember**: This tool is for educational purposes. Support the developers if you find value in Kiro IDE.
