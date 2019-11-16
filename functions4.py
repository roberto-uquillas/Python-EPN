# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:50:03 2019

@author: CEC
"""

def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)
    
s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)