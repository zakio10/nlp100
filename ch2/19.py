import pandas as pd


df = pd.read_csv('popular-names.txt', sep='\t', header=None)
vc = df[0].value_counts()

print(vc)

# James      118
# William    111
# Robert     108
# John       108
# Mary        92
#           ... 
# Scott        1
# Rachel       1
# Kelly        1
# Crystal      1
# Lucas        1
# Name: 0, Length: 136, dtype: int64