from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Window:
    def __init__(self,root):
         self.root=root
         self.root.title("Hotel Management System")
         self.root.geometry("1295x550+230+220")
         
         
         #=======================variables=============================
         self.var_ref=StringVar()
         x=random.randint(1000,9999)
         self.var_ref.set(str(x))
         
         self.var_cust_name=StringVar()
         self.var_father=StringVar()
         self.var_gender=StringVar()
         self.var_post=StringVar()
         self.var_mobile=StringVar()
         self.var_email=StringVar()
         self.var_nationality=StringVar()
         self.var_idnumber=StringVar()
         self.var_idproof=StringVar()
         self.var_address=StringVar()
        


         #========================title=================================
         lbl_title=Label(self.root,text="CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=0,width=1295,height=50)


         #=======================logo==================================
         img2=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\logo.jpg")
         img2=img2.resize((100,40),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
         lblimg.place(x=5,y=2,width=100,height=40)

         #=======================label frame============================
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
         labelframeleft.place(x=5,y=50,width=425,height=490)

         #=======================labels and entries=====================
         #custRef
         lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_cust_ref.grid(row=0,column=0,sticky=W)

         entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"),state="readonly")
         entry_ref.grid(row=0,column=1)

         #custName
         cname=Label(labelframeleft,text="Customer name",font=("times new roman",12,"bold"),padx=2,pady=6)
         cname.grid(row=1,column=0,sticky=W)

         txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,width=29,font=("times new roman",13,"bold"))
         txtcname.grid(row=1,column=1)

         #fatherName
         lblfname=Label(labelframeleft,text="Father name",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblfname.grid(row=2,column=0,sticky=W)

         txtfname=ttk.Entry(labelframeleft,textvariable=self.var_father,width=29,font=("times new roman",13,"bold"))
         txtfname.grid(row=2,column=1)

         #gender combobox
         lbl_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_gender.grid(row=3,column=0,sticky=W)

         combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,width=27,font=("times new roman",13,"bold"),state="readonly")
         combo_gender["value"]=("Male","Female","Other")
         combo_gender.grid(row=3,column=1)

         #postCode
         lblPostCode=Label(labelframeleft,text="Post Code",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblPostCode.grid(row=4,column=0,sticky=W)

         txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,width=29,font=("times new roman",13,"bold"))
         txtPostCode.grid(row=4,column=1)

         #mobileNumber
         lblMobile=Label(labelframeleft,text="Mobile",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblMobile.grid(row=5,column=0,sticky=W)

         txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=29,font=("times new roman",13,"bold"))
         txtMobile.grid(row=5,column=1)

         #email
         lblEmail=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblEmail.grid(row=6,column=0,sticky=W)

         txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,width=29,font=("times new roman",13,"bold"))
         txtEmail.grid(row=6,column=1)

         #nationality
         lblNationality=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblNationality.grid(row=7,column=0,sticky=W)

         combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,width=27,font=("times new roman",13,"bold"),state="readonly")
         combo_Nationality["value"]=("Indian","American","British")
         combo_Nationality.grid(row=7,column=1)

         #idProof
         lblIdProof=Label(labelframeleft,text="Id Proof",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblIdProof.grid(row=8,column=0,sticky=W)

         combo_IdProof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,width=27,font=("times new roman",13,"bold"),state="readonly")
         combo_IdProof["value"]=("Aadhar Card","Driving License","PAN Card")
         combo_IdProof.grid(row=8,column=1)

         #idNumber
         lblIdNumber=Label(labelframeleft,text="Id Number",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblIdNumber.grid(row=9,column=0,sticky=W)

         txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,width=29,font=("times new roman",13,"bold"))
         txtIdNumber.grid(row=9,column=1)

         #address
         lblAddress=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
         lblAddress.grid(row=10,column=0,sticky=W)

         txtAddress=ttk.Entry(labelframeleft,textvariable=self.var_address,width=29,font=("times new roman",13,"bold"))
         txtAddress.grid(row=10,column=1)
        
        #=================================buttons==================================
         btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=400,width=412,height=40)

         btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnAdd.grid(row=0,column=0,padx=1)

         btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnUpdate.grid(row=0,column=1,padx=1)

         btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnDelete.grid(row=0,column=2,padx=1)

         btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnReset.grid(row=0,column=3,padx=1)

          #=======================table frame============================
         table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Search and View Details",padx=2,font=("times new roman",16,"bold"))
         table_Frame.place(x=435,y=50,width=860,height=490)


        
         lblSearchBy=Label(table_Frame,text="Search By",font=("times new roman",12,"bold"))
         lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
         
         
         self.search_var=StringVar()
         combo_Search=ttk.Combobox(table_Frame,textvariable=self.search_var,width=24,font=("times new roman",13,"bold"),state="readonly")
         combo_Search["value"]=("Mobile","Ref")
         combo_Search.grid(row=0,column=1,padx=2)
         
         self.txt_search=StringVar()

         txtSearch=ttk.Entry(table_Frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
         txtSearch.grid(row=0,column=2,padx=2)

         btnSearch=Button(table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="grey",fg="black",width=10)
         btnSearch.grid(row=0,column=3,padx=1)

         btnShowAll=Button(table_Frame,text="Show All",command=self.fetch_data,font=("arial",12,"bold"),bg="grey",fg="black",width=10)
         btnShowAll.grid(row=0,column=4,padx=1)

         #================================Show Data Table==================
         details_table=Frame(table_Frame,bd=2,relief=RIDGE)
         details_table.place(x=0,y=50,width=860,height=350)

         
         scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

         self.Cust_Details_Table=ttk.Treeview(details_table,column=("Ref","Name","Father","Gender","Post","Mobile","Email","Nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.Cust_Details_Table.xview)
         scroll_y.config(command=self.Cust_Details_Table.yview)

         self.Cust_Details_Table.heading("Ref",text="Refer No")
         self.Cust_Details_Table.heading("Name",text="Name")
         self.Cust_Details_Table.heading("Father",text="Father Name")
         self.Cust_Details_Table.heading("Gender",text="Gender")
         self.Cust_Details_Table.heading("Post",text="Post Code")
         self.Cust_Details_Table.heading("Mobile",text="Mobile No")
         self.Cust_Details_Table.heading("Email",text="Email-ID")
         self.Cust_Details_Table.heading("Nationality",text="Nationality")
         self.Cust_Details_Table.heading("idproof",text="ID Proof")
         self.Cust_Details_Table.heading("idnumber",text="ID Number")
         self.Cust_Details_Table.heading("address",text="Address")

         self.Cust_Details_Table["show"]="headings"

         self.Cust_Details_Table.column("Ref", width=100)
         self.Cust_Details_Table.column("Name", width=100)
         self.Cust_Details_Table.column("Father", width=100)
         self.Cust_Details_Table.column("Gender", width=100)
         self.Cust_Details_Table.column("Post", width=100)
         self.Cust_Details_Table.column("Mobile", width=100)
         self.Cust_Details_Table.column("Email", width=100)
         self.Cust_Details_Table.column("Nationality", width=100)
         self.Cust_Details_Table.column("idproof", width=100)
         self.Cust_Details_Table.column("idnumber", width=100)
         self.Cust_Details_Table.column("address", width=100)

         self.Cust_Details_Table.pack(fill=BOTH,expand=1)
         self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()
         
         
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_father.get()=="":
           
                messagebox.showerror("Error","All fields are necessary",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                            self.var_cust_name.get(),
                                                                                            self.var_father.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_post.get(),
                                                                                            self.var_mobile.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_nationality.get(),
                                                                                            self.var_idproof.get(),
                                                                                            self.var_idnumber.get(),
                                                                                            self.var_address.get(),
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                    
                messagebox.showinfo("Success","Customer Details has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])
        
        
    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter your mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Father=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                 
                                                                                                                                    self.var_cust_name.get(),
                                                                                                                                    self.var_father.get(),
                                                                                                                                    self.var_gender.get(),
                                                                                                                                    self.var_post.get(),
                                                                                                                                    self.var_mobile.get(),
                                                                                                                                    self.var_email.get(),
                                                                                                                                    self.var_nationality.get(),
                                                                                                                                    self.var_idproof.get(),
                                                                                                                                    self.var_idnumber.get(),
                                                                                                                                    self.var_address.get(),
                                                                                                                                    self.var_ref.get()
                                                                                                                                 ))
        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Updated succesfully",parent=self.root)
            
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        #self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_father.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("")
        self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")
 
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
         
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
                
        
            
             
        
        
            
                                           
        
                
                
                
            
            
            

            
            
        














if __name__=="__main__":
    root=Tk()
    obj=Cust_Window(root)
    root.mainloop()