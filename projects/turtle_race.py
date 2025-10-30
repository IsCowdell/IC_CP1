#IC 1st turtle race 

import turtle as t 
import random 

screen = t.Screen()
screen.setup(600, 400)
t1side = random.randint(10,100)
t2side = random.randint(20,150)
t3side = random.randint(70,200)
t4side = random.randint(70,100)
t5side = random.randint(13,125)


t1 = t.Turtle()
t2= t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5= t.Turtle()
finish_line = t.Turtle()

def turtle_starting():
 finish_line.penup()
 finish_line.goto(250,300)
 finish_line.pendown()
 finish_line.goto(250,-300)
 t1.penup()
 t1.goto(-250,20)
 t1.pendown()
 t2.penup()
 t2.goto(-250,40)
 t2.pendown()
 t3.penup()
 t3.goto(-250,60)
 t3.pendown()
 t4.penup()
 t4.goto(-250,80)
 t4.pendown()
 t5.penup()
 t5.goto(-250,100)
 t5.pendown()
 t1.speed(4)
 t2.speed(3)
 t3.speed(5)
 t4.speed(16)
 t5.speed(8)
 finish_line.speed(20)


def making_turtles(): 

 t1.shape("turtle")
 t2.shape("turtle")
 t3.shape("turtle")
 t4.shape("turtle")
 t5.shape("turtle")

 t1.color("green")
 t2.color("blue")
 t3.color("purple")
 t4.color("teal")
 t5.color("black")

making_turtles()
turtle_starting()

for x in range(1,5):
    t1.forward(t1side)
    t2.forward(t2side)
    t3.forward(t3side)
    t4.forward(t4side)
    t5.forward(t5side) 
else:
    print("wow")






def check_colliosm():
    if t1 or t2 or t3 or t4 or t5 >= finish_line:
        print("YAS")
check_colliosm()





   

