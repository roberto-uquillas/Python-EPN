# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 09:33:19 2019

@author: CEC
"""
devices=[]
file=open("devices.txt","r")
for item in file:
    item = item.strip()
    devices.append(item)
file.close()
print(devices)

