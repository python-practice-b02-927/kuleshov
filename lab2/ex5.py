#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:44:48 2019

@author: student
"""

import turtle

def square(a):
    for i in range(4):
        turtle.forward(a)
        turtle.right(90)

n = 10
a = 30
c = 30

turtle.shape('turtle')
for i in range(n):
    square(a)
    turtle.penup()
    turtle.backward(c)
    turtle.left(90)
    turtle.forward(c)
    turtle.right(90)
    turtle.pendown()
    a += 2*c