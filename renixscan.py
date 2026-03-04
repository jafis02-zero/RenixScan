#!/usr/bin/env python3

import subprocess
import socket
import time
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def banner():
    print(CYAN + r"""
██████╗ ███████╗███╗   ██╗██╗██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝████╗  ██║██║╚██╗██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝█████╗  ██╔██╗ ██║██║ ╚███╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██╔══╝  ██║╚██╗██║██║ ██╔██╗ ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗██║ ╚████║██║██╔╝ ██╗███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

              RENIXSCAN
                 by Jafis
""" + RESET)


def progress(prefix, current, total):
    percent = (current / total) * 100
    bar_len = 28
    filled = int(bar_len * current // total)
    bar = "#" * filled + "-" * (bar_len - filled)

    sys.stdout.write(f"\r{prefix} : [{bar}] {percent:.0f}%")
    sys.stdout.flush()


def run(cmd):
    try:
        output = subprocess.check_output(cmd, shell=True, text=True)
        return output.splitlines()
    except:
        return []


def clean(domain, subs):
    results = set()

    for sub in subs:
        if sub.startswith("*."):
            continue

        if sub == domain:
            continue

        if domain in sub:
            results.add(sub.strip())

    return results


def check_host(host):
    try:
        ip = socket.gethostbyname(host)

        try:
            r = requests.get(f"http://{host}", timeout=3)
            return (host, ip, "ALIVE", r.status_code)
        except:
            try:
                r = requests.get(f"https://{host}", timeout=3)
                return (host, ip, "ALIVE", r.status_code)
            except:
                return (host, ip, "DEAD", "-")

    except:
        return (host, "N/A", "DEAD", "-")


def print_table(title, data, color, start):
    print(color + f"\n{title}" + RESET)
    print("─" * 68)
    print(f"{'No':<4} {'Subdomain':<35} {'IP Address':<15} {'Status':<6} Code")
    print("─" * 68)

    index = start

    for host, ip, status, code in data:
        print(f"{index:<4} {host:<35} {ip:<15} {status:<6} {code}")
        index += 1

    return index


def main():
    start = time.time()

    banner()

    domain = input("Enter target domain: ")
    print()

    tools = ["subfinder", "assetfinder"]
    results = []

    for i, tool in enumerate(tools, 1):

        if tool == "subfinder":
            results += run(f"subfinder -silent -d {domain}")

        if tool == "assetfinder":
            results += run(f"assetfinder --subs-only {domain}")

        progress("Finding subdomains", i, len(tools))

    print("\n")

    subs = clean(domain, results)

    alive = []
    dead = []

    total = len(subs)
    completed = 0

    with ThreadPoolExecutor(max_workers=50) as executor:

        futures = [executor.submit(check_host, sub) for sub in subs]

        for future in as_completed(futures):

            result = future.result()
            completed += 1

            progress("Scanning hosts    ", completed, total)

            if result[2] == "ALIVE":
                alive.append(result)
            else:
                dead.append(result)

    print("\n")

    alive.sort()
    dead.sort()

    index = 1

    index = print_table("Alive Domains", alive, GREEN, index)
    print_table("Dead Domains", dead, RED, index)

    end = time.time()

    print("\n" + "─" * 40)
    print(f"Total subdomains : {len(subs)}")
    print(f"Alive domains    : {len(alive)}")
    print(f"Dead domains     : {len(dead)}")
    print(f"Scan time        : {round(end-start,2)} seconds")
    print("─" * 40)


if __name__ == "__main__":
    main()
