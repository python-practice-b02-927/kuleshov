#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:52:34 2019

@author: student
"""

from turtle import *

    
a = 100
n = 4

penup()
forward(400)
left(90)
pendown()
shape('turtle')
for i in range(n):
    circle(a,180)
    circle(a/5,180)
circle(a,180)
    