nPayments = 0
sum = 0
nPayments = eval(input("Enter the number of installments: "))

for i in range(nPayments):
    installment = eval(input("Enter installment#:"+str(i+1)+":"))
    sum += installment
sum *= 12
print("The total annual of installments is :" ,  sum)
