from tkinter import *
root=Tk()

root.title('Log In')
root.geometry('500x500+400+120')
root.resizable(False, False)
# root.config(bg='#262626')
# label 1
entry_nam=Label(root,text= 'User Entry Form', bg='gray',font=('times new roman',20,'bold'))
entry_nam.place(x=5,y=0,relwidth=1)
user_nam=Label(root,text= 'USER NAME    : ', font=('times new roman',14,'bold'))
user_nam.place(x=5,y=70)
email_nam=Label(root,text='EMAil                : ', font=('times new roman',14,'bold'))
email_nam.place(x=5,y=100)
gender_nam=Label(root,text='Gender               : ', font=('times new roman',14,'bold'))
gender_nam.place(x=5,y=130)


# ENtry
# entry
entry_var1=StringVar()
entry_var2=StringVar()
# entry1 
entry1=Entry(root, font=('times new roman','12','bold'),bd=5,textvariable=entry_var1,relief=GROOVE)
entry1.place(x=220,y=70)
# entry2
entry2=Entry(root, font=('times new roman',12,'bold'),bd=5,textvariable=entry_var2,relief=GROOVE)
entry2.place(x=220,y=100)


# radio var
xd=StringVar()
# rdio_btn_1
rdio_btn_1=Radiobutton(root,text='MAle',value='male', variable=xd,activeforeground='#262626', font=('times new roman',14,'bold'))
rdio_btn_1.place(x=220,y=130)
# # # rdio_btn_2
rdio_btn_2=Radiobutton(root,text='FeMAle',value='female',variable=xd,activeforeground='#262626', font=('times new roman',14,'bold'))
rdio_btn_2.place(x=300,y=130)
# xd.set('female')

# # check_btn_2
Check_var=IntVar()
Check_btn=Checkbutton(root,text='I accept all the terms and condisions',onvalue=1,offvalue=0,variable=Check_var, font=('times new roman',14,'normal'))
Check_btn.place(x=5,y=155)


    
# submit Btn  
def submit():
    e1=entry_var1.get()
    e2=entry_var2.get()
    r=xd.get()
    c=Check_var.get()
    if e1 and e2 and r and c:
        err_nam=Label(root,text= f'name : {e1} \nemail :{e2}   {r}   {c}', font=('times new roman',14,'bold'))
        err_nam.place(x=5,y=250)
       
    else:
        err_nam=Label(root,text= 'fill all blanks   : ', font=('times new roman',14,'bold'))
        err_nam.place(x=5,y=250)
        






submit_btn=Button(root, text='SUBMIT',bg='light gray',font=('times new roman',15,'bold'),command=submit)
submit_btn.place(x=200,y=190, width=100,height=30)


root.mainloop()

