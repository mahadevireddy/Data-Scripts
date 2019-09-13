import os
import pandas as pd

current_directory = os.getcwd()
a = current_directory +'\\files'
result = str(a)+ '\\result.xlsx'
b = os.listdir(a)
file1 = str(a)+"\\" + b[1]
file2 = str(a) +"\\" + b[2]

read_table1 = pd.read_excel(file1, sheet_name='Sheet1')
read_table2 = pd.read_excel(file2, sheet_name='Sheet1')

read_table1 = read_table1.iloc[1:]
read_table1.columns = read_table1.iloc[0]
read_table1 = read_table1.iloc[1:]

read_table2 = read_table2.iloc[1:]
read_table2.columns = read_table2.iloc[0]
read_table2 = read_table2.iloc[1:]

combined_table = pd.concat([read_table1,read_table2])

table_reshaping = pd.DataFrame(combined_table.pivot_table(index='RULE NAME',columns='EXTRACT DATE', values='#ACCTS IMPACTED',aggfunc='sum'))

table_reshaping['Difference_Percent'] = 100 - ((table_reshaping.iloc[:,1]*100)/table_reshaping.iloc[:,0])

table_reshaping['Difference_Percent'] = table_reshaping['Difference_Percent'].round(2)

table_reshaping.to_excel(result, 'sheet1')


