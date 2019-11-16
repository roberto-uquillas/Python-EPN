# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:32:43 2019

@author: Juan Carlos
"""
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b
    print()
#fib(1000)   
    
#limite = int(input("Ingrese imput"))
#fib(limite)