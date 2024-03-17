from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import Image,ImageTk #pip install pillow




background="#06283D"
framebg="#EDEDED"
framefg="06283D"

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Antim@123",
    database="Hotelmanagement"
)
cursor = db.cursor()

class Add_User:
     def __init__(self,root) :
          self.root=root
          self.root.title("Register")
          self.root.geometry('1550x800+0+0')
          self.root.config(bg=background)
          self.root.resizable(False,False)
          
          
          self.admin_password_entry=StringVar()
          self.username_entry = StringVar()
          self.password_entry = StringVar()
     

          
          # #=======================background Image==================

          img2=Image.open("Image/back1.jpg")

          self.photoimg2=ImageTk.PhotoImage(img2)

          labimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE )
          labimg.place(x=5,y=2)
          
          
          
          
          User_id=Label(self.root,text="New User",font=("arial",20,"bold"),padx=2,pady=6)
          User_id.place(x=720,y=180)
          
          
           #USER ID
          
          self.admin_entry=Entry(self.root,width=29,show="*",textvariable=self.admin_password_entry, font=("arial",13,"bold"))
          self.admin_entry.place(x=607,y=250,height=55,width=345)
          self.admin_entry.insert(0, "Admin")
          self.admin_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.admin_entry))
          self.admin_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.admin_entry))
                  
          self.username_entry=Entry(self.root,width=29,textvariable=self.username_entry, font=("arial",13,"bold"))
          self.username_entry.place(x=607,y=320,height=55,width=345)
          self.username_entry.insert(0, "Username")
          self.username_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.username_entry))
          self.username_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.username_entry))
          
          
          #Password
          # user_password=Label(self.root,text="Password",font=("arial",12,"bold"),padx=2,pady=6)
          # user_password.place(x=100,y=100)
          self.password_entry=Entry(self.root,width=29,show="*",textvariable=self.password_entry, font=("arial",13,"bold"))
          self.password_entry.place(x=607,y=390,height=55,width=345)
          self.password_entry.insert(0, "Password")
          self.password_entry.bind("<FocusIn>", lambda event: self.clear_placeholder(self.password_entry))
          self.password_entry.bind("<FocusOut>", lambda event: self.restore_placeholder(self.password_entry))
          
          
          
          btnAdd=Button(self.root,text="Register Now",font=("arial",12,"bold"),command=self.add_new_user,bg="skyblue",fg="white")
          btnAdd.place(x=607,y=468,width=345,height=55)
          #FUNCTION 
     
     def add_new_user(self):
        admin_password = self.admin_password_entry.get()

        # Check if admin password is correct
        if admin_password == "Antim@123":
            new_username = self.username_entry.get()
            new_password = self.password_entry.get()

            # Insert new user into the database
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (new_username, new_password))
            db.commit()

            messagebox.showinfo("Success", "New user added successfully.")
        else:
            messagebox.showerror("Error", "Incorrect admin password.")
            
     def clear_placeholder(self, entry_widget):
        current_text = entry_widget.get()
        if current_text in ["Username", "Password", "Admin"]:
            entry_widget.delete(0, END)

     def restore_placeholder(self, entry_widget):
        current_text = entry_widget.get()
        if current_text.strip() == "":
            if entry_widget in [self.username_entry, self.password_entry, self.admin_entry]:
                entry_widget.insert(0, entry_widget['placeholder'])
     
          
          
if __name__=="__main__":
     root=Tk()
     obj=Add_User(root)
     root.mainloop()