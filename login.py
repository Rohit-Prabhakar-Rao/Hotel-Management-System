from tkinter import*
from tkinter import ttk
from tkinter import Entry, Tk
from PIL import Image,ImageTk   #pip install pillow
from tkinter import messagebox
import mysql.connector
from customer import Cust_Window
from room import RoomBooking
from details import DetailsRoom
from hotel import HotelManagementSystem
from register import Register

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\website3.jpg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=450,height=490)
        
        img1=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\logo5.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=770,y=175,width=100,height=100)
        
        get_str=Label(frame, text="LOGIN", font=("times new roman",22,"bold"),bg="white",fg="black")
        get_str.place(x=160,y=110)
        
        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),bg="white",fg="black")
        username.place(x=88,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=80,y=190,width=270)
        
        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        password.place(x=88,y=225)
        ep = StringVar()
        self.txtpass=ttk.Entry(frame, textvariable = ep, show= '*',font=("times new roman",15,"bold"))
        self.txtpass.place(x=80,y=260,width=270)
        
        img2=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\login_logo.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg2.place(x=670,y=323,width=25,height=25)
        
        img3=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\password.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg3.place(x=670,y=395,width=25,height=25)
        
        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,bg="grey",fg="black")
        loginbtn.place(x=150,y=320,width=120,height=35)
        
        #register button
        registerbtn=Button(frame,text="Create new account",command=self.register_window,font=("times new roman",12,"bold"),borderwidth=0,bg="white",fg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=137,y=370,width=160)
        
        #forgot password button
        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",12,"bold"),borderwidth=0,bg="white",fg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=129,y=400,width=160)
    
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="samyukta" and self.txtpass.get()=="sam2101":
            messagebox.showinfo("Success","Welcome to Hotel Park Land")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
             my_cursor=conn.cursor()
             my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
                                                                                       ))
             
             row=my_cursor.fetchone()
             if row==None:
                 messagebox.showerror("Error","Invalid username or password")
             else:
                 open_main=messagebox.askyesno("YesNo","Access only admin")
                 if open_main>0:
                     self.new_window=Toplevel(self.root)
                     self.app=HotelManagementSystem(self.new_window)
                 else:
                     if not open_main:
                         return
             conn.commit()
             conn.close()
             
    def reset_pass(self):
        if self.combo_security_Q.get()=="" or self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select security question",parent=self.root2)
        elif self.txt_security_A.get()=="":
            messagebox.showerror("Error","Enter answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Enter new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security_A.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showinfo("Error","Enter correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Password has been changed successfully",parent=self.root2)
                self.root2.destroy()
            
             
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter username")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            
            if row==None:
                messagebox.showerror("Error","Enter valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="black",bg="white")
                l.place(x=0,y=10,relwidth=1)
                
                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")   
                security_Q.place(x=50,y=80) 
        
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Date","Your Last Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250) 
        
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")   
                security_A.place(x=50,y=150)
        
                self.txt_security_A=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security_A.place(x=50,y=180,width=250)
                
                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")   
                new_password.place(x=50,y=220)
        
                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)  
                
                btn=Button(self.root2,text="Change Password",command=self.reset_pass,font=("times new roman",15,"bold"),fg="black",bg="grey")
                btn.place(x=100,y=290)
                
                
                
                
                
            
            
            
        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
                   
           
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\website3.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #self.bg1=ImageTk.PhotoImage(file=r"C:\Users\HP\Hotel Management\images\register1.jpg")
        #left_lbl=Label(self.root,image=self.bg1)
        #left_lbl.place(x=50,y=100,width=470,height=550)
        
        frame=Frame(self.root,bg="white")
        frame.place(x=360,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="black",bg="white")
        register_lbl.place(x=20,y=20)
        
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=370,y=100)
        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=370,y=130,width=250)
        
        contact=Label(frame,text="Mobile No.",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)     
        
        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")   
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)   
        
        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")   
        security_Q.place(x=50,y=240) 
        
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Date","Your Last Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250) 
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")   
        security_A.place(x=370,y=240)
        
        self.txt_security_A=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security_A.place(x=370,y=270,width=250) 
        
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")   
        pswd.place(x=50,y=310) 
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250) 
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")   
        confirm_pswd.place(x=370,y=310) 
        
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250) 
        
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree with Terms and Conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=390)
        
        #register button
        img=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\register now.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",20,"bold"))
        b1.place(x=10,y=430,width=300)
        
        img1=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\login now.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",20,"bold"))
        b1.place(x=330,y=430,width=300)
        
        
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="":
            messagebox.showerror("Error","All fields are necessary")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Incorrect Password")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Agree terms and conditions")
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="Samraj@2101",database="management")
             my_cursor=conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","User already exist")
             else:
                 my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.var_fname.get(),
                                                                                         self.var_lname.get(),
                                                                                         self.var_contact.get(),
                                                                                         self.var_email.get(),
                                                                                         self.var_securityQ.get(),
                                                                                         self.var_securityA.get(),
                                                                                         self.var_pass.get()                                                                                        
                                                                                       ))
            
             conn.commit()
             conn.close()
             messagebox.showinfo("Success","Registerd Successfully")
             
    def return_login(self):
        self.root.destroy()


class HotelManagementSystem:
    def __init__(self,root):
         self.root=root
         self.root.title("Hotel Management System")
         self.root.geometry("1500x800+0+0")


         #=======================1st image=============================
         img1=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\hotel.jpg")
         img1=img1.resize((1550,140),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)

         lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=0,width=1550,height=140)

         #=======================logo================================== 
         img2=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\logo.jpg")
         img2=img2.resize((230,140),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
         lblimg.place(x=0,y=0,width=230,height=140)

         #========================title=================================
         lbl_title=Label(self.root,text="HOTEL PARK  LAND", font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_title.place(x=0,y=140,width=1550,height=50)

         #========================main Frame============================
         main_frame=Frame(self.root,bd=4,relief=RIDGE)
         main_frame.place(x=0,y=190,width=1550,height=1000)

         #========================menu==================================
         lbl_menu=Label(main_frame,text="MENU", font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
         lbl_menu.place(x=0,y=0,width=230)

         #========================btn frame=============================
         btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
         btn_frame.place(x=0,y=35,width=230,height=190)

         cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         cust_btn.grid(row=0,column=0,pady=6)

         room_btn=Button(btn_frame,text="ROOMS",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         room_btn.grid(row=1,column=0,pady=6)

         details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         details_btn.grid(row=2,column=0,pady=6)

         #report_btn=Button(btn_frame,text="REPORT",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         #report_btn.grid(row=3,column=0,pady=1)

         logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
         logout_btn.grid(row=4,column=0,pady=6)


         #==============================right side image=========================================
         img3=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\hotel1.jpg")
         img3=img3.resize((1310,590),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
         lblimg1.place(x=225,y=0,width=1310,height=590)

          #==============================down image=========================================
         img4=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\room.jpg")
         img4=img4.resize((230,210),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
         lblimg1.place(x=0,y=225,width=230,height=210)

         img5=Image.open(r"C:\Users\ROHIT RAO\Downloads\Hotel Management\Hotel Management\images\restaurant.jpg")
         img5=img5.resize((230,190),Image.ANTIALIAS)
         self.photoimg5=ImageTk.PhotoImage(img5)

         lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
         lblimg1.place(x=0,y=420,width=230,height=190)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Window(self.new_window)
        
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=RoomBooking(self.new_window)
        
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)
        
    def logout(self):
        self.root.destroy()
               
        
        
        




if __name__ == "__main__":
    main()