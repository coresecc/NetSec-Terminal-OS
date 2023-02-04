from pystyle import Write, Colors
from pystyle import Colors, Colorate
import socket
import time
import os
hostname = socket.gethostname()


def help():
    print(Colorate.Horizontal(Colors.red_to_purple, f"""
https://github.com/coresecc

  __    __    _______  ___         _______   
 /" |  | "\  /"     "||"  |       |   __ "\  
(:  (__)  :)(: ______)||  |       (. |__) :) 
 \/      \/  \/    |  |:  |       |:  ____/  
 //  __  \\  // ___)_  \  |___    (|  /      
(:  (  )  :)(:      "|( \_|:  \  /|__/ \     
 \__|  |__/  \_______) \_______)(_______)    
                                             

This Will Get Deleted in 10 seconds!

[1] Logout - Usage: logout
[2] IPLookup - Usage: ip ip_adress
[3] DDOS - Usage: ddos ip_adress
[4] Discord Token Gen - Usage: tgen
[5] Otax - Usage: otax id
[6] PIP - Usage: pip install module
[7] Selfbot - Usage: selfbot
[8] IPGEN - Usage: ipgen
[9] DOXXING - Usage: doxing
[10] Credits - Usage: creds
"""))


print(Colorate.Horizontal(Colors.red_to_purple, f"""
https://github.com/coresecc
 _____  ___    _______  ___________  ________  _______   ______          ______    ________  
(\"   \|"  \  /"     "|("     _   ")/"       )/"     "| /" _  "\        /    " \  /"       ) 
|.\\   \    |(: ______) )__/  \\__/(:   \___/(: ______)(: ( \___)      // ____  \(:   \___/  
|: \.   \\  | \/    |      \\_ /    \___  \   \/    |   \/ \          /  /    ) :)\___  \    
|.  \    \. | // ___)_     |.  |     __/  \\  // ___)_  //  \ _      (: (____/ //  __/  \\   
|    \    \ |(:      "|    \:  |    /" \   :)(:      "|(:   _) \      \        /  /" \   :)  
 \___|\____\) \_______)     \__|   (_______/  \_______) \_______)      \"_____/  (_______/   
                                                                                             

"""))
terminal = Write.Input(f"""[ {hostname} ] : """, Colors.red_to_purple)

if terminal == "help":
    os.system('cls')
    help()
    time.sleep(10)
    os.system('cls')
    os.system('python netsec.py')