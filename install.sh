#!/bin/bash

echo "Installing RenixScan..."

sudo apt update

sudo apt install -y golang
sudo apt install -y assetfinder
sudo apt install -y python3-pip

echo "Installing subfinder..."

go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

pip3 install requests

sudo cp renixscan.py /usr/bin/renixscan
sudo chmod +x /usr/bin/renixscan

echo ""
echo "RenixScan Installed!"
echo "Run using: renixscan"

