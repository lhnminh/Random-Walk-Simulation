"""CSC 161: Simulations and Designs

Minh Le
Spring 2020
"""

from random import random
from graphics import Point, GraphWin, Line, Circle, Rectangle, Polygon
from math import sqrt
from time import sleep

def main():
    intro()
    walks = get_walks()
    steps = get_step()
    dist = random_walk_2d(walks, steps)
    print_result(dist)

def intro():
    print('Simulation of two dimensional random walk')
    print()

def get_walks():
    walks = int(input('How many walks should I do? '))
    return walks
def get_step():
    steps = int(input('How many steps should I take on each? '))
    return steps

def random_walk_2d(w, s):
    '''
    This random_walk_2d function simulate 'w' number of walks
    with 's' number of steps and create a Graphing Window
    '''
    total_dist = 0
    
    win = GraphWin("Random walk simulation",600,600)
    for i in range(w):
        Eraser = Rectangle(Point(0,0), Point(600,600))
        Eraser.setFill('White')
        Eraser.draw(win)
        
        for i in range(600):
            if i % 50 == 0:
                line = Line(Point(0,i), Point(600,i))
                line.draw(win)
                line2 = Line(Point(i,0), Point(i,600))
                line2.draw(win)           
        total_dist += random_1_walk(s,win)
    dist = total_dist/w
    return dist

def random_1_walk(s,win):
    '''
    The function random_1_walk simulate 1 random walk
    witk 's' amount of steps on 'win' Graphing Window
    '''
    i = Point(300,300)
    start = Circle(i, 10)
    start.draw(win)
    i2 = i.clone()
    for h in range(s):
        if random() < 0.25: #MOVE UP
            i3 = i2.clone()
            i2.move(0,-50)
            line = Line(i2,i3)
            Arrow = Polygon(i2, Point((i2.x - 5),(i2.y+10)),\
                            Point((i2.x + 5),(i2.y+10)))
            
        elif random() < 0.50: #MOVE DOWN
            i3 = i2.clone()
            i2.move(0,50)
            line = Line(i2,i3)
            Arrow = Polygon(i2, Point((i2.x - 5),(i2.y - 10)),\
                            Point((i2.x + 5),(i2.y-10)))
            
        elif random() < 0.75: #MOVE LEFT
            i3 = i2.clone()
            i2.move(-50,0)
            line = Line(i2,i3)
            Arrow = Polygon(i2, Point((i2.x + 10), (i2.y + 5)),\
                            Point((i2.x + 10), (i2.y - 5))) 
            
        elif random() < 1: #MOVE RIGHT
            i3 = i2.clone()
            i2.move(50,0)
            line = Line(i2,i3)
            Arrow = Polygon(i2, Point((i2.x - 10), (i2.y + 5)),\
                            Point((i2.x - 10), (i2.y - 5)))

        Arrow.setFill('Red')
        Arrow.setOutline('Red')

        if h == (s - 1):
            end = Circle(i2, 10)
            end.draw(win)
        
        line.setWidth(5)
        line.setFill('Red')
        
        Arrow.draw(win)
        line.draw(win)
        sleep(0.5)
    dist = sqrt((i2.x - i.x)**2 + (i2.y - i.y)**2)
    return dist

def print_result(d):
    print(f'Average distance from start: {d:0.2f}')

    
