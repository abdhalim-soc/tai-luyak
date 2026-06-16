import os
import time
import random

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def matrix():
    chars = "01ABCDEFXYZ#@$%"
    for _ in range(20):
        print(GREEN + "".join(random.choice(chars) for _ in range(60)) + RESET)
        time.sleep(0.05)

def progress():
    for i in range(0, 101, 5):
        bar = "█" * (i // 5)
        print(f"\r{CYAN}[{bar:<20}] {i}%{RESET}", end="")
        time.sleep(0.1)
    print()

def banner():
    clear()
    print(CYAN + r"""
███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗
██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║
██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
""" + RESET)

    print(YELLOW + "      NEXUS CORE v99.9\n" + RESET)

def run_mode(mode):
    clear()

    target = input(f"{CYAN}TARGET ID > {RESET}")

    clear()
    print(f"{GREEN}TARGET ACQUIRED : {target}{RESET}")
    time.sleep(1)

    matrix()

    print(CYAN + "\nINITIALIZING SYSTEM...\n" + RESET)

    stages = [
        "Loading Neural Matrix",
        "Synchronizing Core",
        "Scanning Reality",
        "Calibrating Quantum Layer",
        "Analyzing Universe"
    ]

    for s in stages:
        print(GREEN + "[+]" + RESET, s)
        time.sleep(0.8)

    print()
    progress()

    score = random.randint(9000, 99999)

    print(CYAN + "\n═══════════════════════════════")
    print("       OPERATION COMPLETE")
    print("═══════════════════════════════" + RESET)

    print(f"MODE         : {mode}")
    print(f"TARGET       : {target}")
    print(f"POWER LEVEL  : {score}")
    print("STATUS       : DRAMATIC")
    print("RESULT       : NOTHING HAPPENED")
    print("COOL FACTOR  : MAXIMUM")

    input("\nPress Enter...")

while True:
    banner()

    print("""
[1] Quantum Engine
[2] Neural Matrix
[3] Reality Scanner
[4] Cosmic Analyzer
[5] Power Diagnostics
[0] Exit
""")

    choice = input("Select > ")

    if choice == "1":
        run_mode("Quantum Engine")
    elif choice == "2":
        run_mode("Neural Matrix")
    elif choice == "3":
        run_mode("Reality Scanner")
    elif choice == "4":
        run_mode("Cosmic Analyzer")
    elif choice == "5":
        run_mode("Power Diagnostics")
    elif choice == "0":
        break
