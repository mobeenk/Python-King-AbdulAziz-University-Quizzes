# built-in fuinctions
import math

abs(-5)
max(1,2,5)
min(5,9)
pow(3,2)
round(3.49)
round(3.234,2)
# to the minimum
math.ceil(3.4)
math.ceil(3.4)
math.ceil(-3.9)
# to max
math.floor(-2.5)
math.degrees(1.5)
math.radians(90)
math.sqrt(2)
math.exp(0)
math.log(2.71)
print(math.fabs(2))
print(math.pi)
print(math.cos(5.89))

# string literals using single quotation or double
# Python Escape sequences
print(" \"this is a quote\" ")
print(" \"this is a \n \t quote\" ")
print("ABC\rDEF")
print("ABC\bDEF")
print("ABC\\DEF")

# print without newline
print(" \"this is a quote\" ", end='')
print(" \"this is a quote\" ", end='***')
print("\n")
#PAGE 42 concat
string = "this "+"is "+"the "+str(1)
print(string)

#PAGE 46 excersize

x=14.35225
# round
x= int(x*100)/100 # is equivalennt to round(x,2)
print(x)


# format what's being printed
print("x is :",format(x,".2f"))
print("Justifying")
print(format(41.4641241,"10.2f"),end='d')
print(format(41.4641241,"<10.2f"))
print(format(41.4641241,">10.2f"))
print(format("My name is Ahemd",">40s") )
print(format(32233242,">30d"))

print(format(0.52342,"10.2%"))
print(format(0.52342,"10.1%"))

      #PAGE 73 programm to print a table
#x1,x2,x3,x4 = eval(input("input all 4 values"))
x1=5
x2=500
x3=20
x4=3000
print(format("---------------------------","40s"))
print(format('x',">4s") ,format('x^2',">10s"),format('Vx',">10s"))
print(format("---------------------------","40s"))
print( format(x1,"4d") +'|' ,format(pow(x1,2),"10d") +'|' ,  format(math.sqrt(x2),"10.2f") )
print( format(x2,"4d") +'|' ,format(pow(x2,2),"10d") +'|' ,  format(math.sqrt(x2),"10.2f") )
print( format(x3,"4d") +'|' ,format(pow(x3,2),"10d") +'|' ,  format(math.sqrt(x3),"10.2f") )
print( format(x4,"4d") +'|' ,format(pow(x4,2),"10d") +'|' ,  format(math.sqrt(x4),"10.2f") )






