# 68
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.hierarchy.linkage.html
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
# https://pypi.org/project/pycountry/
import pycountry
from gensim.models import keyedvectors
# https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html
from sklearn.cluster import KMeans

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

z = linkage(countries_v, 'ward', metric='euclidean')
print(z)

plt.figure(figsize=(25, 10))
dn = dendrogram(z, labels=countries_)
# plt.show()
plt.savefig('graph68.png')