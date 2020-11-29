sec = 3
print('spam code will start in '+str(sec)+' seconds')
import pynput
from pynput.keyboard import Key, Controller
import time
Keyboard = Controller()
time.sleep(sec)
a = 1
control = True
while control:
    b = str(a)
    # its loop limit
    if a == 6:
        break
    for x in 'spam bot yaptım':
        Keyboard.press(x)
        Keyboard.release(x)
    a+=1
    time.sleep(0.5)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

