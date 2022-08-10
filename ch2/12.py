import pandas as pd

df = pd.read_csv('popular-names.txt', sep='\t', header=None)

print("==popular-names.txt==")
print(df.head())

df_col1 = df.iloc[:, 0]
df_col2 = df.iloc[:, 1]

print("\n==col1==\n", df_col1.head())
print("\n==col2==\n", df_col2.head())

df_col1.to_csv('col1py.txt', sep='\t',  index=False, header=False)
df_col2.to_csv('col2py.txt', sep='\t',  index=False, header=False)