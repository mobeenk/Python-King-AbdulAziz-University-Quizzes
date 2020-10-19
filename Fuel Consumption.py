cost = distance = 0
cities = eval(input("Enter the number of cities : "))
for i in range(cities):
    distance = eval(input("Enter the distance to the city #"+str(i+1)+":"))
    cost += distance
cost *= 0.25
print('{0} {1} {2} '.format('The cost of fuel consumption is :', cost, " SR"))
