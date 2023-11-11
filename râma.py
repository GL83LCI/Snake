# By Lucian

import turtle
import time
import random

delay = 0.1

# Scor
scor = 0
scor_maxim = 0

# Creare tabel

wn = turtle.Screen()
wn.title("Râma by Lucian")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # Oprire screen updates

# Capul râmei

cap = turtle.Turtle()
cap.speed()
cap.shape("circle")
cap.color("yellow")
cap.penup()
cap.goto(0,0)
cap.direction = "stop"

# Mâncare
mâncare = turtle.Turtle()
mâncare.speed()
mâncare.shape("circle")
mâncare.color("black")
mâncare.penup()
mâncare.goto(0,100)

mâncare1 = turtle.Turtle()
mâncare1.speed()
mâncare1.shape("triangle")
mâncare1.color("green")
mâncare1.penup()
mâncare1.goto(0,100)

mâncare2 = turtle.Turtle()
mâncare2.speed()
mâncare2.shape("square")
mâncare2.color("red")
mâncare2.penup()
mâncare2.goto(0,100)

elemente = []

# Chenar 

chenar = turtle.Turtle()
chenar.speed()
chenar.shape("square")
chenar.color("white")
chenar.penup()
chenar.hideturtle()
chenar.goto(0, 260)
chenar.write("Scor: 0  Scor Maxim: 0", align="center", font=("Arial", 14, "italic"))

# Direcții

def go_up():
    if cap.direction != "down":
        cap.direction = "up"

def go_down():
    if cap.direction != "up":
        cap.direction = "down"

def go_left():
    if cap.direction != "right":
        cap.direction = "left"

def go_right():
    if cap.direction != "left":
        cap.direction = "right"

def move():
    if cap.direction == "up":
        y = cap.ycor()
        cap.sety(y + 20)

    if cap.direction == "down":
        y = cap.ycor()
        cap.sety(y - 20)

    if cap.direction == "left":
        x = cap.xcor()
        cap.setx(x - 20)

    if cap.direction == "right":
        x = cap.xcor()
        cap.setx(x + 20)

# Legături direcții

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Bucla 

while True:
    wn.update()

    # Lovirea de pereți

    if cap.xcor()>290 or cap.xcor()<-290 or cap.ycor()>290 or cap.ycor()<-290:
        time.sleep(1)
        cap.goto(0,0)
        cap.direction = "stop"

        # Ascundere elemente râmă

        for element in elemente:
            element.goto(1000, 1000)
        
        # Ștergere elemente râmă

        elemente.clear()

        # Resetare scor
        scor = 0

        # Resetare delay
        delay = 0.1

        chenar.clear()
        chenar.write("Scor: {}  Scor Maxim: {}".format(scor, scor_maxim), align="center", font=("Arial", 14, "italic")) 


    # Mâncarea elementului de râmă

    if cap.distance(mâncare) < 20:

        # Adăugare mâncare aleatoriu în tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mâncare.goto(x,y)

        # Adăugare segment
        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Creștere scor
        scor += 1

    if cap.distance(mâncare1) < 20:

        # Adăugare mâncare aleatoriu în tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mâncare1.goto(x,y)

        # Adăugare segment
        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Creștere scor
        scor += 5

    if cap.distance(mâncare2) < 20:
        
        # Adăugare mâncare aleatoriu în tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mâncare2.goto(x,y)

        # Adăugare segment
        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Creștere scor
        scor += 10

        if scor > scor_maxim :
            scor_maxim = scor
        
        chenar.clear()
        chenar.write("Scor: {}  Scor Maxim: {}".format(scor, scor_maxim), align="center", font=("Arial", 14, "italic")) 

    # Inversarea segmentelor

    for index in range(len(elemente)-1, 0, -1):
        x = elemente[index-1].xcor()
        y = elemente[index-1].ycor()
        elemente[index].goto(x, y)

    # Relocare primul segment

    if len(elemente) > 0:
        x = cap.xcor()
        y = cap.ycor()
        elemente[0].goto(x,y)

    move()    

    # Impact cap-coadă

    for segment in elemente:
        if segment.distance(cap) < 20:
            time.sleep(1)
            cap.goto(0,0)
            cap.direction = "stop"
        
            # Ascundere segmente

            for element in elemente:
                element.goto(1000, 1000)
        
            # Ștergere segmente
            elemente.clear()

            # Resetare scor
            scor = 0

            # Resetare delay
            delay = 0.1
        
            # Actualizare
            chenar.clear()
            chenar.write("Scor: {}  Scor Maxim: {}".format(scor, scor_maxim), align="center", font=("Arial", 14, "italic"))

    time.sleep(delay)

wn.mainloop()
