# 🐉 RenixScan

<p align="center">
  <img src="logo.png" width="200">
</p>

### 💻 Terminal Image


<p align="center">
  <img src="terminal.png">
</p>

---

## 🔎 Description

RenixScan is a fast reconnaissance tool designed for security researchers and bug bounty hunters.

It enumerates subdomains using multiple tools and checks whether they are alive using DNS resolution and HTTP requests.

The tool provides clean output with progress bars and organized tables, making reconnaissance simple and efficient.

RenixScan uses Subfinder and Assetfinder to discover subdomains and then checks which hosts are alive.

---

## 🚀 Features

- Multi-source subdomain enumeration
- Uses Subfinder and Assetfinder
- Alive host detection
- Displays IP addresses
- HTTP status code detection
- Multi-thread scanning
- Progress bar interface
- Clean organized output

---

## 📦 Installation

### 1️⃣ Clone the Repository

git clone https://github.com/jafis02-zero/RenixScan.git

### 2️⃣ Enter the Directory

cd RenixScan

### 3️⃣ Run Installer
chmod +x install.sh
sudo ./install.sh

---

## 💻 Usage

Run the tool:

renixscan

Enter target domain when prompted:

Enter target domain: example.com

---

## 🖥️ Example Output

➜  ~ renixscan

██████╗ ███████╗███╗   ██╗██╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝████╗  ██║██║╚██╗██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██╔██╗ ██║██║ ╚███╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║╚██╗██║██║ ██╔██╗ ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██║ ╚████║██║██╔╝ ██╗███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

              RENIXSCAN
                 by Jafis

Enter target domain: example.com

Finding subdomains : [############################] 100%

Scanning hosts     : [############################] 100%


Alive Domains
────────────────────────────────────────────────────────────────────
No   Subdomain                           IP Address      Status Code
────────────────────────────────────────────────────────────────────
1    api.example.com                     192.168.1.10    ALIVE  200
2    docs.example.com                    192.168.1.11    ALIVE  200
3    blog.example.com                    192.168.1.12    ALIVE  301
4    mail.example.com                    192.168.1.13    ALIVE  200
5    shop.example.com                    192.168.1.14    ALIVE  200
6    dev.example.com                     192.168.1.15    ALIVE  403
7    support.example.com                 192.168.1.16    ALIVE  200
8    cdn.example.com                     192.168.1.17    ALIVE  200
9    status.example.com                  192.168.1.18    ALIVE  200
10   www.example.com                     192.168.1.19    ALIVE  200

Dead Domains
────────────────────────────────────────────────────────────────────
No   Subdomain                           IP Address      Status Code
────────────────────────────────────────────────────────────────────
11   old.example.com                     N/A             DEAD   -
12   beta.example.com                    N/A             DEAD   -
13   test.example.com                    N/A             DEAD   -
14   staging.example.com                 N/A             DEAD   -
15   admin.example.com                   N/A             DEAD   -

────────────────────────────────────────
Total subdomains : 15
Alive domains    : 10
Dead domains     : 5
Scan time        : 18.42 seconds
────────────────────────────────────────
---

## 👨‍💻 Author

Jafis

LinkedIn
https://www.linkedin.com/in/jafis-k-a-a73952389

---

## 🤝 Contributing

Contributions are welcome!

If you like RenixScan, please consider giving the repository a ⭐
🐉RenixScan — Unleash the power of deep domain reconnaissance. 🚀
