# QUESTION 1

# age = float(input('Enter the age of student:'))
# GPA = float(input('Enter the GPA of student: '))
#
# if (GPA > 4.5 and age < 25) :
#      print( "you have three chances")
# elif (GPA > 3.5 and age < 27):
#     print("you have two chances")
# else:
#      print("You have one chance")


# QUESTION 2

# total = 0
# myItems = int(input('Enter number of Items :'))
# for i in range(myItems):
#     itemPrice = int(input("Enter the price of item #" + str(i + 1) + '  : '))
#     total = total + itemPrice
#
# print('The total price of items is', total)

# *******************************************************************
# *******************************************************************
# *******************************************************************

# EXAM2 18/04/2020
# import math
#
# def calculateEquation(a,b,c,d):
#     eq = 0
#     eq = math.sin((a+b)/d)*math.cos(c)
#     return eq
#
#
# a,b,c,d = eval(input("enter numbers seperated by "))
#
#
# if (d > 10 ) :
#      print(calculateEquation(a,b,c,d))
# elif (d <= 10):
#     print("invalid input")


#QUESTION 2
#
def getDiscount(price):
    discount = 0
    if price > 300:
     discount = 50
    else:
     discount = 20
    return discount

endvalue ='y'
order =1
sumItem =0
sumDiscount =0
sumTotal =0
while (endvalue == 'y'):
    price = int(input("Enter price #" + str(order) + ":"))

    if(price < 0):
        endvalue = 0
        print('invalid input ending program ')
        continue

    discount = getDiscount(price)
    print('Discount for #' + str(order)+' :'+str(discount))
    order +=1
    sumItem += price
    sumDiscount += discount
    sumTotal = sumItem - sumDiscount
    endvalue = (input("Do you want to enter another price (y for yes):  "))

print('----------------- INFO -------------------')
print('sum of discounts:',sumDiscount,'\nTotal Before the discount:',sumItem,'\nTotal after the discount:',sumTotal)
if(sumTotal  <= 0):
    print('invalid inputs')



