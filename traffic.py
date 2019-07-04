#from turtle import Turtle
import turtle
import time
import datetime
wn = turtle.Turtle()

wn.screen.bgpic("TFimg.gif")
wn.color("black")
wn.shape("arrow")
wn.hideturtle()
"""t.shapesize(3)
t.speed(1)
#t.pensize(0)
t.up()
t.goto(-150,-50)
t.down()
t.fd(200)"""

tess = turtle.Turtle()
alex = turtle.Turtle()
henry = turtle.Turtle()

car = turtle.Turtle()
car.hideturtle()
car.speed(1)
car.shapesize(3)

car1 = turtle.Turtle()
car1.color("blue")
car1.shapesize(3)
car1.hideturtle()
car1.speed(1)
scanner = turtle.Turtle()
scanner.color("red")
scanner.pensize(10)
scanner.hideturtle()
scanner.up()
scanner.goto(250,0)
scanner.down()
scanner.speed(0)

def draw_housing():
    """ Draw a nice housing to hold the traffic lights"""
    tess.pensize(3)  # Change tess' pen width
    tess.color('black', 'black')  # Set tess' color
    tess.up()
    tess.hideturtle()
    alex.up()
    alex.hideturtle()
    henry.up()
    henry.hideturtle()
    tess.goto(200,0)
    alex.goto(200,0)
    henry.goto(200,0)
    tess.down()
    alex.down()
    henry.down()
    tess.begin_fill()  # Tell tess to start filling the color
    tess.forward(80)  # Tell tess to move forward by 80 units
    tess.left(90)  # Tell tess to turn left by 90 degrees
    tess.forward(200)
    tess.circle(40, 180)  # Tell tess to draw a semi-circle
    tess.forward(200)
    tess.left(90)
    tess.end_fill() # Tell tess to stop filling the color
    tess.showturtle()
    alex.showturtle()
    henry.showturtle()


draw_housing()


def circle(t, ht, colr):
    """Position turtle onto the place where the lights should be, and
    turn turtle into a big circle"""
    t.penup()  # This allows us to move a turtle without drawing a line
    t.forward(40)
    t.left(90)
    t.forward(ht)
    t.shape('circle')  # Set tutle's shape to circle
    t.shapesize(3)  # Set size of circle
    t.fillcolor(colr)  # Fill color in circle


circle(tess, 50, 'green')
circle(alex, 120, 'orange')
circle(henry, 190, 'red')

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    """A state machine for traffic light"""
    global state_num  # Tells Python not to create a new local variable for state_num

    if state_num == 0:  # Transition from state 0 to state 1
        henry.color('darkgrey')
        alex.color('darkgrey')
        tess.color('green')

        car.up()
        car.goto(-250,-50)
        
        car.showturtle()
        car.fd(600)
        car.hideturtle()
        

        #time.sleep(5)
        

        #wn.screen.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3 sec

        

        car1.up()
        car1.goto(-250,-50)
        
        car1.showturtle()
        car1.fd(600)
        car1.hideturtle()

        state_num = 1
    if state_num == 1:  # Transition from state 1 to state 2
        henry.color('darkgrey')
        alex.color('orange')

        car.up()
        car.goto(-250,-50)
        
        car.showturtle()
        car.fd(400)
        car.hideturtle()

        #time.sleep(2)
        

        #wn.screen.ontimer(advance_state_machine, 3000)  # set the timer to explode in 3 sec

        

        car1.up()
        car1.goto(-250,-50)
        
        car1.showturtle()
        car1.fd(600)
        car1.hideturtle()

        
        #wn.screen.ontimer(advance_state_machine, 1000)
        state_num = 2
    if state_num == 2:  # Transition from state 2 to state 3
        tess.color('darkgrey')
        #wn.screen.ontimer(advance_state_machine, 1000)
        time.sleep(2)
        
        state_num = 3
    if state_num == 3:                 # Transition from state 3 to state 0
        henry.color('red')
        alex.color('darkgrey')
        
        #wn.screen.ontimer(advance_state_machine, 2000)
        scanner.right(90)
        scanner.fd(150)

        with open("car_no.txt",'r') as fo:
            for line in fo:
                car.up()
                car.goto(-250,-50)

                car.showturtle()
                car.fd(600)
                car.hideturtle()

                out = line.strip('\n')

                print "CAR NO. "+out+" VIOLATED AT TIME "+str(datetime.datetime.now())

        car.up()
        car.goto(-250,-50)
        car.showturtle()
        car.fd(490)

        
        car1.up()
        car1.goto(-250,-70)
        car1.showturtle()
        car1.fd(490)
        





advance_state_machine()

print "\n\nMADE BY AAKANKSHA, BHAGYA AND RICHA"
print "\n\n THANKYOU!!! "


wn.screen.exitonclick()

