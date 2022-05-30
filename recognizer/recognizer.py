import speech_recognition as sr
import sys

# filename = sys.argv[1]

# initialize the recognizer
r = sr.Recognizer()

edison = sr.WavFile("manson_devil.wav")
with edison as source:
    #load audio ke memori
    audio = r.record(source)
    type(audio)
try:
    #me recognize dari speech ke text
    print("Transkripsi: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Tidak bisa menerjemahkan audio")


