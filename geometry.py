# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:16:46 2018

@author: VidyaSagar
"""


import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    for i in range(1,36):
        for i in range(1,5):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    window.exitonclick()
draw_square()
