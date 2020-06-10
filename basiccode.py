import speech_recognition as sr
import time
from time import ctime

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Recording........")
    r.adjust_for_ambient_noise(source, duration = 1)#Checks external noise
    #audio=r.listen(source,offset =4 ,duration = 4)
    audio=r.listen(source)
    print("Recording time:", ctime())

try:
    text=r.recognize_google(audio)
    print("Text converted from audio:" + text)
    print("Execution time:", ctime())

except:
    print("Error")
