from tkinter import *
from tkinter import messagebox
root=Tk()

root.title('Scroll bar')
root.geometry('1200x600+100+70')
root.resizable(False, False)
root.config(bg='#262626')

# frmae
frame1=Frame(root, bg='gray')
frame1.place(x=50,y=50, width=200,height=300)


# scroll bar
scrollY=Scrollbar(frame1,orient=VERTICAL)
scrollY.pack(side=RIGHT,fill=Y)


#  list 
list_data=Listbox(frame1,font=('times new roman',20),justify=CENTER, yscrollcommand=scrollY.set)
list_data.pack()
scrollY.config(command=list_data.yview)#config must be after list_data or Listbox object
for i in range(100):
    list_data.insert(i,'Hussain '+str(i+1))






root.mainloop()

