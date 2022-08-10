import pandas as pd

n = input(">")
n = int(n)

df = pd.read_csv('popular-names.txt', sep='\t', header=None)

print(df.head(n))