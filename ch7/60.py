# 60
from gensim.models import keyedvectors

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

print(w2v['United_States'])