
#Code to play games, text ppl, etc.

import keyboard
import random
import time

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

exit = False
print('5')
time.sleep(1)
print('4')
time.sleep(1)
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
while (exit == False):
    
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

    exit = keyboard.is_pressed('esc')

release_all()
