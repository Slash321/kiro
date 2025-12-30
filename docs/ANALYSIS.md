# Cursor Free VIP to Kiro Bypass - Comprehensive Analysis

## Project Overview
This project bypasses Cursor IDE's token limits and trial restrictions. We're adapting it for Kiro IDE.

## Core Bypass Mechanisms

### 1. Machine ID Reset (`reset_machine_manual.py`, `totally_reset_cursor.py`)
**What it does:**
- Generates new UUIDs for device identification
- Modifies `storage.json` and `state.vscdb` SQLite database
- Updates system-level machine IDs (Windows Registry, macOS UUID files)
- Patches `main.js` to bypass machine ID validation

**Key IDs Modified:**
- `telemetry.devDeviceId` - Device UUID
- `telemetry.machineId` - 64-char hex hash
- `telemetry.macMachineId` - 128-char hex hash  
- `telemetry.sqmId` - Software Quality Metrics ID
- `storage.serviceMachineId` - Service machine identifier

### 2. Token Limit Bypass (`bypass_token_limit.py`)
**What it does:**
- Modifies `workbench.desktop.main.js`
- Changes token limit from 200,000 to 9,000,000
- Pattern: `async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;`
- Replacement: `async getEffectiveTokenLimit(e){return 9000000;...`

### 3. UI Modifications
**What it does:**
- Changes "Upgrade to Pro" button to "yeongpin GitHub" link
- Replaces "Pro Trial" badge with "Pro"
- Hides notification toasts
- Shows "Pro" status in settings

### 4. Auto-Update Disable (`disable_auto_update.py`)
**What it does:**
- Kills IDE processes
- Deletes updater directory
- Clears `app-update.yml`
- Removes update URLs from `product.json`
- Creates read-only blocking files

### 5. Version Check Bypass (`bypass_version.py`)
**What it does:**
- Patches version validation logic
- Allows older/modified versions to run

## File Paths Comparison

### Cursor Paths:
**Windows:**
- Storage: `%APPDATA%\Cursor\User\globalStorage\storage.json`
- SQLite: `%APPDATA%\Cursor\User\globalStorage\state.vscdb`
- Machine ID: `%APPDATA%\Cursor\machineId`
- App: `%LOCALAPPDATA%\Programs\Cursor\resources\app`

**macOS:**
- Storage: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
- SQLite: `~/Library/Application Support/Cursor/User/globalStorage/state.vscdb`
- Machine ID: `~/Library/Application Support/Cursor/machineId`
- App: `/Applications/Cursor.app/Contents/Resources/app`

**Linux:**
- Storage: `~/.config/cursor/User/globalStorage/storage.json`
- SQLite: `~/.config/cursor/User/globalStorage/state.vscdb`
- Machine ID: `~/.config/cursor/machineid`
- App: `/opt/Cursor/resources/app` or `/usr/share/cursor/resources/app`

### Kiro Paths (Adapted):
**Windows:**
- Storage: `%APPDATA%\Kiro\User\globalStorage\storage.json`
- SQLite: `%APPDATA%\Kiro\User\globalStorage\state.vscdb`
- Machine ID: `%APPDATA%\Kiro\machineId`
- App: `%LOCALAPPDATA%\Programs\Kiro\resources\app`

**macOS:**
- Storage: `~/Library/Application Support/Kiro/User/globalStorage/storage.json`
- SQLite: `~/Library/Application Support/Kiro/User/globalStorage/state.vscdb`
- Machine ID: `~/Library/Application Support/Kiro/machineId`
- App: `/Applications/Kiro.app/Contents/Resources/app`

**Linux:**
- Storage: `~/.config/kiro/User/globalStorage/storage.json`
- SQLite: `~/.config/kiro/User/globalStorage/state.vscdb`
- Machine ID: `~/.config/kiro/machineid`
- App: `/opt/Kiro/resources/app` or `/usr/share/kiro/resources/app`

## Key Code Patterns to Modify

### 1. Machine ID Functions (in `out/main.js`):
```javascript
// Pattern to find:
async getMachineId(){return [^??]+??([^}]+)}
async getMacMachineId(){return [^??]+??([^}]+)}

// Replace with:
async getMachineId(){return \1}
async getMacMachineId(){return \1}
```

### 2. Token Limit (in `out/vs/workbench/workbench.desktop.main.js`):
```javascript
// Pattern to find:
async getEffectiveTokenLimit(e){const n=e.modelName;if(!n)return 2e5;

// Replace with:
async getEffectiveTokenLimit(e){return 9000000;const n=e.modelName;if(!n)return 9e5;
```

### 3. UI Buttons (in `workbench.desktop.main.js`):
```javascript
// Pattern to find (varies by platform):
{title:"Upgrade to Pro",size:"small",get codicon(){return A.rocket},get onClick(){return t.pay}}

// Replace with:
{title:"yeongpin GitHub",size:"small",get codicon(){return A.github},get onClick(){return function(){window.open("https://github.com/yeongpin/cursor-free-vip","_blank")}}}
```

## Adaptation Strategy for Kiro

### Phase 1: Path Configuration
1. Create `kiro_config.py` with Kiro-specific paths
2. Update all path references from "cursor" to "kiro"
3. Handle `.kiro` vs `.cursor` folder naming

### Phase 2: Core Scripts Adaptation
1. `kiro_reset_machine.py` - Adapt machine ID reset
2. `kiro_bypass_token_limit.py` - Adapt token bypass
3. `kiro_disable_auto_update.py` - Adapt update disabler
4. `kiro_main.py` - Main menu interface

### Phase 3: Testing & Validation
1. Test on Windows with provided Kiro installation
2. Verify file paths exist
3. Test each bypass mechanism individually
4. Create backup/restore functionality

## Important Considerations

### Security & Ethics:
- This is for educational purposes only
- May violate Kiro's Terms of Service
- Could result in account bans
- Use at your own risk

### Technical Risks:
- File corruption if not backed up properly
- IDE may become unstable
- Updates may break modifications
- System-level changes (Registry, UUID files) are risky

### Best Practices:
1. Always backup files before modification
2. Test on non-production systems first
3. Keep original files with timestamps
4. Document all changes made
5. Provide easy restore functionality

## Next Steps

1. Create Kiro-specific configuration module
2. Adapt core bypass scripts
3. Test with provided Kiro installation
4. Create comprehensive documentation
5. Add safety checks and validations
