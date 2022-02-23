from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk #for other than png format
root=Tk()

root.title('Images')
root.geometry('640x480+100+70')
root.resizable(False, False)
root.config(bg='#262626')

# for other than png image
# we have to import pillow librat
ba=ImageTk.PhotoImage(file=r"C:\Users\AKH\Desktop\python gui\codding\w.jpg")
lbl3=Label(root,image=ba,).place(x=0,y=0)

def openfile():
    ####folder
    # openfolder=filedialog.askdirectory(title='Select a Folder')
    # print(openfolder)

    ####file
    # openfile=filedialog.askopenfile(title='Select a Folder')
    # print(openfile) 
    # print(openfile.name) ###orwe use askopenfilename as shown in below
   
   
    ####filename
    # openfile=filedialog.askopenfilename(title='Select a file + name wala')
    # print(openfile) 
    # print(openfile.split('/')[-1]) ###just name with out path
   
    ####filenames more than 1
    # openfile=filedialog.askopenfilenames(title='Select a file + name wala')
    # print(openfile) 
    
   
    # ####filens more than one
    # openfile=filedialog.askopenfiles(title='Select a file + name wala')
    # print(openfile) 

    
   
    # ####save file
    # openfile=filedialog.asksaveasfile(title='save the file',filetypes=(('Txt file','.txt'),('All files''*.*')))
    # print(openfile) 
    
   
    # ####save file name
    openfile=filedialog.asksaveasfilename(title='save the file',filetypes=(('Txt file','.txt'),('All files','*.*')))
    print(openfile) 

   

# btn
btn1=Button(root, text='submit',font=('',15), command=openfile)
btn1.place(x=20,y=300)
 



root.mainloop()

