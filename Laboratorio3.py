# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:48:32 2019

@author: CEC
"""

def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
                

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res
 
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testData[i]
    mo = testMonths[i]
    print(yr, mo,"->", end="")
    result = daysinMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
        
