#mindstorms - from the book by the same name
import turtle


#define a function to draw a square
def draw_square(t):
    x = 1
    while x <= 4:
        t.right(90)
        t.forward(100)
        x = x+1

# define a function to draw a circle
def draw_circle():
    circ = turtle.Turtle()
    circ.shape("arrow")
    circ.color("blue")
    circ.speed(4)
    circ.circle(100)

#define a function to draw a triangle
def draw_triangle(tri):
    tri.forward(100)
    tri.left(160)
    tri.forward(100)
    tri.left(100)
    tri.forward(34.73)
    tri.left(100)


#define a function that drawsa circle from squares
def draw_circ_with_squares(t, angle_increment):
    curr_angle = 0
    while curr_angle < 360:
        draw_square(t)
        t.right(angle_increment)
        curr_angle = curr_angle+angle_increment

#define a function to draw a flower from triangle
def draw_flower_with_triangle(t,angle_increment):
    curr_angle = 0
    while curr_angle <= 360:
        draw_triangle(t)
        t.left(angle_increment)
        curr_angle = curr_angle+angle_increment
    t.right(100)
    t.forward(200)
    
            
#start exeuction of the program
window = turtle.Screen()
window.bgcolor("red")

#sqr = turtle.Turtle()
#sqr.shape("turtle")
#sqr.color("green")
#sqr.speed(10)
#draw_circ_with_squares(sqr,6)
#draw_square(sqr)
#draw_circle()
tri = turtle.Turtle()
tri.shape("arrow")
tri.color("white")
tri.speed(15)
#draw_triangle(tri)
draw_flower_with_triangle(tri,10)

window.exitonclick()
print("Program mindstorms.py has completed")
