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

RenixScan is a fast reconnaissance tool designed for security researchers and bug bounty hunters.

It enumerates subdomains using multiple tools and checks whether they are alive using DNS resolution and HTTP requests.

The tool provides clean output with progress bars and organized tables.

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

Usage

Run the tool:

renixscan

Enter target domain when prompted:

Enter target domain: example.com
Example Output
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
------------------------------------------------------------
No   Subdomain                IP Address      Status Code
------------------------------------------------------------
1    api.example.com          192.168.1.10    ALIVE 200
2    docs.example.com         192.168.1.11    ALIVE 200
3    blog.example.com         192.168.1.12    ALIVE 301
4    mail.example.com         192.168.1.13    ALIVE 200
5    shop.example.com         192.168.1.14    ALIVE 200
6    dev.example.com          192.168.1.15    ALIVE 403
7    support.example.com      192.168.1.16    ALIVE 200
8    cdn.example.com          192.168.1.17    ALIVE 200

Dead Domains
------------------------------------------------------------
No   Subdomain                IP Address      Status Code
------------------------------------------------------------
9    old.example.com          N/A             DEAD -
10   beta.example.com         N/A             DEAD -
11   test.example.com         N/A             DEAD -
12   staging.example.com      N/A             DEAD -
13   admin.example.com        N/A             DEAD -

------------------------------------------------------------
Total subdomains : 13
Alive domains    : 8
Dead domains     : 5
Scan time        : 18.42 seconds
------------------------------------------------------------
Author 

jafis
linkedin-https://www.linkedin.com/in/jafis-k-a-a73952389
---

# Contributing

If you like RenixScan, please consider giving the repository a ⭐

🐉 RenixScan — Unleash the power of deep domain reconnaissance.
