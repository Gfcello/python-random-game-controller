
#Code to play games, text ppl, etc.

import keyboard
import random
import time

exit = False
print('3')
time.sleep(1)
print('2')
time.sleep(1)
print('1')
time.sleep(1)
while (exit == False):
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

    exit = keyboard.is_pressed('esc')