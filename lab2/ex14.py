#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:38:02 2019

@author: student
"""

from turtle import *
def star(a, n):
    for i in range(n):
        forward(a)
        right(180*(1-1/n))
        
a = 200

penup()
backward(400)
shape('turtle')
pendown()
star(a, 5)
penup()
forward(300)
pendown()
star(a, 11)