# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:14:22 2018

@author: VidyaSagar
"""

import os
def renameFiles():
    fileList = os.listdir(r"C:\Users\VidyaSagar\Desktop\prank\prank")
    print(fileList)
    savedPath = os.getcwd()
    os.chdir(r"C:\Users\VidyaSagar\Desktop\prank\prank")
    for fileName in fileList:
        os.rename(fileName,fileName.translate(None,"0123456789"))
    os.chdir(savedPath)
renameFiles()
