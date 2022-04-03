import cutlet
import random
import os
from rich.console import Console
os.system("cls")
console = Console()

def title():
    console.print('[bold red] /$$   /$$ /$$ /$$                                 [white]/$$$$$$$                            /$$')                    
    console.print('[bold red]| $$$ | $$|__/| $$                                [white]| $$__  $$                          | $$')                    
    console.print('[bold red]| $$$$| $$ /$$| $$$$$$$   /$$$$$$  /$$$$$$$       [white]| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$')
    console.print('[bold red]| $$ $$ $$| $$| $$__  $$ /$$__  $$| $$__  $$      [white]| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$')
    console.print('[bold red]| $$  $$$$| $$| $$  \ $$| $$  \ $$| $$  \ $$      [white]| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/')
    console.print('[bold red]| $$\  $$$| $$| $$  | $$| $$  | $$| $$  | $$      [white]| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$_____/| $$')      
    console.print('[bold red]| $$ \  $$| $$| $$  | $$|  $$$$$$/| $$  | $$      [white]| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$')      
    console.print('[bold red]|__/  \__/|__/|__/  |__/ \______/ |__/  |__/      [white]|__/  |__/ \_______/ \_______/ \_______/ \_______/|__/ ')
    console.print('[bold red]Created By C0MP'+'[white]L3X With <3 \n')                                                         
title()

menu_options = {
    1: 'Hiragana',
    2: 'Katakana',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        console.print(key, '[red][ * ]', menu_options[key])

def Hiragana():
    while (True):   
        lines = open('texts\hiragana.txt', encoding='utf-8').read().splitlines()
        myline = random.choice(lines)
        katsu = cutlet.Cutlet()
        katsu.use_foreign_spelling = False
        sent = myline
        print(sent)
        katsu.romaji(sent)
        risposta = str(input("Enter The Reading in Romaji: \n"))
        if risposta != katsu.romaji(sent):
             console.print("[bold red][ ! ]Error!")
             console.print("[green3][ * ]The Correct Version Was:", "[bold red] %s" %(katsu.romaji(sent)))
        else:
            console.print("[green3][ * ]Correct answer!", "[green3] %s" %(katsu.romaji(sent)))

def Katakana():
    while (True):
        lines = open('texts\katakana.txt', encoding='utf-8').read().splitlines()
        myline = random.choice(lines)
        katsu = cutlet.Cutlet()
        katsu.use_foreign_spelling = False
        sent = myline
        print(sent)
        katsu.romaji(sent)
        risposta = str(input("Enter The Reading in Romaji: \n"))
        if risposta != katsu.romaji(sent):
             console.print("[bold red][ ! ]Error!")
             console.print("[green3][ * ]The Correct Version Was:", "[bold red] %s" %(katsu.romaji(sent)))
        else:
            console.print("[green3][ * ]Correct answer!", "[green3] %s" %(katsu.romaji(sent)))

if __name__ == "__main__":
    while(True):
        print_menu()
        options = ''
        try:
            options = int(console.input('[bold red][ * ]Enter your choice: '))
        except:
            console.print("[bold red][ ! ]Wrong Option, Enter an Correct Option... ")
        if options == 1:
            Hiragana()
        elif options == 2:
            Katakana()
        elif options == 3:
            console.print('[ * ]Thanks For Using Nihon Reader :)', style="#FFA500")
            exit()
        else:
            print("Invalid Option. Please enter a number between 1 and 3")
