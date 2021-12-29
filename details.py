from tkinter import*
from PIL import Image,ImageTk    #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
         self.root=root
         self.root.title("Hotel Management System")
         self.root.geometry("1295x550+230+220")
         
         #========================title=================================
         lbl_title=Label(self.root,text="ROOM BOOKING DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=0,width=1295,height=50)


         #=======================logo==================================
         img2=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\logo.jpg")
         img2=img2.resize((100,40),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
         lblimg.place(x=5,y=2,width=100,height=40)
         
          #=======================label frame============================
         labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add new Room",padx=2,font=("times new roman",12,"bold"))
         labelframeleft.place(x=5,y=50,width=540,height=350)
         
          #=======================labels and entries=====================
         #Floor
         lbl_floor=Label(labelframeleft,text="Floor",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_floor.grid(row=0,column=0,sticky=W)
         
         self.var_floor=StringVar()
         entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("times new roman",13,"bold"))
         entry_floor.grid(row=0,column=1,sticky=W)
         
         #RoomNo
         lbl_RoomNo=Label(labelframeleft,text="Room No.",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_RoomNo.grid(row=1,column=0,sticky=W)

         self.var_RoomNo=StringVar()
         entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("times new roman",13,"bold"))
         entry_RoomNo.grid(row=1,column=1,sticky=W)
         
         #RoomType
         lbl_RoomType=Label(labelframeleft,text="Room Type",font=("times new roman",12,"bold"),padx=2,pady=6)
         lbl_RoomType.grid(row=2,column=0,sticky=W)

         self.var_RoomType=StringVar()
         entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("times new roman",13,"bold"))
         entry_RoomType.grid(row=2,column=1,sticky=W)
         
         #====================btns=========================
         btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
         btn_frame.place(x=0,y=200,width=412,height=40)

         btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnAdd.grid(row=0,column=0,padx=1)

         btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnUpdate.grid(row=0,column=1,padx=1)

         btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnDelete.grid(row=0,column=2,padx=1)

         btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="grey",fg="black",width=9)
         btnReset.grid(row=0,column=3,padx=1)
         
         #=======================table frame============================
         table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",padx=2,font=("times new roman",16,"bold"))
         table_Frame.place(x=600,y=55,width=600,height=350)
         
         scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

         self.roomTable=ttk.Treeview(table_Frame,column=("floor","roomno","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)

         scroll_x.config(command=self.roomTable.xview)
         scroll_y.config(command=self.roomTable.yview)
         
         self.roomTable.heading("floor",text="Floor")
         self.roomTable.heading("roomno",text="Room no")
         self.roomTable.heading("roomType",text="Room Type")
         

         self.roomTable["show"]="headings"

         self.roomTable.column("floor", width=100)
         self.roomTable.column("roomno", width=100)
         self.roomTable.column("roomType", width=100)

         self.roomTable.pack(fill=BOTH,expand=1)
         self.roomTable.bind("<ButtonRelease-1>",self.get_cursor)
         self.fetch_data()
         
    
    #==========================add data======================    
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
           messagebox.showerror("Error","All fields are necessary",parent=self.root)
        else:
           try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(self.var_floor.get(),
                                                                          self.var_RoomNo.get(),
                                                                          self.var_RoomType.get()
         
                                                                        ))
         
                conn.commit()
                self.fetch_data()
                conn.close()
                    
                messagebox.showinfo("Success","Room Added Successfully",parent=self.root)
           except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
                    
 
    #=============================================fetch data===============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
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
        
        self.var_floor.set(row[0])
        self.var_RoomNo.set(row[1])
        self.var_RoomType.set(row[2]) 
        
    #update function   
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter your Floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomType=%s where roomno=%s",( self.var_floor.get(),
                                                                                          self.var_RoomType.get(),
                                                                                          self.var_RoomNo.get()
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
            query="delete from details where roomno=%s"
            value=(self.var_RoomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    #Reset function
    def reset(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")
        
         
         




if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
    