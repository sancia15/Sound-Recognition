import speech_recognition as sr
import time

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Recording........")
    r.adjust_for_ambient_noise(source, duration = 1)#Checks external noise
    #audio=r.listen(source,offset =4 ,duration = 4)
    audio=r.listen(source)
    print("Recording time:", time.strftime("%H:%M:%S:%A:%B:%Y"))

try:
    text=r.recognize_google(audio)
    print("Text converted from audio:" + text)
    print("Execution time:", time.strftime("%H:%M:%S:%A:%B:%Y"))

except:
    print("Error")
