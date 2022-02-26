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

    randInt = random.randint(0, 360)
    if(randInt < 100):
        keyboard.press('z')
        time.sleep(0.2)
        keyboard.release('z')
    elif randInt < 150 :
        keyboard.press('x')
        time.sleep(0.2)
        keyboard.release('x')
    elif randInt < 200 :
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')
    elif randInt < 250 :
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
    elif randInt < 300 :
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
    elif randInt < 350 :
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
    else :
        keyboard.press('enter')
        time.sleep(0.2)
        keyboard.release('enter')
    time.sleep(0.01)
