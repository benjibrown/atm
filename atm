#!/usr/bin/python

# Import Required Libs
import os
import rich
import argparse
import subprocess
import time
import json
import requests
from rich import print
from rich.console import Console
from subprocess import DEVNULL, STDOUT, check_call
console = Console()
# Variables N' Stuff

username = os.popen("whoami").read()[:-1]
f = open(f"/home/{username}/.config/openbox-themes/themes/.current")
activetheme = f.read().strip('\n')
f.close()
width = os.get_terminal_size().columns
# Argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--info', help='Displays info for the given theme')
parser.add_argument('-d', '--download', help='Downloads and applies the chosen theme')
args = parser.parse_args()
# Information 
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
        # Ignore this spaghetti lel
        console.print(f"└─ [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
        console.print(f"   [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
    except Exception:
        console.print("[!] A fatal error occured! Please do some investigating :)", style="bold red")    
# Download option code

if args.download:
    theme = args.download.lower()
    f = open('themes.json')
    data = json.load(f)
    
    console.print('[*] Downloading theme...', style="bold")
    r = requests.get(data[theme]['downloadlink'], allow_redirects=True)
    open('temp.tar.gz', 'wb').write(r.content)
    try:
        console.print('[*] Installing theme...', style="bold")
        subprocess.run(['mkdir temp && tar -xzvf temp.tar.gz -C temp --strip-components=1 && cd temp && bash install.sh >/dev/null 2>&1'], shell=True, stdout=DEVNULL, stderr=STDOUT)

        console.print('[*] Applying theme...', style="bold")
        subprocess.run([f'nohup bash /home/{username}/.config/openbox-themes/themes/{theme}/apply.sh & >/dev/null 2>&1'], shell=True, stdout=DEVNULL, stderr=STDOUT)
        time.sleep(5)
        subprocess.run([f'nohup bash /home/{username}/.config/openbox-themes/themes/{theme}/apply.sh & >/dev/null 2>&1'], shell=True, stdout=DEVNULL, stderr=STDOUT)
    
        console.print('[*] Cleaning up...', style="bold")
        subprocess.run(['rm -r -f temp temp.tar.gz nohup.out >/dev/null 2>&1'], shell=True, stdout=DEVNULL, stderr=STDOUT)
        # Print loads lmao
        console.print('[*] All done, enjoy your new theme!', style="bold")
        console.print('[*] Check out some stats about it below! \n', style="bold")
        console.print(f"{data[theme]['name']}", style="bold")
        console.print(f"├─ {data[theme]['description']}")
        console.print(f"├─ Author: {data[theme]['author']}")
        console.print(f"├─ File Size: {data[theme]['size']}")
        console.print(f"├─ WM: {data[theme]['wm']}")
        console.print(f"├─ Launcher: {data[theme]['launcher']}")
        console.print(f"├─ Bar: {data[theme]['bar']}")
        console.print(f"├─ Dock: {data[theme]['dock']}")
        # Ignore this spaghetti lel
        console.print(f"└─ [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
        console.print(f"   [{data[theme]['black']}]████[{data[theme]['red']}]████[{data[theme]['green']}]████[{data[theme]['yellow']}]████[{data[theme]['blue']}]████[{data[theme]['magenta']}]████[{data[theme]['cyan']}]████[{data[theme]['white']}]████")
    
    except Exception as e:
        console.print('[!] Uh Oh! An error occured, we\'ll print it below so you investigate...', style="bold red")


