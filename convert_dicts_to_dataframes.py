"""BASIC CHUNK - Converting Dictionaries into Dataframes"""
import pandas as pd
#Convert a normal Dictionary to Pandas Dataframe
#Con - All arrays of the dict values have same length
my_dict = {'A': [1,2,3],
           'B': [1,4,3],
           'C': [1,2,4]}
df = pd.DataFrame.from_dict(my_dict)
print df
"""OUTPUT:
   A  B  C
0  1  1  1
1  2  4  2
2  3  3  4"""
#Convert a dictionary with values of different lengths  into a pandas Dataframe

my_dict = {'A': [1,2,3],
           'B': [1,2,3,4],
           'C': [1,2,4,5,6]}
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in my_dict.iteritems()]))
print df
"""OUTPUT:
     A    B  C
0  1.0  1.0  1
1  2.0  2.0  2
2  3.0  3.0  4
3  NaN  4.0  5
4  NaN  NaN  6
"""