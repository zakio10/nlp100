import pandas as pd


df = pd.read_csv('popular-names.txt', sep='\t', header=None)
df = df.sort_values(2, ascending=False)
df = df.reset_index(drop=True)

print(df)

#             0  1      2     3
# 0       Linda  F  99689  1947
# 1       Linda  F  96211  1948
# 2       James  M  94757  1947
# 3     Michael  M  92704  1957
# 4      Robert  M  91640  1947
# ...       ... ..    ...   ...
# 2775    Annie  F   1326  1881
# 2776   Bertha  F   1324  1881
# 2777   Bertha  F   1320  1880
# 2778    Alice  F   1308  1881
# 2779    Sarah  F   1288  1880

# [2780 rows x 4 columns]