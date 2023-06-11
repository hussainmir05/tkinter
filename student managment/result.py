from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk 


class  result_class:
    def __init__(self,root):
        self.root= root
        self.root.title('Course Details')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()
        
       # title
        title=Label(self.root,text='Result Details',font=('gondy old style',15 ,'bold'),bg='orange',fg='#262626')
        title.place(x=0,y=0,relwidth=1)
    #labels
        lbl_select_student=Label(self.root, text='Select Student',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_select_student.place(x=50,y=100 )
        lbl_name=Label(self.root, text='Name',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_name.place(x=50,y=160)
        lbl_course=Label(self.root, text='Course',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_course.place(x=50,y=220 )
        lbl_marks_obtained=Label(self.root, text='Marks Obtained',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_marks_obtained.place(x=50,y=280 )
        lbl_Full_Marks=Label(self.root, text='Full Marks',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_Full_Marks.place(x=50,y=340 )

    # variables
        self.Var_rollnbr=StringVar()
        self.Var_name=StringVar()
        self.Var_course=StringVar()
        self.Var_marks=StringVar()
        self.Var_full_marks=StringVar()
        self.Var_roll_list=[]
        self.fetch_rollnbr()
    
    
    # Entry boxes
       # combobox
        self.entry_select_student=ttk.Combobox(self.root,textvariable=self.Var_rollnbr,values=self.Var_roll_list,font=('gondy old style',12 ,''),state='readonly',justify=CENTER)
        self.entry_select_student.place(x=280,y=100,width=200)
        
        # self.entry_course.current(0)
        self.entry_select_student.set('Empty')
      # entries
        entry_name=Entry(self.root,textvariable=self.Var_name ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_name.place(x=280,y=160,width=320)
        entry_course=Entry(self.root,textvariable=self.Var_course ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_course.place(x=280,y=220,width=320)
        entry_marks=Entry(self.root,textvariable=self.Var_marks ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_marks.place(x=280,y=280,width=320)
        entry_full_marks=Entry(self.root,textvariable=self.Var_full_marks ,font=('gondy old style',12 ,''),bg='lightyellow')
        entry_full_marks.place(x=280,y=340,width=320)

          
    #Buttons 
        self.Btn_Search=Button(self.root,text='Search', font=('gondy old style',15 ,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search_db)
        self.Btn_Search.place(x=500,y=100,width=100,height=23)

        
        self.Btn_Add=Button(self.root,text='Submit', font=('gondy old style',15 ,'bold'),bg='lightgray',fg='white',cursor='hand2',command=self.Add_db)
        self.Btn_Add.place(x=300,y=420,width=110,height=40)

        self.Btn_Clear=Button(self.root,text='Clear', font=('gondy old style',15 ,'bold'),bg='#607d8b',fg='white',cursor='hand2', command=self.clear)
        self.Btn_Clear.place(x=430,y=420,width=110,height=40)

    # Background image 
    

      # Background image
        self.bg_img=Image.open(r"C:\Users\AKH\Desktop\python\student managment system\student managment\icons\result.jpg")
        self.bg_img=self.bg_img.resize((500,300),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg_img=Label(self.root,image=self.bg_img)
        self.lbl_bg_img.place(x=630,y=100)


##def rollnbr fetch##
    def fetch_rollnbr(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute('select rollnbr from student')
            rows=cur.fetchall()
           
            if len(rows)>0:
                for row in rows:
                    self.Var_roll_list.append(row[0])
            # print (v)
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')


# def search
        
    def Search_db(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute(f"select name,course from student where rollnbr=?",(self.Var_rollnbr.get(),))
            row=cur.fetchone()
            if row != None:                    
                self.Var_name.set(row[0])
                self.Var_course.set(row[1]) 
            else:
                messagebox.showerror('error','No record Found')            
            
        except Exception as ex:
            messagebox.showerror('uck',f'{str(ex)} Error')


# add data


    def Add_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_name.get()=='':
                messagebox.showerror('Error', 'Kindly select a Student')
            else:
                #
                cur.execute('select * from result where rollnbr=?  and course=? ',(self.Var_rollnbr.get(),self.Var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error', 'Result Already Present')
                else:
                    #  course  text,ob_marks  text,total_marks  text,percentage  text
                    per=(int(self.Var_marks.get())*100)/int(self.Var_full_marks.get())
                    # rollnbr  text,name  text,course  text,ob_marks  text,total_marks  text,percentage  text
                    
                    cur.execute('insert into result (rollnbr,name,course,ob_marks,total_marks,per)values(?,?,?,?,?,?)',(
                    self.Var_rollnbr.get(),
                    self.Var_name.get(),
                    self.Var_course.get(),
                    self.Var_marks.get(),
                    self.Var_full_marks.get(),
                    str(per)
                    ))
                    con.commit()
                    messagebox.showinfo('Congrates', 'Result added Successfully')
                    # self.show()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')

# ##clear###

    def clear(self):
        self.Var_rollnbr.set('Select')
        self.Var_name.set('')
        self.Var_course.set('')
        self.Var_marks.set('')
        self.Var_full_marks.set('')

    


 





        


if __name__=='__main__':
    root= Tk()
    obj= result_class(root)
    root.mainloop()
