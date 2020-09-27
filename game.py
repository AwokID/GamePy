# CODE BY AWOK ID
import os, sys
import random

bidak = ["Batu", "Kertas", "Gunting"]
Kamu = ["Batu", "Kertas", "Gunting"]

random = random.choice(bidak)

menu = """
\033[1;31mAWOK \033[1;37mID

[ \033[41mBatu Kertas Gunting\033[0m ]

1).Gunting
2).Batu
3).Kertas

"""

def clear():
  os.system("clear" if os.name == "nt" else "clear")
try:
  clear()
  print(menu)
  pilih = int(input("Bidak: "))
  print ("")
  if pilih == 1 and random == "Gunting":
    print ("\033[1;33mD R A W\033[0m")
    print ("•> Pil kamu: "+Kamu[2])
    print ("•> Pil musuh: "+random)
    print ("")
  elif pilih == 1  and random == "Batu":
    print ("\033[1;31mK A L A H\033[0m")
    print ("Pil kamu: "+Kamu[2])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 1 and random == "Kertas":
    print ("\033[1;32mM E N A N G\033[0m")
    print ("Pil kamu: "+Kamu[2])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 2 and random == "Batu":
    print ("\033[1;33mD R A W\033[0m")
    print ("Pil kamu: "+Kamu[0])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 2 and random == "Kertas":
    print ("\033[1;31mK A L A H\033[0m")
    print ("Pil kamu: "+Kamu[0])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 2 and random == "Gunting":
    print ("\033[1;32mM E N A N G\033[0m")
    print ("Pil kamu: "+Kamu[0])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 3 and random == "Kertas":
    print ("\033[1;33mD R A W\033[0m")
    print ("Pil kamu: "+Kamu[1])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 3 and random == "Gunting":
    print ("\033[1;31mK A L A H\033[0m")
    print ("Pil kamu: "+Kamu[1])
    print ("Pil musuh: "+random)
    print ("")
  elif pilih == 3 and random == "Batu":
    print ("\033[1;32mM E N A N G\033[0m")
    print ("Pil kamu: "+Kamu[1])
    print ("Pil musuh: "+random)
    print ("")
  elif (pilih > 3):
    exit("\033[1;31mE R R O R")
  else:
    print ("\n\033[1;31mGUNAKAN ANGKA\033[0m")
except KeyboardInterrupt:
  exit ("\n\033[1;31mOK Exit\033[0m")
except Exception as e:
  exit ("\033[1;31mUse Numbers\033[0m")
