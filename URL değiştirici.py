import os
from time import sleep
import pyshorteners


def programm():
    os.system('clear')
    print("\nÖR:google.com")
    original_domain = str(input("\nSahte URL girin: "))

    os.system('clear') 
    

    print("\nVideo ekleri girin: en-komik-videolar-serisi")
    postlink = str(input("ekleri girin: "))

    os.system('clear')
    

    url_to_short = str(input("Orjinal URL girin:"))
    s = pyshorteners.Shortener()
    shorten=(s.dagd.short(f'{url_to_short}'))
    withoutprotocol = shorten[8:]
    
    os.system('clear')
    print(f"\033[95m\nSenin linkin: https://{original_domain}-{postlink}@{withoutprotocol}")


    defanother()
    

def defanother():
    another=str(input("\033[93m\nBaşka bir URL yi dönüştür? (y/n): ")) 
    if another == "y":
        programm()

    elif another == "n":
        exit()

    else:
        print("Yeniden dene")
        sleep(3)
        os.system('clear')
        defanother()

programm()
