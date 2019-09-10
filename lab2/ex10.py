#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:32:56 2019

@author: student
"""

from turtle import *

def circle(a,k):
    for i in range(k):
        forward(a)
        left(360/k)
    
a = 7
k = 100
n = 6

shape('turtle')
for i in range(n):
    circle(a,k)
    right(360/n)