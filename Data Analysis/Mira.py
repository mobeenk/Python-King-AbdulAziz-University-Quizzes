# QUESTion 1
# noofdays = int(input('Enter the number of days:'))
#
# if (noofdays < 8):
#   print( "total amount is :",noofdays*120)
# elif (noofdays >= 8 and noofdays <= 14):
#   print("total amount is :", noofdays * 100)
# elif (noofdays >= 15 and noofdays <= 30):
#   # print("total amount is :", noofdays * 80)
# elif (noofdays > 30 ):
#   print("total amount is :", noofdays * 60)
# else:
#   print("invalid input")
#


# QUESTion 2
# sum = 0
# for i in range(5):
#     mark = int(input("enter mark of the student:"))
#     sum = sum + mark
#
# print("average hight of the student:", sum)

# QUESTION 3
import np as np
import pandas as p
import numpy as np
import matplotlib.pyplot as plt

data = p.read_excel("SalesData.xlsx", sheet_name="Dubai")
# data = data.dropna(how='any')           # assign back
# data.dropna(how='any', inplace=False)
data.plot(kind='bar',x='Units',y='Unit Cost')
plt.show()
print(data)
# data['Units'].replace('', 99, inplace=True)
# print(data["Units"].fillna(1))
# print(data.loc[0:5,'region':"item"])
# question 6
# dfGill = data.loc[(data['Rep'].__eq__('Gill')) & (data['Units'] < 40)]
# print(dfGill)
# question 7 average of unity group by Rep
# print(data.groupby('Rep')['Units'].mean())
# question 8
# print(data.sort_values(by=['Rep', 'Units'], ascending=(False, True)))
# question 9


#stuDF.loc[(stuDF['Births_Count']) and (stuDF['Hospital']=="Amal Hospital") and  (stuDF['Emirate_En']== "Dubai")]
#stuDF.sort_values(by=['Emirate_En', 'Births_Count'], ascending=(True, True))



