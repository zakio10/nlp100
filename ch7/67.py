# 67
# https://pypi.org/project/pycountry/
import pycountry
from gensim.models import keyedvectors
from sklearn.cluster import KMeans
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

countries = [_.name for _ in pycountry.countries]

countries_v = []
for _ in countries:
    try:
        countries_v.append(w2v[_])
    except:
        countries_v.append([0.0]*300)

kmeans = KMeans(n_clusters=5, random_state=0).fit(countries_v)

for n, l in zip(countries, kmeans.labels_):
  print("{:60s}{}".format(n, l))
