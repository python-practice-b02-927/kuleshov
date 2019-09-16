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


def face():
    pendown()
    begin_fill()
    circle(a)
    color('yellow')
    end_fill()
    color('black')
    penup()


def eye():
    pendown()
    begin_fill()
    circle(a / 5)
    color('blue')
    end_fill()
    color('black')
    penup()


def nose():
    pendown()
    color('black')
    width(10)
    forward(a * 0.5)
    penup()


def mouth():
    pendown()
    color('red')
    width(10)
    circle(a * 0.5, 180)
    color('black')
    penup()


shape('turtle')

face()

left(90)
forward(a*1.6)
left(90)
forward(a*0.3)

eye()

backward(a*0.6)

eye()

forward(a*0.3)
left(90)
forward(a*0.4)

nose()

forward(a*0.1)
right(90)
forward(a*0.5)
left(90)

mouth()

