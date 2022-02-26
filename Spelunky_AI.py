import keyboard
import random
import time
import sys

def release_all():
    keyboard.release('i')
    keyboard.release('j')
    keyboard.release('k')
    keyboard.release('l')
    keyboard.release('x')
    keyboard.release('z')
    keyboard.release('s')
    keyboard.release('a')
    keyboard.release('space')

print('Press Space to begin')
keyboard.wait("space")

while (True):
    if keyboard.is_pressed('Esc'):
            print("Exiting...")
            release_all()
            sys.exit(0)

    # First key press
    randInt = random.randint(0, 100)
    if(randInt < 10):
        keyboard.press('i')
    elif randInt < 20 :
        keyboard.press('j')
    elif randInt < 30 :
        keyboard.press('k')
    elif randInt < 40 :
        keyboard.press('l')
    elif randInt < 60 :
        keyboard.press('x')
    elif randInt < 80 :
        keyboard.press('z')
    elif randInt < 82 :
        keyboard.press('s')
    elif randInt < 85 :
        keyboard.press('a')
    else :
        keyboard.press('space')

    # Second key press
    randInt = random.randint(0, 100)
    if(randInt < 10):
        keyboard.press('i')
    elif randInt < 20 :
        keyboard.press('j')
    elif randInt < 30 :
        keyboard.press('k')
    elif randInt < 40 :
        keyboard.press('l')
    elif randInt < 60 :
        keyboard.press('x')
    elif randInt < 80 :
        keyboard.press('z')
    elif randInt < 82 :
        keyboard.press('s')
    elif randInt < 85 :
        keyboard.press('a')
    else :
        keyboard.press('space')

    time.sleep(0.1)

    release_all()
