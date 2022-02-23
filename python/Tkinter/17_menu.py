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


mymenu=Menu(root)
# main menu
# mymenu.add_command(label='hussain', command=submit_Btn)
# mymenu.add_command(label='khadim', command=submit_Btn1)
# mymenu.add_command(label='astori', command=submit_Btn2)
#manager sub of view employee
managermenu=Menu(mymenu,tearoff=0)
managermenu.add_command(label='pakisatan')
managermenu.add_command(label='pakisatan')
managermenu.add_command(label='pakisatan')


# 2nd menu
# view employes 
viewEMployee=Menu(mymenu,tearoff=0)
viewEMployee.add_command(label='attandence', command=submit_Btn1)
viewEMployee.add_cascade(label='manager', menu=managermenu)
viewEMployee.add_command(label='employee', command=submit_Btn1)

# main menu
# add  cascade
EmployeeMenu=Menu(mymenu,tearoff=0)
EmployeeMenu.add_command(label="add employee",command=submit_Btn)
EmployeeMenu.add_cascade(label="view employee",menu=viewEMployee)
EmployeeMenu.add_command(label="delete employee",command=submit_Btn)

# ##########################################################
mymenu.add_cascade(label='employee',menu=EmployeeMenu)
# ##########################################################


root.config(menu=mymenu)

root.mainloop()

