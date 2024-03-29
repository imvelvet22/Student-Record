import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime
from PIL import Image, ImageTk

# Constants or configuration variables
WINDOW_WIDTH = 427
WINDOW_HEIGHT = 400
ID_SIZE = "123456"
CONTACT_NUMBER_SIZE = "12345678900"


class StudentRecordManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Information System")
        self.root.wm_state("zoom")

        self.copyright_label = tk.Label( self.root, text="© 2024 Baltazar, Bautista, Cabigting, Rueras", font=("Helvetica", 10))
        self.copyright_label.place(relx=1.0, rely=1.0, anchor='se', x=-130, y=-90)
        
# "C:\\Users\\Monique Kyle\\OneDrive\\Documents\\Desktop\\GitHub\\projectclone\\asset\\ui.png"/-
        self.image_path =("C:\\Users\\HomePC\\Desktop\\projectclone\\Student-Record\\uii.png")
        self.image = Image.open("C:\\Users\\HomePC\\Desktop\\projectclone\\Student-Record\\uii.png")

        self.resized_image = self.image.resize((200, 200)) # Adjust the size as needed, resize image to yung sa gilid
        self.photo = ImageTk.PhotoImage(self.resized_image)

        self.image_label = tk.Label(self.root, image=self.photo)
        self.image_label.place(x=50, y=50)

        self.pink_frame = tk.Frame(self.root, bg="black", width=360, height=590)  #yung box
        self.pink_frame.place(relx=0.2, rely=0.05, anchor='nw')  # Adjust relx to move the frame to the right

        self.title_label = tk.Label(self.root, text="Student\nInformation\nSystem", font=("Times New Roman", 60), anchor='e', justify='right')
        self.title_label.place(relx=1, rely=0.4, anchor='e', x=-130, y=90)

        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(side='top', padx=20, pady=(100, 200), anchor='se')  #  move it higher

        self.search_label = tk.Label(self.search_frame, text="Enter ID:", font=("Helvetica", 14))
        self.search_label.grid(row=0, column=0, padx=(0, 10))  # move it to the right

        self.search_entry = tk.Entry(self.search_frame, width=40)
        self.search_entry.grid(row=0, column=1, padx=(0, 10))

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_student, font=("Helvetica", 12), bg="black", fg="#DBBB5F")
        self.search_button.grid(row=0, column=2, padx=(0, 100)) 

        self.buttons = []
        button_info = [("Add Student", self.open_add_student_window),
                       ("View Students", self.view_students),
                       ("Update Record", self.update_student_record),
                       ("Delete Record", self.delete_student_record)]

        for i, (btn_text, command) in enumerate(button_info):
            btn = tk.Button(self.root, text=btn_text, command=command, font=("Helvetica", 12), bg="black", fg="#DBBB5F", width=30, height=3)
            btn.place(relx=0.43, rely=0.4, anchor='center', x=-115, y=100*i - 30)
            btn.bind("<Enter>", self.on_enter)
            btn.bind("<Leave>", self.on_leave)
            self.buttons.append(btn)

    def on_enter(self, event):
        event.widget.config(bg="white")

    def on_leave(self, event):
        event.widget.config(bg="black")  

    def open_add_student_window(self):
        AddStudentWindow(self.root)

    def view_students(self):
        ViewStudentsWindow(self.root)

    def update_student_record(self):
        UpdateStudentRecordWindow(self.root)

    def delete_student_record(self):
        DeleteStudentRecordWindow(self.root)
    def search_student(self):
        student_id = self.search_entry.get()
        if not student_id:  # Check if the student ID entry is empty
                messagebox.showerror("Error", "Please enter the student ID.")
                return
        if not student_id.isdigit() or len(student_id) != 6:  # Check if the student ID is not 6 digits
            messagebox.showerror("Error", "Student ID must be a 6-digit number.")
            return
        
        found, student_info = find_student_info(student_id)
        
        if found:
            DisplaySearchResultWindow(self.root, student_info)
        else:
            messagebox.showinfo("Student Not Found", "Student not found.")

    def run(self):
        self.root.mainloop()

