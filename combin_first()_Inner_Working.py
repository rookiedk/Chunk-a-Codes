import pandas as pd
import numpy as np

"""
Combine two dataframes in such a way that if 1st dataframe has empty values and 2nd dataframe has non-empty cells for same values,
the values from 2nd dataframe as substituted into the 1st dataframe.
"""
df = pd.DataFrame({"A":[1,np.nan], "B":[np.nan, 1]})
df_2 = pd.DataFrame({"A":[1,0], "B":[0,1]})
df = df.combine_first(df_2)
print df
"""
     A    B
0  1.0  0.0
1  0.0  1.0
"""

"""What is instead of np.nan we had a 'NAN' string"""
df_3 = pd.DataFrame({"A":[1,'NaN'], "B":['NaN', 1]})
df_4 = pd.DataFrame({"A":[1,0], "B":[0,1]})
df_3 = df_3.combine_first(df_4)
#print df_3
"""
     A    B
0    1  NaN
1  NaN    1
"""

"""In the absence of missing elements, combine_first has no effect and simply gives the  first df"""
df_5 = pd.DataFrame({"A":[2,2], "B":[2, 1]})
df_6 = pd.DataFrame({"A":[1,0], "B":[0,1]})
df_5 = df_5.combine_first(df_6)
#print df_5
"""   A  B
0  2  2
1  2  1
"""