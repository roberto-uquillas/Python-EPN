# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 10:09:33 2019

@author: CEC
"""

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month]
	if month == 2 and isYearLeap(year):
		res = 29
	return res
print(daysInMonth(2019,10 ))