from sqlite3.dbapi2 import Row
from tkinter import*
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image, ImageTk 


class  repot_result_class:
    def __init__(self,root):

        self.root= root
        self.root.title('Course Details')
        self.root.geometry('1200x480+80+170')
        self.root.config(bg='white')
        self.root.focus_force()
        
       # title
        title=Label(self.root,text='View Result Details',font=('gondy old style',15 ,'bold'),bg='orange',fg='#262626')
        title.place(x=0,y=0,relwidth=1)
    #labels
        lbl_select_student=Label(self.root, text='Search by Roll No.',font=('gondy old style',15 ,'bold'),bg='white')
        lbl_select_student.place(x=250,y=100 )
       #    label  .write
        lbl_rollnbr=Label(self.root, text='Roll No',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_rollnbr.place(x=150,y=230,width=150,height=50)
        lbl_name=Label(self.root, text='Name',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_name.place(x=300,y=230,width=150,height=50)
        lbl_course=Label(self.root, text='Course',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_course.place(x=450,y=230,width=150,height=50)
        lbl_obtained_marks=Label(self.root, text='Marks Obtained',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_obtained_marks.place(x=600,y=230,width=150,height=50)
        lbl_total_marks=Label(self.root, text='Total Marks',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_total_marks.place(x=750,y=230,width=150,height=50)
        lbl_percentage=Label(self.root, text='Percentage',font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        lbl_percentage.place(x=900,y=230,width=150,height=50)

       #    label  to config
       
        self.lbl_rollnbr=Label(self.root, font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_rollnbr.place(x=150,y=280,width=150,height=50)
        self.lbl_name=Label(self.root, font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_name.place(x=300,y=280,width=150,height=50)
        self.lbl_course=Label(self.root,font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_course.place(x=450,y=280,width=150,height=50)
        self.lbl_obtained_marks=Label(self.root,font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_obtained_marks.place(x=600,y=280,width=150,height=50)
        self.lbl_total_marks=Label(self.root, font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_total_marks.place(x=750,y=280,width=150,height=50)
        self.lbl_percentage=Label(self.root, font=('gondy old style',15 ,''),bd=2,relief=GROOVE,bg='white')
        self.lbl_percentage.place(x=900,y=280,width=150,height=50)



        
    # variables
        self.Var_rollnbr_search=StringVar()
        self.Var_rid=''


            
    # Entry boxes
       
        self.entry_select_student=Entry(self.root,textvariable=self.Var_rollnbr_search,font=('gondy old style',12 ,''),bg='lightyellow')
        self.entry_select_student.place(x=480,y=100,width=200)


        
          
    #Buttons 
        self.Btn_Search=Button(self.root,text='Search', font=('gondy old style',15 ,'bold'),bg='#03a9f4',fg='white',cursor='hand2',command=self.Search_db)
        self.Btn_Search.place(x=700,y=100,width=100,height=23)

        self.Btn_clear=Button(self.root,text='Clear', font=('gondy old style',15 ,'bold'),bg='gray',fg='white',cursor='hand2',command=self.Clear_db)
        self.Btn_clear.place(x=820,y=100,width=100,height=23)



        self.Btn_delete=Button(self.root,text='Delete', font=('gondy old style',15 ,'bold'),bg='red',fg='white',cursor='hand2',command=self.Delete_db)
        self.Btn_delete.place(x=550,y=360,width=100,height=50)



    
# def search#########################
        
    def Search_db(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_rollnbr_search.get()=='':
                messagebox.showerror('Error','Kindly Enter a Roll No')
            else:
                    
                cur.execute(f"select * from result where rollnbr=?",(self.Var_rollnbr_search.get(),))
                row=cur.fetchone()
                if row != None:       
                    self.Var_rid=row[0]
                    self.lbl_rollnbr.config(text=row[1])
                    self.lbl_name.config(text=row[2])
                    self.lbl_course.config(text=row[3])
                    self.lbl_obtained_marks.config(text=row[4])
                    self.lbl_total_marks.config(text=row[5])
                    self.lbl_percentage.config(text=row[6])
                else:
                    messagebox.showerror('error','No record Found')            
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')




    
# def Clear #########################
        
    def Clear_db(self):
        self.lbl_rollnbr.config(text='')
        self.lbl_name.config(text='')
        self.lbl_course.config(text='')
        self.lbl_obtained_marks.config(text='')
        self.lbl_total_marks.config(text='')
        self.lbl_percentage.config(text='')
        self.Var_rollnbr_search.set('')
        self.Var_rid=''          



# #########################################################################################################



    def Delete_db(self):

        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            if self.Var_rid=='':
                messagebox.showerror('Error', 'Kindly enter a Roll No')
            else:
                cur.execute('select * from result where rid=?',(self.Var_rid,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error', 'Select a Roll No to be deleted')
                else:
                   op=messagebox.askyesno('Conformation', 'Do you relly want to delete this course')
                   if op==True:
                       cur.execute('delete from  result where rid=?',(self.Var_rid,))
                       con.commit()
                       messagebox.showinfo('Congrates', 'The result has beeen  Deleted Successfully')
                       self.Clear_db()

            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')
# #########################################################################################################


               
              


if __name__=='__main__':
    root= Tk()
    obj= repot_result_class(root)
    root.mainloop()
