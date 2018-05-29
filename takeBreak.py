# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:55:27 2018

@author: VidyaSagar
"""

import webbrowser
import time

breakCount = 0
totalBreaks = 3
print ("This program started at " + time.ctime())
while (breakCount < totalBreaks):
    time.sleep(3)
    webbrowser.open("facebook.com")
    breakCount = breakCount + 1
