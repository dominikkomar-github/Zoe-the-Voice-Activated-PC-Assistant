from __future__ import print_function
import datetime
import pickle
import os.path
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import webbrowser
import pyautogui


def speak(text):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("rate", 180)
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()
    del(text) #to make it faster

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()


wake = "zoe"
print("start")

while True:
    print("listening")
    text = get_audio()
    if text.count(wake) > 0:
        speak("yes?")
        text = get_audio()

        if "show me news" in text.lower():
            speak("what news would you like? Everyday news, Sports news, Technology news, Music news or Stock news?")
            text = get_audio()
            if "everyday news" in text.lower():
                speak ("opening everyday news from bbc news")
                url = "https://www.bbc.co.uk/news"
                webbrowser.get().open(url)

            elif "sports news" in text.lower():
                speak ("opening sport news from bbc news")
                url = "https://www.bbc.co.uk/sport"
                webbrowser.get().open(url)

            elif "technology news" in text.lower():
                speak ("opening technology news from bbc news")
                url = "https://www.bbc.co.uk/news/technology"
                webbrowser.get().open(url)

            elif "music news" in text.lower():
                speak ("opening music news from mtv music news")
                url = "https://www.mtv.com/news/music/"
                webbrowser.get().open(url)

            elif "stock news" in text.lower():
                speak ("opening stock market news from market watch")
                url = "https://www.marketwatch.com/"
                webbrowser.get().open(url)

        elif "make a note" in text.lower():
            date = datetime.datetime.now()
            file_name = str(date).replace(":", "-") + "-note.txt"
            with open(file_name, "w") as f:
                speak("What would you like me to write down?")
                write_down = get_audio()
                f.write(write_down)
                speak("I've made a note of that.")
                subprocess.Popen(["notepad.exe", file_name])

        elif "open youtube" in text.lower():
            speak("opening youtube")
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)

        elif "search on youtube" in text.lower():
            speak("What would you like to search for?")
            search = get_audio()
            keyword = search.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)

        elif "search on google" in text.lower():
            speak("What would you like to search for?")
            search = get_audio()
            keyword = search.split("for")[-1]
            url = f"https://www.google.com/search?q={keyword}"
            webbrowser.get().open(url)

        elif "what's the time" in text.lower():
            now = datetime.datetime.now()
            speak(now.strftime("the time is %I:%M %p"))

        elif "check location" in text.lower():
            speak("What location do you want to check?")
            search = get_audio()
            keyword = search.split("for")[-1]
            url = f"https://www.google.co.uk/maps/search/{keyword}"
            webbrowser.get().open(url)

        elif "navigate" in text.lower():
            speak("Where from?")
            search = get_audio()
            keyword = search.split("for")[-1]
            time.sleep(1)
            speak("To where?")
            search = get_audio()
            keyword2 = search.split("for")[-1]
            url = f"https://www.google.co.uk/maps/dir/{keyword}/{keyword2}"
            webbrowser.get().open(url)

        elif "play my music" in text.lower():
            speak("There u go")
            url = "https://youtu.be/9FPD_yaZvK0"
            webbrowser.get().open(url)
            time.sleep(3)
            pyautogui.click()
            pyautogui.press('space')

        elif "what are the commands" in text.lower():
            speak ("The commands are")
            speak ("Open youtube, Open google, Search youtube, Search google, Make a note, Show me news, Location, Navigation, What's the time, Play my music.")

        else:
            speak ("I'd didn't get that, sorry.")
