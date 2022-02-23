import tkinter as tk
from tkinter import *
from tkinter import  ttk
from tkinter import messagebox as m_box#to create message box

from tkinter.constants import PAGES
from tkinter.font import BOLD
from typing import Text
win=tk.Tk()

#label fram
label_fram=ttk.LabelFrame(win,text='contact details')
label_fram.grid(row=0,column=0,padx=40,pady=10)

# labels
name_label=ttk.Label(label_fram,text='Enter your Name: ', font=('Helvetica',14,'bold'))
age_label=ttk.Label(label_fram,text='Enter your Age: ', font=('Helvetica',14,'bold'))

# entry boxesvariables
nam_var=tk.StringVar()
age_var=tk.StringVar()

# entry boxes
name_entry=ttk.Entry(label_fram,width=36,textvariable=nam_var)
age_entry=ttk.Entry(label_fram,width=36,textvariable=age_var)

# Grid
name_label.grid(row=0,column=0,padx=5 ,pady=5 ,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5 ,pady=5 ,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5 ,pady=5 ,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5 ,pady=5 ,sticky=tk.W)

def action():
    # m_box.showinfo('title','muhammad')
    # m_box.showerror('title','yaqoob')
    # m_box.showwarning('title','batherpmiko')
    name=nam_var.get()
    age=age_var.get()
    if name==''or age=='':
        m_box.showinfo('title','please fill bouth ')
    else:
        try:
            age=int(age)
        except ValueError:
            m_box.showerror('title','Only digits are Allowed')
        else:
            if age<18:
                m_box.showwarning('warning', 'YOU are Under 18, try on your own risk')
            print(f'the {name} and age {age} ')


sub_butn=ttk.Button(win,text='SUBMIT', command=action)
sub_butn.grid(row=1,columnspan=2,padx=40)




win.mainloop()