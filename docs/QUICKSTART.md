# Kiro Bypass Tool - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install colorama
```

### Step 2: Verify Kiro Installation

```bash
python kiro_config.py
```

You should see:
```
✅ Found: C:\Users\...\Kiro\resources\app\package.json
✅ Found: C:\Users\...\Kiro\resources\app\out\main.js
✅ Found: C:\Users\...\Kiro\resources\app\out\vs\workbench\workbench.desktop.main.js
✅ Kiro installation verified!
```

### Step 3: Run the Tool

```bash
python kiro_main.py
```

## 📋 Main Menu Options

```
1. Reset Machine ID          - Bypass trial limits
2. Bypass Token Limit        - Increase to 9M tokens
3. Disable Auto-Update       - Prevent updates
4. Verify Kiro Installation  - Check paths
5. Show Configuration        - View settings
0. Exit
```

## 🎯 Recommended Usage Order

### First Time Setup

1. **Verify Installation** (Option 4)
   - Ensures all Kiro files are accessible
   - Shows current paths

2. **Disable Auto-Update** (Option 3)
   - Prevents Kiro from updating
   - Protects your modifications

3. **Reset Machine ID** (Option 1)
   - Generates new device identifiers
   - Bypasses trial restrictions

4. **Bypass Token Limit** (Option 2)
   - Increases token limit to 9M
   - Modifies UI elements

5. **Restart Kiro**
   - Close Kiro completely
   - Start it again to apply changes

### Subsequent Uses

If you need to reset again:

1. Run **Reset Machine ID** (Option 1)
2. Restart Kiro

## ⚠️ Important Notes

### Before You Start

- ✅ **Backup your work** - Save any open files
- ✅ **Close Kiro** - Ensure Kiro is not running
- ✅ **Run as Administrator** (Windows) or with sudo (Linux/macOS)
- ✅ **Read the disclaimer** - Understand the risks

### After Running

- 🔄 **Restart Kiro** - Changes take effect after restart
- 💾 **Backups created** - All modified files are backed up with timestamps
- 📝 **Check output** - Review any warnings or errors

## 🛠️ Individual Tools

### Reset Machine ID Only

```bash
python kiro_reset_machine.py
```

**What it does:**
- Generates new UUIDs
- Updates storage.json
- Updates SQLite database
- Patches main.js

**When to use:**
- Trial period expired
- Need fresh device identity