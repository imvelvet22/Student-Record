import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

id_entry = None
name_entry = None
age_entry = None
sex_var = None
email_entry = None
address_entry = None
contact_entry = None
birthday_entry = None
add_window = None

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        encrypted_ascii = (ord(char) + shift) % 256  # Shift within ASCII range
        encrypted_text += chr(encrypted_ascii)
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        decrypted_ascii = (ord(char) - shift) % 256  # Shift within ASCII range
        decrypted_text += chr(decrypted_ascii)
    return decrypted_text

def encrypt_filename(filename, shift):
    encrypted_filename = filename + ".txt"
    return caesar_cipher_encrypt(encrypted_filename, shift)

def decrypt_filename(encrypted_filename, shift):
    return caesar_cipher_decrypt(encrypted_filename, shift)

def save_student():
    id_no = id_entry.get()
    full_name = name_entry.get()
    age = age_entry.get()
    sex = sex_var.get()
    email_add = email_entry.get()
    address = address_entry.get()
    contact_number = contact_entry.get()
    birthday = birthday_entry.get()

    if not all([id_no, full_name, age, sex, email_add, address, contact_number, birthday]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if not id_no.isdigit():
        messagebox.showerror("Error" , "Id must be a number.")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number.")
        return

    if not contact_number.isdigit():
        messagebox.showerror("Error", "Contact number must be a number.")
        return

    student_info = f"{id_no},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}\n"

    encrypted_student_info = caesar_cipher_encrypt(student_info, shift=3)

    encrypted_filename = encrypt_filename("student_records.txt", shift=3)

    with open(encrypted_filename, "a") as file:
        file.write(encrypted_student_info)

    messagebox.showinfo("Success", "Student information added successfully!")
    clear_entries()
    add_window.destroy()

def open_add_student_window():
    global id_entry, name_entry, age_entry, sex_var, email_entry, address_entry, contact_entry, birthday_entry, add_window

    add_window = tk.Toplevel(root)
    add_window.title("Add Student")

    window_width = 500
    window_height = 400
    screen_width = add_window.winfo_screenwidth()
    screen_height = add_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    add_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    title_label = tk.Label(add_window, text="Add Student Information", font=("Helvetica", 20))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    id_label = tk.Label(add_window, text="Student ID:", font=("Helvetica", 12))
    id_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    id_entry = tk.Entry(add_window, width=30)
    id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    name_label = tk.Label(add_window, text="Full Name:", font=("Helvetica", 12))
    name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    name_entry = tk.Entry(add_window, width=30)
    name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    age_label = tk.Label(add_window, text="Age:", font=("Helvetica", 12))
    age_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    age_entry = tk.Entry(add_window, width=30)
    age_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

   
    sex_label = tk.Label(add_window, text="Sex:", font=("Helvetica", 12))
    sex_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
    sex_var = tk.StringVar(value="Male")
    sex_male = tk.Radiobutton(add_window, text="Male", variable=sex_var, value="Male", font=("Helvetica", 12))
    sex_male.grid(row=4, column=1, padx=10, pady=5, sticky="w")
    sex_female = tk.Radiobutton(add_window, text="Female", variable=sex_var, value="Female", font=("Helvetica", 12))
    sex_female.grid(row=4, column=1, padx=100, pady=5, sticky="w")

    email_label = tk.Label(add_window, text="Email Address:", font=("Helvetica", 12))
    email_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    email_entry = tk.Entry(add_window, width=30)
    email_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

    address_label = tk.Label(add_window, text="Address:", font=("Helvetica", 12))
    address_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
    address_entry = tk.Entry(add_window, width=30)
    address_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

    contact_label = tk.Label(add_window, text="Contact Number:", font=("Helvetica", 12))
    contact_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
    contact_entry = tk.Entry(add_window, width=30)
    contact_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    birthday_label = tk.Label(add_window, text="Birthday:", font=("Helvetica", 12))
    birthday_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
    birthday_entry = DateEntry(add_window, width=12, background='darkblue', foreground='white', borderwidth=2)
    birthday_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

    add_button = tk.Button(add_window, text="Add Student", command=save_student, font=("Helvetica", 12))
    add_button.grid(row=9, column=0, columnspan=2, pady=10, padx=20, sticky="we")

    add_window.mainloop()
    

def clear_entries():
    global id_entry, name_entry, age_entry, sex_var, email_entry, address_entry, contact_entry, birthday_entry
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    sex_var.set("Male")
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    birthday_entry.set_date(datetime.strptime("2000-01-01", "%Y-%m-%d"))


def view_students():
    try:
        view_window = tk.Toplevel(root)
        view_window.title("View Students")

        tree = ttk.Treeview(view_window, columns=("Full Name", "Age", "Sex", "Email Address", "Address", "Contact Number", "Birthday"))
        tree.heading("#0", text="Student ID")
        tree.heading("Full Name", text="Full Name", anchor="w")
        tree.heading("Age", text="Age", anchor="w")
        tree.heading("Sex", text="Sex", anchor="w")
        tree.heading("Email Address", text="Email Address", anchor="w")
        tree.heading("Address", text="Address", anchor="w")
        tree.heading("Contact Number", text="Contact Number", anchor="w")
        tree.heading("Birthday", text="Birthday", anchor="w")

        encrypted_filename = encrypt_filename("student_records.txt", shift=3)

        with open(encrypted_filename, "r") as file:
            for line in file:
                decrypted_student_info = caesar_cipher_decrypt(line.strip(), shift=3)
                student_data = decrypted_student_info.split(',')
                if len(student_data) >= 8:
                    tree.insert("", tk.END, text=student_data[0], values=(student_data[1], student_data[2], student_data[3], student_data[4], student_data[5], student_data[6], student_data[7]))

        tree.pack()

    except FileNotFoundError:
        messagebox.showinfo("No Records", "No student records found. Please add a student first.")


search_entry = None
def search_student():
    global search_entry
    student_id = search_entry.get()
    found = False
    with open("student_records.txt", "r") as file:
        for line in file:
            if line.startswith(student_id):
                found = True
                student_info = line.split(',')
                display_search_result(student_info)
                break
    if not found:
        messagebox.showinfo("Student Not Found", "Student not found.")

def display_search_result(student_info):
    search_window = tk.Toplevel(root)
    search_window.title("Search Result")
    window_width = 600
    window_height = 400
    screen_width = search_window.winfo_screenwidth()
    screen_height = search_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    search_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    tk.Label(search_window, text="Student Information", font=("Helvetica", 20)).pack(pady=10)

    tk.Label(search_window, text=f"Student Id:       {student_info[0]}").pack(pady=5)
    tk.Label(search_window, text=f"Full Name:        {student_info[1]}").pack(pady=5)
    tk.Label(search_window, text=f"Age:              {student_info[2]}").pack(pady=5)
    tk.Label(search_window, text=f"Sex:              {student_info[3]}").pack(pady=5)
    tk.Label(search_window, text=f"Email Address:    {student_info[4]}").pack(pady=5)
    tk.Label(search_window, text=f"Address:          {student_info[5]}").pack(pady=5)
    tk.Label(search_window, text=f"Contact Number:   {student_info[6]}").pack(pady=5)
    tk.Label(search_window, text=f"Birthday:         {student_info[7]}").pack(pady=5)


def delete_student_record(student_id):
    if not student_id:
        messagebox.showinfo("Error", "Please enter the student ID first.")
        return

    found = False
    updated_records = []

    with open("student_records.txt", "r") as file:
        for line in file:
            if line.startswith(student_id):
                found = True
            else:
                updated_records.append(line)

    if not found:
        messagebox.showinfo("Student Not Found", "Student not found.")
    else:
        with open("student_records.txt", "w") as file:
            file.writelines(updated_records)
        messagebox.showinfo("Success", "Student record deleted successfully.")

def delete_button_clicked():
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Record")

    window_width = 300
    window_height = 200
    screen_width = delete_window.winfo_screenwidth()
    screen_height = delete_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    delete_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    delete_label = tk.Label(delete_window, text="Enter Student ID to delete:", font=("Helvetica", 12))
    delete_label.pack(pady=10)

    delete_entry = tk.Entry(delete_window, font=("Helvetica", 12))
    delete_entry.pack(pady=10)

    delete_button = tk.Button(delete_window, text="Delete", command=lambda: delete_student_record(delete_entry.get()), font=("Helvetica", 12))
    delete_button.pack(pady=10)

def update_student_record():
    def verify_student_id():
        student_id = id_entry.get()
        found = False
        with open("student_records.txt", "r") as file:
            for line in file:
                if line.startswith(student_id):
                    found = True
                    break

        if not found:
            messagebox.showerror("Error", "Student ID not found.")
            return

        # Hide the verification window and show the update window
        verify_window.destroy()
        show_update_window(student_id)

    def show_update_window(student_id):
        update_window = tk.Toplevel(root)
        update_window.title("Update Record")

        window_width = 500
        window_height = 400
        screen_width = update_window.winfo_screenwidth()
        screen_height = update_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        update_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        # Function to save updated record
        def save_updated_record():
            # Get updated information
            full_name = name_entry.get()
            age = age_entry.get()
            sex = sex_var.get()
            email_add = email_entry.get()
            address = address_entry.get()
            contact_number = contact_entry.get()
            birthday = birthday_entry.get()

            # Construct updated student record
            updated_student_info = f"{student_id},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}\n"

            # Read existing records, update the required record, and write back to the file
            updated_records = []
            with open("student_records.txt", "r") as file:
                for line in file:
                    if line.startswith(student_id):
                        updated_records.append(updated_student_info)
                    else:
                        updated_records.append(line)

            # Write updated records back to the file
            with open("student_records.txt", "w") as file:
                file.writelines(updated_records)

            messagebox.showinfo("Success", "Student information updated successfully!")
            update_window.destroy()

        with open("student_records.txt", "r") as file:
            for line in file:
                if line.startswith(student_id):
                    student_info = line.split(',')
                    break

        name_label = tk.Label(update_window, text="Full Name:", font=("Helvetica", 12))
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(update_window, width=30)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        name_entry.insert(0, student_info[1])

        age_label = tk.Label(update_window, text="Age:", font=("Helvetica", 12))
        age_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        age_entry = tk.Entry(update_window, width=30)
        age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        age_entry.insert(0, student_info[2])

        sex_label = tk.Label(update_window, text="Sex:", font=("Helvetica", 12))
        sex_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        sex_var = tk.StringVar(value=student_info[3])
        sex_male = tk.Radiobutton(update_window, text="Male", variable=sex_var, value="Male", font=("Helvetica", 12))
        sex_male.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        sex_female = tk.Radiobutton(update_window, text="Female", variable=sex_var, value="Female", font=("Helvetica", 12))
        sex_female.grid(row=3, column=1, padx=100, pady=5, sticky="w")

        email_label = tk.Label(update_window, text="Email Address:", font=("Helvetica", 12))
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        email_entry = tk.Entry(update_window, width=30)
        email_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        email_entry.insert(0, student_info[4])

        address_label = tk.Label(update_window, text="Address:", font=("Helvetica", 12))
        address_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(update_window, width=30)
        address_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        address_entry.insert(0, student_info[5])

        contact_label = tk.Label(update_window, text="Contact Number:", font=("Helvetica", 12))
        contact_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(update_window, width=30)
        contact_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        contact_entry.insert(0, student_info[6])

        birthday_label = tk.Label(update_window, text="Birthday:", font=("Helvetica", 12))
        birthday_label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        birthday_entry = DateEntry(update_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        birthday_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        birthday_entry.set_date(student_info[7])

        save_button = tk.Button(update_window, text="Save", command=save_updated_record, font=("Helvetica", 12))
        save_button.grid(row=8, column=0, columnspan=2, pady=10, padx=20, sticky="we")

    verify_window = tk.Toplevel(root)
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

    verify_button = tk.Button(verify_window, text="Verify", command=verify_student_id, font=("Helvetica", 12))
    verify_button.pack(pady=5)

root = tk.Tk()
root.title("Student Record Management System")
root.wm_state("zoom")

title_label = tk.Label(root, text="Student Record Management System", font=("Helvetica", 45))
title_label.pack(pady=80)

button_frame = tk.Frame(root)
button_frame.pack()

add_button = tk.Button(button_frame, text="Add Student", font=("Helvetica", 12), command=open_add_student_window, width=20, height=3)
add_button.grid(row=0, column=0, padx=10, pady=5)

update_button = tk.Button(button_frame, text="Update Record", font=("Helvetica", 12), command=update_student_record, width=20, height=3)
update_button.grid(row=0, column=1, padx=10, pady=5)

view_button = tk.Button(button_frame, text="View Students", font=("Helvetica", 12), command=view_students, width=20, height=3)
view_button.grid(row=1, column=0, padx=10, pady=5)

delete_button = tk.Button(button_frame, text="Delete Record", font=("Helvetica", 12), command=delete_button_clicked, width=20, height=3)
delete_button.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()



