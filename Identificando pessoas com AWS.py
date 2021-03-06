#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import json


# In[6]:


def recognize_celebrites(photo):
    #cria o serviço com as suas credenciais da aws
    
    client=boto3.client(
    service_name='rekognition',
    region_name='us=east-1',
    aws_acess_key_id='Sua Acess Key',
    aws_secret_acess_key='Sua Secret Key'
    )


# In[7]:


#Envia a imagem para analise no servico aws rekognition e capatura resultados

with open(photo, 'rb') as image:
    response = client.recognize_celebrites(Image={'Bytes': image.read()})


# In[ ]:


#Mostra resultados obtidos
for celebrity in response['CelebrityFaces']:
    print('\n Nome: ' + celebrity['Name'])
    print('Id: ' + celebrity['Id'])
    print('Posição: ')
    print('Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
    print('Top: ' + '{:.2f}'.format(celebrity['Face']['BoudndingBox']['Top']))
    print('Info')
    for url in celebrity['Urls']:
        print('  ' + url)
    print
return len(response['CelebrityFaces'])


# In[ ]:


def main():
    photo = input('Digite o local onde está a imagem: ')
    
    celeb_count=recognize_celebrites(photo)
    print('\n Celebridades detectadas: ' + str(celeb_count))
    
if __name__ == '__main__':
    main()

