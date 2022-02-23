from tkinter import *
from  tkinter import ttk   #comobox
root=Tk()

root.title('Combo Box')
root.geometry('500x500+400+120')
root.resizable(False, False)
# root.config(bg='#262626')

# combobox
# there is no bg,fg proprtty in combobox, import ttk module
# combo_var=StringVAr()
combo_nam=ttk.Combobox(root,font=('times new roman',14,'bold'),values=('c++','java','python','c#','matlab'), justify=CENTER, state='readonly')
combo_nam.place(x=5,y=0,width=200) 
# # # if we use place in same line we cant use current and set proprty 
combo_nam.current(2)
# combo_nam.set('select language')

# submit

    
# submit Btn  
def submit():
   print(combo_nam.get())


submit_btn=Button(root, text='SUBMIT',bg='light gray',font=('times new roman',15,'bold'),command=submit)
submit_btn.place(x=200,y=190, width=100,height=30)





root.mainloop()

