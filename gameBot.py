# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import ImageGrab, ImageOps
import os
import time
import win32api, win32con
from numpy import *

class base:
    x = 89
    y = 165

class values:
    bo = 823
    op = 568
    n1 = 597
    n2 = 640
    n3 = 644
    n4 = 582
    n5 = 604
    n6 = 654
    fg = 899
    x  = 710
    
def printValues(num):
    if num == values.bo:
        print('b', end = '')
    elif num == values.op:
        print('o', end = '')
    elif num == values.n1:
        print('1', end = '')
    elif num == values.n2:
        print('2', end = '')
    elif num == values.n3:
        print('3', end = '')
    elif num == values.n4:
        print('4', end = '')
    elif num == values.n5:
        print('5', end = '')
    elif num == values.fg:
        print('f', end = '')
    


position = []
percentage = []
#posForOne = []
flag = False

def leftClick(pos):
    pose = (base.x + pos[1]*16 + 5, base.y + pos[0]*16 + 5)
    win32api.SetCursorPos(pose)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ("Left Click.")
    #time.sleep(1)
    
def rightClick(pos):
    pose = (base.x + pos[1]*16 + 5, base.y + pos[0]*16 + 5)
    win32api.SetCursorPos(pose)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    print ("Right Click.")
    #time.sleep(1)

def imageGG():
    global grayImage
    grayImage = ImageGrab.grab()
    image = ImageOps.grayscale(grayImage)
    grayImage = image
    
def getImage(pos):
    image = grayImage.crop((pos[0], pos[1], pos[0] + 16, pos[1] + 16))
    gImage = ImageOps.grayscale(image)
    a = array(gImage.getcolors())
    ap = a.sum()
    return ap

def screenGrab():
    global position
    position = []
    for i in range(16):
        temp = []
        for j in range(30):
            a = getImage((base.x + j*16, base.y + i*16))
            #print(a, 'i = ', i, 'j = ', j)
            temp.append(a)
        position.append(temp)
    position

