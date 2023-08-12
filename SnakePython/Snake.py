from turtle import *
from random import randrange
from freegames import squre, vector

snake = [vector(10, 0)]
food = vector(0, 0)
aim = vector(0, -10)

def inside(x,y):
    aim.x = x
    aim.y = y


    
