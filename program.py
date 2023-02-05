from pynput import keyboard
from time import sleep
import pyautogui as r

name = 'Imagen'
sys = print
num = 1

def keylogger_(function_):
    keylogger_array = []

    def on_press(key): 
        if key == keyboard.Key.esc:
            return False
        
        try: k = key.char
        except: k = key.name

        keylogger_array.append(str(k))

        if k == '1': function_()
        if k == '0': return False
        
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    print(keylogger_array)

def screenShot(): 
    global name, num
    img = r.screenshot()

    img.save(
        r'C:/Users/%USERNAME%/Pictures/{0}{1}.png'.format(
            name, num
        )
    )

    sys(f'\n [+] Capture saved as: {name}{num}.png...')
    num += 1

def main(): 
    sys('\n [+] Press 1 to take a screenshot...')
    keylogger_(screenShot)

if __name__ == '__main__':
    main()
    
# Author: Francisco Velez
