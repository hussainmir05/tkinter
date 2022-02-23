from tkinter import *
from tkinter import messagebox
root=Tk()

root.title('frames')
root.geometry('1200x600+100+70')
root.resizable(False, False)
root.config(bg='#262626')

# frmae
frame1=Frame(root, bg='gray')
frame1.place(x=50,y=100, width=500,height=300)
labl1=Label(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=10,y=10)
labl1=Button(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=400,y=10)
labl1=Label(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=10,y=250)
labl1=Button(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=400,y=250)

# LABEL frmae
frame1=LabelFrame(root, bg='gray', text='Hussain login',font=('times new roman',20,'bold'))
frame1.place(x=600,y=100, width=500,height=300)
labl1=Label(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=10,y=10)
labl1=Button(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=400,y=10)
labl1=Label(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=10,y=250)
labl1=Button(frame1,text='hello',bg='gray', font=('times new roman',16,'bold')).place(x=400,y=250)


root.mainloop()

