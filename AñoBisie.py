# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:45:12 2019

@author: CEC
"""

def AñoBisiesto(año):
    var1=año%4
    var2=año%100
    var3=año%400
    if var1==0 and var2!=0 or var3==0:
        return True
    else:
        return False
      
testData=[1900,2000,2016,1987]
testResults=[False,True,True,False]

for i in range(len(testData)):
    yr=testData[i]
    result=AñoBisiesto(yr)
    if result==testResults[i]:
        print("OK")
    else:
        print ("Failed")
    