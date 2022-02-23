from tkinter import *
root=Tk()

root.title('Hussain')
root.geometry('400x500+400+120')
root.resizable(False, False)
root.config(bg='#262626')

labl_title=Label(root,text='yaqoob')
labl_title.pack(fill=X,pady=10 )
labl_title1=Label(root, text='pack',font=('arial','45','bold'), fg='red', bg='yellow',pady=50,bd=10,relief=GROOVE).pack(fill=X,padx=10,pady=5)
labl_title2=Label(root, text='place',font=('times new roman','45','bold'), fg='red', bg='white',pady=50,bd=10,relief=GROOVE).place(x=100,y=200, width=300)

root.mainloop()