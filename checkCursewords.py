# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:38:27 2018

@author: VidyaSagar
"""


import urllib


def read_text():
    quotes = open("D:\python\movieQuotes.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity alert")
    elif "false" in output:
        print("No curse words in document")
    else:
        "couldnt read document"
read_text()
