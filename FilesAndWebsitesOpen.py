from importlib.metadata import files
import pyttsx3
import datetime
import os
import webbrowser

#wishme():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    talk = pyttsx3.init()
    print("good morning")
    talk.say("good morning")
    print("Current date and time is:")
    talk.say("Current date and time is:")
    now = datetime.datetime.now()
    from datetime import date
    print(date.today())
    talk.say(date.today())
    talk.say("and")
    print(now.strftime("%H:%M:%S"))    
    talk.say(now.strftime("%H:%M:%S"))
    print("Hello sir, how may i help you")
    talk.say("Hello sir, how may i help you")
    talk.runAndWait()

elif hour>=12 and hour<18:
    talk = pyttsx3.init()
    talk.say("good afternoon")
    print("good afternoon, Hello sir, how may i help you")
    talk.say("Hello sir, how may i help you")
    talk.runAndWait()

else:
    talk = pyttsx3.init()
    talk.say("good evening")
    print("good evening, Hello sir, how may i help you")
    talk.say("Hello sir, how may i help you")
    talk.runAndWait()
talk = pyttsx3.init()
print("in this version you have only two options sir")
talk.say("in this version, you have only two options sir")
print("you can open any file, in your drive, E and F,open a website")
talk.say("you can open any file, in your drive, E and F, or open a website")
talk.runAndWait()


def web():
    talk = pyttsx3.init()
    talk.say("enter your web address")
    talk.runAndWait()
    print("which website do you want to open sir")
    talk = pyttsx3.init()
    talk.say("which web site do you want to open sir")
    talk.runAndWait()
    wanttoopen = input()
    print('opening ' +wanttoopen)
    talk = pyttsx3.init()
    talk.say('opening')
    talk.say(wanttoopen)
    talk.runAndWait()
    webbrowser.open(wanttoopen)
    all()
            
def file():
    talk = pyttsx3.init()
    talk.say("enter your file name")
    talk.runAndWait()
    searchfile = input("enter your file name(ex:- file.mp4): ")
    Dir = "E:\\"
    Dir1 = "F:\\"
    
    for relPath,dirs,files in os.walk(Dir):
        if (searchfile in files):
            fullpath = os.path.join(Dir,relPath,searchfile)
            print(fullpath)
            print("opening")
            talk = pyttsx3.init()
            talk.say("opening")
            talk.runAndWait()
            os.startfile(fullpath)
            all()

    for relPath,dirs,files in os.walk(Dir1):
        if (searchfile in files):
            fullpath = os.path.join(Dir1,relPath,searchfile)
            print(fullpath)
            print("opening")
            talk = pyttsx3.init()
            talk.say("opening")
            talk.runAndWait()
            os.startfile(fullpath)
            all()
        else:
            print("file not found")
            all()

          

def all():
    print ("1.a website")
    print ("2.a file")
    iwo1 =  input("what do you want to open? : ")
    iwo = iwo1.lower()
    if iwo == 'a website':
        web()
    elif iwo == 'a file':
        file()

all()