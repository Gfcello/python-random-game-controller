from PIL import ImageGrab
import keyboard
import random
import time
import sys

BATTLE_MENU_X = 1680/1920
BATTLE_MENU_Y = 733/1080
BATTLE_ACTIVE = (248, 248, 248)

HEALTH_X = 1290/1920
HEALTH_Y = 613/1080

used_keys = [
    'w', 'a', 's', 'd', 'x', 'z', 'enter'
]

def get_img():
    img = ImageGrab.grab(bbox=None, include_layered_windows=False, \
                             all_screens=False, xdisplay=None)
    return img

def check_state():
    img = get_img()
    pix = img.load()
    state = "walk"
    if pix[BATTLE_MENU_X * img.size[0], BATTLE_MENU_Y * img.size[1]] == BATTLE_ACTIVE:
        health_px = pix[HEALTH_X * img.size[0], HEALTH_Y * img.size[1]]
        if health_px[1] > 200:
            state = "battle"
        else:
            state = "run"
                
    return state

def exit_menu():
    keyboard.press('x')
    time.sleep(0.2)
    release_all()

def battle():
    exit_menu()

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
    exit_menu()

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
    exit_menu()

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
    elif randInt < 150:
        keyboard.press('x')
    elif randInt < 200:
        keyboard.press('w')
    elif randInt < 250:
        keyboard.press('a')
    elif randInt < 300:
        keyboard.press('s')
    elif randInt < 350:
        keyboard.press('d')
    else:
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