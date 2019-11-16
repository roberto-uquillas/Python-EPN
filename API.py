# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:25:23 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimaore"
key = "dhSdDD3IgMkSF6WRsCM8EQbmLONLJsA7"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)