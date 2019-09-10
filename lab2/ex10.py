#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:32:56 2019

@author: student
"""

from turtle import *

a = 100
n = 6

shape('turtle')
for i in range(n):
    circle(a)
    right(360/n)