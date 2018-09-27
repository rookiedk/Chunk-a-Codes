#BASIC PANDAS - DATAFRAME MANIPULATION
#NEXT ITERATION - do this for entire df instead of single column
import pandas as pd
my_dict = {'A':[1000, 2000, 34999],
      'B':[10000, 23339, 1000000]}
df = pd.DataFrame.from_dict(my_dict)
#1. Convert a column in a dataframe into a thousands-separated, $-symbol-added column
df['A'] = df.apply(lambda x: "${:,.2f}".format(x['A']), axis=1)

#2. Convert a column in a dataframe into a thousands-separated, Million-symbol column
df['B'] = '$' + (df['B'].astype(float) / 1000000).round(2).astype(str) + 'M'
print df

"""OUTPUT:
            A       B
0   $1,000.00  $0.01M
1   $2,000.00  $0.02M
2  $34,999.00   $1.0M

"""