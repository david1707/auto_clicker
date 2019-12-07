import pyautogui
import keyboard
import time

clicker_active = False

try:
    while True:

        if clicker_active:
            pyautogui.click()

        if keyboard.is_pressed('q'):
            print('Stopping the script')
            break

        if keyboard.is_pressed('x') and clicker_active:
            clicker_active = False
            print('Stopping the clicker')

        elif keyboard.is_pressed('c') and not clicker_active:
            print('Starting the clicker')
            clicker_active = True


except KeyboardInterrupt:
    print('Script stopped by the user')
