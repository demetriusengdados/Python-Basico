#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install boto3


# In[2]:


import boto3


# In[ ]:


#Cria o serviço com as suas credenciais da AWS
ses = boto3.client(
    service_name = 'ses',
    region_name = 'us-east-1',
    aws_acess_key_id = '***Sua chave de acesso***',
    aws_secret_acess_key = '***Sua chave secreta***')


# In[ ]:


#envia o email atraves do serviço SES da AWS
ses.semd_email(
    Destiantion={
        'ToAddresses': [
            'destinatario@gmail.com'  #E-mail que vai receber
        ],
    },
    Message={
        'Body': {
           'Text': {
               'Charset': 'utf-8',
               'Data': 'Olá destinatario',    #texto do email
           }, 
        },
        'Subject': {
            'Charset': 'utf-8',
            'Data': 'Enviando email pela AWS',    #Assunto do email
        },
    },
    Source='*** Seu email para envio***' # email que vaia fazer o envio
)


# 
