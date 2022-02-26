import keyboard
import random
import time
import sys

used_keys = [
    'w', 'a', 's', 'd', 'x', 'z', 'enter'
]

def release_all():
    for key in used_keys:
        keyboard.release(key)

def main():
    print('Press Space to begin')
    keyboard.wait("space")

    while (True):
        if keyboard.is_pressed('Esc'):
                print("Exiting...")
                release_all()
                sys.exit(0)

        randInt = random.randint(0, 360)
        if(randInt < 100):
            keyboard.press('z')
        elif randInt < 150 :
            keyboard.press('x')
        elif randInt < 200 :
            keyboard.press('w')
        elif randInt < 250 :
            keyboard.press('a')
        elif randInt < 300 :
            keyboard.press('s')
        elif randInt < 350 :
            keyboard.press('d')
        else :
            keyboard.press('enter')
        time.sleep(0.2)
        release_all()

if __name__ == '__main__':
    main()