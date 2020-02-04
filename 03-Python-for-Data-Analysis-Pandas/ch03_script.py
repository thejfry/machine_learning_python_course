import numpy as np
import pandas as pd
from numpy.random import randn
import lxml

# single index dataframe
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())

df.reset_index(inplace=True)
df['Provinces'] = 'BC AB SK MB ON'.split()
df.set_index('Provinces', inplace=True)
df.reset_index(inplace=True)

print(df)

# multi-index dataframe
out_idx = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
in_idx = [1, 2, 3, 1, 2, 3]
heir_idx = list(zip(out_idx, in_idx))
heir_idx = pd.MultiIndex.from_tuples(heir_idx)

df2 = pd.DataFrame(np.random.randn(6, 2), index=heir_idx, columns=['A', 'B'])

print(df2)

# reading in data
df_csv = pd.read_csv('example')
print(df_csv)

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
df_html = pd.read_html(url)
print(df_html[0])