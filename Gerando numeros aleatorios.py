import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#caso não tenha as bibliotecas instaladas:
#!pip install numpy
#!pip install matplotlib
#Gera numeros inteiros aleatórios entre 1 e 2000
n = 50 #tamanho da amostra
dados = np.random.randint(low = 1, high = 2000, size = n)

#vizualizando os dados gerados
plt.plot(dados)
plt.title("Números aleatorios entre 1-200")

#gera dados aleatorios a partir de uma distribuição normal
#parametros da função:
#loc: média
#scale: desvio padrão
#size: shape dos dados

dados = np.random.normal(loc = 15, scale = 5, size =100)

#gera uma vizualição dos dados gerados
plt.plot(dados)

#gerando o histograma
plt.hist(dados)

#gera dados aleatorios a partir de uma distribuição qui-quadrado
#parametros da função
#df: numeros de grau de liberdade
#size: shape dos dados

dados = np.random.chisquare(df = 3, size = 50)
#gera um histograma dos dados gerados
sns.displot(dados)

#gera dados aleatorios a partir de uma distribuição uniforme;
#parametrosd a função
#low: menor numero do intervalo[a,b]
#high: maior numero do intervalo[a,b]
#size: shape dos dados

dados = np.random.uniform(low = 1, high = 10, size = 100)

#gerando o histograma dos dados gerados
sns.displot(dados)

#gerando dados aleatórios a partir de uma distribuição normal padrão
dados = np.random.standard_normal(size = 1000)

#gerando histograma dos dados
sns.displot(dados)