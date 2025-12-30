# Kiro Pro Free

<div align="center">

![Kiro Pro Free](https://img.shields.io/badge/Kiro-Pro%20Free-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)

**Educational tool for understanding IDE bypass mechanisms**

[Quick Start](#-quick-start) • [Features](#-features) • [Documentation](#-documentation) • [FAQ](FAQ.md) • [Contributing](CONTRIBUTING.md)

</div>

---

## ⚠️ IMPORTANT DISCLAIMER

**FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**

This project demonstrates software bypass techniques for learning purposes. By using this software, you acknowledge:

- ❌ May violate Kiro IDE's Terms of Service
- ❌ Could result in account suspension
- ❌ Authors NOT responsible for consequences
- ✅ For learning and research only
- ✅ Support developers with legitimate licenses

**Use at your own risk. Educational purposes only.**

---

## 🔬 Compatibility Status

**Current Status**: ⚠️ **PARTIALLY COMPATIBLE** with Kiro 0.5.9

### What Works ✅
- ✅ **Machine ID Reset** - Generates new device identifiers
- ✅ **Auto-Update Disable** - Prevents Kiro updates
- ✅ **Pattern Discovery** - Analyzes Kiro's code structure
- ✅ **Configuration Management** - Automatic path detection
- ✅ **Backup System** - Automatic file backups

### What Doesn't Work ❌
- ❌ **Token Limit Bypass** - Kiro uses different code patterns than Cursor
- ❌ **UI Modifications** - Different UI structure

### What's New 🆕
- 🔍 **Pattern Analysis** - Identifies potential modification points
- 📊 **Compatibility Status** - Clear indication of what works
- 🛠️ **Enhanced Error Handling** - Better feedback when features don't work
- 🤝 **Community Contribution** - Framework for sharing working patterns

### Why?
Kiro's internal code differs from Cursor IDE. While both are VSCode forks, they use different function names and patterns. The new pattern discovery mode helps identify what needs to be modified for full compatibility.

### Help Wanted! 🤝
We need community help to identify Kiro-specific patterns. Use the Pattern Discovery mode (Option 2 in Token Bypass) to analyze your Kiro installation and share findings.

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/iamaanahmad/kiro-pro-free.git
cd kiro-pro-free

# Run setup (Windows: setup.bat | Linux/macOS: ./setup.sh)
setup.bat  # or ./setup.sh

# Run tool
python kiro_main.py
```

---

## ✨ Features

- 🔄 **Machine ID Reset** - Bypass trial limitations
- 🚀 **Token Limit Bypass** - 200k → 9M tokens
- 🛑 **Auto-Update Disabler** - Protect modifications
- 💾 **Automatic Backups** - Timestamped safety
- 🖥️ **Cross-Platform** - Windows, macOS, Linux

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- Kiro IDE installed
- Admin/sudo privileges

### Setup
```bash
# Automated
setup.bat  # Windows
./setup.sh # Linux/macOS

# Manual
pip install -r requirements.txt
python kiro_config.py
```

---

## 🎯 Usage

### Main Menu
```bash
python kiro_main.py
```

**Options:**
1. **Reset Machine ID** ✅ - Fully functional
2. **Bypass Token Limit** ⚠️ - Limited (includes Pattern Discovery)
3. **Disable Auto-Update** ✅ - Fully functional
4. **Verify Installation** - Check Kiro installation
5. **Show Configuration** - Display current settings
6. **Compatibility Status** - Detailed compatibility info

### Individual Tools
```bash
python kiro_reset_machine.py      # Machine ID reset
python kiro_bypass_token_limit.py # Token bypass + pattern discovery
python kiro_disable_auto_update.py # Auto-update disable
```

### Pattern Discovery Mode
When using the Token Bypass tool, choose option 2 for Pattern Discovery:
- Analyzes Kiro's JavaScript files
- Identifies potential modification points
- Shows what patterns exist in your Kiro version
- Helps community identify working patterns

---

## 📖 Documentation

- **[Quick Start](docs/QUICKSTART.md)** - 3-step guide
- **[User Guide](docs/KIRO_BYPASS_README.md)** - Complete docs
- **[Technical Analysis](docs/ANALYSIS.md)** - How it works
- **[FAQ](FAQ.md)** - Common questions
- **[Contributing](CONTRIBUTING.md)** - How to help

---

## 🛡️ Safety

- ✅ Automatic timestamped backups
- ✅ File verification before changes
- ✅ Permission checks
- ✅ User confirmations
- ✅ Error handling & recovery

---

## 🐛 Troubleshooting

**File not found:**
```bash
python kiro_config.py  # Verify installation
```

**Permission denied:**
```bash
# Windows: Run as Administrator
# Linux/macOS: sudo python3 kiro_main.py
```

**Restore backup:**
```bash
# Backups: filename.backup.TIMESTAMP
mv file.backup.20250117_143022 file
```

More help: [FAQ](FAQ.md) | [Issues](https://github.com/iamaanahmad/kiro-pro-free/issues)

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md)

- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve docs
- 💻 Submit code

---

## 📜 License

MIT License - See [LICENSE](LICENSE)

**Educational purposes only. No warranty provided.**

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=iamaanahmad/kiro-pro-free&type=date&legend=top-left)](https://www.star-history.com/#iamaanahmad/kiro-pro-free&type=date&legend=top-left)

---

## 🙏 Credits

- **Author**: [Amaan Ahmad](https://github.com/iamaanahmad)
- **Contributors**: [CONTRIBUTORS.md](CONTRIBUTORS.md)

---

## ⚖️ Legal

For educational/research only. Users responsible for:
- Legal compliance
- Terms of Service respect
- Consequences of use

Authors not liable for misuse.

---

<div align="center">

**Made with ❤️ for education**

⭐ Star if helpful! | [Report Issue](https://github.com/iamaanahmad/kiro-pro-free/issues)

**Version 1.1.0** | December 2025

</div>
