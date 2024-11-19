# Dylan Stitt
# Unit 3 Unit Project
# Recursive Tree

import turtle, random

DA = 2
DL = 8
DT = 1

def drawLeaf(t, thickness):
    t.color('green')
    t.pensize(thickness + 12)
    t.forward(5)
    t.backward(5)
    t.color('brown4')
    t.pensize(thickness)

def drawAsym(t, treeLength, rotationAngle, branchLength, thickness):
    if treeLength == 1:
        drawLeaf(t, thickness)
        return

    t.pensize(thickness)
    rotNum = random.randint(-12, 11)

    t.forward(branchLength)
    t.left(rotationAngle)
    drawAsym(t, treeLength - 1, rotationAngle + rotNum, branchLength - DL, thickness - DT)

    t.right(2 * rotationAngle)
    drawAsym(t, treeLength - 1, rotationAngle + rotNum, branchLength - DL, thickness - DT)
    t.left(rotationAngle)
    t.backward(branchLength)
    return

def drawSym(t, treeLength, rotationAngle, branchLength, thickness):
    if treeLength == 1:
        drawLeaf(t, thickness)
        return

    t.pensize(thickness)
    t.forward(branchLength)
    t.left(rotationAngle)
    drawSym(t, treeLength - 1, rotationAngle, branchLength - DL, thickness - DT)

    t.right(2 * rotationAngle)
    drawSym(t, treeLength - 1, rotationAngle, branchLength - DL, thickness - DT)
    t.left(rotationAngle)
    t.backward(branchLength)
    return

def setup(t):
    turtle.mode("logo")
    t.color("brown4")
    t.speed("fastest")
    t.hideturtle()

    t.penup()
    t.setx(0)
    t.sety(-250)
    t.pendown()

def main():
    t = turtle.Turtle()
    setup(t)
    drawAsym(t, 8, 15, 80, 10)
    #drawSym(t, 8, 15, 80, 10)

    turtle.mainloop()

if __name__ == '__main__':
    main()
