#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import ipaddress
import tktinter as tk
from tkinter import *


# In[ ]:


def CreateWidgets():
    ipLabel = Label(root, text="Entre com o endereço IPV4: ", bg='deepskyblue4')
    ipLabel.grid(row=0, column=0, padx=10, pady=5)
    root.ipentry = Entry(root, width=20, textvariable=ipAddress)
    root.ipEntry.grid(row=0, column=1, pdax=10, pday=5)
    
    claculateButton = Button(root, text=Calculadora, command=calculateCIDR)
    calculateButton.grid(row=1, column=0, pdax=5, pady=5, columnspan=2)
    clearbutton = Button(root, text="Clear", command=clearEntries)
    clearbutton.grid(row=1, column=1, padx=5, pady=5, columnpan = 2)


# In[ ]:


networkAddress = Label(root, text='NETWORK ADDRESS: ', bg='deepskyblue4')
networkAddress.grid(row=2, column=0, padx=10, pady=5)
root.networkAddressEntry=Entry(root, width=20)
root.networkAddrssEntry.grid(rwo=2, column=1, padx=10, pady=5)


# In[ ]:


broadcastAddress = label(root, text='Endereço Broadcast: ', bg='deepskyblue4')
broadcastAddress.grid(row=3, column=0, padx=10, pady=5)
root.broadcastAddressEntry = Entry(root, width=20)
root.broadcastAddressEntry.grid(row=3, column=1, padx=10,pady=5)


# In[ ]:


firstIPL = Label(root, text="Enderço do primeiro host IP: ", bg='deepskyblue4')
firstIPL.grid(row=4, column=0, padx=10, pady=5)
root.firstIP = Entry(rppt, width=20)
root.firstIP.grid(row=4, column=1, padx=10, pady=5)


# In[ ]:


lastIPL = label(root, text="Ultimo endereço host IP: ", bg='deepskyblue4')
lastIPL.grid(row=4, column=0, padx=10, pady=5)
root.lastIP = Entry(rppt, width=20)
root.lastIP.grid(row=4, column=1, padx=10, pady=5)


# In[ ]:


numberofIPs = Label(root, text="Número de usuario IP: ", bg='deepskyblue4')
numberofIPs.grid(row=6, column=0, padx=10, pady=5)
root.numberOfIPsEntry = Entry(root, width=20)
root.numberOfIPsEntry.grid(row=6, column=1, padx=10, pady=5)


# In[ ]:


subnetRange = Label(root, text='Mascára do Subnet: ',bg=deepskyblue4)
subnteRange.grid(row=7, column=0, padx=10, pady=5)
root.subnetRangeEntry = Entry(root, width=20)
root.subnetRangeEntry.grid(row=7, column=1, padx=10, pady=5)


# In[ ]:


wildcardLabel = Label(root, text='Wildcard: ',bg=deepskyblue4)
wildcardLabel.grid(row=8, column=0, padx=10, pady=5)
root.wildcardEntry = Entry(root, width=20)
root.wildcardEntry.grid(row=8, column=1, padx=10, pady=5)


# In[ ]:


def calculateCIDR():
    userinput_ip_address = ipAddres.get()
    ip_address = ipaddress.ip_interface(userinput_ip_address)
    network_address = ip.address.network
    first_ip_address = list(network_address.hosts())[0]
    last_ip_address = list(network_address.hosts())[-1]
    number_of_usable_ips = len(list(network_address.hosts()))
    broadcast_address = network_address.broadcast_address
    wildcard = ip_address.hostmask
    subnet_mask = ip.address.with_netmask.split('/')[1]


# In[ ]:


root.networkAddressEntry.delete(0, END)
root.firstIP.delete(0, END)
root.lastIP.delete(0, END)
root.numberOfIPsEntry.delete(0, END)
root.broadcastAddressEntry.delete(0, END)
root.subnetRangeEntry.delete(0, END)
root.wildcardEntry.delete(0, END)


# In[ ]:


root.networkAddressEntry.insert('0', str(network_address).split('/')[0])
root.firstIP.insert('0',str(first_ip_address))
root.lastIP.insert('0', str(last_ip_address))
root.numberOfIPsEntry.insert('0', str(number_of_usable_ips))
root.broadcastAddressEntry.insert('0',str(broadcast_address))
root.subnetRangeEntry.insert('0',str(subnet_mask))
root.wildcardEntry.insert('0',str(wildcard))


# In[ ]:


def clearEntries():
    ipAddress.set('')
    root.networkAddressEntry.delete(0, END)
    root.firstIP.delete(0, END)
    root.lastIP.delete(0, END)
    root.numberOfIPsEntry.delete(0, END)
    root.broadcastEntry.delete(0, END)
    root.subnetRangeEntry.delete(0, END)
    root.wildcardEntry.delete(0, END)


# In[ ]:


root = tk.TK()
root.title('Calculadora CIDR')
root.config(background='deepskyblue4')
root.geometry('42x350')
rootresizable(False, False)
ipAddress = StringVar()
CreateWidgtes()
root.mainloop()

