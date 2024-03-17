from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Report_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Report Generation")
        self.root.geometry("600x400")

        # Database connection
        self.conn = mysql.connector.connect(host='localhost', user='root', password='Antim@123', database='Hotelmanagement')
        self.cursor = self.conn.cursor()

        # Title Label
        lbl_title = Label(self.root, text="Generate Report", font=("times new roman", 18, "bold"))
        lbl_title.pack(pady=10)

        # Label and Combobox for Room Number
        lbl_room_no = Label(self.root, text="Room No:", font=("times new roman", 12, "bold"))
        lbl_room_no.pack(pady=5)

        self.combo_room_no = ttk.Combobox(self.root, font=("times new roman", 12), state="readonly")
        self.combo_room_no.pack(pady=5)

        # Generate Report Button
        btn_generate = Button(self.root, text="Generate", command=self.generate_report, font=("times new roman", 12, "bold"))
        btn_generate.pack(pady=10)

    def generate_report(self):
        room_no = self.combo_room_no.get()

        if room_no == '':
            messagebox.showerror("Error", "Please select a room number!")
        else:
            try:
                self.cursor.execute("SELECT * FROM Detail WHERE roomno=%s", (room_no,))
                data = self.cursor.fetchone()
                if data:
                    report_window = Toplevel(self.root)
                    report_window.title("Report")
                    report_window.geometry("400x300")

                    report_label = Label(report_window, text=f"Report for Room No: {room_no}", font=("times new roman", 16, "bold"))
                    report_label.pack(pady=10)

                    # Display room details in the report
                    report_text = Text(report_window, width=40, height=10, font=("times new roman", 12))
                    report_text.pack(pady=10)

                    report_text.insert(END, f"Floor: {data[0]}\n")
                    report_text.insert(END, f"Room No: {data[1]}\n")
                    report_text.insert(END, f"Room Type: {data[2]}\n")

                    report_text.config(state=DISABLED)  # Disable editing
                else:
                    messagebox.showerror("Error", f"No data found for Room No: {room_no}")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")

    def fetch_room_numbers(self):
        try:
            self.cursor.execute("SELECT roomno FROM Detail")
            rooms = self.cursor.fetchall()
            room_list = [room[0] for room in rooms]
            self.combo_room_no['values'] = room_list
        except Exception as e:
            messagebox.showerror("Error", f"Error fetching room numbers: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Report_win(root)
    obj.fetch_room_numbers()  # Fetch room numbers for combobox
    root.mainloop()
