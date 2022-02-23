from tkinter import *
root=Tk()

root.title('Radio Btn')
root.geometry('500x500+400+120')
# root.resizable(False, False)
root.config(bg='#262626')
# label 1
lbl_1=Label(root,text='Click  your Gender    : ', bg='#262626',fg='#0CD1BF', font=('times new roman',14,'bold'))
lbl_1.place(x=5,y=20)


def submit():
    fah=xd.get()
    
    lbl_1=Label(root,text=fah, bg='#262626',fg='#0CD1BF', font=('times new roman',20,'bold'))
    lbl_1.place(x=200,y=130)
    
# submit Btn 

xd=StringVar()#also use intvar()
submit_btn=Button(root, text='SUBMIT',command=submit).place(x=250,y=80)

# check Btn
rdio_btn_1=Checkbutton(root,text='I agree all the terms and conditions',onvalue='yes',offvalue='not', variable=xd,fg='#0CD1BF',bg='#262626',activeforeground='#262626',activebackground='#262626', font=('times new roman',14,'bold'))
rdio_btn_1.place(x=0,y=50)
xd.set('not') 


root.mainloop()