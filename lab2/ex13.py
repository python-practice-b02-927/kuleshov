#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:13:10 2019

@author: student
"""

from turtle import *

def arc(a,k,deg):
    for i in range(k):
        forward(a)
        left(deg/k)
    forward(a)
    
a = 10
k = 30
n = 4
c = 1

penup()
forward(400)
left(90)
pendown()
shape('turtle')
for i in range(n):
    arc(a,k,180)
    arc(a/5,k,180)
arc(a,k,180)