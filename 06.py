# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:35:33 2019

@author: CEC
"""

devices=["R1","R2","R3","S1","S2"]
for item in devices:
    print(item)

for item in devices:
    if "R" in item:
        print(item)
        
switches=[]
for item in devices:
    if "S" in item:
        switches.append(item)
        
switches