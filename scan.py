import requests
import colorama
import os
import time
from colorama import Fore
os.system('clear')
ascii_text = r"""
        ╔═══════════════════════════╗
        ║                           ║
        ║        BLRX ROCKY         ║
        ║                           ║
        ╚═══════════════════════════╝
"""
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print(BLUE + ascii_text + RESET)
print(Fore.CYAN+"                  Insta : @blrx.rocky")
print()
print()

path = input(Fore.BLUE+ "  ["+ Fore.RED+"+"+Fore.BLUE+"]"+Fore.GREEN+" Enter File Path :"+Fore.RED)
file = input(Fore.BLUE+ "  ["+ Fore.RED+"+"+Fore.BLUE+"]"+Fore.GREEN+" Enter File Name :"+Fore.RED)
print()
print(f"{Fore.BLUE}  [{Fore.RED}+{Fore.BLUE}]{Fore.GREEN} Scaning Started{Fore.RED}{RESET}")
print()

filep = (path + file)
with open( filep , "r") as f:
    urls = f.read().splitlines()

failed = []
success = []
count = 0

for url in urls:
    count += 1
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.BLUE}  [{Fore.RED}+{Fore.BLUE}]{Fore.GREEN} {url} : 200 OK{Fore.RED}{RESET}")
            success.append(url)
        else:
            failed.append(url)
    except:
        failed.append(url)

    if count % 5 == 0:
        os.system('clear')
        print(GREEN + ascii_text + RESET)
        for fail_url in failed:
            print(f"{RED}Failed: {fail_url}{RESET}")
        failed.clear()

    time.sleep(0.2)


if success:
    with open("success.txt", "w") as s:
     for url in success:
            s.write(url + "\n")

with open("failed.txt", "w") as f:
    for url in failed:
        f.write(url + "\n")
print(Fore.BLUE+ "  ["+ Fore.RED+"+"+Fore.BLUE+"]"+Fore.GREEN+" Finished "+Fore.RED)
print(Fore.BLUE+ "  ["+ Fore.RED+"+"+Fore.BLUE+"]"+Fore.GREEN+" Working Links Are Saved in success.txt")
print()
print()
print(Fore.BLUE+ "  ["+ Fore.RED+"+"+Fore.BLUE+"]"+Fore.CYAN+" BY BLRX ROCKY "+Fore.RED)
print()
print()
print()