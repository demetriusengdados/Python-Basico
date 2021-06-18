#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*


# In[ ]:


me = Tk()
me.geometry("354x460")
me.title("Calculadora")
melabel = Label(me,text="Calculadora",bg='White',font=("Times",30,"bold"))
melabel.pack(side=TOP)
me.config(background='Dark gray')

textin=Stringvar()
operator=""


# In[ ]:


def clickbut(number):   #lambda:clickbut(1)
    global operator
    operator = operator + str(number)
    textin.ste(operator)


# In[ ]:


def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''


# In[ ]:


def equbult():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator =''


# In[ ]:


def equbult():
    global operator
    add = str(eval(operator))
    textin.set(sub)
    operator = ''


# In[ ]:


def equbult():
    global operator
    add = str(eval(operator))
    textin.add(mul)
    operator = ''


# In[ ]:


def equbult():
    global operator
    add = str(eval(operator))
    textin.add(div)
    operator = ''


# In[ ]:


def clrbut():
    textin.set('')


# In[ ]:


metext = Entry(me, fonot=("Courier New",12,'bold'),textvar=textin,width=25,bd=5,bg'powder blue')
metext.pack()


# In[ ]:


but1=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(1),text=1,font=("Courier New",16,bold))
but1.place(x=10, y=100)


# In[ ]:


but2=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(2),text=2,font=("Courier New",16,bold))
but2.place(x=10, y=170)


# In[ ]:


but3=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(3),text=3,font=("Courier New",16,bold))
but3.place(x=10, y=240)


# In[ ]:


but4=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(4),text=4,font=("Courier New",16,bold))
but4.place(x=75, y=100)


# In[ ]:


but5=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(5),text=5,font=("Courier New",16,bold))
but5.place(x=75, y=170)


# In[ ]:


but6=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(6),text=6,font=("Courier New",16,bold))
but6.place(x=75, y=240)


# In[ ]:


but7=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(7),text=7,font=("Courier New",16,bold))
but7.place(x=140, y=100)


# In[ ]:


but8=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(8),text=8,font=("Courier New",16,bold))
but8.place(x=140, y=170)


# In[ ]:


but9=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(9),text=9,font=("Courier New",16,bold))
but9.place(x=140, y=240)


# In[ ]:


but0=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout(0),text=0,font=("Courier New",16,bold))
but0.place(x=10, y=310)


# In[ ]:


butdot=Button(me,padx=47,pady=14,bd=4,bg='white',command=Lambda:clickout("."),text=".",font=("Courier New",16,bold))
butdot.place(x=75, y=310)


# In[ ]:


butp1=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout("+"),text="+",font=("Courier New",16,bold))
butp1.place(x=205, y=100)


# In[ ]:


butsub=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout("-"),text='-',font=("Courier New",16,bold))
butsub.place(x=205, y=170)


# In[ ]:


butm1=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout("*"),text='*',font=("Courier New",16,bold))
butm1.place(x=205, y=240)


# In[ ]:


butdiv=Button(me,padx=14,pady=14,bd=4,bg='white',command=Lambda:clickout("/"),text="/",font=("Courier New",16,bold))"
butdiv.place=(x=205, y=310)


# In[ ]:


butclear=Button(me,padx=14,pady=119,bd=4,bg='white',command=clrbut,text="CE",font=("Courier New",16,bold))
butclear.place(x=270, y=100)


# In[ ]:


butequal=Button(me,padx=151,pady=14,bd=4,bg='white',command=equbut,text="=",font=("Courier New",16,bold))
butequal.place(x=10, y=380)
me.mainloop()

