#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:47:18 2019

@author: student
"""
from turtle import *

def circle(a,k):
    for i in range(k):
        forward(a)
        left(360/k)
    
a = 1
k = 100
n = 6
c = 1

right(90)
shape('turtle')
for i in range(n):
    circle(a,k)
    right(180)
    circle(a,k)
    a += c
