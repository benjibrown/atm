#!/usr/bin/python

# Import Required Libs
import os
import rich
import argparse
import json
from rich import print
from rich.console import Console

console = Console()
# Variables N' Stuff

username = os.popen("whoami").read()[:-1]
f = open(f"/home/{username}/.config/openbox-themes/themes/.current")
activetheme = f.read().strip('\n')
f.close()
width = os.get_terminal_size().columns
# Argparse Options

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--info', help='Displays info for the given theme')
args = parser.parse_args()

if args.info:
    theme = args.info.lower()
    f = open('themes.json')
    data = json.load(f)
    try:
        console.print(f"{data[theme]['name']}", style="bold")
        console.print(f"├─ {data[theme]['description']}")
        console.print(f"├─ Author: {data[theme]['author']}")
        console.print(f"├─ File Size: {data[theme]['size']}")
        console.print(f"├─ WM: {data[theme]['wm']}")
        console.print(f"├─ Launcher: {data[theme]['launcher']}")
        console.print(f"├─ Bar: {data[theme]['bar']}")
        console.print(f"├─ Dock: {data[theme]['dock']}")
        console.print(f"└─ [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
        console.print(f"   [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
    except KeyError:
        console.print("A fatal error occured!", style="bold red")







    except KeyError as e:
        print("[+] Theme not found, sorry!")
    
    
