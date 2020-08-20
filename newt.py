import pyttsx3 
import os

#pyttsx3.speak('welcome to your program')
print('.......welcom.....')
pyttsx3.speak('how can help')
pyttsx3.speak('write below')

while True:
  p=input('>>')
  if (('open' in p) or ('run' in p)or('start' in p) ) and (('chrome' in p)or('browser' in p)):
        os.system('chrome')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('spotify' in p)or('music' in p)): 
        os.system('spotify')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('whatsapp' in p)or('message' in p)): 
        os.system('whatsapp')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('vlc' in p)or('media' in p)): 
        os.system('VlC')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('editor' in p)or('notepad' in p)): 
        os.system('notepad++')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('media' in p)or('player' in p)): 
        os.system('wmplayer')
  elif (('open' in p) or ('run' in p)or('start' in p)) and (('settings' in p)or('control panel' in p)): 
        os.system('control panel')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('google' in p)or('search engeine' in p)):     
        os.system('chrome google.com')    
  elif (('open' in p) or ('run' in p)or('start' in p) ) and ('linkedin' in p): 
        os.system('chrome linkedin.com')   
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('facebook' in p)or('socialmedia' in p)): 
        os.system('chrome facebook.com')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('google' in p)or('search engeine' in p)): 
        os.system('chrome google')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and ('youtube' in p): 
        os.system('chrome youtube.com')
  elif (('open' in p) or ('run' in p)or('start' in p) ) and (('gmail' in p)or('mail' in p)): 
        os.system('chrome gmail.com')
  else: 
     pyttsx3.speak("i cannot understand")




