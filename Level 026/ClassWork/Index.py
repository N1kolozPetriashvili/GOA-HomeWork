from turtle import *

def walk():
    forwar(200)
def fall_back():
    right(200)
    forward(200)
def walk_and_fall_back():
    walk()
    fall_back()
walk_and_fall_back