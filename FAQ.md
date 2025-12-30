# Frequently Asked Questions (FAQ)

## General Questions

### What is Kiro Pro Free?

Kiro Pro Free is an educational tool that demonstrates bypass techniques for Kiro IDE's token limits and trial restrictions. It's designed for learning and research purposes.

### Is this legal?

This tool is provided for **educational purposes only**. Using it may violate Kiro IDE's Terms of Service. Users are responsible for understanding and complying with applicable laws and terms. We recommend using it only for learning and supporting developers by purchasing legitimate licenses.

### Is this safe to use?

The tool includes safety features like automatic backups and verification checks. However, it modifies core IDE files, which carries inherent risks. Always backup your data and test in non-production environments first.

### Will I get banned?

Possibly. Using bypass tools may result in account suspension or termination. This is a risk you accept by using the tool. We recommend using test accounts only.

## Installation & Setup

### What are the requirements?

- Python 3.8 or higher
- Kiro IDE installed
- Administrator/sudo privileges
- colorama Python package

### How do I install it?

```bash
# Clone the repository
git clone https://github.com/iamaanahmad/kiro-pro-free.git
cd kiro-pro-free

# Run setup
# Windows:
setup.bat

# Linux/macOS:
chmod +x setup.sh
./setup.sh
```

### Installation fails with "Python not found"

Ensure Python 3.8+ is installed and in your PATH:
```bash
python --version  # or python3 --version
```

