# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:03:55 2018

@author: VidyaSagar
"""

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
        
    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye Color -"+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
        
    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        print("Number of Toys - "+str(self.number_of_toys))

#billy_cyrus = Parent("cyrus","blue")
miley_cyrus = Child("cyrus","yellow","7")
# print(billy_cyrus.last_name)
#print(miley_cyrus.eye_color)
#billy_cyrus.show_info()
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()