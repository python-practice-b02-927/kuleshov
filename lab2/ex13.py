#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:13:10 2019

@author: student
"""

from turtle import *

a = 100
n = 4
c = 1

shape('turtle')
begin_fill()
circle(a)
color('yellow')
end_fill()
penup()
color('black')
left(90)
forward(a*1.6)
left(90)
forward(a*0.3)
pendown()
begin_fill()
circle(a/5)
color('blue')
end_fill()
color('black')
penup()
backward(a*0.6)
pendown()
begin_fill()
circle(a/5)
color('blue')
end_fill()
color('black')
penup()
forward(a*0.3)
left(90)
forward(a*0.4)
pendown()
width(10)
forward(a*0.5)
penup()
forward(a*0.1)
right(90)
forward(a*0.5)
left(90)
pendown()
color('red')
width(10)
circle(a*0.5,180)

