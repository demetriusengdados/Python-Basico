from sklearn.datasets import load_iris
iris = load_iris()
from skelarn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=10)

#treinando o modelo
model.fit(iris.data, iris.target)

#selecionando uma das arvores para mostrar
estiamtor = model.estimators_[5]

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

#gera o objeto que ira armazenar a arvore

fig = plt.figure(figsize(15,10))
#plota a arvore desejada

plot_tree(estimator,
          feature_name=iris.feature_names,
          class_names=iris.target_names,
          filled=True, impurity=True,
          rounded=True)
