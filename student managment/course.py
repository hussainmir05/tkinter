from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk 


class Course_class:
    def __init__(self,root):
        self.root= root
        self.root.title('Course Details')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()
        
        # title
        title=Label(self.root,text='Course Details',font=('gondy old style',15 ,'bold'),bg='#033054',fg='white')
        title.place(x=0,y=0,relwidth=1)

# widgets
        lbl_courseName=Label(self.root,text='Course Name',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_courseName.place(x=10,y=60)

        lbl_duration=Label(self.root,text='Course Duration',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_duration.place(x=10,y=100)

        lbl_charges=Label(self.root,text='Course Charges',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_charges.place(x=10,y=140)

        self.lbl_description=Label(self.root,text='Course Description',font=('gondy old style',15 ,'bold'),bg='white')
        self.lbl_description.place(x=10,y=180)
        # variables 
        self.Var_Course=StringVar()
        self.Var_Duration=StringVar()
        self.Var_Charges=StringVar()

        # Entries
        
        self.entry_courseName=Entry(self.root,textvariable=self.Var_Course ,font=('gondy old style',12 ,''),bg='lightyellow')
        self.entry_courseName.place(x=220,y=60,width=200)

        entry_duration=Entry(self.root,textvariable=self.Var_Duration,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_duration.place(x=220,y=100,width=200)

        entry_charges=Entry(self.root,textvariable=self.Var_Charges,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_charges.place(x=220,y=140,width=200)

        self.entry_description=Text(self.root,font=('gondy old style',12 ,''),bg='lightyellow')
        self.entry_description.place(x=220,y=180 ,width=480,height=100)

        # Buttons:
        
        self.Btn_Add=Button(self.root,text='Add', font=('gondy old style',15 ,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.Add_db)
        self.Btn_Add.place(x=150,y=400,width=110,height=40)
        self.Btn_Update=Button(self.root,text='Update', font=('gondy old style',15 ,'bold'),bg='#4caf50',fg='white',cursor='hand2', command=self.Update_db)
        self.Btn_Update.place(x=270,y=400,width=110,height=40)
        self.Btn_Delete=Button(self.root,text='Delete',font=('gondy old style',15 ,'bold'), bg='#f44336',fg='white',cursor='hand2',command=self.Delete_db)
        self.Btn_Delete.place(x=400,y=400,width=110,height=40)
        self.Btn_Clear=Button(self.root,text='Clear', font=('gondy old style',15 ,'bold'),bg='#607d8b',fg='white',cursor='hand2',command=self.Clear_db)
        self.Btn_Clear.place(x=520,y=400,width=110,height=40)

        # search panel
        self.search_entry=StringVar()


        lbl_search_courseName=Label(self.root,text='Course Name',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_search_courseName.place(x=720,y=60)

        entry_courseName_search=Entry(self.root,textvariable=self.search_entry ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_courseName_search.place(x=870,y=60,width=180)        
        
        self.Btn_Search=Button(self.root,text='Search', font=('gondy old style',15 ,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search_db)
        self.Btn_Search.place(x=1070,y=60,width=120,height=23)


        #result of search  content frame
        self.frame_search=Frame(self.root,bd=2, relief=RIDGE)
        self.frame_search.place(x=720,y=100,width=470,height=340) 

        # scroll br 
        scrolly=Scrollbar(self.frame_search,orient=VERTICAL)
        scrollx=Scrollbar(self.frame_search,orient=HORIZONTAL)

        # coureTable
        self.table_search=ttk.Treeview(self.frame_search,columns=('cid','name','duration','charges','description'), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
       
       # scroll grid and config
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)  
        # config scroll bar
        scrolly.config(command=self.table_search.yview)
        scrollx.config(command=self.table_search.xview)

        
        self.table_search.heading('cid', text='Course ID')
        self.table_search.heading('name', text='Name')
        self.table_search.heading('duration', text='Duration')
        self.table_search.heading('charges', text='Charges')
        self.table_search.heading('description', text='Description')
        self.table_search['show']='headings'
        
        self.table_search.column('cid',width=100)
        self.table_search.column('name',width=100)
        self.table_search.column('duration',width=100)
        self.table_search.column('charges',width=100)
        self.table_search.column('description',width=150)
        self.table_search.pack(fill=BOTH,expand=1)
        self.table_search.bind('<ButtonRelease-1>',self.get_data) #this funcion takes data from search table to entry boxes 
        self.show()




    
# #########################################################################################################
# #########################################################################################################
    # import pdb
    # pdb.set_trace()





    def get_data(self,ev):#this funcion takes data from search table to entry boxes 
        self.entry_courseName.config(state='readonly')
        r=self.table_search.focus()
        content=self.table_search.item(r)
        row=content['values']
        # print(r)
        # print('????????????????????????????')
        # print('????????????????????????????')
        # print(content)
        # print(row)
        self.Var_Course.set(row[1])
        self.Var_Duration.set(row[2])
        self.Var_Charges.set(row[3])
        # self.Var_Course.set(row[1])
        self.entry_description.delete(1.0,END)
        self.entry_description.insert(END,row[4])

# #########################################################################################################

    def Clear_db(self):#this funcion takes data from search table to entry boxes 
        self.show()
        r=self.table_search.focus()
        content=self.table_search.item(r)
        row=content['values']
        self.Var_Course.set('')
        self.Var_Duration.set('')
        self.search_entry.set('')
        self.Var_Charges.set('')
        self.entry_description.delete(1.0,END)
        self.entry_courseName.config(state='normal')


# #########################################################################################################


    def Add_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_Course.get()=='':
                messagebox.showerror('Error', 'Kindly enter a course')
            else:
                cur.execute('select * from course where name=?',(self.Var_Course.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Course Name Alread Present')
                else:
                    cur.execute('insert into course (name, duration,charges, description)values(?,?,?,?)',
                    (self.Var_Course.get(),
                    self.Var_Duration.get(),
                    self.Var_Charges.get(),
                    self.entry_description.get('1.0',END)))
                    con.commit()
                    messagebox.showinfo('Congrates', 'your course is added Successfully')
                    self.show()

            
        except Exception as ex:
            messagebox.showerror('uck',f'{str(ex)} Error')
# #########################################################################################################



    def Delete_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_Course.get()=='':
                messagebox.showerror('Error', 'Kindly enter a course')
            else:
                cur.execute('select * from course where name=?',(self.Var_Course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select a course to be deleted')
                else:
                   op=messagebox.askyesno('Conformation', 'Do you relly want to delete this course')
                   if op==True:
                       cur.execute('delete from  course where name=?',(self.Var_Course.get(),))
                       con.commit()
                       messagebox.showinfo('Congrates', 'your course is Deleted Successfully')
                       self.Clear_db()

            
        except Exception as ex:
            messagebox.showerror('Fu***',f'{str(ex)} Error')
# #########################################################################################################



# #########################################################################################################


    def Update_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_Course.get()=='':
                messagebox.showerror('Error', 'Kindly enter a course')
            else:
                cur.execute('select * from course where name=?',(self.Var_Course.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select a course to Update')
                else:
                    cur.execute('update course set  duration=?,charges=?, description=? where name=?',(                    
                    self.Var_Duration.get(),
                    self.Var_Charges.get(),
                    self.entry_description.get('1.0',END),
                    self.Var_Course.get()
                    ))
                    con.commit()
                    messagebox.showinfo('Congrates', 'your course is Updated Successfully')
                    self.show()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')


# #########################################################################################################

        
    def show(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute('select * from course')
            rows=cur.fetchall()
            self.table_search.delete(*self.table_search.get_children())
            for row in rows:
                self.table_search.insert('',END,values=row)
               
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')
# #########################################################################################################

        
    def Search_db(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.search_entry.get()}%'" )
            rows=cur.fetchall()
            self.table_search.delete(*self.table_search.get_children())
            for row in rows:
                self.table_search.insert('',END,values=row)             
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

        
    







if __name__=='__main__':
    root= Tk()
    obj=Course_class(root)
    root.mainloop()
