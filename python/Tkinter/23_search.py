from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
import wikipedia


class search_app:
    def __init__(self,root):
        self.root=root
                
        self.root.geometry('1200x600+100+70')
        # self.root.resizable(False, False)
        self.root.config(bg='#262626')
        self.root.title('search app by hussain')

        #label  title
        title=Label(self.root,text='Search Application', font=('',20),bg='white',fg='#262626')
        title.place(x=0,y=0,relwidth=1)

        #labe search name
        lbl_search_nam=Label(self.root,text='Enter Word', font=('',13),fg='white',bg='#262626')
        lbl_search_nam.place(x=10,y=50)

        # entry variable 
        self.var_search=StringVar()

        # Entry  
        entry_nam=Entry(self.root,textvariable=self.var_search, font=('',12),bg='white',fg='#262626') 
        entry_nam.place(x=120,y=50)

        # search btn
        btn_search=Button(self.root,text='Search Word',command=self.search, font=('',13),fg='white',activebackground='#8C8F8F',bg='#262626')
        btn_search.place(x=360,y=50)


        #clear  btn
        btn_clear=Button(self.root,text='Clear',command=self.clear, font=('Arial',13),fg='white',activebackground='#8C8F8F',bg='#262626')
        btn_clear.place(x=540,y=50)

      


        #enabel mode    btn
        btn_enable=Button(self.root,text='Enable', command=self.enable,font=('',13),fg='white',activebackground='#8C8F8F',bg='#262626')
        btn_enable.place(x=720,y=50)


        #disable mode   btn
        btn_disable=Button(self.root,text='Disable', command=self.disable,font=('',13),fg='white',activebackground='#8C8F8F',bg='#262626')
        btn_disable.place(x=900,y=50)
        

        # mode  labl
        self.lbl_mode=Label(self.root,text='Mode',font=('',8),fg='white',activebackground='#8C8F8F',bg='#262626' )
        self.lbl_mode.place(x=20,y=130)

        # Frame 
        frame1=Frame(self.root,bd=2,relief=RIDGE)
        frame1.place(x=20,y=150,width=1100,height=500)

        # Scrollbar
        scroly=Scrollbar(frame1,orient=VERTICAL)
        scroly.pack(side=RIGHT,fill=Y) #or smal 'y'

        # text area 
        self.text1=Text(frame1,font=('',14,''),yscrollcommand=scroly.set)
        self.text1.pack(fill=BOTH,expand=1)
        scroly.config(command=self.text1.yview)

          
        # enable
    def enable(self):
            self.text1.config(state=NORMAL)
            self.lbl_mode.config(text='Mode=Enables')

            
        # disenable
    def disable(self):
            self.text1.config(state=DISABLED)
            self.lbl_mode.config(text='Mode=Disabled')

    def search(self):
        if self.var_search.get()=='':
            messagebox.showinfo('Attension', "kindly wirte a word on search box and hit on search button")
        else:
            fetch_data=wikipedia.summary(self.var_search.get())
            self.text1.insert('1.0',fetch_data)

    def clear(self):
        self.var_search.set('')
        self.text1.delete(1.0,END)
        self.lbl_mode.config(text='')




            

root=Tk()
obj=search_app(root)
root.mainloop()
