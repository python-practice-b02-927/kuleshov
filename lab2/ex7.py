#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:52:57 2019

@author: student
"""

from turtle import *
import math

n = 1000
k = 0.05
f = 5

shape('turtle')
for i in range(n):
    right(f)
    forward(k*f*(1+(i*f*math.pi/180)**2)**0.5)