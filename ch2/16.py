import pandas as pd

n = input(">")
n = int(n)

df = pd.read_csv('popular-names.txt', sep='\t', header=None)
k = int((len(df)+(n - 1)) / n + 0.5)

dfs = [df.loc[i:i+n-1, :] for i in range(0, len(df), k)]

for _df in dfs:
    print(_df.head())