#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC, abstractmethod


# In[ ]:


class Payment(ABC):
    def print_slip(self,amount):
        print('Purchase of amount: ', amount)
    @abstractmethod
    def payment(self, amount):
        pass


# In[ ]:


class CreditCardPayment(Payment):
    def payment(self, amount):
        print('Credit, card payment of: ', amount)


# In[ ]:


#criando objeto CreditCardPayment
obj = CreditCardPayment()
obj.payment(100)
obj.print_slip(100)
print(isinstance(obj, Payment))

