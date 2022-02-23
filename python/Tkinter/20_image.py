from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #for other than png format
root=Tk()

root.title('Images')
root.geometry('640x480+100+70')
root.resizable(False, False)
# root.config(bg='#262626')
 

# for other than png image
# we have to import pillow librat
ba=ImageTk.PhotoImage(file=r"C:\Users\AKH\Desktop\python gui\codding\w.jpg")
lbl3=Label(root,image=ba,).place(x=0,y=0)


# for png image
Exit=PhotoImage(file="F:\python tutorials\project\icons\exit.png")

lbl1=Label(root,text='Exit',fg='black', padx=20,image=Exit,compound=LEFT).place(x=0,y=0)





root.mainloop()

