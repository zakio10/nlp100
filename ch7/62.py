# 62
from gensim.models import keyedvectors

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

# https://tedboy.github.io/nlps/generated/generated/gensim.models.Word2Vec.similar_by_word.html#gensim.models.Word2Vec.similar_by_word
for _ in w2v.similar_by_word("United_States", topn=10):
    print("word: {:20s}, score: {:10f}".format(_[0], _[1]))