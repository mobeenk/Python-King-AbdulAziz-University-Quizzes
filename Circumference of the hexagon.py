import math
A = 0
s = eval(input("Enter the circumference of the hexagon"))
A = 0.5*s*5*math.sqrt(3)
print("the value of Area is: {:.2f}".format(A))
if (A > 100):
    print("The value of area is greater than 100 cm^2")
elif (A > 50 and A <100):
    print("The value of area is less than 100 cm^2 and greater than 50")
elif (A <50):
    print("The value of area is less than 50 cm^2")
else:
    print("error")
