#LOOPS

count = 1
#while (count <= 10):
#    print("print",count)
#    count = count+1

#the_input = ''
# (the_input != 'quit'):
#    the_input = input("enter \n")
#PAGE 30



#while True:
 #   print("it's true")

# PAGE 63

#For loop
#for i in range(0,6 ,2): # same as range(6)   (start, end, step)
#    print(i)

# for i in range(10, 1, -2):  # same as range(6)   (start, end, step)
#     print(i)
# you cannot use floats in end parameter

#multiplication table
for i in range(1, 10, 1):  # same as range(6)   (start, end, step)
    if (i == 7):# continue leave the iteration and continue to next one
        continue
    for j in range(1,11,1):
        if(j == 5): #Break end the loop completely
            break
        print(str(i) +'*'+str(j)+'='+str(i*j) +'')
    print('===================')
print('done')


# #FActor
# n = eval(input("enter number \n"))
# factor = 2
# while (factor <= n):
#     if n  % factor == 0:
#         break
#     factor +=1
# print("the smallest fator",n,"is",factor)

#GDC PAGE 155
#PAGE 157 increase/decrease in %


#PAGE 207 difference

sum= 0
for i in range(4):
    if( i % 3 == 0):
        continue # when it's 3%3 ==0 it will skip adding it to sum
sum += i
print(sum)

#PAGE 212 alternative approach


#PRIMES // only can be divied on itself
NUMBER_OF_PRIMES = 50
NUMBER_OF_PRIMES_PER_LINE = 10
count = 0
number = 13
print("the first 50 prime numbers are")
while(count < NUMBER_OF_PRIMES):
    isPrime = True
    divisor = 2

    while divisor <= number / 2: # to be prime example     7 <= (13/2) 6.5
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count+=1
        print(format(number,'5d'),end = '')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()
    number+=1













