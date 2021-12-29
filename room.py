from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class RoomBooking:
    def __init__(self,root):
         self.root=root
         self.root.title("Hotel Management System")
         self.root.geometry("1295x550+230+220")
         
         #=======================variables=============================
         self.var_contact=StringVar()
         self.var_checkin=StringVar()
         self.var_checkout=StringVar()
         self.var_roomtype=StringVar()
         self.var_roomavailable=StringVar()
         self.var_meal=StringVar()
         self.var_noOfDays=StringVar()
         self.var_paidtax=StringVar()
         self.var_actualtotal=StringVar()
         self.var_total=StringVar()
         
         #========================title=================================
         lbl_title=Label(self.root,text="ROOM BOOKING", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=0,width=1295,height=50)


         #=======================logo==================================
         img2=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\logo.jpg")
         img2=img2.resize((100,40),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
         lblimg.place(x=5,y=2,width=100,height=40)
         
          #=======================label frame============================
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",padx=2,font=("times new roman",12,"bold"))
         labelframeleft.place(x=5,y=50,width=425,height=490)
         
         #=======================labels and entries=====================
         #custContact
         lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_cust_contact.grid(row=0,column=0,sticky=W)

         entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("times new roman",13,"bold"))
         entry_contact.grid(row=0,column=1,sticky=W)
         
         btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="grey",fg="black",width=8)
         btnFetchData.place(x=340,y=4)
         
         #CheckInDate
         check_in_date=Label(labelframeleft,text="Checkin Date",font=("times new roman",12,"bold"),padx=2,pady=6)
         check_in_date.grid(row=1,column=0,sticky=W)

         txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("times new roman",13,"bold"))
         txtcheck_in_date.grid(row=1,column=1)
         
         #CheckOutDate
         check_out_date=Label(labelframeleft,text="Checkout Date",font=("times new roman",12,"bold"),padx=2,pady=6)
         check_out_date.grid(row=2,column=0,sticky=W)

         txtcheck_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("times new roman",13,"bold"))
         txtcheck_out_date.grid(row=2,column=1)
         
         #RoomType
         label_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
         label_RoomType.grid(row=3,column=0,sticky=W)
         
         conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select roomType from details")
         ide=my_cursor.fetchall()
         
         combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("times new roman",13,"bold"),width=27,state="readonly")
         combo_RoomType["value"]=ide
         combo_RoomType.grid(row=3,column=1)
         
         #AvailableRoom
         lblRoomAvailable=Label(labelframeleft,font=("times new roman",12,"bold"),text="Available Room",padx=2,pady=6)
         lblRoomAvailable.grid(row=4,column=0,sticky=W)
         
         #txtAvailableRoom=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",13,"bold"),width=29)
         #txtAvailableRoom.grid(row=4,column=1)
         
         conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
         my_cursor=conn.cursor()
         my_cursor.execute("select roomno from details")
         rows=my_cursor.fetchall()
         
         combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("times new roman",13,"bold"),width=27,state="readonly")
         combo_RoomNo["value"]=rows
         combo_RoomNo.grid(row=4,column=1)
         
         #Meal
         lblMeal=Label(labelframeleft,font=("times new roman",12,"bold"),text="Meal",padx=2,pady=6)
         lblMeal.grid(row=5,column=0,sticky=W)
         
         txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,font=("times new roman",13,"bold"),width=29)
         txtMeal.grid(row=5,column=1)
         
         #NoOfDays
         lblNoOfDays=Label(labelframeleft,font=("times new roman",12,"bold"),text="No. of Days",padx=2,pady=6)
         lblNoOfDays.grid(row=6,column=0,sticky=W)
         
         txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noOfDays,font=("times new roman",13,"bold"),width=29)
         txtNoOfDays.grid(row=6,column=1)
         
         #PaidTax
         lblNoOfDays=Label(labelframeleft,font=("times new roman",12,"bold"),text="Paid Tax",padx=2,pady=6)
         lblNoOfDays.grid(row=7,column=0,sticky=W)
         
         txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("times new roman",13,"bold"),width=29)
         txtNoOfDays.grid(row=7,column=1)
         
         #SubTotal
         lblNoOfDays=Label(labelframeleft,font=("times new roman",12,"bold"),text="Sub Total",padx=2,pady=6)
         lblNoOfDays.grid(row=8,column=0,sticky=W)
         
         txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("times new roman",13,"bold"),width=29)
         txtNoOfDays.grid(row=8,column=1)
         
         #TotalCost
         lblIdNumber=Label(labelframeleft,font=("times new roman",12,"bold"),text="Total Cost",padx=2,pady=6)
         lblIdNumber.grid(row=9,column=0,sticky=W)
         
         txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("times new roman",13,"bold"),width=29)
         txtIdNumber.grid(row=9,column=1)
         
         #=========================Bill Btn===================================
         btnBill=Button(labelframeleft,command=self.total,text="Bill",font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnBill.grid(row=10,column=0,padx=1,stick=W)
         
         
         #==========================btns=======================================
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
         
         #=========================right side image====================
         img4=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\room.jpg")
         img4=img4.resize((520,200),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         lblimg=Label(self.root,image=self.photoimg4,bd=0,relief=RIDGE)
         lblimg.place(x=760,y=55,width=520,height=200)
         
         
         
         #=======================table frame============================
         table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and  Search System",padx=2,font=("times new roman",16,"bold"))
         table_Frame.place(x=435,y=280,width=860,height=260)

         lblSearchBy=Label(table_Frame,text="Search By",font=("times new roman",12,"bold"))
         lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
         
         
         self.search_var=StringVar()
         combo_Search=ttk.Combobox(table_Frame,textvariable=self.search_var,width=24,font=("times new roman",13,"bold"),state="readonly")
         combo_Search["value"]=("Contact","Room")
         combo_Search.grid(row=0,column=1,padx=2)
         
         self.txt_search=StringVar()
         txtSearch=ttk.Entry(table_Frame,textvariable=self.txt_search,width=24,font=("times new roman",13,"bold"))
         txtSearch.grid(row=0,column=2,padx=2)

         btnSearch=Button(table_Frame,text="Search",command=self.search,font=("times new roman",12,"bold"),bg="grey",fg="black",width=10)
         btnSearch.grid(row=0,column=3,padx=1)

         btnShowAll=Button(table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",12,"bold"),bg="grey",fg="black",width=10)
         btnShowAll.grid(row=0,column=4,padx=1)
         
         #================================Show Data Table=======================
         details_table=Frame(table_Frame,bd=2,relief=RIDGE)
         details_table.place(x=0,y=50,width=860,height=180)

         scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

         self.roomTable=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","no.of days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.roomTable.xview)
         scroll_y.config(command=self.roomTable.yview)

         self.roomTable.heading("contact",text="Contact")
         self.roomTable.heading("checkin",text="Check-in")
         self.roomTable.heading("checkout",text="Check-out")
         self.roomTable.heading("roomtype",text="Room Type")
         self.roomTable.heading("roomavailable",text="Room No")
         self.roomTable.heading("meal",text="Meal")
         self.roomTable.heading("no.of days",text="No of Days")
         

         self.roomTable["show"]="headings"

         self.roomTable.column("contact", width=100)
         self.roomTable.column("checkin", width=100)
         self.roomTable.column("checkout", width=100)
         self.roomTable.column("roomtype", width=100)
         self.roomTable.column("roomavailable", width=100)
         self.roomTable.column("meal", width=100)
         self.roomTable.column("no.of days", width=100)
         self.roomTable.pack(fill=BOTH,expand=1)
         
         self.roomTable.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()
         
         
     #==========================add data======================    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
           messagebox.showerror("Error","All fields are necessary",parent=self.root)
        else:
           try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(self.var_contact.get(),
                                                                                   self.var_checkin.get(),
                                                                                   self.var_checkout.get(),
                                                                                   self.var_roomtype.get(),
                                                                                   self.var_roomavailable.get(),
                                                                                   self.var_meal.get(),
                                                                                   self.var_noOfDays.get()
         
                                                                                 ))
         
                conn.commit()
                self.fetch_data()
                conn.close()
                    
                messagebox.showinfo("Success","Booked Successfully",parent=self.root)
           except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                    
    #=============================================fetch data===============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.roomTable.delete(*self.roomTable.get_children())
            for i in rows:
                self.roomTable.insert("",END,values=i)
            conn.commit()
        conn.close()   
    
    #get cursor    
    def get_cursor(self,event=""):
        cursor_row=self.roomTable.focus()
        content=self.roomTable.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noOfDays.set(row[6])       
        
    #update function   
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter your mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,Room=%s,meal=%s,noOfDays=%s where Contact=%s",(
                                                                                                                                 
                                                                                                                                    self.var_checkin.get(),
                                                                                                                                    self.var_checkout.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noOfDays.get(),
                                                                                                                                    self.var_contact.get()
                                                                                                                                 ))
        
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Updated succesfully",parent=self.root)     
            
    #delete function
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete?",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    #reset function
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noOfDays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")        
         
     #===============================All Data Fetch==================================    
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Contact not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2) 
                showDataframe.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #========================Gender============================
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                
                #============================Email==============================
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)
                
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
                
                #===============================Nationality=====================
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)
                
                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                
                #==================================Address========================
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=120)
                
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
                
    #==========================search system==============================
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
        my_cursor=conn.cursor()
        
        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.roomTable.delete(*self.roomTable.get_children())
            for i in rows:
                self.roomTable.insert("",END,values=i)
            conn.commit()
        conn.close()
                
                
    
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noOfDays.set(abs(outDate-inDate).days)
        
        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
            
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(700)
            q2=float(1000)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
            
        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)    
            
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(700)
            q2=float(700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
            
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(700)
            q2=float(700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
            
        elif(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Suite"):
            q1=float(500)
            q2=float(2700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)  
            
        elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Suite"):
            q1=float(700)
            q2=float(2700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)        
            
        elif(self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Suite"):
            q1=float(700)
            q2=float(2700)
            q3=float(self.var_noOfDays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.3))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%((q5+(q5)*0.3)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)      
                
                
            
            
                                 
        
         
         
         
         
         

         
         
if __name__=="__main__":
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
    