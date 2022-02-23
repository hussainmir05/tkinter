from tkinter import *
root=Tk()

root.title('Hussain')
root.geometry('400x500+400+120')
root.resizable(False, False)
root.config(bg='#262626')

# label
labl_title2=Label(root, text='place',font=('times new roman','45','bold'), fg='red', bg='white',pady=20,bd=10,relief=GROOVE).pack(fil=X)
labl_title3 =Label(root, text='place',font=('times new roman','45','bold'), fg='red', bg='white',pady=50,bd=10,relief=GROOVE).place(x=100,y=200, width=300)


# entry
entry=Entry(root, font=('times new roman','15','bold'), fg='black', bg='lightyellow',bd=10,relief=GROOVE).pack(padx=10,pady=10)
entry=Entry(root, font=('times new roman',15,'bold'), fg='black', bg='lightyellow',bd=10,relief=GROOVE).place(x=0,y=450, relwidth=1)
# ---------------------

labl_title4 =Label(root, text='its hussain',font=('times new roman','20','bold'), fg='red', bg='white',pady=10,bd=10,relief=GROOVE).place(x=0,y=370, relwidth=1)


root.mainloop()