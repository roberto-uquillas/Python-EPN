# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:46:40 2019

@author: CEC
"""

def isYearLeap(year):
    if year % 4 == 0  and  (year % 100 != 0  or  year % 400 == 0):
        return True
    else:
        return False

 
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
