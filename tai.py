import os
import time
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading(title):
    print(f"\n{title}\n")

    steps = [
        "Initializing Hacker Core...",
        "Loading Military Database...",
        "Connecting To Satellite...",
        "Accessing Secret Network...",
        "Decrypting Quantum Firewall...",
        "Synchronizing Matrix...",
        "Analyzing Target..."
    ]

    for step in steps:
        print(step)
        time.sleep(0.7)

    print("\n[████████████████████] 100%")
    time.sleep(1)

def result():
    print("\n╔════════════════════════════╗")
    print("║      OPERATION RESULT      ║")
    print("╠════════════════════════════╣")
    print(f"║ Damage      : {random.randint(0,0)}%           ║")
    print("║ Website     : Normal       ║")
    print(f"║ Hacker Ego  : +{random.randint(1000,9999)}      ║")
    print("║ Reality     : Unchanged    ║")
    print("╚════════════════════════════╝")
    input("\nPress Enter...")

def banner():
    clear()

    print(r"""
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")

    print("      OMEGA HACKER TERMINAL v99.9")
    print("══════════════════════════════════════════════")

def menu():
    while True:
        banner()

        print("""
[1] Hancurkan Website
[2] Retas Website
[3] Ambil Data Website
[4] Virus Website
[5] Bajak Website
[0] Keluar
""")

        pilih = input("Select > ")

        if pilih == "1":
            loading("MODE : HANCURKAN WEBSITE")
            result()

        elif pilih == "2":
            loading("MODE : RETAS WEBSITE")
            result()

        elif pilih == "3":
            loading("MODE : AMBIL DATA WEBSITE")
            result()

        elif pilih == "4":
            loading("MODE : VIRUS WEBSITE")

            print("""
ERROR

Virus forgot its password.
Operation cancelled.
""")

            input("\nPress Enter...")

        elif pilih == "5":
            loading("MODE : BAJAK WEBSITE")

            print("""
SUCCESS

Website ownership:
Still not yours.
""")

            input("\nPress Enter...")

        elif pilih == "0":
            print("\nGoodbye Hacker 😹")
            break

        else:
            input("Menu tidak valid!")

menu()
