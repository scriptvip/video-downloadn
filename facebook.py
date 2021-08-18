import os
import urllib.request
import requests
import re

print(" _____   _____        _     _   _   _____   _____   _____       ")
print("|  ___| |  _  \      | |   / / | | |  _  \ | ____| /  _  \      ")
print("| |__   | |_| |      | |  / /  | | | | | | | |__   | | | |      ")
print("|  __|  |  _  {      | | / /   | | | | | | |  __|  | | | |      ")
print("| |     | |_| |      | |/ /    | | | |_| | | |___  | |_| |      ")
print("|_|     |_____/      |___/     |_| |_____/ |_____| \_____/      ")
print("                    Abdo sleem (*__^) ")
print(" ")
print(" ")




link = input("  Video Link ==> ")
print(" ")
nam = input(" put name for video ==> ")
print(" ")
print("  ")
e = ".mp4"
name = nam+e
ss = "/sdcard"
sp = " "

html = requests.get(link)

try:
    url = re.search('hd_src:"(.+?)"',html.text)[1]
    print(" HD Video")

except:
    url = re.search('sd_src:"(.+?)"',html.text)[1]
    print(" SD Video")

print ("    Downloading ... Please be patient (^__^) ")
urllib.request.urlretrieve(url, name)
print("   ")
print("    ")
print ("     Download Successfully !!!")
