#!/usr/bin/python

from wavebender import *
from math import pi, sqrt
import pygame

from time import time

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

kick = pygame.mixer.Sound('/root/hack/samples/kick.wav')
kick.set_volume(1);
snare = pygame.mixer.Sound('/root/hack/samples/snare.wav')
snare.set_volume(1);
closedhh = pygame.mixer.Sound('/root/hack/samples/closed.wav')
closedhh.set_volume(1);
cymbal = pygame.mixer.Sound('/root/hack/samples/cymbal.wav')
cymbal.set_volume(1);

## Horizontal Sector Based Kit

def play(yaw, pitch, roll, g, t, p):
#     print yaw
#     return 0
     a = abs(1 - g)
     v = a - 0.8
     d = int(yaw * 3 / pi) 
     if a > 1.3 and t - p > 0.15:
         print d
         if (d == -1):
             snare.set_volume(v);
             snare.play()
             print 'snare'
         elif (d == 0):
             closedhh.set_volume(v);
             closedhh.play()
             print 'hat'
         elif (d == 1):
             cymbal.set_volume(v);
             cymbal.play()
             print 'crash' 
         else:
             kick.set_volume(v);
             kick.play()
             print 'kick'
         return float(time())

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
