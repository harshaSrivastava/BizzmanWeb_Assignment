from tkinter import *
from tkinter import Tk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1024x576+100+50")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Harsha\Desktop\Python_Refresh\Login.jpeg")
        
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1, relheight=1)

        frame= Frame(self.root, bg="lightgrey")
        frame.place(x=610, y=170,width=340, height=480)

        img1=Image.open(r"C:\Users\Harsha\Desktop\Python_Refresh\login_logo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="lightgrey", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        username=lbl=Label(frame, text="Username", font=("Times New Roman",15,"bold"), fg="black", bg="lightgrey") 
        username.place(x=70, y=155)
        self.txtuser=Entry(frame,font=("Times New Roman",15,), fg="black", bg="lightgrey")
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame, text="Password", font=("Times New Roman",15,"bold"), fg="black", bg="lightgrey") 
        password.place(x=70, y=225)
        self.txtpass=Entry(frame,font=("Times New Roman",15,), fg="black", bg="lightgrey")
        self.txtpass.place(x=40,y=250,width=270)

        loginbtn=Button(frame,command=self.login_func, text="Login",font=("Times New Roman",15,"bold"), bd=3, relief=RIDGE, fg="black", bg="lightgrey")  
        loginbtn.place(x=100, y=300, width=120, height=35)

        registerbtn=Button(frame,text="New User Registration",font=("Times New Roman",10),borderwidth=0, fg="black", bg="lightgrey")  
        registerbtn.place(x=20, y=350, width=160)

        forgetbtn=Button(frame,text="Forget Password",font=("Times New Roman",10), borderwidth=0, fg="black", bg="lightgrey")  
        forgetbtn.place(x=10, y=370, width=160)

    def login_func(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error!","All fields are required")
        else:
            try:
                connection=mysql.connector.connect(host="localhost",user="root",password="system",database="register")
                cur = connection.cursor()
                cur.execute("select * from login where username=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error!","Invalid USERNAME & PASSWORD")
                else:
                    messagebox.showinfo("Success","login Successful")
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}")


root=Tk()
app=login_window(root)
root.mainloop()        