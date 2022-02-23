from tkinter import *
from tkinter import messagebox
root=Tk()

root.title('message BOx')
root.geometry('500x500+400+120')
root.resizable(False, False)
root.config(bg='#262626')

def submit_Btn():
    messagebox.showerror('showerror','this is show error')
    
def submit_Btn1():
    messagebox.showinfo('showinfo','this is show info')


def submit_Btn2(): 
    messagebox.showwarning('showWarning','this is show Warning')
    # messagebox.askyesno('error','are you want to leave')


# listbox
# modes MULTIPLE, EXTENDED and the default one is BROWSE
btn1=Button(root,text="hussain",bg='#262626',fg='light gray',font=('times new roman',15,'bold'),command=submit_Btn)
btn1.place(x=0,y=20) 


btn2=Button(root,text="hussain1",bg='#262626',fg='light gray',font=('times new roman',15,'bold'),command=submit_Btn1)
btn2.place(x=100,y=20) 
btn3=Button(root,text="hussain2",bg='#262626',fg='light gray',font=('times new roman',15,'bold'),command=submit_Btn2)
btn3.place(x=200,y=20) 



root.mainloop()

