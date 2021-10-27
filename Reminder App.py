#!/usr/bin/env python
# coding: utf-8

# Primeiro faça um banco de dados e uma tabela para manter as tarefas

# In[ ]:


CREATE DATABASE to_do
USE to_do
CREATE TABLE tasks(task varchar(225));


# Instalação

# In[ ]:


pip install my-sql-connector-python


# In[ ]:


import tkinter as tk
from tkinter.messagebox import *
import mysql.connector as mysql


# In[ ]:


mycon = mysql.connect(
    user='USERNAME',
    passwd='PASSWORD',
    host='localhost',
    database='to_do'
)


# In[ ]:


def add_to_db(task):
    mycur = mycon.cursor()
    mycur.execute('INSERT into tasks(task) values("{}")'.format(task))
    mycon.commit()


# In[ ]:


def delete_from_db(task):
    mycur = mycon.cursor()
    mycur.execute('DELETE from tasks where task = "{}"'.format(task))
    mycon.commit()
    def add_task():
        task = task_entry.get()
        if task != '':
            tasks_list.insert(tk.END,task)
            add_to_db(task)
            task_entry.delete(0,tk,END)
        else:
            showerror('Error', 'Please enter a task')


# In[ ]:


def del_task():
    try:
        selection = task_list.curselection()[0]
        task = tasks_list.get(selection)
        delete_from_db(task)
        tasks_list.delete(selection)
    except:
        showerror("Error", 'Please select a task to delete')


# In[ ]:


def load_task():
    tasks_list.delete(0,tk.END)
    mycur = mycon.cursor()
    mycur.execute('select * from tasks')
    tasks = mycur.fetchall()
    if len(tasks) = 0:
        showerror('No tasks!', 'As tasks não foram salvas')
    for tasks in tasks:
        tasks_list.insert(tk.END,task[0])      


# In[ ]:


root = tk.TK()
root.config(bg='#edge3d9')
root.title('to-do-app.py')
root.geometry('290x420+550+250')
root.iconbitmap('icon.ico')


# In[ ]:


bg_picture = tk.PhotoImage(file='todo_bg.png')
bg = tk.Label(root, image=bg_picture)
bg.pack()


# In[ ]:


tasks_list = tk.Listbox(root,width=50, font=('Times', 15),bg='#ede3d9', fg='#000000')
tasks_list.pack()


# In[ ]:


task_entry = tk.Entry(root,width=50, font=('Times', 15), bg = '#ede3d9', fg='#000000')
task_entry.pack()


# In[ ]:


add task_button = tk.Button(root, text='Add Task', command=add_task_width=45,
                           font=('Helvetica', 10), bg='#ede3d9', fg='#000000', relief=tk.FLAT)
add_task_button.pack()


# In[ ]:


delete_task_button = tk.Button(root, text='Delete Task', command = del_task, width=45,
                              font=('Helvetica',10), bg='#ede3d9', fg='#000000',relief=tk.FLAT)
delete_task_button.pack()


# In[ ]:


clear_task_button = tk.button(root, text='Load Tasks', command=load_tasks, width=45,
                             font('Helvetica',10), bg='#ede3d9', fg='#000000', relief=tk.FLAT)
clear_task_button.pack()


# In[ ]:


root.main.loop()

