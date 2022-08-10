import pandas as pd

df_col1 = pd.read_csv('col1.txt', header=None)
df_col2 = pd.read_csv('col2.txt', header=None)

print(df_col1.head())
print(df_col2.head())

df = pd.concat([df_col1, df_col2],axis=1)

print(df.head())

df.to_csv('13_concat_py.txt', sep='\t', index=False, header=False)