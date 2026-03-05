#!/bin/bash

echo ""
echo "===================================="
echo "        Installing RenixScan"
echo "===================================="
echo ""

# Update system
echo "[1] Updating system..."
sudo apt update -y

# Install dependencies
echo "[2] Installing dependencies..."
sudo apt install -y golang assetfinder python3 python3-pip curl

# Install subfinder
echo "[3] Installing subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Move subfinder to PATH
sudo cp ~/go/bin/subfinder /usr/local/bin/

# Install Python modules
echo "[4] Installing Python modules..."
pip3 install requests colorama tabulate --break-system-packages

# Install RenixScan globally
echo "[5] Installing RenixScan..."
sudo cp renixscan.py /usr/local/bin/renixscan
sudo chmod +x /usr/local/bin/renixscan

echo ""
echo "===================================="
echo " RenixScan Installed Successfully!"
echo "===================================="
echo ""
