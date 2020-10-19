import pandas as p
import math
import random
def main(p1,p2,p3):
    print(random.randint(0,2))

'''' main(1,p2=2,p3=3) 
sadfasdas
da
'''
data = p.read_excel("Grades.xlsx", sheet_name="list")

print("after modification")

empDF = pd.read_excel("Employee.xlsx", sheet_name="Year 2020")
data.dropna(how ='all')
data["Salary"].mean()

# print(data["preTestScore"].fillna(data["preTestScore"].mean(), inplace=True))
# print(data.fillna(0))
# print(data["age"].fillna(1))
# print(data.tail(6))
# print(data.fillna(data["postTestScore"].mean()))
# print(data['age'].replace('', 99, inplace=True))
# print(data.sort_values(by='preTestScore', ascending=True))

# DISPLAY ROWS WHERE DURATION MORE THAN 60

# print(data.loc[(data['age'] >= 40) & (data['preTestScore'] == 3.0)])
# print(data.loc[data['age'] == 42])
# print(data.sort_values(by=['age', 'sex'], ascending=False))
# print(data['age'].max())
# data.rename(columns={"age":"agenew",
#                      "sex":"sexy",},inplace = True)


# dropwill delete all rows that contain any missing data
# print(data)
# print(data.dropna())
# data
# delete rows that are missing all its data.
# data.dropna(how ='all')

# force dropna to work on columns you need to add axis=1.
# df_dropna(axis =1,how='all')

# fill in missing data with zero NaN=0
# data.fillna(0)

# data.columns
# data.tail()
# print(data[2:10]) #ignores row 10
# print(data.head(10))
# print(data[['first_name','last_name']])
# print(data.loc[0:5,'first_name':"sex"])
# print(data.loc[[3,4,6],'first_name':"sex"])
# print(data.iloc[1:3,0:2])

# make a certain column is the main index
# data.set_index("last_name",inplace=True)
# data.reset_index(inplace=True)
# data

# QUERY FUNCTIONS
# data["agenew"].describe()
# data["agenew"].sum()
# data["agenew"].count()
# print(data["agenew"].mean())
# print(data["age"].min())
# data["agenew"].min()
# data["agenew"].max()
# data

# NEW COLUMN WITH ASSIGNMENT
# data["sumcol"]= data["preTestScore"]+data["postTestScore"]
# print(data.head())


# WRITE TO EXCEL
# writer = p.ExcelWriter('NewDataa.xlsx')
# data.to_excel(writer,'Sheet1')
# writer.save()
