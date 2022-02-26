import keyboard
import random
import time
import sys

print('Press Space to begin')
keyboard.wait("space")

while (True):
    if keyboard.is_pressed('Esc'):
            print("Exiting...")
            sys.exit(0)

    # Generate Int for Decision Making
    randInt = random.randint(0, 181)
    # Lowercase Letter Inputs
    if randInt < 52 :
        randInt = randInt % 26
        if randInt == 7 : # Keys to avoid (history)
            randInt = randInt + 1
        key = ord('a') + randInt
        keyboard.press(chr(key))
        time.sleep(0.1)
        keyboard.release(chr(key))
    # Uppercase Letter Inputs
    elif randInt < 104 :
        randInt = randInt % 26
        if randInt == 14 or randInt == 18 or randInt == 21: # Keys to avoid (save, options)
            randInt = randInt + 1
        key = ord('a') + randInt
        keyboard.press('shift')
        keyboard.press(chr(key))
        time.sleep(0.1)
        keyboard.release('shift')
        keyboard.release(chr(key))
    # Directions (numbers)
    elif randInt < 154 :
        randInt = randInt % 10 #Doesn't put them in order, but gets 0-9 at 5 randInt chances
        key = ord('0') + randInt
        keyboard.press(chr(key))
        time.sleep(0.1)
        keyboard.release(chr(key))
    # Exit Menus
    elif randInt < 169 :
        keyboard.press('space')
        time.sleep(0.1)
        keyboard.release('space')
    # Pick up Item
    elif randInt < 174 :
        keyboard.press(',')
        time.sleep(0.1)
        keyboard.release(',')
    # Direction at Self
    elif randInt < 176 :
        keyboard.press('.')
        time.sleep(0.1)
        keyboard.release('.')
    else :
        keyboard.press('enter')
        time.sleep(0.1)
        keyboard.release('enter')
    time.sleep(0.01)
