import turtle 
import random

w = 500
h = 500
foodSize = 10
delay = 100

offsets ={
    "up": ( 0, 20),
    "down": (0, -20),
    "left": (-20,0),
    "right": (20,0)
}

def reset():
    global snake, snakeDir, foodPos, pen 
    snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
    snakeDir = "up"
    foodPos = get_random_foodPos()
    food.goto(foodPos)
    moveSnake()

def moveSnake():
    global snakeDir

    newHead = snake[-1].copy()
    newHead[0] = snake[-1][0] + offsets[snakeDir][0]
    newHead[1] = snake[-1][1] + offsets[snakeDir][1]

    if newHead in snake[:-1]:
        reset()
    else:
        snake.append(newHead)

        if not foodCollision():
            snake.pop(0)

        if snake[-1][0] > w / 2 :
            snake[-1][0] -= w
        elif snake [-1][0] < -w / 2:
            snake[-1][0] += w
        elif snake[-1][1] > h / 2 :
            snake[-1][1] -= h
        elif snake[-1][1] < -h / 2:
            snake[-1][1] += h
        
        pen.clearstamps()

        for segments in snake:
            pen.goto(segments[0], segments[1])
            pen.stamp()

        screen.update()

        turtle.ontimer(moveSnake, delay)

def foodCollision():
    global foodPos
    if getDistance(snake[-1], foodPos) <20:
        foodPos = get_random_foodPos()
        food.goto(foodPos)
        return True
    return False
def get_random_foodPos():
    x = random.randint(- w / 2 + foodSize, w / 2 - foodSize)
    y = random.randint(- h / 2 + foodSize, h /2 - foodSize)
    return(x, y)

def getDistance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance =((y2 - y1) ** 2 +(x2 - x1) ** 2) ** 0.5
    return distance

def goUp():
    global snakeDir
    if snakeDir != "down":
        snakeDir ="up"

def goRight():
    global snakeDir
    if snakeDir != "left":
        snakeDir ="right"

def goDown():
    global snakeDir
    if snakeDir != "up":
        snakeDir ="down"

def goLeft():
    global snakeDir
    if snakeDir != "right":
        snakeDir ="left"

screen = turtle.Screen()
screen.setup(w , h)
screen.title("Snake")
screen.bgcolor("Green")
screen.setup(500 , 500)
screen.tracer(0)

pen = turtle.Turtle("square")
pen.penup()

food = turtle.Turtle()
food.shape("square")
food.color("red")
food.shapesize(foodSize / 20)
food.penup()

screen.listen()
screen.onkey(goUp, "Up")
screen.onkey(goRight, "Right")
screen.onkey(goDown, "Down")
screen.onkey(goLeft, "Left")
screen.onkey(screen.bye, "Escape")

reset()
turtle.done()
