import requests
import os , webbrowser


clear = lambda: os.system('cls')
errorinsta = '4fsjkilkam0w4w8w.pkg,js\/7g6l59zj8eg448w4.pkg,js\/53fjp92f0288www0.pkg'
errorgithub = 'https://github.com/'
errorfb = 'data-content-len'
errorred = 'data-testid="comment_timestamp"'
errorroblox = '<h3 class="error-title">Page cannot be found or no longer exists</h3>'
errortelegram = '<a class="tgme_action_button_new shine" href="tg://resolve?'

while 1:
 print("Enter any username")
 inp = input()
 clear()
 print("Searching For Users")



 iurl = 'https://www.instagram.com/' + inp
 data = requests.get(iurl).text
 if errorinsta in data:
     print('instagram - ' + iurl + '/')


 iurl1 = 'https://www.github.com/' + inp
 data1 = requests.get(iurl1).text
 if errorgithub in data1:
     print('github - ' + iurl1)


 iurl2 = 'https://www.facebook.com/' + inp
 data2 = requests.get(iurl2).text
 if errorfb in data2:
     print('facebook - ' + iurl2)


 iurl3 = 'https://www.reddit.com/user/' + inp
 data3 = requests.get(iurl3).text
 if errorred in data3:
    print('reddit - ' + iurl3)


 iurl4 = 'https://www.roblox.com/user.aspx?username=' + inp
 data4 = requests.get(iurl4).text 
 if not errorinsta in data4:
    print('roblox - ' + iurl4)

 iurl5 = 'https://t.me/' + inp
 data5 = requests.get(iurl5).text
 if errorinsta in data5:
    print('telegram - ' + iurl5)



        
    
    
    








