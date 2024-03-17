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

        # Report Button for All Data
        btn_all_data = Button(self.root, text="Generate Report (All Data)", command=self.generate_all_data_report, font=("times new roman", 12, "bold"))
        btn_all_data.pack(pady=10)

    def generate_all_data_report(self):
        try:
            # Fetch all room details
            self.cursor.execute("SELECT * FROM Detail")
            room_data = self.cursor.fetchall()

            # Fetch all customer details
            self.cursor.execute("SELECT * FROM customer")
            customer_data = self.cursor.fetchall()

            # Fetch all meals
            self.cursor.execute("SELECT * FROM meals")
            meals_data = self.cursor.fetchall()

            # Generate report window
            report_window = Toplevel(self.root)
            report_window.title("All Data Report")
            report_window.geometry("600x400")

            # Display room details in the report
            report_label = Label(report_window, text="All Room Data:", font=("times new roman", 16, "bold"))
            report_label.pack(pady=10)

            report_text = Text(report_window, width=80, height=15, font=("times new roman", 12))
            report_text.pack(pady=10)

            for room in room_data:
                report_text.insert(END, f"Floor: {room[0]}, Room No: {room[1]}, Room Type: {room[2]}\n")

            # Display customer details in the report
            report_label = Label(report_window, text="All Customer Data:", font=("times new roman", 16, "bold"))
            report_label.pack(pady=10)

            report_text = Text(report_window, width=80, height=15, font=("times new roman", 12))
            report_text.pack(pady=10)

            for customer in customer_data:
                report_text.insert(END, f"Name: {customer[0]}, Age: {customer[1]}, Gender: {customer[2]}, Email: {customer[3]}\n")

            # Display meals details in the report
            report_label = Label(report_window, text="All Meals Data:", font=("times new roman", 16, "bold"))
            report_label.pack(pady=10)

            report_text = Text(report_window, width=80, height=15, font=("times new roman", 12))
            report_text.pack(pady=10)

            for meal in meals_data:
                report_text.insert(END, f"Meal ID: {meal[0]}, Name: {meal[1]}, Price: {meal[2]}\n")

            report_text.config(state=DISABLED)  # Disable editing
        except Exception as e:
            messagebox.showerror("Error", f"Error generating report: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    obj = Report_win(root)
    root.mainloop()
