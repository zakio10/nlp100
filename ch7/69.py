# 69
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
# https://pypi.org/project/pycountry/
import pycountry
from gensim.models import keyedvectors
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans
# https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
from sklearn.manifold import TSNE
import numpy as np


w2v = keyedvectors.load_word2vec_format("data/GoogleNews-vectors-negative300.bin", binary=True)

countries = [_.name for _ in pycountry.countries]
countries_ = []

countries_v = []
for _ in countries:
    try:
        countries_v.append(w2v[_])
        countries_.append(_)
    except:
        # countries_v.append([0.0]*300)
        pass

countries_v = np.array(countries_v)

x_embedded = TSNE(n_components=2, learning_rate='auto', init='random', perplexity=3).fit_transform(countries_v)
# z = linkage(countries_v, 'ward', metric='euclidean')
print(x_embedded)

# plt.figure(figsize = (30, 30))
plt.scatter([_[0] for _ in x_embedded], [_[1] for _ in x_embedded])
for i, txt, x, y in enumerate(zip(countries_, x_embedded)):
    plt.annotate(txt, (x, y))
plt.savefig('graph69.png')