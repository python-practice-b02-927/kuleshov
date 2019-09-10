#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:47:18 2019

@author: student
"""
from turtle import *

    
a = 100
n = 6
c = 10

right(90)
shape('turtle')
for i in range(n):
    circle(a)
    right(180)
    circle(a)
    a += c
