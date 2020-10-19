#FUNCTIONS Definctions

def add(a,b):
    return a+b
def maximum(x1,x2):
    return x1 if x1>x2 else x2

def void_function(x1,x2):
    print(x1+x2)

def B():
    print("B")
    if  True:
        return 10
    else:
        return  3
    return 5

def GDC(n1,n2):
    the_gdc = 1
    k=2
    while (k <= n1 ) and (k <= n2):
        if (n1 % k ==0) and (n2 % k ==0):
            the_gdc =k
        k +=1
    return the_gdc

def Primes(numberOfPrimes):
    NUMBER_OF_PRIMES_PER_LINE = 10
    count = 0
    number = 13
    print("the first 50 prime numbers are")
    while (count < numberOfPrimes):
         if isPrime(number):
            count += 1
            print(number,  end = " ")
            if count % NUMBER_OF_PRIMES_PER_LINE == 0:
                print()
         number += 1

def isPrime(number):
    divisor = 2
    while divisor <= number / 2:  # to be prime example     7 <= (13/2) 6.5
       if number % divisor == 0:
        return  False
       divisor += 1
    return True

#main method which containts the functions
def main():
    #print(add(2,5))
    #print(maximum(13,8))
    print(void_function(1,2))

#run main
#main()
#void_function('g','g')
#print(B())


#PAGE 98
#Positinal passing of parameters
print(maximum(x2=3,x1=4))
print(GDC(12,6))
Primes(50)

#PAGE 109 passing by value and no return value

#PAGE 150

#PAGE 154 Default arguemts for functions

def maximum2(x1=4,x2=6):
    return x1 if x1>x2 else x2

print(maximum2())


#MULTIPLE VALUES
def sort(n1,n2):
    if(n1<n2):
        return n1,n2
    else:
        return n2,n1

m1,m2 = sort(4,20)
print("n1 is ", m1)
print("n2 is ", m2)

