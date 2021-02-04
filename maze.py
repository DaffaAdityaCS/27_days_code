#Maze by daffa aditya
#code on python 3 
#Part 1: setting up the maze
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("MAZE")
wn.setup(700,700)

# screen_x = int(input("x: "))
# screen_y = int(input("x: "))

#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)



#create level list
levels = [""]

#define first level
level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
    "x x xxxxxxxxxxxx xxxx xxxxxxxxx",
]
#add maze to mazes list
levels.append(level_1)

#create level setup function
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 -(y * 24)

            if character == "x":
                pen.goto(screen_x,screen_y)
                pen.stamp()


#creat class instaces
pen = Pen()

#setup up the level
setup_maze(levels[1])

while True:
    pass