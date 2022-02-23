from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
root=Tk()

root.title('Scroll bar')
root.geometry('1200x600+100+70')
root.resizable(False, False)
root.config(bg='#262626')

def openfile():
    openfile=filedialog.askopenfile(title='Select a Folder')
    # print(openfile) 
    # print(openfile.name)
    if openfile!=None:
        file_lbl.config(text='File name :   '+str(openfile.name.split('/')[-1]))
        file_path.set(str(openfile.name))
        for i in openfile:
            txt_area.insert(END,str(i))



def savefile():
    
    if file_path.get()=='':
        saveasfile()
    else:
        if file_path!='':

            savefile=open(file_path.get(),'w')        
            savefile.write(txt_area.get(1.0,END))
            savefile.close()
            messagebox.showinfo('Saved','File has been saved successfully')





def saveasfile():
    saveasfile=filedialog.asksaveasfile(title='save as ',filetypes=(('Txt file','.txt'),('All files''*.*')))
    if saveasfile!=None:
        saveasfile.write(txt_area.get(1.0,END))
        saveasfile.close()
        messagebox.showinfo('Saved','File has been saved successfully')


    
# btn
btn1=Button(root, text='open',font=('',15),bg='#975975', command=openfile)
btn1.place(x=200,y=50,width=150)
    

# btn
btn2=Button(root, text='save',font=('',15),bg='#975975', command=savefile)
btn2.place(x=400,y=50,width=150)
    

# btn
btn3=Button(root, text='Save As',font=('',15),bg='#975975', command=saveasfile)
btn3.place(x=600,y=50,width=150)

# text label
file_lbl=Label(root, text='File name : ', font=('',14),fg='lightgray',bg='#262626')
file_lbl.place(x=100, y=120)


# path 
file_path=StringVar()

# txt area 
txt_area=Text(root,font=('',15),bd=2 ,relief=RAISED)
txt_area.place(x=100,y=200,width=1000,height=350)
 


root.mainloop()



##################################
####folder
    # openfolder=filedialog.askdirectory(title='Select a Folder')
    # print(openfolder)

    ####file
     ###orwe use askopenfilename as shown in below
   
   
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
    
   
    # # ####save file name
    # openfile=filedialog.asksaveasfilename(title='save the file',filetypes=(('Txt file','.txt'),('All files','*.*')))
    # print(openfile) 

   


