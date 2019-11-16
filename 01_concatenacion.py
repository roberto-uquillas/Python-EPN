# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 10:15:36 2019

@author: CEC
"""

str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
print((str1+str2+str3))
x=3
print("This value of X is " + str(x))
print(type(x))
x=str(x)
type(x)
print("This value of X is " + x)
pi = 22/7
print(pi)
print("{:.5f}".format(pi))
hostnames=["R1","R2","R3","S1","S2"]
type(hostnames)
len(hostnames)
print(hostnames)
hostnames[0]
hostnames[-1]
hostnames[0]="RTR1"
hostnames
ipAddress = {"R1":"10.1.1.1","R2":"10.2.2.1","R3":"10.3.3.1"}
type(ipAddress)
