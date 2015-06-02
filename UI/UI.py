# -*- coding: utf-8 -*-

# -- cmd -- pip install PyUserInput

import time
import win32gui
import win32con
import ImageGrab
from pymouse import PyMouse

PIECE_X = 44
PIECE_Y = 40
NUM_X = 14
NUM_Y = 10

def getOrigin():
    cwllk = '宠物连连看'.decode('utf8')
    hwnd = win32gui.FindWindow("#32770", cwllk)
    print hwnd
    
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32gui.SetForegroundWindow(hwnd)
    rect = win32gui.GetWindowRect(hwnd)
    time.sleep(0.5)
    print rect
    
    newRect = (rect[0] + 58, rect[1] + 104, rect[0] + 674, rect[1] + 504)
    
    return newRect

RECT = getOrigin()

def getPic():
    pic = ImageGrab.grab(RECT)
    return pic

def pause():
    m = PyMouse()
    m.click(RECT[0] -58 + 307, RECT[1] - 104 + 62)
    time.sleep(0.5)

def click(pos):
    '''
    pos: (x, y) # (0, 0) for top left piece
    '''
    m = PyMouse()
    m.click(RECT[0] + PIECE_X / 2 + PIECE_X * pos[0], RECT[1] + PIECE_Y / 2 + PIECE_Y * pos[1])
    time.sleep(0.5)

'''
# only for test

pic = getPic()
pic.save(time.strftime("%y%m%d%H%M%S") + ".png")

click((0,0))
click((0,9))
click((13,9))
click((13,0))

pause()
'''