def checkOne():
    print('Check One--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n1:
                k = 0
                pos = ()
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k = -1
                            break
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k += 1
                            pos = (i - 1 + p1, j - 1 + p2)
                    if k == -1:
                        break
                if k == 1:
                    print(pos)
                    rightClick(pos)
                    imageGG()
                    screenGrab()
                    #printGrid(position)
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n1:
                #print('n1 i = ', i, ' j = ', j)
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if p1 == 1 and p2 == 1:
                        #    continue
                        #print('yy p1 = ', p1, ' p2 = ', p2)
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            #print('yyi = ', i, ' j = ', j)
                            continue
                        #print('i = ', i, ' j = ', j)
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k = 1
                            #print(k)
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                            #print(pos)
                if k == 1:
                    #print(pos)
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                
def checkTwo():
    print('Check Two--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n2:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if (k1 == 2 and k2 == 0) or (k2 == -1 and k1 == 1):
                    for i in range(len(pos)):
                        print(pos[i])
                        rightClick(pos[i])
                        imageGG()
                        screenGrab()
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n2:
                #print('n1 i = ', i, ' j = ', j)
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        if p1 == 1 and p2 == 1:
                            continue
                        #print('yy p1 = ', p1, ' p2 = ', p2)
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            #print('yyi = ', i, ' j = ', j)
                            continue
                        #print('i = ', i, ' j = ', j)
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k += 1
                            #print(k)
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                            #print(pos)
                if k == 2:
                    #print(pos)
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                
def checkThree():
    print('Check Three--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n3:
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if (k1 == 3 and k2 == 0) or (k2 == -1 and k1 == 2) or (k2 == -2 and k1 == 1):
                    for i in range(len(pos)):
                        print(pos[i])
                        rightClick(pos[i])
                        imageGG()
                        screenGrab()
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n3:
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k += 1
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k == 3:
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                        
def checkFour():
    print('Check Four--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n4:
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if (k1 == 4 and k2 == 0) or (k2 == -1 and k1 == 3) or (k2 == -2 and k1 == 2) or (k2 == -3 and k1 == 1):
                    for i in range(len(pos)):
                        print(pos[i])
                        rightClick(pos[i])
                        imageGG()
                        screenGrab()
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n4:
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k += 1
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k == 4:
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                        
def checkFive():
    print('Check Five--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n5:
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if (k1 == 5 and k2 == 0) or (k2 == -1 and k1 == 4) or (k2 == -2 and k1 == 3) or (k2 == -3 and k1 == 2) or (k2 == -4 and k1 == 1):
                    for i in range(len(pos)):
                        print(pos[i])
                        rightClick(pos[i])
                        imageGG()
                        screenGrab()
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n5:
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k += 1
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k == 5:
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                        
def checkSix():
    print('Check Six--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n6:
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if (k1 == 6 and k2 == 0) or (k2 == -1 and k1 == 5) or (k2 == -2 and k1 == 4) or (k2 == -3 and k1 == 3) or (k2 == -4 and k1 == 2) or (k2 == -5 and k1 == 1):
                    for i in range(len(pos)):
                        print(pos[i])
                        rightClick(pos[i])
                        imageGG()
                        screenGrab()
                    
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n6:
                pos = []
                k = 0
                for p1 in range(3):
                    for p2 in range(3):
                        
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k += 1
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k == 6:
                    for i in range(len(pos)):
                        print(pos[i])
                        leftClick(pos[i])
                        imageGG()
                        screenGrab()
                        #printGrid(position)
                        
                        
def advance():
    global flag
    posForOne = []
    imageGG()
    screenGrab()
    print('Check Advance One--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n1:
                k = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k = -1
                            break
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                    if k == -1:
                        break
                if k >= 1:
                    posForOne.append(pos)
                    
    print('Check Advance Two--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n2:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k2 == -1 and k1 > 1:
                    posForOne.append(pos)
                    
    print('Check Advance Three--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n3:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k2 == -2 and k1 > 1:
                    posForOne.append(pos)
                    
    print('Check Advance Four--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n4:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k2 == -3 and k1 > 1:
                    posForOne.append(pos)
                    
    print('Check Advance Five--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n5:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k2 == -4 and k1 > 1:
                    posForOne.append(pos)
                    
    print('Check Advance Six--------')
    for i in range(16):
        for j in range(30):
            if position[i][j] == values.n6:
                #print('i = ', i, 'j = ', j)
                k1 = 0
                k2 = 0
                pos = []
                for p1 in range(3):
                    for p2 in range(3):
                        
                        #if i == 12 and j == 27:
                        #    print('i - 1 + p1 = ', i - 1 + p1, end = ' ')
                        #    print('j - 1 + p2 = ', j - 1 + p2)
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.fg:
                            k2 -= 1
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.bo:
                            k1 += 1
                            p = (i - 1 + p1, j - 1 + p2)
                            #print(p)
                            pos.append(p)
                if k2 == -5 and k1 > 1:
                    posForOne.append(pos)
    flag = False               
    for i in posForOne:
        for j in posForOne:
            if i == j:
                continue
            else:
                if set(i) < set(j):
                    setOfNull = set(j) - set(i)
                    print(setOfNull)
                    flag = True
                    for i in setOfNull:
                        leftClick(i)
    posForOne = []
                    
    
def printGrid(grid):
    for i in grid:
        for j in i:
            printValues(j)
        print(' ')
        
def pattern(grid):
    #global percentage
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == values.n1:
                for p1 in range(3):
                    for p2 in range(3):
                        if p1 == 1 and p2 == 1:
                            continue
                        if (i - 1 + p1) < 0 or (j - 1 + p2) < 0 or (i - 1 + p1) > 15 or (j - 1 + p2) > 29:
                            continue
                        if position[i - 1 + p1][j - 1 + p2] == values.n2:
                            pass
    
def main():
    global position
    screenGrab()
    cal = 2
    #printGrid(position)
    for j in range(15):
        for i in range(30):
            checkOne()
            checkTwo()
            checkThree()
            checkFour()
            checkFive()
            checkSix()
            print(i)
        #print(position[1][2])
        #printGrid(position)
        screenGrab()
        advance()
        if flag == False:
            cal -= 1
            screenGrab()
            if cal <= 0:
                print("False", j + 1)
                break
        else:
            cal += 1
    
grayImage = ImageGrab.grab()
imageGG()
main()

