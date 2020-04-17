import pyaudio
import speech_recognition as sr
import pyautogui as pg

#pg.FAILSAFE = False

       
def function(source):
    audio = r.listen(source)
    user = r.recognize_google(audio)
    print(user)
    if user == "jump":
        print("jumped")
        pg.press("space")
    elif user == "dunk":
        print("escaped")
        pg.press("down")
    elif user == "start":
        pg.press("space")
    else :
        print("towards death")
        
        
if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            function(source)
            