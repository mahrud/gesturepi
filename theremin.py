#!/usr/bin/python

from wavebender import *
from math import pi, sqrt
import pygame

from time import time, sleep

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

A = pygame.mixer.Sound('/root/hack/samples/A.wav')
A.set_volume(1);
B = pygame.mixer.Sound('/root/hack/samples/B.wav')
B.set_volume(1);
C = pygame.mixer.Sound('/root/hack/samples/C.wav')
C.set_volume(1);
D = pygame.mixer.Sound('/root/hack/samples/D.wav')
D.set_volume(1);
E = pygame.mixer.Sound('/root/hack/samples/E.wav')
E.set_volume(1);

## Horizontal Sector Based Kit

def play(yaw, pitch, roll):
     v = roll * 0.25 / pi + 1.0
     d = int((pitch + pi / 2) * 180 / pi) / (180 / 5)
#     print d
     if (d == 0):
         A.set_volume(v);
         A.play()
         print 'A'
     elif (d == 1):
         B.set_volume(v);
         B.play()
         print 'B'
     elif (d == 2):
         C.set_volume(v);
         C.play()
         print 'C' 
     elif (d == 3):
         D.set_volume(v);
         D.play()
         print 'D' 
     else:
         E.set_volume(v);
         E.play()
         print 'E'
     sleep(0.071)

     return 0

## Axis-Specific Translation Kit

#def play(yaw, pitch, roll, g, t, p):
#    a = a
#    X , Y , Z = yaw , pitch , roll
#    if X > 10*( Y + Z ):
#         snare.play()
#         print 'hoo-hah'
#    if Y > 10*( X + Z ):
#         closedhh.play()
#         print 'titties'
#    if Z > 10*( Y + Z ):
#         kick.play()
#         print 'ass'
#    return float(time())
