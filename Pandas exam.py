import pandas as p
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# from prettytable import PrettyTable

desired_width = 450
p.set_option('display.width', desired_width)
p.set_option('display.max_columns', 12)
p.set_option('display.max_rows', 140)
p.options.display.float_format = '{:,.0f}'.format
data = p.read_excel("C:\\Users\\asus\PycharmProjects\\first\\Data\cod.xlsx", sheet_name="s1")
data = data.rename(columns={"no. of accidents": "#accidents", "Type of Accident_ar": "Accident_type_AR",
                            "Type of Accident_en": "Accident_type_EN", "Emirate_en": "e_en"})
# df1 = data.dropna()
# data.set_index("Year", inplace=True)

# data = data.dropna(axis=1, how='all')
# data = data.dropna(how='all')
# data = data.fillna(0)

# data =data.drop(['order'], axis=1)
# data.reset_index(drop=True, inplace=True)
# data = data.sort_values('#accidents', ascending=True, inplace=False)

# 1 Number of Accidents per years
# acc_per_year = data.groupby('year', as_index=False)['#accidents'].sum().round()
# acc_per_year = acc_per_year.sort_values('#accidents', ascending=False)

# print(acc_per_year)

# 2 Types of Accidents in Emirates
# acc_types = data["Accident_type_EN"].unique()
# gg = data.groupby('Accident_type_EN', as_index=False)['#accidents'].unique()
# print(acc_types)
# 3 Acccidents in Emirates

# acc_of_emirates = data.groupby(['e_en'], as_index=False)['#accidents'].sum().round()
# acc_of_emirates = acc_of_emirates.sort_values('#accidents', ascending=False)
# print(acc_of_emirates)
'''
writer = p.ExcelWriter('cnt_by_type.xlsx')
acc_of_emirates.to_excel(writer, 'Sheet1')
writer.save()
'''


# 4 MIN MAX MEAN
# em_min = data.groupby('e_en', as_index=False)['#accidents'].min()
# em_max = data.groupby('e_en', as_index=False)['#accidents'].max()
# min_max = em_min.append(em_max)
# mean_of_minmax = min_max.mean()
# print(em_max)
# print(mean_of_minmax)
# print(min_max)
# print(min_max)
# 5 count of acc types

# cnt_by_type = data.groupby(['Accident_type_EN', 'e_en', '#accidents']).sum()
# cnt_by_type = cnt_by_type.sort_values(by=['Accident_type_EN', 'year'], ascending=(False, False))

# print(cnt_by_type)

# 6 Expectations if -10%
# estimation = data
# estimation["Year2003"] = estimation["#accidents"] - ((estimation["#accidents"] * 10) / 100)
# estimation["Year2004"] = estimation["Year2003"] - ((estimation["Year2003"] * 10) / 100)
# estimation["Year2005"] = estimation["Year2004"] - ((estimation["Year2004"] * 10) / 100)
# est = estimation[['e_en','Year2003']].head(7)
# print(estimation[['Accident_type_EN','#accidents','e_en','Year2003', 'Year2004','Year2005']].head(7))
# print(est)

# 7
# count_by_type = data.groupby('Accident_type_EN', as_index=False)['#accidents'].sum()
# best_results = count_by_type[count_by_type["#accidents"] > 1000]
# print(count_by_type)
# print(best_results)
# print(best_results[best_results["#accidents"] > 70])

# with p.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
# print(tabulate(cnt_by_type[0:140], showindex="always" ,headers="keys", tablefmt="orgtbl"))

# acc_of_emirates.set_index("e_en", inplace=True)
# print(acc_of_emirates)

# est['Year2003'].plot.pie(autopct='%.2f')
# acc_of_emirates[['e_en', '#accidents']].plot.bar( color=["green"])
# acc_of_emirates.plot( kind='bar',x='e_en',y='#accidents' )


# style
# plt.style.use('seaborn-darkgrid')

# create a color palette
# palette = plt.get_cmap('Set1')

# plt.plot(acc_per_year['#accidents'], acc_per_year['year'], marker='', color=palette(0), linewidth=1, alpha=0.9,label='')

# Add legend
# plt.legend(loc=2, ncol=2)

# Add titles
# plt.title("Plot for Accidents in each Emirate", loc='left', fontsize=12, fontweight=0, color='blue')
# plt.xlabel("Emirate")
# plt.ylabel("Accidents")
# plt.show()


# count_rows = df['Type of Accident_ar'].count()
# print(data.head(10))
# print(df1.to_string())
# print(df.to_string())
# print('number of rows',count_rows)
# data = data.dropna(how='any')           # assign back
# data.dropna(how='any', inplace=False)
# data['no. of accidents'].plot()
# data[['no. of accidents','Emirate_en']].plot()

# float to int
# p.options.display.float_format = '{:,.0f}'.format
# print(data.groupby('year')['no. of accidents'].sum().round())
# grouped = data.groupby('Emirate_en', as_index=False)['no. of accidents'].sum().round()
# data.rename(columns={"Emirate_en":"agenew","no. of accidents":"sexy",},inplace = True)

# print(grouped)

'''
sdsds
sdfs
'''
# grouped.sort_values('Emirate_en', ascending=False)
# print(data.to_string())
