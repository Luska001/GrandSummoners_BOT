import cv2
import numpy as np
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(5)
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while not keyboard.is_pressed('q'):
    newfase = pyautogui.locateCenterOnScreen('Stars.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    new = pyautogui.locateCenterOnScreen('NEW.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    newMundo = pyautogui.locateCenterOnScreen('newMundo.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    soloplay = pyautogui.locateCenterOnScreen('soloPlay.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    #newfraco = pyautogui.locateCenterOnScreen('NEWfraco.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    #newfog = pyautogui.locateCenterOnScreen('NEWfog.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.70)
    battle = pyautogui.locateCenterOnScreen('Battle.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    oKG = pyautogui.locateCenterOnScreen('OKorange.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    oKB = pyautogui.locateCenterOnScreen('OKblue.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    skip2 = pyautogui.locateCenterOnScreen('skip2.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    skip1 = pyautogui.locateCenterOnScreen('skip.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    next1 = pyautogui.locateCenterOnScreen('Next.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)
    estrela4 = pyautogui.locateCenterOnScreen('Estrela4.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.90)
    estrela5 = pyautogui.locateCenterOnScreen('Estrela5.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.90)
    chat = pyautogui.locateCenterOnScreen('chat.png', region=(0, 0, 1600, 900), grayscale=True, confidence=0.80)


    if newfase is not None:
        pyautogui.moveTo(newfase)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    #elif newfog is not None:
        #cv2.waitKey(5000)
        #pyautogui.moveTo(newfog)  # Moves the mouse to the coordinates of the image
        #click()
        #time.sleep(3)
    elif battle is not None:
        pyautogui.moveTo(battle)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif oKG is not None:
        pyautogui.moveTo(oKG)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif oKB is not None:
        pyautogui.moveTo(oKB)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif skip2 is not None:
        pyautogui.moveTo(skip2)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif skip1 is not None:
        pyautogui.moveTo(skip1)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif next1 is not None:
        pyautogui.moveTo(next1)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif estrela4 is not None:
        pyautogui.moveTo(estrela4)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif estrela5 is not None:
        pyautogui.moveTo(estrela5)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif chat is not None:
        pyautogui.moveTo(chat)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    elif soloplay is not None:
        pyautogui.moveTo(soloplay)  # Moves the mouse to the coordinates of the image
        click()
        time.sleep(2)
    else:
        if new is not None:
            time.sleep(5)
            pyautogui.moveTo(new)  # Moves the mouse to the coordinates of the image
            click()
            time.sleep(4)
        elif newMundo is not None:
            time.sleep(5)
            pyautogui.moveTo(newMundo)  # Moves the mouse to the coordinates of the image
            click()
            time.sleep(4)


        


    
