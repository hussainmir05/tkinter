from tkinter import *
from  tkinter import ttk #comobox
root=Tk()

root.title('Combo Box')
root.geometry('500x500+400+120')
root.resizable(False, False)
root.config(bg='#262626')

# # submit
def submit_Btn(innt): #as the scale returns an integer
    # label_scale.config(text=str(scale_nam.get()))
    label_scale.config(text=str(innt))
    


# listbox
# modes MULTIPLE, EXTENDED and the default one is BROWSE
scale_nam=Scale(root,from_=90,to=200,orient=HORIZONTAL,length=400, sliderlength=70,showvalue=False ,command=submit_Btn)
scale_nam.place(x=20,y=20) 

#label
label_scale=Label(root ,bg='#262626',fg='light gray',font=('times new roman',15,'bold'))
label_scale.place(x=190,y=300, width=100,height=30)





root.mainloop()

