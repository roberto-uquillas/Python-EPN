# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:52:45 2019

@author: CEC
"""

x=input("Enter a number to count to: ")
x=int(x)
y=1
while y<=x:
    print(y)
    y=y+1
    if y>x:
        break
            