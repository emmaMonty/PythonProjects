import turtle
import random
import time

def tree(branchLen,t):
    t.speed(0)
    if branchLen > 5:
        angle = random.randint(-10, 20)
        length = random.randint(-15, 10)
        t.forward(branchLen)
        t.right(20 + angle)
        tree(branchLen-20 + length,t)
        t.left(40)
        tree(branchLen-15 + length,t)
        t.right(20 - angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(120,t)

    myWin.exitonclick()

main()
