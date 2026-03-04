#!/bin/bash

echo ""
echo "===================================="
echo "        Installing RenixScan"
echo "===================================="
echo ""

echo "[1] Updating system..."
sudo apt update

echo "[2] Installing dependencies..."
sudo apt install -y golang
sudo apt install -y assetfinder
sudo apt install -y python3-pip

echo "[3] Installing subfinder..."
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

echo "[4] Installing Python modules..."
pip3 install requests

echo "[5] Installing RenixScan..."

sudo cp renixscan.py /usr/bin/renixscan
sudo chmod +x /usr/bin/renixscan

echo ""
echo "===================================="
echo " RenixScan Installed Successfully!"
echo "===================================="
echo ""
echo "Run the tool using:"
echo "renixscan"
