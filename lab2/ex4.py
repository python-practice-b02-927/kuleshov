#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:42:08 2019

@author: student
"""

import turtle

n = 100
a = 7
turtle.shape('turtle')
for i in range(n):
    turtle.forward(a)
    turtle.left(360/n)