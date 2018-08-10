import pandas as pd

#declare dictionary
dict1 = {'1': 'One',
         '2': 'Two',
         '3': ' '}

dict2 = {'We have': '1 tree',
         'They have': '2 trees',
         'They should have': '3 trees'}

df = pd.DataFrame(dict2.items(), columns=['neighbour', 'trees'])
#Replace partial substringof a df from a dictionary

# 1. Replace substring using just the column name
df1 = df
df1['trees'] = df['trees'].replace(dict1, regex=True)
print df1
#Output
#           neighbour      trees
# 0  They should have      trees
# 1           We have   One tree
# 2         They have  Two trees

# 2. Replace substring for last column
df1 = df
df1['trees'] = df.iloc[:,-1].replace(dict1, regex=True)
print df1
#output
#           neighbour      trees
# 0  They should have      trees
# 1           We have   One tree
# 2         They have  Two trees

# 3. Use sorted(dict.items()) in case of sorting before creating a dataframe
df1 = df
df1 = df1.sort_values('neighbour')
df1['trees'] = df1.iloc[:,-1].replace(sorted(dict1.items()), regex=True)
print df1
#output
#           neighbour      trees
# 2         They have  Two trees
# 0  They should have      trees
# 1           We have   One tree