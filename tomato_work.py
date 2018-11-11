# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:01:37 2018

@author: Administrator

learn from: pengranxindong1990/BBPlayer
"""
#import re
import time
import os
import ctypes


q = 1.06 #Ã¿½×ÒôµÄ±¶Êý
q2 = q * q
dolist = {'C':523,'D':587,'E':659,'F':698,'G':784,'A':880,'B':988}
pitchs = {'l':0.5,'m':1,'h':2}
player = ctypes.windll.kernel32

def bbPlayer(filename, dokey, speed):
    do = int(dolist[dokey])
    re = int(do * q2)
    mi = int(re *q2)
    fa = int(mi *q)
    sol = int(fa *q2)
    la = int(sol *q2)
    si = int(la *q2)
    notes = [0, do, re, mi, fa,sol, la, si]
    beats = 60/speed*1000

    #print(beats)
    with open(filename) as fp:
        song = fp.read().replace('\n', '').split(',')
        #print(type(song))
        #print(song)

        for music in song:
            print(music)
            #p = re.findall(r'[lmh]', music)[0]
            p = music[1]
            p = float(pitchs[p])
            n = int(notes[int(music[0])])
            b = float(music[2:])

            if n==0:
                time.sleep(b*beats/1000)
            else:
                player.Beep(int(n*p), int(b*beats))
    return 1


miniute = 0.1
second = miniute * 60
per1 = 1
per2 = 0.2
time.sleep(second)
# ----- player music by beep ----
bbPlayer('f:\\ZTE_Time\\dayu', 'D', 100)


'''
for i in range(3):
    for j in range(3):
        print("\a")
        time.sleep(per2)  
    time.sleep(per1)
'''
