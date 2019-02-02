import pyaudio
import wave
import speech_recognition as sr
import os
from gtts import gTTS
from detect_face import capture

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)            # use "test.wav" as the audio source
    audio = r.listen(source)
try:
    tells=r.recognize_google(audio)
    print(tells)
    test=tells.lower()
    test2="open"
    #print(test2)
    to_compare=test2.lower()
    #print(to_compare)
    if to_compare in test:
        #print("k")
        mytext = 'Please come in front of the camera and hold still'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("respond.mp3")
        os.system("mpg321 respond.mp3")
        os.remove("respond.mp3")
        capture()
except sr.UnknownValueError:
        mytext = 'Sorry could not understand '
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("respond.mp3")
        os.system("mpg321 respond.mp3")
        os.remove("respond.mp3")
