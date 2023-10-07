# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:37:57 2023

@author: Molly
"""

import turtle

#Method to draw and fill square
def drawSquare(myTurtle,sideLength):
    myTurtle.begin_fill()
    for i in range(4):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
    myTurtle.end_fill()
    
#Method to turn a specific angle then draw a square    
def drawFlower(myTurtle,numOfSquares,sideLength):
    turnAngle= 360/numOfSquares
    for i in range(numOfSquares):
        myTurtle.right(turnAngle)
        drawSquare(myTurtle,sideLength)
        
#Method to create turtle object and call drawFlower method to create flower    
def main():  
    t = turtle.Turtle()
    drawFlower(t, 20, 40)

main()
    
