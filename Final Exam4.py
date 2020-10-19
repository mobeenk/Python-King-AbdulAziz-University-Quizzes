# QUESTION 1

# stores_username = "Jameel"
# stores_password = "Cpit110"
#
# username = (input('Enter the user name:'))
# password = (input('Enter the password: '))
#
# if (username.__eq__(stores_username) and   password.__eq__(stores_password)) :
#      print( "Welcome Mr.Jameel")
# elif username.__eq__(stores_username) and not(password.__eq__(stores_password)):
#     print("wrong username or password")
# elif not username.__eq__(stores_username) and (password.__eq__(stores_password)):
#     print("wrong username or password")
# else:
#      print("both are wrong")

# QUESTION 2

# sumincome = 0
# no_of_jobs = int(input('Enter number of Jobs :'))
# for i in range(no_of_jobs):
#     income = int(input("Enter income #" + str(i + 1) + '  : '))
#     sumincome = sumincome + income
#
# print('The total annual income is', sumincome * 12)

#*******************************************************************
#*******************************************************************
#*******************************************************************

#EXAM2 18/04/2020



# import math
#
#
# def calculateEquation(a, b, c, d):
#     eq = 0
#     eq = math.sqrt((a - b) + math.pow((c + d), 2))
#     return eq
#
# final =0
# a, b, c, d = eval(input("enter numbers seperated by "))
# final = calculateEquation(a, b, c, d)
# if (final > 5):
#     print('the result is:',final)
#     print('High number')
# elif (final <= 10):
#     print('the result is:', final)
#     print("normal number")




#QUESTION 2

def getTaxAccount(totalPurchases):
    tax = 0
    tax = totalPurchases *(5/100)
    return tax

endvalue =1
sumItem =0
sumVAT =0
sumTotal =0
item =0
VAT =0
while (endvalue != 0):
    item = int(input("Enter purchases value #" + str(endvalue) + ":"))
    endvalue += 1
    if(item < 0 or item == 0):
        endvalue = 0
        print('invalid input ending program ')
        continue

    VAT = getTaxAccount(item)
    total = item + VAT
    sumItem += item
    sumVAT += VAT
    sumTotal += total

print('The Tax amount:',sumVAT,'\ntotal of purchases:',sumItem,'\nTOTAL purchases after tax:',sumTotal)



