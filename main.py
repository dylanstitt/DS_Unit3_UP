# Dylan Stitt
# Unit 3 Unit Project
# Recursive Tree

import turtle, random

######################################### GREEN LEAVES AND RANDOM CHILDREN OFF BRANCHES

DA = 2
DL = 5
DT = .5

def draw(t, treeLength, rotationAngle, branchLength, thickness):
    if treeLength == 1:
        return

    t.pensize(thickness)
    num = random.randint(0, 2)
    rotNum = random.randint(-7, 7)

    if num != 0:
        t.forward(branchLength)
        t.left(rotationAngle)
        draw(t, treeLength - 1, rotationAngle + rotNum, branchLength - DL, thickness - DT)

        if num == 2:
            t.right(2*rotationAngle)
            draw(t, treeLength - 1, rotationAngle+rotNum, branchLength-DL, thickness-DT)
            t.left(rotationAngle)
            t.backward(branchLength)
            return
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
    draw(t, 8, 15, 80, 4)

    turtle.mainloop()


if __name__ == '__main__':
    main()
