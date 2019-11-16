# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:32:35 2019

@author: CEC
"""


fibonacci_numbers = [0, 1]
for i in range(2,10):
    #if i<1000:
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
        #break
#if i < 10:
print(fibonacci_numbers)