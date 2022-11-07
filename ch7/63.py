# 63
from gensim.models import keyedvectors

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

# https://tedboy.github.io/nlps/generated/generated/gensim.models.Word2Vec.most_similar.html#gensim.models.Word2Vec.most_similar
for _ in w2v.most_similar(positive=["Spain", "Athens"], negative=["Madrid"]):
    print("word: {:25s}, score: {:10f}".format(_[0], _[1]))

# word: Greece                   , score:   0.689848
# word: Aristeidis_Grigoriadis   , score:   0.560685
# word: Ioannis_Drymonakos       , score:   0.555291
# word: Greeks                   , score:   0.545069
# word: Ioannis_Christou         , score:   0.540086
# word: Hrysopiyi_Devetzi        , score:   0.524845
# word: Heraklio                 , score:   0.520776
# word: Athens_Greece            , score:   0.516881
# word: Lithuania                , score:   0.516687
# word: Iraklion                 , score:   0.514679