import speech_recognition as sr  # recognise speech
import playsound  # to play an audio file
from gtts import gTTS  # google text to speech
import random
from time import ctime  # get time details
import webbrowser  # open browser
import ssl
import certifi
import time
import os  # to remove created audio files
import colorama
import sys
import pyttsx3 as p
voice_data = ''


class person:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


r = sr.Recognizer()
# listen for audio and convert it to text:


def get_text():
    voice_data = input("Enter your responce:  ")
    return voice_data


def record_audio(ask=False):
    with sr.Microphone() as source:  # microphone
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error
            speak('What was that')
        except sr.RequestError:
            speak('Sorry, the service is down')
        print(f">> {voice_data.lower()}")  # print what user said
        return voice_data.lower()


def speak(audio_string):
    # tts = gTTS(text=audio_string, lang='en')  # text to speech
    # print(f"Friday: {audio_string}")
    # r = random.randint(1, 20000000)
    # audio_file = 'audio' + str(r) + '.mp3'
    # tts.save(audio_file)  # save as mp3
    # playsound.playsound(audio_file)  # play the audio file
    # os.remove(audio_file)  # remove audio file
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print(f"Friday: {audio_string}")
    engine.say(audio_string)
    engine.runAndWait()


def respond(voice_data):
    i = 1
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello', 'sup']):
        i = 0
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}",
                     f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings)-1)]
        speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        i = 0
        if person_obj.name:
            speak("my name is Friday")
        else:
            speak("my name is Friday. what's your name?")

    if there_exists(["my name is"]):
        i = 0
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name)

    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        i = 0
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        i = 0
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = f'{hours} {minutes}'
        speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        i = 0
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')

    # 6: search youtube
    if there_exists(["youtube"]):
        i = 0
        search_term = voice_data.split("for")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')

    if there_exists(["exit", "quit", "goodbye"]):
        i = 0
        speak("Okay goodbye")
        exit()

    if i == 1:
        i = 0
        print("Invalid Command")


person_obj = person()
while(1):
    voice_data = get_text().lower()
    respond(voice_data)


if __name__ == '__main__':
    if sys.version_info[0] != 3:
        print("Sorry! Only Python 3 supported.")