If not installed, download from [python.org](https://www.python.org/downloads/)

### "Permission denied" errors

Run with elevated privileges:
```bash
# Windows: Run Command Prompt as Administrator
# Linux/macOS:
sudo python3 kiro_main.py
```

## Usage Questions

### How do I use the tool?

```bash
python kiro_main.py
```

Follow the menu:
1. Verify Installation (Option 4)
2. Disable Auto-Update (Option 3)
3. Reset Machine ID (Option 1)
4. Bypass Token Limit (Option 2)
5. Restart Kiro

### What does "Reset Machine ID" do?

It generates new device identifiers and updates:
- storage.json
- SQLite database (state.vscdb)
- machineId file
- main.js validation logic

This makes Kiro think it's a new device.

### What does "Bypass Token Limit" do?

It modifies workbench.desktop.main.js to:
- Increase token limit from 200,000 to 9,000,000
- Change UI elements to show "Pro" status
- Hide upgrade prompts

### What does "Disable Auto-Update" do?

It prevents Kiro from auto-updating by:
- Removing updater directory
- Clearing update configuration
- Blocking update URLs
- Creating blocking files

This protects your modifications from being overwritten.

### Do I need to run all three?

For best results:
1. **Disable Auto-Update** - Protects modifications
2. **Reset Machine ID** - Bypasses trial limits
3. **Bypass Token Limit** - Increases token capacity

You can run them individually, but all three provide complete functionality.

### How often do I need to reset?

Typically only when:
- Trial period expires again
- Kiro detects the bypass
- After major Kiro updates
- Switching to a new system

## Troubleshooting

### "File not found" errors

Run verification:
```bash
python kiro_config.py
```

This checks if Kiro is properly installed and paths are correct.

### "No patterns matched" warning

Your Kiro version may be different. The tool looks for specific code patterns. This may mean:
- Different Kiro version
- Files already modified
- Kiro structure changed

Check your Kiro version in package.json.

### Kiro won't start after modifications

Restore from backups:
```bash
# Find backup files (they have .backup.TIMESTAMP extension)
# Example on Windows:
cd %APPDATA%\Kiro\User\globalStorage
dir *.backup.*

# Restore by renaming
del storage.json
ren storage.json.backup.20250117_143022 storage.json
```

### Changes don't take effect

1. Ensure Kiro is completely closed
2. Check if modifications were successful (look for success messages)
3. Restart Kiro
4. Clear Kiro's cache if needed

### "Permission denied" on Linux/macOS

Some files may be owned by root. Use sudo:
```bash
sudo python3 kiro_main.py
```

Or fix ownership:
```bash
sudo chown -R $USER:$USER ~/.config/kiro
```

## Technical Questions

### Where are backups stored?

Backups are created in the same directory as the original file with extension:
```
.backup.YYYYMMDD_HHMMSS
```

Example:
```
storage.json.backup.20250117_143022
```

### How do I restore from backup?

1. Delete or rename the current file
2. Rename the backup file to the original name

```bash
# Windows
del storage.json
ren storage.json.backup.20250117_143022 storage.json

# Linux/macOS
rm storage.json
mv storage.json.backup.20250117_143022 storage.json
```

### What files are modified?

The tool modifies:
- `storage.json` - Device IDs
- `state.vscdb` - SQLite database
- `machineId` - Machine identifier
- `main.js` - Validation logic
- `workbench.desktop.main.js` - Token limits and UI
- `product.json` - Update URLs
- `app-update.yml` - Update configuration

### Can I undo the changes?

Yes! The tool creates automatic backups. You can:
1. Restore from backups manually
2. Reinstall Kiro IDE
3. Use Kiro's repair function (if available)

### Does this work on all Kiro versions?

Tested on Kiro 0.5.9. Other versions may work but aren't guaranteed. The tool looks for specific code patterns that may change between versions.

### Will this work after Kiro updates?

Maybe not. Updates may:
- Change file structure
- Modify code patterns
- Add new security measures
- Break the bypass

That's why we disable auto-updates first.

## Platform-Specific

### Windows-specific issues

**Antivirus blocking:**
- Some antivirus software may flag the tool
- Add exception if you trust it
- This is common for tools that modify files

**UAC prompts:**
- Run Command Prompt as Administrator
- Right-click → "Run as administrator"

### macOS-specific issues

**Gatekeeper warnings:**
```bash
# Allow execution
chmod +x setup.sh
xattr -d com.apple.quarantine setup.sh
```

**SIP (System Integrity Protection):**
- Shouldn't affect Kiro files in user directories
- If issues, check SIP status: `csrutil status`

### Linux-specific issues

**Multiple Kiro installations:**
- Tool checks common locations
- May need to specify path manually
- Edit config.ini if needed

**AppImage installations:**
- Extract AppImage first
- Tool looks for extracted directories

## Safety & Ethics

### Is my data safe?

The tool:
- ✅ Only modifies Kiro IDE files
- ✅ Creates automatic backups
- ✅ Doesn't transmit data
- ✅ Doesn't collect information
- ❌ Doesn't access personal files

### Should I use this on my main account?

**No.** We strongly recommend:
- Use test accounts only
- Test in isolated environments
- Understand the risks
- Support developers when possible

### What are the ethical considerations?

Consider:
- Developers deserve compensation for their work
- This violates Terms of Service
- You're bypassing intended limitations
- There may be legal consequences

**Recommendation**: Use for learning, then purchase a legitimate license if you find value.

### How can I support the developers?

- Purchase a legitimate Kiro Pro license
- Provide feedback to improve the product
- Recommend Kiro to others
- Contribute to the community

## Contributing

### How can I contribute?

See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Reporting bugs
- Suggesting features
- Submitting code
- Improving documentation

### I found a bug, what should I do?

1. Check if it's already reported in Issues
2. Gather information (OS, Python version, error messages)
3. Create a detailed bug report
4. Include steps to reproduce

### Can I add support for other IDEs?

Yes! Fork the project and adapt it. Consider:
- Creating a separate repository
- Crediting this project
- Following the same ethical guidelines

## Legal & Licensing

### What license is this under?

MIT License with additional disclaimers. See [LICENSE](LICENSE) for details.

### Can I use this commercially?

The MIT License allows commercial use, but:
- You're responsible for legal compliance
- Using bypass tools commercially is risky
- We don't recommend it
- Support legitimate licenses instead

### Can I modify and redistribute?

Yes, under MIT License terms:
- Keep the original license
- Credit the original authors
- Include disclaimers
- Don't hold us liable

## Getting Help

### Where can I get help?

1. Read the documentation in `docs/`
2. Check this FAQ
3. Search existing GitHub Issues
4. Create a new Issue with details
5. Join discussions

### How do I report issues?

Create a GitHub Issue with:
- Clear title and description
- Steps to reproduce
- Expected vs actual behavior
- System information
- Error messages/logs
- Screenshots if helpful

### Is there a community?

- GitHub Discussions
- Issue tracker
- Pull requests welcome
- See CONTRIBUTING.md

---

## Still Have Questions?

- 📖 Read the [Complete User Guide](docs/KIRO_BYPASS_README.md)
- 🔍 Check [Technical Analysis](docs/ANALYSIS.md)
- 💬 Open a [GitHub Issue](https://github.com/iamaanahmad/kiro-pro-free/issues)
- 🤝 See [Contributing Guidelines](CONTRIBUTING.md)

---

**Last Updated**: November 17, 2025  
**Version**: 1.0.0
