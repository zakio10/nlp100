# 66

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.spearmanr.html

from scipy import stats
import pandas as pd
from gensim.models import keyedvectors

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

w2v_s_list = []
s_list = []


df = pd.read_csv('data/combined.tab', sep='\t')
# df = pd.read_csv('data/wordsim353/combined.tab', sep='\t')

for index, (w1, w2, s) in df.iterrows():
  s = s/10 # データセットのスコアは0-10なので0-1に正規化
  s_list.append(s)
  w2v_s = w2v.similarity(w1, w2)
  w2v_s_list.append(w2v_s)
  
 
correlation, pvalue = stats.spearmanr(w2v_s_list, s_list)
print(correlation)