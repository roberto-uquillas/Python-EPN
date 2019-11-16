# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:25:56 2019

@author: CEC
"""

aclNum = int(input("Cuál es el número?"))
if aclNum == 0:
    print("Es 0")
elif aclNum%2 == 0:
    print ("Es par")
else:
    print("Es impar")