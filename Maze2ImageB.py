import json
from turtle import *

"""
Maze2Image.py
Written by Joseph Roten, 2019-01-26.
This script will read the json file created by MadManMax.py,
and will draw it on the screen.
It's using turtle.py, but you could easily used PyGame,
svgWrite, or any other graphics package.
"""

def SetCell(x, y, value = "undefined"):
    """Set the value of a cell of the maze."""
    n = "Cx" + str(x).strip() + "y" + str(y).strip()
    TheMaze[n] = value

def GetCell(x, y):
    """Returns the value of a cell of the maze."""
    n = "Cx" + str(x).strip() + "y" + str(y).strip()
    return TheMaze.get(n, "undefined")

if __name__ == "__main__":

    # Define the name of the file that holds the info.
    FileName = "MazeB.json"

    # Define the size of the cell on the screen.
    CellSize = 20

    # Load the maze from the file.
    with open(FileName) as InputFile:
        TheMaze = json.load(InputFile)

    # Define our old friend 'Bob the Turtle'.
    #Bob = turtle.Turtle()
    bgcolor("#99AAF8")
    penup()
    shape("turtle")
    speed("fastest")

    # Get the Width and Height values from the maze.
    MazeWidth = TheMaze['MazeWidth']
    MazeHeight = TheMaze['MazeHeight']

    # Draw the maze on the screen.
    for x in range(0, MazeWidth):
        for y in range(0, MazeHeight):
            xg = (y * CellSize) - 200
            yg = MazeWidth - (x * CellSize) + 200 + CellSize / 2
            pensize(CellSize)
            setpos(xg, yg)
            if GetCell(x,y) == "block":
                color("black", "grey")
                pendown()
                #begin_fill()
            if GetCell(x,y) == "water":
                color("black", "blue")
                pendown()
                #begin_fill()
            #for k in range(4):
            #    forward(CellSize)
            #    right(90)
            #end_fill()
            forward(CellSize / 8)
            penup()
    
    right(180)
    forward(CellSize)
    right(90)
    pensize(1)
    pendown()
    color("Red")
    pencolor("Red")

    
    #CODIGO DE ESTUDIANTE INICIA DESDE AQUI
    print(pos())
    value=float(input("value:"))
    forward(value)
    print(pos())
    value=float(input("value:"))
    forward(value)
    print(pos())

    mainloop()

    