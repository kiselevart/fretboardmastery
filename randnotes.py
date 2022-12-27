import random
import time
from gtts import gTTS
import os

notes = ["Ab","A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G", "G#"]
prev = 0
rand = 0

while True:

    if len(notes) == 0:
        stat = int(input("Congratulations! You've found every note! Enter 1 to continue practicing, 0 to exit."))
        if stat == 0:
            break
        else:
            notes = ["Ab","A","A#","Bb","B","C","C#","Db","D","D#","Eb","E","F","F#","Gb","G", "G#"]

    while prev == rand:
        rand = random.randint(0, len(notes)-1)
    prev = rand
    mytext = notes[rand]
    print(f"{mytext}")

    tts = gTTS(text = f"{mytext}", lang = "en", slow = False)
    tts.save("tts.mp3")

    os.system("start tts.mp3")
    time.sleep(0.2)

    for x in range(len(notes)):
        if notes[x] == mytext:
            notes.remove(mytext)
            break
    print(notes)
    

    