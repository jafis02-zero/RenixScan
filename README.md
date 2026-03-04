<p align="center">
<img src="logo.png" width="420">
</p>

<h1 align="center">RenixScan</h1>

<p align="center">
Advanced Subdomain Scanner
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Linux-green)
![Recon Tool](https://img.shields.io/badge/Type-Recon-red)

</p>

---

# Description

RenixScan is a Python-based subdomain discovery and validation tool.

It uses **Subfinder** and **Assetfinder** to discover subdomains and checks which hosts are alive.

---

# Terminal Preview

<p align="center">
<img src="terminal.png" width="900">
</p>

---

# Features

* Multi-source subdomain enumeration
* Uses Subfinder and Assetfinder
* Alive host detection
* Displays IP addresses
* HTTP status code detection
* Multi-thread scanning
* Progress bar interface

---

# Installation

Clone the repository

```
git clone https://github.com/jafis02-zero/RenixScan.git
```

Enter the directory

```
cd RenixScan
```

Run installer

```
chmod +x install.sh
sudo ./install.sh
```

---

# Usage

Run the tool:

```
renixscan
```

Enter target domain when prompted:

```
Enter target domain: hackerone.com
```

---

# Example Output

```
██████╗ ███████╗███╗   ██╗██╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝████╗  ██║██║╚██╗██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██╔██╗ ██║██║ ╚███╔╝ ███████╗██║     ███████║██╔██╗ ██║

RENIXSCAN
by Jafis

Enter target domain: hackerone.com

Finding subdomains : [############################] 100%
Scanning hosts     : [############################] 100%

Alive Domains
------------------------------------------------------------
api.hackerone.com
docs.hackerone.com
support.hackerone.com
```

---

# Author

Jafis

GitHub
https://github.com/jafis02-zero

---

# Contributing

If you like RenixScan, please consider giving the repository a ⭐

🐉 RenixScan — Unleash the power of deep domain reconnaissance.
