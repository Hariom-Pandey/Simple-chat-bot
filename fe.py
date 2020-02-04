''' Author : Hariom Pandey
'''
import random
import time
import re
import datetime
from gtts import gTTS
import os
from pygame import mixer

dict = {":)": "happy", ":'(": "sad", "<3": "romantic", ":/": "unsure", ":*": "kiss", "o.O": "confused", ">:O": "upset",
        "(y)": "Like"}
mood_che = ["happy", "sad", "romantic", "unsure", "kiss", "confused", "upset", "Like"]
mood_list = list(dict.values())

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up", "hey", "namaste")
GREETING_RESPONSES = ["Yo!", "hey", "hi", "hello", ]
qask = ["what about You", "how are you"]

moodq = ["happy", "nice", "good", "awesome", "fine"]
moodr = ["Oh! thats very good", "I am also like you", "good thing"]
moods = ["sad", "bad", "very sad", "not good"]

ownerq = ["who made you", "who is you owner", "who is your head", "to whom you belong"]
ownera = ["My lord", "My lord is your friend", "Your friend", "He is like you only", "A person like you"]

laughq = ["laugh", "joke"]
nameq = ["call me", "my name is"]
dateq = ["date", "time"]


def sad(sd):
    for i in range(0, 3):
        if sd == mood_che[i]:
            print("Why?", " ", "How can I Help?")
            onj = gTTS(text="How can I Help?", lang='en', slow=False)
            onj.save("dd.mp3")
            mixer.init()
            mixer.music.load('dd.mp3')
            mixer.music.play()
        elif sd == moodq[i]:
            print("nice", " ", "How can I Help?")
            onj = gTTS(text="nice How can I Help?", lang='en', slow=False)
            onj.save("dd.mp3")
            mixer.init()
            mixer.music.load('dd.mp3')
            mixer.music.play()


def check_for_greeting(sentence):
    for i in dict:
        if sentence in dict.keys():
            val2 = dict[sentence]
            print("You are in", val2, "mood")
            onj = gTTS(text="You are in " + val2 + "mood", lang='en', slow=False)
            onj.save("mood_q.mp3")
            mixer.init()
            mixer.music.load('mood_q.mp3')
            mixer.music.play()
            sad(val2)
            break

    for i in range(0, 7):

        if GREETING_KEYWORDS[i] in sentence:
            print(random.choice(GREETING_RESPONSES))
            print("How are you?")
            onj = gTTS(text=random.choice(GREETING_RESPONSES) + "How are you", lang='en', slow=False)
            onj.save("md.mp3")
            mixer.init()
            mixer.music.load('md.mp3')
            mixer.music.play()

    for i in range(0, 5):
        if moodq[i] in sentence:
            print("Now, What you want me to do")
            onj = gTTS(text=random.choice(moodr) + "It would be great to talk with you" + "Now, What you want me to do",
                       lang='en', slow=False)
            onj.save("kd.mp3")
            mixer.init()
            mixer.music.load('kd.mp3')
            mixer.music.play()

    for i in range(0, 3):
        if sentence == moods[i]:
            print("Why?", " ", "How can I Help?")
            onj = gTTS(text="Why? How can I Help?", lang='en', slow=False)
            onj.save("dd.mp3")
            mixer.init()
            mixer.music.load('dd.mp3')
            mixer.music.play()

    if sentence == "sing a song":
        print("Which types of song you want?")
        onj = gTTS(text="Which types of song you want?", lang='en', slow=False)
        onj.save("jd.mp3")
        mixer.init()
        mixer.music.load('jd.mp3')
        mixer.music.play()
        j = input()
        if "hindi" in j:
            print("You should go for Saavn.com or Gaana.com")
            onj = gTTS(text="You should go for Saavn.com or Gaana.com", lang='en', slow=False)
            onj.save("pd.mp3")
            mixer.init()
            mixer.music.load('pd.mp3')
            mixer.music.play()
        elif "punjabi" in j:
            print("You should go for djpunjab.com or pagaljatt.com")
            onj = gTTS(text="You shound go for djpunjab.com or pagaljatt.com", lang='en', slow=False)
            onj.save("cd.mp3")
            mixer.init()
            mixer.music.load('cd.mp3')
            mixer.music.play()
        elif "english" in j:
            print("You should go for google only I am an Indian")
            onj = gTTS(text="You should go for google only I am an Indian", lang='en', slow=False)
            onj.save("gd.mp3")
            mixer.init()
            mixer.music.load('gd.mp3')
            mixer.music.play()

        else:
            print("Search it on google", "\r", "I know about only english, hindi, punjabi")
            onj = gTTS(text="Search it on google  know about only english, hindi, punjabi", lang='en', slow=False)
            onj.save("dd.mp3")
            mixer.init()
            mixer.music.load('dd.mp3')
            mixer.music.play()

    for i in range(0, 4):
        if sentence == ownerq[i]:
            print(random.choice(ownera))
            print("His Name is: Hariom Pandey")
            print("My lord mail is: .com", "\n")
            print("His contact number is: ", "\n")
            onj = gTTS(text=(random.choice(ownera)) + "His Name is: Hariom Pandey", lang='en', slow=False)
            onj.save("hd.mp3")
            mixer.init()
            mixer.music.load('hd.mp3')
            mixer.music.play()

    for i in range(0, 2):
        if laughq[i] in sentence:
            print(random.choice(laugha))

    for i in range(0, 2):
        if dateq[i] in sentence:
            now = datetime.datetime.now()
            print("Current date and time: ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))


while (True):
    i = input()
    check_for_greeting(i)

# print("Hello")
