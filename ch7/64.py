# 64
from gensim.models import keyedvectors
from tqdm import tqdm

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

with open('data/questions-words.txt') as f:
    data = f.readlines()

ans = []

for s in tqdm(data):
    s = s.rstrip()
    if s[0] == ':':
        column = s[2:]
        # print(column)
    else:
        words = s.split(' ')
        # print(words)
        # https://tedboy.github.io/nlps/generated/generated/gensim.models.Word2Vec.most_similar.html#gensim.models.Word2Vec.most_similar
        _ = w2v.most_similar(positive=[words[1], words[2]], negative=[words[0]], topn=1)[0]
        similar_word = _[0]
        similar_score = _[1]
        ans.append(' '.join([column]+words+[similar_word, str(similar_score)]))

# print(ans[:10])
with open('ans64.txt', mode='w') as f:
    f.write('\n'.join(ans))