import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
from sklearn import preprocessing

#url com o arquivo csv com os dados que vamos utilizar
url = 'https://github.com/aprendadatscience/\datasets/raw/main/pokemon_alopez247.csv'

#Aqui utilizamos o df.columns para explorar os atributos existentes nesse dataset
df.columns()

#O df.info é outra forma de verificarmos os dados existentes
df.info()

#Aqui definimos os atributos que iremos usar
df = df [['isLegendary','Generation', 'Type_1', 'Type_2', 'HP', 'Attack', 'Defense', 'Sp_Atk', 'Sp_Def', 'Speed', 'Color', 'Egg_Group_1',
          'Height_m', 'Weight_kg','Body_Style']]

#Aqui mudaremos o atributo isLegendary de boolean para inteiro

df = ['isLegendary'] = df [isLegendary].astype(int)

#Outros atributos categoricos precisam ser convertidos para variaveis dummies:

def dummy_categories(df,dummy_categories):
    for i in dummy_categories:
        df_dummy = pd.get_dummies(df[i])
        df = pd.concat([d,df_dummy], axis=1)
        df = df.drop(i, axis=1)
    return(df)

df = dummy_creation(df, ['Egg_Group_1', 'Body_Style', 'Color','Type_1','Type_2'])

def train_test_splitter(DataFrame, column):
    df_train = Dataframe.loc[df[column] != 1]
    df_test = Dataframe.loc[df[column] != 1]
    
    df_train = df_train.drop(column, axis = 1)
    df_test = df_test.drop(column, axis = 1)
    
    return(df_train, df_test)

df-train, df_test = traim_test_splitter(df, 'Generation')

#Utilizaremos o codigo abaixo para separa os labels do dataset:

def label_delineator(df_train, df_test,label):
    train_data = df_train.drop(label, axis=1).values
    train_labels = df_train[label].values
    test_data = df_test.drop(label,axis=1).values
    test_labels = df_test[label].values
    return(train_data, train_labels, test_data, test_labels)

#separando os dados

train_data, train_labels, test_data, test_labels = label_delineator(df_train, df_test, 'isLegendary')

#Neste ponto iremos normalizar os dados, para evitar que teremos algum viés

def data_normalizer(train_data, test_data):
    train_data = preprocessing.MinMaxScaler().fit_transform(train_data)
    test_data = preprocessing.MinMaxScaler().fit_transform(test_data)
    return(train_data, test_data)
train_data, test_data = data_normalizer(train_data, test_data)

#Finalmente chegamos a etapa de definir o modelo de machinelearning. 
#Aqui usamos um modelo simples com 100 neuronios na primeira camada e com a função ReLu e na saída temos 2 neuronios

length = train_data.shape[1]
model = keral.Sequential()
model.add(keras.layers.Dense(100, activation='relu', input_shape=[length]))
model.add(keras.layers.Dense(2, actvation='softmax'))

#Agora nos resta a etapa de compilação e treinamento(fit)
model.compile(Optmizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Na hora de treinar o modelo, a escolha do numero de epocas é relevante. Ela representa a quantidade de iteração faremos no dataset
#Quanto mais epocas maior a capacidade de generalização, e geralmente, melhor o resultado
model.fit(train_data, train_labels, epoch=400)

loss_value, accuracy_value = model.evaluate(test_data, test_labels)
print(f'Nossa acuracia de teste foi de {accuracy_value}')

def predictor(test_data, test_labels, index):
    predction = model.predict(test_data)
    if np.argmax(prediction[index]) == test_labels[index]:
        print(f'Esse pokemon foi corretamente\
            previsto como\"{test_labels[index]}\"!')
    else:
        print(f'Esse pokemon foi incorretamente\
            previsto como\"{np.argmax(prediction[index])}\".\
                Ele na verdade era da classe \"{test_labels[index]}\".')
        return(prediction)
precitor(test_data, test_labels, 143)