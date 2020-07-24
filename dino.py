import pyautogui #pip install pyautogui
from PIL import Image, ImageGrab #pip install pillow
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # for birdy
    for i in range(180, 215):
        for j in range(205, 335):
            if data[i, j] < 100:
                hit("down")
                return 


    for i in range(215, 290):
        for j in range(335, 420):
            if data[i, j] < 100:
                hit("up")
                return 
    return 

if __name__ == "__main__":
    print("Hey.. Dino game is about to start in 3..2..1..")
    time.sleep(3)
#    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
            
    #     print(asarray(image))
'''
        # for cactus
            for i in range(202, 293):
                for j in range(335, 440):
                    data[i, j] = 0
                    
        # for birdy
            for i in range(202, 293):
                for j in range(205, 335):
                    data[i, j] = 171


    image.show()
''' 
    
    

