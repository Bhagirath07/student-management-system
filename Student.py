"""

Created on Fri July 03 2020

@author: BhagiraTh Desani
@discription: Create Student Management System Project Using Python GUI And MySQL Database.

"""

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self , root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1366x768+0+0")

        title=Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("Georgia",40,"bold"),bg="DarkSlateGray",fg="white")
        title.pack(side = TOP,fill = X)


        # <<<<<<<<------------------All Variables -------------->>>>>>>>>

        self.enroll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.con_var = StringVar()
        self.bdate_var = StringVar()
        self.gen_var = StringVar()

        self.search_menu = StringVar()
        self.search_txt = StringVar()

        # <<<<<<<<<<<<<<<<<<--------------- Manage Block/Frame --------------------->>>>>>>>>>>>>>>>

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE, bg="Gray")
        Manage_Frame.place(x=20,y=100,width=480,height=610)

        m_title = Label(Manage_Frame, text="Manage Students", bg="Gray",fg="black",font=("Georgia",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        # <<<<<--------::::: Enrollment No. :::::------>>>>>>
        lbl_roll = Label(Manage_Frame, text="Enroll No.", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        txt_Roll = Entry(Manage_Frame,width=26,textvar=self.enroll_var,font=("times new roman",15),bd=3,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: Student Name :::::------>>>>>>
        lbl_name = Label(Manage_Frame, text="Name", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")

        txt_Name = Entry(Manage_Frame,width=26,textvar=self.name_var,font=("times new roman",15),bd=3,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: Email ID :::::------>>>>>>
        lbl_email = Label(Manage_Frame, text="Email", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=10,sticky="w")

        txt_Email = Entry(Manage_Frame,width=26,textvar=self.email_var,font=("times new roman",15),bd=3,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: Contact No. :::::------>>>>>>
        lbl_cont = Label(Manage_Frame, text="Contact", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_cont.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        txt_Cont = Entry(Manage_Frame,width=26,textvar=self.con_var,font=("times new roman",15),bd=3,relief=GROOVE)
        txt_Cont.grid(row=4,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: D.O.B :::::------>>>>>>
        lbl_bdate = Label(Manage_Frame, text="D.O.B", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_bdate.grid(row=5,column=0,pady=10,padx=10,sticky="w")

        txt_BDate = Entry(Manage_Frame,width=26,textvar=self.bdate_var,font=("times new roman",15),bd=3,relief=GROOVE)
        txt_BDate.grid(row=5,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: Gender :::::------>>>>>>
        lbl_gen = Label(Manage_Frame, text="Gender", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_gen.grid(row=6,column=0,pady=10,padx=10,sticky="w")

        combo_gen = ttk.Combobox(Manage_Frame,width=25,textvar=self.gen_var,font=("times new roman",15),state='readonly')        
        combo_gen['values'] = ('Male','Female','Other')
        combo_gen.grid(row=6,column=1,pady=10,padx=10,sticky="w")

        # <<<<<--------::::: Address :::::------>>>>>>
        lbl_add = Label(Manage_Frame, text="Address", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_add.grid(row=7,column=0,pady=10,padx=10,sticky="w")

        self.txt_Address = Text(Manage_Frame,width=26,height=4, font=("times new roman",15),bd=3,relief=GROOVE)
        self.txt_Address.grid(row=7,column=1,pady=10,padx=10,sticky="w")

        # <<<======== ::::: Button Frame ::::: ========>>>

        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="Gray")
        btn_Frame.place(x=25,y=525,width=420)

        add_btn = Button(btn_Frame,text="Add",width=10,command=self.add_data).grid(row=0,column=0,padx=15,pady=10)
        update_btn = Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delete_btn = Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clear_btn = Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=15)


        #<<<<<<<<<<<<<<<<<<--------------- Details Block/Frame ------------------->>>>>>>>>>>>>>>>>
    
        Details_Block = Frame(self.root, bd=5, relief=RIDGE, bg="Gray")
        Details_Block.place(x=510,y=100,width=840,height=610)

        lbl_detail = Label(Details_Block, text="Search By", bg="Gray",fg="black",font=("Georgia",20,"bold"))
        lbl_detail.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Details_Block,width=12,textvar=self.search_menu,font=("times new roman",16),state='readonly')        
        combo_search['values'] = ('e_no')
        combo_search.grid(row=0,column=1,pady=10,padx=00,sticky="w")

        txt_search = Entry(Details_Block,width=24,textvar=self.search_txt,font=("times new roman",16),bd=3,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=5,sticky="w")

        search_btn = Button(Details_Block,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=5)
        show_btn = Button(Details_Block,text="Show All",command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=5,pady=10)


        #<<<<<<<<<<<<<<<<<<--------------- Table Block/Frame ------------------->>>>>>>>>>>>>>>>>

        Table_Block = Frame(Details_Block, bd=4, relief=RIDGE, bg="Gray")
        Table_Block.place(x=15,y=70,width=800,height=520)

        scroll_x = Scrollbar(Table_Block,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Block,orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_Block,columns=('enroll','name','email','contact','dob','gender','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side = BOTTOM , fill = X)
        scroll_y.pack(side = RIGHT , fill = Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        
        self.Student_table.heading('enroll',text="Enroll No.")
        self.Student_table.heading('name',text="Name")
        self.Student_table.heading('email',text="Email")
        self.Student_table.heading('contact',text="Contact")
        self.Student_table.heading('dob',text="D.O.B")
        self.Student_table.heading('gender',text="Gender")
        self.Student_table.heading('address',text="Address")
        self.Student_table['show'] = "headings"
        
        self.Student_table.column('enroll',width=100)
        self.Student_table.column('name',width=100)
        self.Student_table.column('email',width=100)
        self.Student_table.column('contact',width=100)
        self.Student_table.column('dob',width=100)
        self.Student_table.column('gender',width=100)
        self.Student_table.column('address',width=100)
        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    #<<<<<------====== Connection with Database ======------>>>>>>>
    def add_data(self):
        
        if self.enroll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")
        else:
            con = pymysql.connect(host="localhost",user="root",password="",database="sms_data")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.enroll_var.get(),
                    self.name_var.get(),
                    self.email_var.get(),
                    self.con_var.get(),
                    self.bdate_var.get(),
                    self.gen_var.get(),
                    self.txt_Address.get('1.0',END))
            ) 
            con.commit()
            self.fetch_data()
            self.clear()
            con.close() 
            messagebox.showinfo("Successfull", "Record has been inserted.")

    def fetch_data(self):
        
        con = pymysql.connect(host="localhost",user="root",password="",database="sms_data")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()

        if len(rows)!=0 :
            self.Student_table.delete(*self.Student_table.get_children())

            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()   

    def clear(self):
        
        self.enroll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.con_var.set("")
        self.bdate_var.set("")
        self.gen_var.set("")
        self.txt_Address.delete('1.0',END)

    def get_cursor(self,evnt):
        
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
 
        self.enroll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.con_var.set(row[3])
        self.bdate_var.set(row[4])
        self.gen_var.set(row[5])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[6]) 

    def update_data(self):
        
        if self.enroll_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "please fill all the fields!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="sms_data")
            cur = con.cursor()
            
            cur.execute("UPDATE students SET name=%s,email=%s,contact=%s,dob=%s,gender=%s,address=%s WHERE e_no=%s;",( 
            self.name_var.get(), 
            self.email_var.get(), 
            self.con_var.get(),
            self.bdate_var.get(), 
            self.gen_var.get(), 
            self.txt_Address.get('1.0', END), 
            self.enroll_var.get()  ))


            con.commit()
            self.fetch_data() # this is for if we add any new student then it will call and update the pool
            self.clear()
            con.close()
            messagebox.showinfo("successfull", "Record has been updated.")

    def delete_data(self):
        
        con = pymysql.connect(host="localhost",user="root",password="",database="sms_data")
        cur = con.cursor()
        cur.execute("delete from students where e_no=%s",self.enroll_var.get())
        
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("successfull", "Record has been deleted.")
    
    def search_data(self):
        
        con = pymysql.connect(host="localhost",user="root",password="",database="sms_data")
        cur = con.cursor()
        sql = "SELECT * FROM students WHERE e_no = %s"
        adr = self.search_txt.get()

        val = cur.execute(sql, adr)
        if(not val):
            messagebox.showinfo("No", "Not availabe!")
        # cur.execute("select * from students where"+str(self.search_menu.get())+" Like '%"+str(self.search_txt.get())+"%'")
        
        rows = cur.fetchall()
        if len(rows)!=0 :
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            
            con.commit()
        con.close()



root = Tk()
s_obj = Student(root)
root.mainloop()        
