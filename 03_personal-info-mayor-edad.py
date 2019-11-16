# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:03:09 2019

@author: CEC
"""

firstName = input("What is your first name?")
lastName = input("What is your last name?")
location = input("What is your location?")
age = input("What is your age?")
space = " "
print("Hi" + space + firstName + space + lastName + space + location + space + age)

x = int(age)

MayorEdad = 17
if x > MayorEdad:
    print("Mayor de edad")
else:
    print("Menor de edad")
    