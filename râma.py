import turtle
import time
import random

delay = 0.1

# Scor
scor = 0
scor_maxim = 0

# Creare tabel

wn = turtle.Screen()
wn.title("Worm by Lucian")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0) # Oprire screen updates

# Capul ramei

cap = turtle.Turtle()
cap.speed()
cap.shape("circle")
cap.color("yellow")
cap.penup()
cap.goto(0,0)
cap.direction = "stop"

# Mancare
mancare = turtle.Turtle()
mancare.speed()
mancare.shape("circle")
mancare.color("black")
mancare.penup()
mancare.goto(0,100)

mancare1 = turtle.Turtle()
mancare1.speed()
mancare1.shape("triangle")
mancare1.color("green")
mancare1.penup()
mancare1.goto(0,100)

mancare2 = turtle.Turtle()
mancare2.speed()
mancare2.shape("square")
mancare2.color("red")
mancare2.penup()
mancare2.goto(0,100)

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

# Directii

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

# Legaturi directii

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Bucla 

while True:
    wn.update()

    # Lovirea de pereti

    if cap.xcor()>290 or cap.xcor()<-290 or cap.ycor()>290 or cap.ycor()<-290:
        time.sleep(1)
        cap.goto(0,0)
        cap.direction = "stop"

        # Ascundere elemente rama

        for element in elemente:
            element.goto(1000, 1000)
        
        # Stergere elemente rama

        elemente.clear()

        # Resetare scor
        scor = 0

        # Resetare delay
        delay = 0.1

        chenar.clear()
        chenar.write("Scor: {}  Scor Maxim: {}".format(scor, scor_maxim), align="center", font=("Arial", 14, "italic")) 


    # Mancarea elementului de rama

    if cap.distance(mancare) < 20:

        # Adaugare mancare aleatoriu in tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mancare.goto(x,y)

        # Adaugare segment

        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Crestere scor
        scor += 1

    if cap.distance(mancare1) < 20:

        # Adaugare mancare aleatoriu in tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mancare1.goto(x,y)

        # Adaugare segment

        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Crestere scor
        scor += 5

    if cap.distance(mancare2) < 20:
        
        # Adaugare mancare aleatoriu in tabel

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        mancare2.goto(x,y)

            # Adaugare segment
        element_nou = turtle.Turtle()
        element_nou.speed(0)
        element_nou.shape("circle")
        element_nou.color("yellow")
        element_nou.penup()
        elemente.append(element_nou)

        # Reducere delay
        delay -= 0.001

        # Crestere scor
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

    # Impact cap-coada

    for segment in elemente:
        if segment.distance(cap) < 20:
            time.sleep(1)
            cap.goto(0,0)
            cap.direction = "stop"
        
            # Ascundere segmente

            for element in elemente:
                element.goto(1000, 1000)
        
            # Stergere segmente
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
