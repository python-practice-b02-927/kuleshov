#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:08:56 2019

@author: student
"""

from turtle import *

a = 10
n = 10

def squarespy(a, j):
    for i in range(3):
        forward(j*a)
        left(90)
    right(90)
    forward(a)
    left(90)
    forward((j+1)*a)
    left(90)

shape('turtle')
j = 1
for i in range(n):
    squarespy(a,j)
    j += 2