import random
import turtle
from turtle import *
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "balance.json")

def load_balance():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return data.get("balance", 0)
            except json.JSONDecodeError:
                return 0
    return 0

def save_balance(balance):
    with open(DATA_FILE, "w") as f:
        json.dump({"balance": balance}, f)

def start():
    global input1
    while True:
        input1 = input("Which will Win the Game? Turtle, Circle or Square? :- ")
        if input1.lower() in ["turtle", "circle", "square"]:
            setup()
            break
        else:
            print("\nPlease enter Turtle, Circle or Square\n")
            continue

def setup():
    global input1
    canvas = turtle.getcanvas()
    window = canvas.winfo_toplevel()
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    start = Turtle()
    turtle.title("Race")
    turtle.bgcolor("red")
    turtle.setup(1526,830, startx = 0, starty = 0)
    start.speed(0)
    start.left(90)
    start.fd(330); start.bk(660)
    start.hideturtle()

    t = Turtle()
    t.shape("turtle")
    t.color("blue")
    t.penup()
    t.speed(0)
    t1 = t.clone()
    t1.color("green"); t1.shape("circle")
    t.goto(-730,-300)
    t1.goto(-730,300)
    t2 = t.clone()
    t2.color("yellow"); t2.shape("square")
    t2.goto(-730,0)

    finish1 = Turtle()
    finish1.penup()
    finish1.left(90)
    finish1.speed(0)
    finish2 = finish1.clone()
    finish3 = finish2.clone()
    finish1.goto(700,-300); finish2.goto(700,300); finish3.goto(700,0)
    finish1.pendown(); finish2.pendown(); finish3.pendown()
    finish1.fd(20); finish1.bk(40); finish2.fd(20); finish2.bk(40); finish3.fd(20); finish3.bk(40)
    finish1.hideturtle(); finish2.hideturtle(); finish3.hideturtle()

    start1 = Turtle()
    start1.speed(0)
    start1.penup()
    start1.goto(-730,-300)
    start1.pendown()
    start1.hideturtle()

    start2 = start1.clone()
    start2.penup()
    start2.goto(-730,300)
    start2.pendown()

    start3 = start2.clone()
    start3.penup()
    start3.goto(-730,0)
    start3.pendown()

    for i in range(72):
        start1.fd(10); start2.fd(10); start3.fd(10)
        start1.penup(); start2.penup(); start3.penup()
        start1.fd(10); start2.fd(10); start3.fd(10)
        start1.pendown(); start2.pendown(); start3.pendown()

    for i in range(870):
        t.fd(random.randrange(7))
        t1.fd(random.randrange(7))
        t2.fd(random.randrange(7))
        if (t.position()[0]) >= 0:
            print("\nTurtle is leading")
            break
        if (t1.position()[0]) >= 0:
            print("\nCircle is leading")
            break
        if (t2.position()[0]) >= 0:
            print("\nSquare is leading")
            break
    winner = ""
    for i in range(870):
        t.fd(random.randrange(7))
        t1.fd(random.randrange(7))
        t2.fd(random.randrange(7))
        if (t.position()[0]) >=700:
            print("Turtle wins!!!")
            winner = "turtle"
            break
        elif (t1.position()[0]) >=700:
            print("Circle wins!!!")
            winner = "circle"
            break
        elif (t2.position()[0]) >=700:
            print("Square wins!!!")
            winner = "square"
            break

    balance = load_balance()

    if input1.lower() == winner:
        print("Congratulations!!! You have won $50")
        balance += 50
    else:
        print("Sorry!!! You have lost $50")
        balance -= 50

    save_balance(balance)
    print("Balance is :- $", balance)

    turtle.done()

start()

