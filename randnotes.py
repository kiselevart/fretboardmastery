import random
import time
import keyboard
from gtts import gTTS
import os

notes = ["Ab","A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G", "G#"]
value = len(notes)
count = 0
prev = 0
rand = 0

while True:

    while prev == rand:
        rand = random.randint(1,value-1)
    prev = rand
    mytext = notes[rand]
    print(f"{mytext}")

    tts = gTTS(text = f"{mytext}", lang = "en", slow = False)
    tts.save("tts.mp3")

    os.system("start tts.mp3")
    time.sleep(2)
    count+=1

    if keyboard.is_pressed("enter"):
        print(f"You practiced {count} times")
        time.sleep(10)
        break