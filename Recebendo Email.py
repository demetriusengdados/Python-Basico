#!/usr/bin/env python
# coding: utf-8

# In[1]:


import email
import imaplib


# In[2]:


EMAIL = 'Seu email do GMAIL'
PASSWORD = 'Sua senha'
SERVER = 'imap.gmail.com'

#Monta a conexão

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
status, data = mail.search(None, 'ALL')
mail_ids = []

for block in data:
    mail_ids += block.split()


# In[ ]:




