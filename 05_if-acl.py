# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:25:56 2019

@author: CEC
"""

aclNum = int(input("What is the IPv4 ACL number?"))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard Ipv4 ACL.")
elif aclNum >=100 and aclNum <= 199:
    print ("This is a extended")
else:
    print("This is not a standard")