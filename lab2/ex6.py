#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:50:40 2019

@author: student
"""
from turtle import *

n = 12
a = 200

shape('turtle')
for i in range(n):
    forward(a)
    stamp()
    backward(a)
    right(360/n)
