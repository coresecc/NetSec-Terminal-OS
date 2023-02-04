import colorama
from colorama import Style, Back, Fore
import os
import sys
import subprocess
import discord
import tkinter as tk
import turtle as t
import time
import socket
from subprocess import call
import stdiomask
from stdiomask import getpass
import hashlib
from tkinter import Button, Tk, HORIZONTAL
from tkinter.ttk import Progressbar
import threading
from tqdm.tk import tqdm
from time import sleep
from pystyle import Colors, Colorate
from pystyle import Write, Colors
clear = lambda: os.system('cls')

colorama.init(autoreset=True)
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

os.system('title NetSec OS Setup')
print("Loading...")
time.sleep(3)
os.system('cls')
print(f"[{Fore.GREEN}200{Fore.WHITE}] Installing Modules")
time.sleep(0.9)
print(f"[{Fore.GREEN}200{Fore.WHITE}] Fetching {ip}")
time.sleep(0.9)
print(f"[{Fore.GREEN}200{Fore.WHITE}] Getting Hostname {hostname}")
time.sleep(0.9)
print(f"[{Fore.RED}405{Fore.WHITE}] Failed to load Proxies")
time.sleep(0.9)
print(f"[{Fore.GREEN}200{Fore.WHITE}] Successfully Installed Modules!")
time.sleep(0.9)
print(f"[{Fore.GREEN}200{Fore.WHITE}] Sucsessfully Fetched IP")
time.sleep(0.9)
print(f"[{Fore.GREEN}200{Fore.WHITE}] Sucessfully Got Username")
time.sleep(0.9)
os.system('cls')

def create_acc():
    user = Write.Input(f"""[ {hostname} ] Enter a Username : """, Colors.red_to_purple)
    password = Write.Input(f"""[ {hostname} ] Enter a Password : """, Colors.red_to_purple)
    confirm_password = Write.Input(f"""[ {hostname} ] Confirm Password : """, Colors.red_to_purple)
    if confirm_password == password:
        with open("data.txt", "w") as f:
            f.write(f"""
            NEW LOG
            USERNAME {user}
            PASSWORD {password}
            CONFIRMED PASSWORD {confirm_password}
            HOSTNAME {hostname}
            """)
            time.sleep(3)
            print(Colorate.Horizontal(Colors.red_to_purple, f"""[ {hostname} ] Logging in..."""))

print(Colorate.Horizontal(Colors.red_to_purple, f"""
https://github.com/coresecc
 ___        ______    _______   __    _____  ___   
|"  |      /    " \  /" _   "| |" \  (\"   \|"  \  
||  |     // ____  \(: ( \___) ||  | |.\\   \    | 
|:  |    /  /    ) :)\/ \      |:  | |: \.   \\  | 
 \  |___(: (____/ // //  \ ___ |.  | |.  \    \. | 
( \_|:  \\        / (:   _(  _|/\  |\|    \    \ | 
 \_______)\"_____/   \_______)(__\_|_)\___|\____\) 
                                                   


[1] Create Account
"""))
choice = Write.Input(f"""
[ {hostname} ] : """, Colors.red_to_purple)
if choice == "1":
    create_acc()
    time.sleep(4)
    os.system('cls')
    os.system('python netsec.py')
