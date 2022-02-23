from tkinter import *
from  tkinter import ttk #comobox
root=Tk()

root.title('Combo Box')
root.geometry('500x500+400+120')
root.resizable(False, False)
# root.config(bg='#262626') 

# listbox
# modes MULTIPLE, EXTENDED and the default one is BROWSE
list_nam=Listbox(root,font=('times new roman  ',14,''),bg='#262626',fg='white', justify=CENTER,selectmode=EXTENDED)
list_nam.place(x=50,y=200,width=200) 

for i in range(1,20):
    list_nam.insert(i,'Hussain  :   '+str(i))


# submit
def submit_Btn():  
    # print(list_nam.get(0))
    curser_selection=list_nam.curselection()
    print(curser_selection)
    # print(curser_selection,list_nam.get(curser_selection))
    # for i in curser_selection:#for MULTIPLE AND EXTENDED mode
    #     print(list_nam.get(i)) 
    list_nam.delete(curser_selection)


submit_btn=Button(root, text='SUBMIT',bg='light gray',font=('times new roman',15,'bold'),command=submit_Btn)
submit_btn.place(x=300,y=400, width=100,height=30)





root.mainloop()

