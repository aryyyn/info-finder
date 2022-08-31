import requests
import os , webbrowser

while 1:
    errorinsta = '<a class="tgme_action_button_new shine" href="tg://resolve?'
    print("Enter any username")
    inp = input()


    iurl = 'https://t.me/' + inp
    data = requests.get(iurl).text
    if errorinsta in data:
        print('roblox - ' + iurl)
    
    








