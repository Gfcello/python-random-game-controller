from PIL import ImageGrab
import keyboard
import random
import time
import sys

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

BATTLE_MENU_X = 1680
BATTLE_MENU_Y = 733
BATTLE_ACTIVE = (248, 248, 248)

HEALTH_X = 1290
HEALTH_Y = 613

used_keys = [
    'w', 'a', 's', 'd', 'x', 'z', 'enter'
]

def get_img():
    img = ImageGrab.grab(bbox=None, include_layered_windows=False, \
                             all_screens=False, xdisplay=None)
    px = img.load()
    return px

def check_state():
    img = get_img()
    state = "walk"
    if img[BATTLE_MENU_X, BATTLE_MENU_Y] == BATTLE_ACTIVE:
        health_px = img[HEALTH_X, HEALTH_Y]
        if health_px[1] > 200:
            state = "battle"
        else:
            state = "run"
                
    return state

def battle():
    # Exit out of any menu game is currently in
    keyboard.press('x')
    time.sleep(0.2)
    release_all()

    # Move to option
    keyboard.press('w')
    time.sleep(0.2)
    keyboard.press('a')
    time.sleep(0.2)
    release_all()

    keyboard.press('z')
    time.sleep(0.2)
    release_all()
    
    move = random.randint(1, 4)
    if move == 1:
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.press('a')

    elif move == 2:
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.press('d')
        
    elif move == 3:
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.press('a')

    else:
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.press('d')

    time.sleep(0.2)
    release_all()

    keyboard.press('z')
    time.sleep(0.2)
    release_all()

def switch_pokemon():
    # Exit out of any menu game is currently in
    keyboard.press('x')
    time.sleep(0.2)
    release_all()

    # Move to option
    keyboard.press('s')
    time.sleep(0.2)
    keyboard.press('a')
    time.sleep(0.2)
    release_all()

    keyboard.press('z')
    time.sleep(0.2)
    release_all()
    
    pokemon = random.randint(0, 5)
    for i in range(pokemon):
        keyboard.press('s')
        time.sleep(0.2)
        release_all()
        
    time.sleep(0.2)
    
    keyboard.press('z')
    time.sleep(0.2)
    release_all()

    time.sleep(0.2)

    keyboard.press('z')
    time.sleep(0.2)
    release_all()

def run():
    # Exit out of any menu game is currently in
    keyboard.press('x')
    time.sleep(0.2)
    release_all()

    coin = random.randint(0, 9)

    if coin > 0:
        switch_pokemon()
    else:
        # Escape
        # Move to option
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.press('d')
        time.sleep(0.2)
        release_all()

        keyboard.press('z')
        time.sleep(0.2)
        release_all()

def walk():
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
        else:
            state = check_state()
            if state == "battle":
                battle()
            elif state == "run":
                run()
            else:
                walk()

if __name__ == '__main__':
    main()