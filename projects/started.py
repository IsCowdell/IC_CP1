import turtle as t

def draw_branch(length):
    if length > 5:
        for i in range(3):
            t.forward(length)
            draw_branch(length/3)
            t.backward(len)
            t.right(60)

t.shape("turtle")
t.color("lightblue")
t.penup()
t.pendown()

def drawingsnowflake():
    for i in range(6):
        draw_branch(180)
        t.right(60)
        t.hideturtle
drawingsnowflake()