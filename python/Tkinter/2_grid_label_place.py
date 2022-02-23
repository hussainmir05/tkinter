from tkinter import *
root=Tk()

root.title('Hussain')
root.geometry('400x500+400+120')
root.resizable(True, False)
root.config(bg='#262626')
# # -------Grid ------------------------
# labl=Label(root,text='hussain', padx=20,pady=20).grid(row=0,column=0)
# labl=Label(root,text='hussain').grid(row=0,column=1)
# labl=Label(root,text='hussain').grid(row=2,column=0)
# -------pack ------------------------
labl1=Label(root,text='hussain  pack 1', padx=20,pady=20).pack(padx=20,pady=20)
labl2=Label(root,text='hussain pack 2').pack(fill=Y, side=RIGHT)
labl3=Label(root,text='hussain pack 3').pack(fill=BOTH,expand=True,pady=20,padx=10)
# -------place-----------------------
labl1=Label(root,text=' place 1', padx=20,pady=20).place(x=0,y=0, width=120, height=120)
labl2=Label(root,text=' place 2').place(x=100,y=10,width=200, height=200)
labl3=Label(root,text='place 3').place(x=200,y=120,width=120, height=120)
# -------pack ------------------------
root.mainloop()