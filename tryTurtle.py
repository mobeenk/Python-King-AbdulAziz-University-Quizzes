
# a program to find circle, square and rectanble circumference and area
import math
import turtle as t

typeOfShape = int(input('Choose the Shape: \n 1-Rectangle \n 2-Circle \n 3-Square ...\n'))
if typeOfShape == 1:
    print('You choose Rectangle\n')
    width = int(input('Input the Width :\n'))
    length = int(input('Input the Width :\n'))
    rec_circumference = (width + length) * 2
    rec_area = width * length
    print('Rectangle Circumference is : ', rec_circumference, '\nRectangle Area is : ', rec_area)
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(length)
        t.left(90)

elif typeOfShape == 2:
    print('You choose Circle\n')
    radius = int(input('Input the Radius :\n'))
    circle_circumference = 2 * math.pi * radius
    circle_area = math.pi * pow(radius, 2)
    print('Circle Circumference is : ', circle_circumference, '\nCircle Area is : ', circle_area)
    t.circle(radius)

elif typeOfShape == 3:
    print('You choose Square\n')
    length = int(input('Input the Length :\n'))
    sqr_circumference = length * 4
    sqr_area = pow(length, 2)
    print('Square Circumference is : ', sqr_circumference, '\nRectangle Area is : ', sqr_area)
    for i in range(4):
        t.forward(length)
        t.left(90)

else:
    print('Invalid Choice !!!')

t.Screen().exitonclick()
