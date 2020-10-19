#Printing welcome message
print("**Welcome to the Divition Calculator**")
numOfLoop = eval(input("Enter the number of times you want to run calculator:"))
for i in range(numOfLoop):
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number:"))
    if num2 == 0:
        print("cannot divide by zero")
    else:
        result = num1 / num2
        print(num1, " ÷ ", num2, " = ", result)
