#IC 1st turtle race 

import turtle as t 
import random 

screen = t.Screen()
screen.setup(600, 400)
t1side = random.randint(10,500)
t2side = random.randint(20,250)
t3side = random.randint(70,500)
t4side = random.randint(70,100)
t5side = random.randint(13,25)



fast = random.randint(1,16)


t1 = t.Turtle()
t2= t.Turtle()
t3 = t.Turtle()
t4 = t.Turtle()
t5= t.Turtle()

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

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
t4.shape("turtle")
t5.shape("turtle")


all_turtles = [t1,t2,t3,t4,t5]

t1.color("green")
t2.color("blue")
t3.color("purple")
t4.color("teal")
t5.color("black")



for x in range(1,5):
    t1.forward(t1side)
    t2.forward(t2side)
    t3.forward(t3side)
    t4.forward(t4side)
    t5.forward(t5side) 
else:
    print("wow")

