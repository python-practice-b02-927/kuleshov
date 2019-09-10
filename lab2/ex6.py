#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:50:40 2019

@author: student
"""

import turtle

n = 12
a = 200

turtle.shape('turtle')
for i in range(12):
    turtle.forward(a)
    turtle.backward(a)
    turtle.right(360/n)
