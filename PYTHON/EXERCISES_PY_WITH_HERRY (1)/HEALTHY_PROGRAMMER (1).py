# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio


from _datetime import datetime
from pygame import mixer
from time import time


def musicOnLoop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True :
        a=input()
        if a==stopper:
            mixer.music.stop()
            break


def logTxt(text):
    with open('logs.txt','a')as f:
        f.write(f"{text} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    waterTime = 30*60
    eyeTime = 40*60
    exerciseTime = 60*60

    while True:
        if time() - init_water > waterTime:
            print("Time to drink water! \nEnter (drank) to stop alarm.")
            musicOnLoop('water.mp3','drank')
            logTxt("Drank water at: ")
            init_water = time()

        if time() - init_eyes > eyeTime:
            print("Time to eye exercise! \nEnter (doneEye) to stop alarm.")
            musicOnLoop('eye.mp3', 'doneEye')
            logTxt("Eye exercise done at: ")
            init_eyes = time()

        if time() - init_exercise > exerciseTime:
            print("Time to exercise! \nEnter (donePhy) to stop alarm.")
            musicOnLoop('exercise.mp3', 'donePhy')
            logTxt("Physical exercise done at: ")
            init_exercise = time()


