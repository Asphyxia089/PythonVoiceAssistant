import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

count = 0

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Спрашивай")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("Говорите")
        global count
        count += 1
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(s, duration=1)
        audio = r.listen(s)

    if count == 4:
        talk("Вы превысили максимальное количество попыток")
        sys.exit()

    try:
        voice = r.recognize_google(audio, language = "ru-RU").lower()
        print("Вы сказали: " + voice)
    except sr.UnknownValueError:
        talk("Повторите")
        voice = command()


    return voice

def makeSomething(voice):
    if "открой ютуб" in voice:
        talk("Открываю ютуб")
        url = "https://www.youtube.com/"
        webbrowser.open(url)
    elif "стоп" in voice:
        sys.exit()
    elif "открой youtube" in voice:
        talk("Открываю youtube")
        url = "https://www.youtube.com/"
        webbrowser.open(url)
    elif "включи super idol" in voice:
        talk("Открываю 'super idol' ")
        os.system(r"C:\Users\Admin\PycharmProjects\main\superidol.mp4")

while True:
    makeSomething(command())