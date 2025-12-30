#!/bin/bash
# Kiro Bypass Tool - Linux/macOS Setup Script

echo "========================================"
echo "Kiro IDE Bypass Tool - Setup"
echo "========================================"
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[OK] Python found"
python3 --version
echo ""

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

echo ""
echo "[OK] Dependencies installed"
echo ""

# Verify Kiro installation
echo "Verifying Kiro installation..."
python3 kiro_config.py
if [ $? -ne 0 ]; then
    echo "[WARNING] Kiro verification had issues"
    echo "Please check the output above"
fi

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "To run the tool:"
echo "  python3 kiro_main.py"
echo ""
echo "For help, see docs/QUICKSTART.md"
echo ""
