from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector







class Report_win :
     def __init__(self,root):
          self.root=root
          self.root.title("HOTEL MANAGEMENT SYSTEM")
          self.root.geometry("1295x570+235+220")
          self.root.resizable(False,False)



















if __name__=="__main__":
     root=Tk()
     obj=Report_win(root)
     root.mainloop()