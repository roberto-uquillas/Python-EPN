# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:54:22 2019

@author: CEC
"""

while True:
    x=input("Enter a number to count to: ")
    if x == "q" or x == "quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break