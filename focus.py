from tkinter import *
from tkinter import messagebox, simpledialog
import mysql.connector
from tkinter import ttk
from datetime import datetime

class Detail_win:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1295x570+235+220")
        self.root.resizable(False,False)
        
        # Initialize variables
        self.entry_floor = StringVar()
        self.entry_RoomNo = StringVar()
        self.combo_RoomType = StringVar()
        self.report_content = StringVar()

        # Title
        lbl_title = Label(self.root, text="ROOM ADDING DEPARTMENT ", font=("times new roman", 18, "bold"),
                          bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo
        # img2 = Image.open("Image/logo2.jpg")
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        # labimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        # labimg2.place(x=5, y=2, width=100, height=40)

        # Label frame for adding rooms
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Rooms Add", foreground="green",
                                    padx=2, font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=60, width=600, height=400)

        # Table frame for search system
        table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="VIEW DETAILS AND SEARCH SYSTEM", padx=2,
                                 font=("times new roman", 12, "bold"))
        table_Frame.place(x=650, y=60, width=600, height=400)

        # Scrollbars for treeview
        scroll_x = Scrollbar(table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame, orient=VERTICAL)
        self.Detail_table = ttk.Treeview(table_Frame, column=("Floor", "RoomNo", "Room Type"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Detail_table.xview)
        scroll_y.config(command=self.Detail_table.yview)

        self.Detail_table.heading("Floor", text="Floor")
        self.Detail_table.heading("RoomNo", text="Room No")
        self.Detail_table.heading("Room Type", text="Room Type")
        self.Detail_table["show"] = "headings"

        self.Detail_table.column("Floor", width=100)
        self.Detail_table.column("RoomNo", width=100)
        self.Detail_table.column("Room Type", width=100)

        self.Detail_table.pack(fill=BOTH, expand=1)
        self.Detail_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # Buttons
        btnAdd = Button(labelframeleft, text="ADD", command=self.add_room, font=("arial", 12, "bold"),
                        bg="black", fg="gold", width=9)
        btnAdd.grid(row=4, column=0, padx=1)
        btnUpdate = Button(labelframeleft, text="UPDATE", font=("arial", 12, "bold"), bg="black", fg="gold",
                           width=9)
        btnUpdate.grid(row=4, column=1, padx=1)
        btnDelete = Button(labelframeleft, text="DELETE", font=("arial", 12, "bold"), bg="black", fg="gold",
                           width=9)
        btnDelete.grid(row=4, column=2, padx=1)
        btnReset = Button(labelframeleft, text="RESET", font=("arial", 12, "bold"), bg="black", fg="gold",
                          width=9)
        btnReset.grid(row=4, column=3, padx=1)

        # Button to generate report
        btnReport = Button(labelframeleft, text="Generate Report", command=self.generate_report, font=("arial", 12, "bold"),
                           bg="black", fg="gold", width=12)
        btnReport.grid(row=5, columnspan=4, pady=10)

        # Text widget to display report
        self.txtReport = Text(self.root, font=("times new roman", 12), padx=10, pady=10)
        self.txtReport.place(x=10, y=470, width=1275, height=250)

    def generate_report(self):
        password = simpledialog.askstring("Password", "Enter password to generate report:", show='*')
        if password != 'Antim':
            messagebox.showerror("Error", "Incorrect password!")
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='Antim@123',
                                               database='Hotelmanagement')
                cursor = conn.cursor()

                # Get the total number of rooms
                cursor.execute("SELECT COUNT(*) FROM Detail")
                total_rooms = cursor.fetchone()[0]

                # Get the total number of bookings
                cursor.execute("SELECT COUNT(*) FROM Bookings")
                total_bookings = cursor.fetchone()[0]

                # Get the current date and time
                current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Generate the report content
                report_content = f"Hotel Management Report\n\n"
                report_content += f"Date and Time: {current_datetime}\n"
                report_content += f"Total Rooms: {total_rooms}\n"
                report_content += f"Total Bookings: {total_bookings}\n\n"

                # Example: Get list of booked rooms
                cursor.execute("SELECT room_no, customer_name, check_in_date, check_out_date FROM Bookings")
                bookings_data = cursor.fetchall()
                report_content += "List of Booked Rooms:\n"
                for booking in bookings_data:
                    room_no, customer_name, check_in_date, check_out_date = booking
                    report_content += f"Room No: {room_no}, Customer Name: {customer_name}, Check-in Date: {check_in_date}, Check-out Date: {check_out_date}\n"

                # Update the report content in the text widget
                self.txtReport.delete("1.0", END)
                self.txtReport.insert(END, report_content)

            except Exception as e:
                messagebox.showerror("Error", f"Error generating report: {e}")

            finally:
                if 'conn' in locals() and conn.is_connected():
                    cursor.close()
                    conn.close()

    def reset_fields(self):
        self.entry_floor.set('')
        self.entry_RoomNo.set('')
        self.combo_RoomType.set('')

    def get_cursor(self, event):
        item = self.Detail_table.focus()
        values = self.Detail_table.item(item, "values")
        if values:
            self.entry_floor.set(values[0])
            self.entry_RoomNo.set(values[1])
            self.combo_RoomType.set(values[2])

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Antim@123",
                                           database="Hotelmanagement")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM Detail")
            rows = my_cursor.fetchall()

            for child in self.Detail_table.get_children():
                self.Detail_table.delete(child)

            for row in rows:
                self.Detail_table.insert("", END, values=row)

            conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching data: {e}")


if __name__ == "__main__":
    root = Tk()
    obj = Detail_win(root)
    root.mainloop()
