#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#pip3 install wmi

import wmi

#carrega informações

c = wmi.WMI()
my_system = c.Win32_ComputerSystem()[0]

#mostrando resultados

print(f"Marca: {my_system.Manufacture}")
print(f"Modelo: {my_system.Model}")
print(f"Nome: {my_system.Name}")
print(f"Qtde CPU's: {my_system.NumberOfProcessors}")
print(f"Arquitetura: {my_system.SystemType}")
print(f"Familia: {my_system.SystemFamily}")

