# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:36:15 2019

@author: CEC
"""

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)