class AddStudentWindow:
    def __init__(self, master):
        self.add_window = tk.Toplevel(master)
        self.add_window.title("Add Student")
        self.screen_width = self.add_window.winfo_screenwidth()
        self.screen_height = self.add_window.winfo_screenheight()
        self.x_coordinate = int((self.screen_width / 2) - (WINDOW_WIDTH / 2))
        self.y_coordinate = int((self.screen_height / 2) - (WINDOW_HEIGHT / 2))
        self.add_window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{self.x_coordinate}+{self.y_coordinate}")


        # Initialize GUI components
        self.initialize_gui()

    def initialize_gui(self):
        # Labels
        title_label = tk.Label(self.add_window, text="Add Student Information", font=("Times New Roman", 30))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        id_label = tk.Label(self.add_window, text="Student ID:", font=("Helvetica", 12))
        id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.id_entry = tk.Entry(self.add_window, width=30)
        self.id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.id_entry.bind('<FocusOut>', lambda event: self.validate_id())
        name_label = tk.Label(self.add_window, text="Full Name:", font=("Helvetica", 12))
        name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(self.add_window, width=30)
        self.name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        sex_label = tk.Label(self.add_window, text="Sex:", font=("Helvetica", 12))
        sex_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.sex_var = tk.StringVar(value="Male")
        sex_male = tk.Radiobutton(self.add_window, text="Male", variable=self.sex_var, value="Male", font=("Helvetica", 12))
        sex_male.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        sex_female = tk.Radiobutton(self.add_window, text="Female", variable=self.sex_var, value="Female", font=("Helvetica", 12))
        sex_female.grid(row=3, column=1, padx=100, pady=5, sticky="w")

        email_label = tk.Label(self.add_window, text="Email Address:", font=("Helvetica", 12))
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = tk.Entry(self.add_window, width=30)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        address_label = tk.Label(self.add_window, text="Address:", font=("Helvetica", 12))
        address_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.address_entry = tk.Entry(self.add_window, width=30)
        self.address_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        contact_label = tk.Label(self.add_window, text="Contact Number:", font=("Helvetica", 12))
        contact_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.contact_entry = tk.Entry(self.add_window, width=30)
        self.contact_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        self.contact_entry.bind('<FocusOut>', lambda event: self.validate_contact())
        birthday_label = tk.Label(self.add_window, text="Birthday:", font=("Helvetica", 12))
        birthday_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.birthday_entry = DateEntry(self.add_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.birthday_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        
        add_button = tk.Button(self.add_window, text="Add Student", command=self.save_student, font=("Helvetica", 12), bg="black", fg="#DBBB5F")
        add_button.grid(row=8, column=1, columnspan=1, pady=20, padx=1, sticky="w")
        
    


    def save_student(self):
        # Add Button
        add_button = tk.Button(self.add_window, text="Add Student", command=self.save_student, font=("Helvetica", 12), bg="black", fg="#DBBB5F")
        add_button.grid(row=8, column=1, columnspan=1, pady=20, padx=1, sticky="w")

    def validate_id(self):
        id_no = self.id_entry.get()
        found, _ = find_student_info(id_no)
        if not id_no:
            self.id_entry.config(bg="pink", fg="red")
        elif not id_no.isdigit() or len(id_no) != 6:
            self.id_entry.config(bg="pink", fg="red")
        elif found:
            self.id_entry.config(bg="pink", fg="red")
        else:
            self.id_entry.config(bg="white", fg="black")

    def validate_contact(self):
        contact = self.contact_entry.get()
        if not contact:
           self.contact_entry.config(bg="pink", fg="red")
        elif not contact.isdigit() or len(contact) != 11:
            self.contact_entry.config(bg="pink", fg="red")
        else:
            self.contact_entry.config(bg="white", fg="black")


    def save_student(self):
        id_no = self.id_entry.get()
        full_name = self.name_entry.get()
        sex = self.sex_var.get()
        email_add = self.email_entry.get()
        address = self.address_entry.get()
        contact_number = self.contact_entry.get()
        birthday = self.birthday_entry.get_date().strftime("%m/%d/%Y")

        if not all([id_no, full_name, sex, email_add, address, contact_number, birthday]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Compute age based on birthday
        try:
            age = calculate_age(birthday)
            self.add_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Invalid birthday format. Please use MM/DD/YYYY.")
            return

        student_info = f"{id_no},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}\n"

        encrypted_student_info = encrypt(student_info, shift=3)

        encrypted_filename = encrypt_filename("student_records", shift=3)

        with open(encrypted_filename, "a") as file:
            file.write(encrypted_student_info)

        messagebox.showinfo("Success", "Student information added successfully!")
        


class ViewStudentsWindow:
    def __init__(self, master):
        self.view_window = tk.Toplevel(master)
        self.view_window.title("View Students")

        # Initialize GUI components
        self.initialize_gui()

    def initialize_gui(self):
        # Treeview to display student records
        self.tree = ttk.Treeview(self.view_window)
        self.tree["columns"] = ("ID", "Name", "Age", "Sex", "Email", "Address", "Contact", "Birthday")
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("ID", text="Student ID", anchor=tk.W)
        self.tree.heading("Name", text="Name", anchor=tk.W)
        self.tree.heading("Age", text="Age", anchor=tk.W)
        self.tree.heading("Sex", text="Sex", anchor=tk.W)
        self.tree.heading("Email", text="Email", anchor=tk.W)
        self.tree.heading("Address", text="Address", anchor=tk.W)
        self.tree.heading("Contact", text="Contact", anchor=tk.W)
        self.tree.heading("Birthday", text="Birthday", anchor=tk.W)
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("ID", width=100, minwidth=50, anchor=tk.W)
        self.tree.column("Name", width=200, minwidth=150, anchor=tk.W)
        self.tree.column("Age", width=50, minwidth=50, anchor=tk.W)
        self.tree.column("Sex", width=100, minwidth=50, anchor=tk.W)
        self.tree.column("Email", width=250, minwidth=150, anchor=tk.W)
        self.tree.column("Address", width=250, minwidth=150, anchor=tk.W)
        self.tree.column("Contact", width=130, minwidth=100, anchor=tk.W)
        self.tree.column("Birthday", width=130, minwidth=100, anchor=tk.W)
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbar
        vsb = ttk.Scrollbar(self.view_window, orient="vertical", command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=vsb.set)

        # Display student records
        self.display_students()

    def display_students(self):
        # Clear existing data
        for record in self.tree.get_children():
            self.tree.delete(record)

        # Retrieve student records from file
        encrypted_filename = encrypt_filename("student_records", shift=3)
        with open(encrypted_filename, "r") as file:
            for line in file:
                if line.strip():  # Check if line is not empty
                    decrypted_student_info = decrypt(line.strip(), shift=3)
                    student_info = decrypted_student_info.split(',')
                    self.tree.insert("", tk.END, values=student_info)


class UpdateStudentRecordWindow:
    def __init__(self, master):
        self.master = master
        self.update_window = tk.Toplevel(self.master)
        self.update_window.title("Update Record")
        self.update_window.destroy()

        # Initialize GUI components
        self.initialize_gui()

    def initialize_gui(self):
        def verify_student_id():
            student_id = id_entry.get()
            if not student_id:  # Check if the student ID entry is empty
                messagebox.showerror("Error", "Please enter the student ID.")
                verify_window.destroy()
                return
            if not student_id.isdigit() or len(student_id) != 6:  # Check if the student ID is not 6 digits
                messagebox.showerror("Error", "Student ID must be a 6-digit number.")
                verify_window.destroy()
                return
            found, student_info = find_student_info(student_id)
            if found:
                verify_window.destroy()
                show_update_window(student_info)
            else:
                messagebox.showerror("Error", "Student ID not found.")
                verify_window.destroy()
            
            

        def show_update_window(student_info):
            
            update_window = tk.Toplevel(self.master)
            update_window.title("Update Record")

            window_width = 470
            window_height = 460
            screen_width = update_window.winfo_screenwidth()
            screen_height = update_window.winfo_screenheight()
            x_coordinate = int((screen_width / 2) - (window_width / 2))
            y_coordinate = int((screen_height / 2) - (window_height / 2))
            update_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

            def save_updated_record():
                full_name = name_entry.get()
                sex = sex_var.get()
                email_add = email_entry.get()
                address = address_entry.get()
                contact_number = contact_entry.get()
                birthday = birthday_entry.get_date().strftime("%m/%d/%Y")

                # Check if contact number is a valid number and has 11 digits
                if not contact_number.isdigit() or len(contact_number) != 11:
                    messagebox.showerror("Error", "Contact number must be a number and should have 11 digits.")
                    return

                # Compute age based on birthday
                try:
                    age = calculate_age(birthday)
                    update_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Invalid birthday format. Please use MM/DD/YYYY.")
                    update_window.destroy()
                    return

                
                updated_student_info = f"\n{student_id},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}"

                encrypted_updated_info = encrypt(updated_student_info, shift=3)

                # Read existing records, update the required record, and write back to the file
                updated_records = []
                encrypted_filename = encrypt_filename("student_records", shift=3)
                with open(encrypted_filename, "r") as file:
                    for line in file:
                        decrypted_student_info = decrypt(line.strip(), shift=3)
                        if decrypted_student_info.startswith(student_id):
                            updated_records.append(encrypted_updated_info)
                        else:
                            updated_records.append(line)

                # Write updated records back to the file
                with open(encrypted_filename, "w") as file:
                    file.writelines(updated_records)
                messagebox.showinfo("Success", "Student information updated successfully!")
                
                

            # Extract student ID from decrypted information
            student_id = student_info[0]

            title_label = tk.Label(update_window, text="Update Student Information", font=("Times New Roman", 30))
            title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

            name_label = tk.Label(update_window, text="Full Name:", font=("Helvetica", 12))
            name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
            name_entry = tk.Entry(update_window, width=30)
            name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
            name_entry.insert(0, student_info[1])

            sex_label = tk.Label(update_window, text="Sex:", font=("Helvetica", 12))
            sex_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
            sex_var = tk.StringVar(value=student_info[3])
            sex_male = tk.Radiobutton(update_window, text="Male", variable=sex_var, value="Male", font=("Helvetica", 12))
            sex_male.grid(row=3, column=1, padx=10, pady=10, sticky="w")
            sex_female = tk.Radiobutton(update_window, text="Female", variable=sex_var, value="Female", font=("Helvetica", 12))
            sex_female.grid(row=3, column=1, padx=100, pady=5, sticky="w")

            email_label = tk.Label(update_window, text="Email Address:", font=("Helvetica", 12))
            email_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
            email_entry = tk.Entry(update_window, width=30)
            email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
            email_entry.insert(0, student_info[4])

            address_label = tk.Label(update_window, text="Address:", font=("Helvetica", 12))
            address_label.grid(row=5, column=0, padx=10, pady=10, sticky="e")
            address_entry = tk.Entry(update_window, width=30)
            address_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
            address_entry.insert(0, student_info[5])

            contact_label = tk.Label(update_window, text="Contact Number:", font=("Helvetica", 12))
            contact_label.grid(row=6, column=0, padx=10, pady=10, sticky="e")
            contact_entry = tk.Entry(update_window, width=30)
            contact_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
            contact_entry.insert(0, student_info[6])

            birthday_label = tk.Label(update_window, text="Birthday:", font=("Helvetica", 12))
            birthday_label.grid(row=7, column=0, padx=10, pady=10, sticky="e")
            birthday_entry = DateEntry(update_window, width=12, background='darkblue', foreground='white', borderwidth=2)
            birthday_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
            birthday_entry.set_date(student_info[7])

            save_button = tk.Button(update_window, text="Save", command=save_updated_record, font=("Helvetica", 12), bg="black", fg="#DBBB5F")
            save_button.grid(row=8, column=1, columnspan=1, pady=20, padx=1, sticky="w")

        verify_window = tk.Toplevel(self.master)
        verify_window.title("Verify Student ID")

        window_width = 300
        window_height = 150
        screen_width = verify_window.winfo_screenwidth()
        screen_height = verify_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        verify_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        verify_label = tk.Label(verify_window, text="Enter Student ID:", font=("Helvetica", 12))
        verify_label.pack(pady=10)

        id_entry = tk.Entry(verify_window, font=("Helvetica", 12))
        id_entry.pack(pady=5)

        verify_button = tk.Button(verify_window, text="Verify", command=verify_student_id, font=("Helvetica", 12), bg="black", fg="#DBBB5F")
        verify_button.pack(pady=5)
        

class DeleteStudentRecordWindow:
    def __init__(self, master):
        self.delete_window = tk.Toplevel(master)
        self.delete_window.title("Delete Student Record")

        # Initialize GUI components
        self.initialize_gui()

    def initialize_gui(self):
        # Labels
        title_label = tk.Label(self.delete_window, text="Enter Student ID to Delete:", font=("Helvetica", 12))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.id_entry = tk.Entry(self.delete_window, width=30)
        self.id_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

        delete_button = tk.Button(self.delete_window, text="Delete", command=self.delete_student, font=("Helvetica", 12))
        delete_button.grid(row=2, column=0, columnspan=2, pady=10)

    def delete_student(self):
        student_id = self.id_entry.get()
        if not student_id:  # Check if the student ID entry is empty
                messagebox.showerror("Error", "Please enter the student ID.")
                self.delete_window.destroy()
                return
        if not student_id.isdigit() or len(student_id) != 6:  # Check if the student ID is not 6 digits
            messagebox.showerror("Error", "Student ID must be a 6-digit number.")
            self.delete_window.destroy()
            return
        found = False
        encrypted_filename = encrypt_filename("student_records", shift=3)
        with open(encrypted_filename, "r") as file:
            lines = file.readlines()
        with open(encrypted_filename, "w") as file:
            for line in lines:
                decrypted_student_info = decrypt(line.strip(), shift=3)
                if not decrypted_student_info.startswith(student_id):
                    file.write(line)
                else:
                    found = True

        if found:
            confirm_delete = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student record?")
            if confirm_delete:
                messagebox.showinfo("Success", "Student record deleted successfully!")
            else:
                messagebox.showinfo("Cancelled", "Deletion cancelled.")
                with open(encrypted_filename, "w") as file:
                    for line in lines:
                        file.write(line)
        else:
            messagebox.showerror("Error", "Student ID not found.")
            self.delete_window.destroy()
        self.delete_window.destroy()
            
class DisplaySearchResultWindow:
    def __init__(self, master, student_info):
        self.search_window = tk.Toplevel(master)
        self.search_window.title("Search Result")

        # Initialize GUI components
        self.initialize_gui(student_info)

    def initialize_gui(self, student_info):
        window_width = 600
        window_height = 400
        screen_width = self.search_window.winfo_screenwidth()
        screen_height = self.search_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        self.search_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        title_font = ("Helvetica", 20)
        label_font = ("Arial", 12)

        tk.Label(self.search_window, text="S T U D E N T    I N F O R M A T I O N", font=(title_font[0], title_font[1], 'bold')).pack(pady=20)

        label_width = 50
        birthday = datetime.strptime(student_info[7], "%m/%d/%Y").strftime("%m/%d/%Y")
        age = calculate_age(birthday)

        tk.Label(self.search_window, text=f"Student Id:                          {student_info[0]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Full Name:                           {student_info[1]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Age:                                      {age}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Sex:                                      {student_info[3]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Email Address:                   {student_info[4]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Address:                             {student_info[5]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Contact Number:                {student_info[6]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
        tk.Label(self.search_window, text=f"Birthday:                              {student_info[7]}", width=label_width, anchor="w", font=label_font).pack(pady=5)


# Utility functions here
        
def find_student_info(student_id):
    found = False
    student_info = None
    encrypted_filename = encrypt_filename("student_records", shift=3)
    with open(encrypted_filename, "r") as file:
        for line in file:
            decrypted_student_info = decrypt(line.strip(), shift=3)
            if decrypted_student_info.startswith(student_id):
                found = True
                student_info = decrypted_student_info.split(',')
                break
    return found, student_info

def reverse_text(text):
    return text[::-1]

def encrypt(text, shift):
    reversed_text = reverse_text(text)
    encrypted_text = ""
    for char in reversed_text:
        encrypted_ascii = (ord(char) + shift) % 256  # Shift within ASCII range
        encrypted_text += chr(encrypted_ascii)
    return encrypted_text


def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        decrypted_ascii = (ord(char) - shift) % 256  # Shift within ASCII range
        decrypted_text += chr(decrypted_ascii)
    return reverse_text(decrypted_text)

def encrypt_filename(filename, shift):
    encrypted_filename = encrypt(filename, shift) + ".txt"
    return encrypted_filename

def decrypt_filename(encrypted_filename, shift):
    return decrypt(encrypted_filename, shift)

def calculate_age(birthdate):
    current_date = datetime.now()
    birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
    age = current_date.year - birthdate.year

    # Check if the birth month and day have passed this year
    if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
        age -= 1

    return age

if __name__ == "__main__":
    app = StudentRecordManagementSystem()
    app.run()
