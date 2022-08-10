import pandas as pd

n = input(">")
n = int(n)

df = pd.read_csv('popular-names.txt', sep='\t', header=None)

df = pd.qcut(df, n)

print(df)