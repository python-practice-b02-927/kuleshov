#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:21:44 2019

@author: student
"""

from turtle import *
from math import *

a = 50
k = 10
c = 10

def polygon(n,a):
    for i in range(n):
        forward(a)
        left(360/n)
        
def rad(n,a):
    return a/(2*sin(180/n))
        
shape('turtle')
n = 3
right(180)

for i in range(k):
    pendown()
    right(180*(n-2)/n/2)
    polygon(n, a)
    left(180*(n-2)/n/2)
    penup()
    backward(c)
    right(180)
    n += 1
    a = (rad(n,a)+c)*2*sin(180/(n+1))
    