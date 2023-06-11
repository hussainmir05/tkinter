from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk 


class Student_class:
    def __init__(self,root):
        self.root= root
        self.root.title('Course Details')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()
        
        # title
        title=Label(self.root,text='Student Details',font=('gondy old style',15 ,'bold'),bg='#033054',fg='white')
        title.place(x=0,y=0,relwidth=1)

    # --------widgets labels----------------
       # column 1
        lbl_roll_nbr=Label(self.root,text='Roll No',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_roll_nbr.place(x=10,y=60)

        lbl_name=Label(self.root,text='Name',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_name.place(x=10,y=100)

        lbl_email=Label(self.root,text='Email',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_email.place(x=10,y=140)

        lbl_gender=Label(self.root,text='Gender',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_gender.place(x=10,y=180)
       # column 2
        lbl_roll_nbr=Label(self.root,text='D.O.B',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_roll_nbr.place(x=320,y=60)

        lbl_name=Label(self.root,text='Contact',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_name.place(x=320,y=100)

        lbl_email=Label(self.root,text='Addimision',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_email.place(x=320,y=140)

        lbl_gender=Label(self.root,text='Course',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_gender.place(x=320,y=180)

        lbl_gender=Label(self.root,text='Course',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_gender.place(x=320,y=180)
       #last row
        lbl_city=Label(self.root,text='City',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_city.place(x=10,y=210)
        lbl_state=Label(self.root,text='State',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_state.place(x=230,y=210)
        lbl_pin=Label(self.root,text='Pin',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_pin.place(x=460,y=210)

        # adress

        # self.lbl_adress=Label(self.root,text='Adress',font=('gondy old style',15 ,'bold'),bg='white')
        # self.lbl_adress.place(x=10,y=220)
    
    
    # variables ---------------------
        self.Var_roll_nbr=StringVar()
        self.Var_name=StringVar()
        self.Var_email=StringVar()
        self.Var_gender=StringVar()
        self.Var_dob=StringVar()
        self.Var_course=StringVar()
        self.Var_contact=StringVar()
        self.Var_admision_date=StringVar()
        self.Var_state=StringVar()
        self.Var_city=StringVar()
        self.Var_pin=StringVar()
        self.course_list=[]


    #----------------- Entries-----------------

       # column 1
        self.entry_roll_nbr=Entry(self.root,textvariable=self.Var_roll_nbr ,font=('gondy old style',12 ,''),bg='lightyellow')
        self.entry_roll_nbr.place(x=100,y=60,width=200)

        entry_name=Entry(self.root,textvariable=self.Var_name,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_name.place(x=100,y=100,width=200)

        entry_email=Entry(self.root,textvariable=self.Var_email,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_email.place(x=100,y=140,width=200)

        self.entry_gender=ttk.Combobox(self.root,textvariable=self.Var_gender,values=('Select','Male','Female','Other'),font=('gondy old style',12 ,''),state='readonly',justify=CENTER)
        self.entry_gender.place(x=100,y=180,width=200)
        self.entry_gender.current(0)

       # colnum 2
        
        entry_dob=Entry(self.root,textvariable=self.Var_dob ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_dob.place(x=450,y=60,width=200)

        entry_contact=Entry(self.root,textvariable=self.Var_contact,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_contact.place(x=450,y=100,width=200)

        entry_admission=Entry(self.root,textvariable=self.Var_admision_date,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_admission.place(x=450,y=140,width=200)

        self.fetch_course()

        self.entry_course=ttk.Combobox(self.root,textvariable=self.Var_course,values=self.course_list,font=('gondy old style',12 ,''),state='readonly',justify=CENTER)
        self.entry_course.place(x=450,y=180,width=200)
        # self.entry_course.current(0)
        self.entry_course.set('Empty')
       # last row 
       
        entry_state=Entry(self.root,textvariable=self.Var_state,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_state.place(x=100,y=210,width=100)
        entry_city=Entry(self.root,textvariable=self.Var_city,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_city.place(x=330,y=210,width=100)
        entry_pin=Entry(self.root,textvariable=self.Var_pin,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_pin.place(x=550,y=210,width=100)
       # --------------adress

        self.entry_adress=Text(self.root,font=('gondy old style',12 ,''),bg='lightyellow')
        self.entry_adress.place(x=100,y=260 ,width=550,height=100)

    #---------- Buttons------------------------:
        
        self.Btn_Add=Button(self.root,text='Add', font=('gondy old style',15 ,'bold'),bg='#2196f3',fg='white',cursor='hand2',command=self.Add_db)
        self.Btn_Add.place(x=150,y=400,width=110,height=40)
        self.Btn_Update=Button(self.root,text='Update', font=('gondy old style',15 ,'bold'),bg='#4caf50',fg='white',cursor='hand2', command=self.Update_db)
        self.Btn_Update.place(x=270,y=400,width=110,height=40)
        self.Btn_Delete=Button(self.root,text='Delete',font=('gondy old style',15 ,'bold'), bg='#f44336',fg='white',cursor='hand2',command=self.Delete_db)
        self.Btn_Delete.place(x=400,y=400,width=110,height=40)
        self.Btn_Clear=Button(self.root,text='Clear', font=('gondy old style',15 ,'bold'),bg='#607d8b',fg='white',cursor='hand2',command=self.Clear_db)
        self.Btn_Clear.place(x=520,y=400,width=110,height=40)

    #------------ search panel---------
        self.search_entry=StringVar()

       # entry , label and button
        lbl_search_Roll_nbr=Label(self.root,text='Roll No',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_search_Roll_nbr.place(x=720,y=60)

        entry_roll_nbr_search=Entry(self.root,textvariable=self.search_entry ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_roll_nbr_search.place(x=870,y=60,width=180)        
        
        self.Btn_Search=Button(self.root,text='Search', font=('gondy old style',15 ,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search_db)
        self.Btn_Search.place(x=1070,y=60,width=120,height=23)


       # search  content frame
        self.frame_search=Frame(self.root,bd=2, relief=RIDGE)
        self.frame_search.place(x=720,y=100,width=470,height=340) 

       # scroll br ----------1---
        scrolly=Scrollbar(self.frame_search,orient=VERTICAL)
        scrollx=Scrollbar(self.frame_search,orient=HORIZONTAL)

       # coureTable   #--serach tree---
        self.table_search=ttk.Treeview(self.frame_search,columns=('rollnbr','name','email','gender','dob','contact','admission','course','state','city','pin','adress'), xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
       
       
       # scroll grid and config ----------2---
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)  
        # config scroll bar ----------3---
        scrolly.config(command=self.table_search.yview)
        scrollx.config(command=self.table_search.xview)

       #course table heading 
        self.table_search.heading('rollnbr', text='Roll No')
        self.table_search.heading('name', text='Name')
        self.table_search.heading('email', text='Email')
        self.table_search.heading('gender', text='Gender')
        self.table_search.heading('dob', text='DOB')
        self.table_search.heading('contact', text='Contact')
        self.table_search.heading('admission', text='Admission')
        self.table_search.heading('course',text='Course')
        self.table_search.heading('state', text='State')
        self.table_search.heading('city', text='City')
        self.table_search.heading('pin', text='Pin')
        self.table_search.heading('adress', text='Adress')
        self.table_search['show']='headings'

        

       #course table place
        
        self.table_search.column('rollnbr',width=100)
        self.table_search.column('name',width=100)
        self.table_search.column('email',width=100)
        self.table_search.column('gender',width=100)
        self.table_search.column('dob',width=100)
        self.table_search.column('contact',width=100)
        self.table_search.column('admission',width=100)
        self.table_search.column('course',width=100)
        self.table_search.column('state',width=100)
        self.table_search.column('city',width=100)
        self.table_search.column('pin',width=100)
        self.table_search.column('adress',width=200)
        self.table_search.pack(fill=BOTH,expand=1)
        self.table_search.bind('<ButtonRelease-1>',self.get_data) #this funcion takes data from search table to entry boxes 
        self.show()
        self.fetch_course()





    
# #########################################################################################################
# #########################################################################################################
    # import pdb
    # pdb.set_trace()

# get data



    def get_data(self,ev):#this funcion takes data from search table to entry boxes 
        self.entry_roll_nbr.config(state='readonly')
        r=self.table_search.focus()
        content=self.table_search.item(r)
        row=content['values']
        # print(r)
        # print('????????????????????????????')
        # print('????????????????????????????')
        # print(content)
        self.Var_roll_nbr.set(row[0])
        self.Var_name.set(row[1])
        self.Var_email.set(row[2])
        self.Var_gender.set(row[3])
        self.Var_dob.set(row[4])
        self.Var_contact.set(row[5])
        self.Var_admision_date.set(row[6])
        self.Var_course.set(row[7])
        self.Var_state.set(row[8])
        self.Var_city.set(row[9])
        self.Var_pin.set(row[10])

        self.entry_adress.delete('1.0',END)
        self.entry_adress.insert(END,row[0])


# clear ####################################################################################################

    def Clear_db(self):#this funcion takes data from search table to entry boxes 
        self.show()
        r=self.table_search.focus()
        content=self.table_search.item(r)
        row=content['values']
        self.Var_name.set(''),
        self.Var_email.set(''),
        self.Var_gender.set(''),
        self.Var_dob.set(''),
        self.Var_contact.set(''),
        self.Var_admision_date.set(''),
        self.Var_course.set(''),
        self.Var_state.set(''),
        self.Var_city.set(''),
        self.Var_pin.set(''),
        self.entry_adress.get('1.0',END),
        self.Var_roll_nbr.set(''),
        self.entry_roll_nbr.config(state='normal')


# addd data#####################################################################################################


    def Add_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_roll_nbr.get()=='':
                messagebox.showerror('Error', 'Kindly enter a course')
            else:
                cur.execute('select * from student where rollnbr=?',(self.Var_roll_nbr.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Roll No Alread Present')
                else:
                    cur.execute('insert into student ( rollnbr,name,email,gender,dob,contact,admission,course,state,city,pin,adress)values(?,?,?,?,?,?,?,?,?,?,?,?)',
                    (self.Var_roll_nbr.get(),
                    self.Var_name.get(),
                    self.Var_email.get(),
                    self.Var_gender.get(),
                    self.Var_dob.get(),
                    self.Var_contact.get(),
                    self.Var_admision_date.get(),
                    self.Var_course.get(),
                    self.Var_state.get(),
                    self.Var_city.get(),
                    self.Var_pin.get(),

                    self.entry_adress.get('1.0',END)))
                    con.commit()
                    messagebox.showinfo('Congrates', 'The Student details are added Successfully')
                    self.show()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

# delete data##################################################################################################


    def Delete_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_roll_nbr.get()=='':
                messagebox.showerror('Error', 'Kindly enter a Roll No')
            else:
                cur.execute('select * from student where rollnbr=?',(self.Var_roll_nbr.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select a student to be deleted')
                else:
                   op=messagebox.askyesno('Conformation', 'Do you relly want to delete this this student')
                   if op==True:
                       cur.execute('delete from  student where rollnbr=?',(self.Var_roll_nbr.get(),))
                       con.commit()
                       messagebox.showinfo('Congrates', 'The student details are Deleted Successfully')
                       self.Clear_db()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

# update data ######################################################################################################


    def Update_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_roll_nbr.get()=='':
                messagebox.showerror('Error', 'Kindly enter a Roll No')
            else:
                cur.execute('select * from student where rollnbr=?',(self.Var_roll_nbr.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select a student to Update')
                else:
                    cur.execute('update student set  name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,adress=? where rollnbr=?',(                    
                    self.Var_name.get(),
                    self.Var_email.get(),
                    self.Var_gender.get(),
                    self.Var_dob.get(),
                    self.Var_contact.get(),
                    self.Var_admision_date.get(),
                    self.Var_course.get(),
                    self.Var_state.get(),
                    self.Var_city.get(),
                    self.Var_pin.get(),

                    self.entry_adress.get('1.0',END),
                    self.Var_roll_nbr.get(),

                    ))
                    con.commit()
                    messagebox.showinfo('Congrates', 'your Student details are Updated Successfully')
                    self.show()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

# show data#####################################################################################################
        
    def show(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute('select * from student')
            rows=cur.fetchall()
            self.table_search.delete(*self.table_search.get_children())
            for row in rows:
                self.table_search.insert('',END,values=row)
               
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

# fetch course#####################################
    def fetch_course(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute('select name from course')
            rows=cur.fetchall()
           
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
            # print (v)
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')



# search data####################################################################################################

        
    def Search_db(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"select * from student where rollnbr=?",(self.search_entry.get(),))
            row=cur.fetchone()
            if row != None:                    
                self.table_search.delete(*self.table_search.get_children())
                self.table_search.insert('',END,values=row) 
            else:
                messagebox.showerror('error','No record Found')            
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

        
    







if __name__=='__main__':
    root= Tk()
    obj=Student_class(root)
    root.mainloop()
