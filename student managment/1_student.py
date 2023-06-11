from tkinter import*
from PIL import Image , ImageTk 
from course import Course_class
from student import Student_class
from reoprt import repot_result_class
from result import result_class
import sqlite3
from tkinter import ttk, messagebox


class RMS:
    def __init__(self,root,*args) :
        self.root= root
        self.root.title('Student Mangment')
        self.root.geometry('1350x700+0+0')
        self.root.config(bg='white')
        # Icon 
        self.logo=ImageTk.PhotoImage(file=r"/home/hussainmir/8th semester/mis/student managment/icons/font_color.png")
        # title
        title=Label(self.root,text='Student Result Management System',compound=LEFT,image=self.logo,padx=10,font=('gondy old style',20 ,'bold'),bg='#033054',fg='white')
        title.place(x=0,y=0,relwidth=1)
      #menu__----frame
        FRmae_1=LabelFrame(self.root,text='Menu', font=('times new roman',15,''),bg='white' )
        FRmae_1.place(x=10,y=70,width=1340,height=80)
      # Background image
        self.bg_img=Image.open(r"/home/hussainmir/8th semester/mis/student managment/icons/main_Background.jpg")
        self.bg_img=self.bg_img.resize((920,400),Image.ANTIALIAS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg_img=Label(self.root,image=self.bg_img)
        self.lbl_bg_img.place(x=400,y=180,width=920,height=400)
    #menu__----Btns
        Btn_course=Button(FRmae_1, text='Course',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.ad_course).place(x=20,y=5,width=200,height=40)
        Btn_Student=Button(FRmae_1, text='Student',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.ad_student).place(x=240,y=5,width=200,height=40)
        Btn_result=Button(FRmae_1, text='result',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.ad_result).place(x=460,y=5,width=200,height=40)
        Btn_View=Button(FRmae_1, text='View Student Result',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.view_result).place(x=680,y=5,width=200,height=40)
        Btn_Logout=Button(FRmae_1, text='Logout',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2').place(x=900,y=5,width=200,height=40)
        Btn_Exit=Button(FRmae_1, text='Exit',font=('gondy old style',15 ,'bold'),bg='#0b5377',fg='white',cursor='hand2').place(x=1120,y=5,width=200,height=40)
        # --Updates---- portion---courses
        self.course_update=Label(self.root,text='Total Courses\n[0]',font=('gondy old style',20 ),bg='#e43b06',fg='white')
        self.course_update.place(x=400,y=530,width=300,height=100)
        # --Updates---- portion---students
        self.students_update=Label(self.root,text='Total Students\n[0]',font=('gondy old style',20 ),bg='#0676ad',fg='white')
        self.students_update.place(x=710,y=530,width=300,height=100)
        # --Updates---- portion---results
        self.results_update=Label(self.root,text='Total Results\n[0]',font=('gondy old style',20 ),bg='#038074',fg='white')
        self.results_update.place(x=1020,y=530,width=300,height=100)
        
        #  upate details 
        self.update_details()

   

        # FOOOTER
        # footer=Label(self.root, text='SRMS Student Result Manageement System\nContact Us For Any Technical Problem',font=('gondy old style',12 ,''),bg='#262626',fg='white').pack(side=BOTTOM,fill=X)
    def ad_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Course_class(self.new_win)

    def ad_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Student_class(self.new_win)

    def view_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=repot_result_class(self.new_win)

    def ad_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=result_class(self.new_win)
    def update_details(self):
        
        con=sqlite3.connect(database='rms.db')
        cur=con.cursor()
        try:
            cur.execute('select * from course')
            cr=cur.fetchall()
            self.course_update.config(text=f"Total Courses [{str(len(cr))}]")
            nbr_courses=len(cr)
            
            cur.execute('select * from student')
            cr=cur.fetchall()
            self.students_update.config(text=f"Total Students [{str(len(cr))}]")
            nbr_students=len(cr)
            
            
            cur.execute('select * from result')
            cr=cur.fetchall()
            self.results_update.config(text=f"Total Results [{str(len(cr))}]")
            nbr_results=len(cr)
            # print(nbr_courses,nbr_students,nbr_results)
            
            
            self.course_update.after(200,self.update_details)       
            
            
            
               
            
        except Exception as ex:
            messagebox.showerror('Fuck',f'{str(ex)} Error')



if __name__=='__main__':
    root= Tk()
    obj=RMS(root)
    root.mainloop()
