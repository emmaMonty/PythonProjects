import time


SLEEPTIME = 0.1
FILENAME = "maze.txt"
VERBOSE = False


def solve(maze, x, y):
    if y >= len(maze[x]) or x >= len(maze):
        return False
    if y < 0 or x < 0:
        return False
    if maze[x][y] == "X":
        return False
    if maze[x][y] == ".":
        return False
    maze[x][y] = '.'
    if VERBOSE == True:
        printMaze(maze)
    if y == len(maze[x]) -1 or x == len(maze)-1:
        return True

    #if maze[x][y] == " ":
     #   return True

    if solve(maze,x+1, y) == True:
        return True
    elif solve(maze,x, y+1) == True:
        return True
    elif solve(maze,x-1, y) == True:
        return True
    elif solve(maze, x, y-1) == True:
        return True
    else:
        maze[x][y] = ' '
    return False

def readMaze(maze):
    mazefile = open(FILENAME, "r")
    for line in mazefile.read().splitlines():
        maze.append([])
        for c in line:
            maze[-1].append(c)
    mazefile.close()


def printMaze(maze):
    print("\n\n\n\n\n\n\n\n\n")
    for i in range(0, len(maze)):
        for j in range(0, len(maze[i])):
            print(maze[i][j], end="")
        print()
    time.sleep(SLEEPTIME)
    print()

def main():
    maze = []
    readMaze(maze)
    if not solve(maze, 1,0):
        print("no solution is possible.")
    else:
        printMaze(maze)


main()
