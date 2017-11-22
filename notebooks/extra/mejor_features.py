# scikit learn nos puede ayudar a elegir las mejores features

import matplotlib.pyplot as plt

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import mutual_info_regression

# k es el numero de features que queremos

selector = SelectKBest(mutual_info_regression, k=4)
selector.fit(X,y)

# ahora vemos resultados

scores = selector.scores_

# y los graficamos

plt.rcParams['figure.figsize'] = [12,8]
plt.plot(scores)
plt.xticks(np.arange(7),list(X.columns))
plt.show()