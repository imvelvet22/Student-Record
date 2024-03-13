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
search_entry = None

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

def calculate_age(birthdate):
    current_date = datetime.now()
    birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
    age = current_date.year - birthdate.year

    # Check if the birth month and day have passed this year
    if current_date.month < birthdate.month or (current_date.month == birthdate.month and current_date.day < birthdate.day):
        age -= 1

    return age

def save_student():
    global birthday_entry
    size = "123456"
    size2 = "12345678900"
    id_no = id_entry.get()
    full_name = name_entry.get()
    sex = sex_var.get()
    email_add = email_entry.get()
    address = address_entry.get()
    contact_number = contact_entry.get()
    birthday = birthday_entry.get_date().strftime("%m/%d/%Y")

    if not all([id_no, full_name, sex, email_add, address, contact_number, birthday]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    if not id_no.isdigit():
        messagebox.showerror("Error" , "Id must be a number.")
        return
    if (len(id_no) != len(size)):
        messagebox.showerror("Error", "Id Number Size must be 6.")
        return
    
    if not contact_number.isdigit():
        messagebox.showerror("Error", "Contact number must be a number.")
        return
    if (len(contact_number) != len(size2)):
        messagebox.showerror("Error", "Phone number must be 11 in length starting with 09.")
        return
    
    # Compute age based on birthday
    try:
        age = calculate_age(birthday)
    except ValueError:
        messagebox.showerror("Error", "Invalid birthday format. Please use MM/DD/YYYY.")
        return
    
    student_info = f"{id_no},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}\n"

    encrypted_student_info = caesar_cipher_encrypt(student_info, shift=3)

    encrypted_filename = encrypt_filename("student_records.txt", shift=3)

    with open(encrypted_filename, "a") as file:
        file.write(encrypted_student_info)

    messagebox.showinfo("Success", "Student information added successfully!")
    add_window.destroy()

def open_add_student_window():
    global id_entry, name_entry, sex_var, email_entry, address_entry, contact_entry, birthday_entry, add_window

    add_window = tk.Toplevel(root)
    add_window.title("Add Student")

    window_width = 428
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
    add_button.grid(row=9, column=0, columnspan=2, pady=10, padx=1, sticky="we")

    add_window.mainloop()

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

def search_student():
    global search_entry
    student_id = search_entry.get()
    found = False
    encrypted_filename = encrypt_filename("student_records.txt", shift=3)
    with open(encrypted_filename, "r") as file:
        for line in file:
            decrypted_student_info = caesar_cipher_decrypt(line.strip(), shift=3)
            if decrypted_student_info.startswith(student_id):
                found = True
                student_info = decrypted_student_info.split(',')
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

    title_font = ("Helvetica", 20)
    label_font = ("Arial", 12)

    tk.Label(search_window, text="S T U D E N T    I N F O R M A T I O N", font=(title_font[0], title_font[1], 'bold')).pack(pady=20)

    label_width = 50
    birthday = datetime.strptime(student_info[7], "%m/%d/%Y").strftime("%m/%d/%Y")
    age = calculate_age(birthday)

    tk.Label(search_window, text=f"Student Id:                          {student_info[0]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Full Name:                           {student_info[1]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Age:                                      {age}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Sex:                                      {student_info[3]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Email Address:                   {student_info[4]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Address:                             {student_info[5]}", width=label_width, anchor="w", font=label_font).pack(pady=5)
    tk.Label(search_window, text=f"Contact Number:                {student_info[6]}", width=label_width, anchor="w", font=label_font).pack(pady=5)

    tk.Label(search_window, text=f"Birthday:                              {student_info[7]}", width=label_width, anchor="w", font=label_font).pack(pady=5)

def update_student_record():
    def verify_student_id():
        student_id = id_entry.get()
        found = False
        encrypted_filename = encrypt_filename("student_records.txt", shift=3)
        with open(encrypted_filename, "r") as file:
            for line in file:
                decrypted_student_info = caesar_cipher_decrypt(line.strip(), shift=3)
                if decrypted_student_info.startswith(student_id):
                    found = True
                    student_info = decrypted_student_info.split(',')
                    break

        if not found:
            messagebox.showerror("Error", "Student ID not found.")
        else:
            messagebox.showinfo("Success", "Student information found successfully!")
            verify_window.destroy()
            show_update_window(student_info)

    def show_update_window(student_info):
        update_window = tk.Toplevel(root)
        update_window.title("Update Record")

        window_width = 430
        window_height = 300
        screen_width = update_window.winfo_screenwidth()
        screen_height = update_window.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        update_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        def save_updated_record(student_id, found):
            search_window = tk.Toplevel(root)
            search_window.title("Update Student Record")

            full_name = name_entry.get()
            sex = sex_var.get()
            email_add = email_entry.get()
            address = address_entry.get()
            contact_number = contact_entry.get()
            birthday = birthday_entry.get_date().strftime("%m/%d/%Y")

            # Check if any required field is empty
            if not (full_name and sex and email_add and address and contact_number and birthday):
                messagebox.showerror("Error", "All fields are required.")
                return

            # Compute age based on birthday
            try:
                age = calculate_age(birthday)
            except ValueError:
                messagebox.showerror("Error", "Invalid birthday format. Please use MM/DD/YYYY.")
                return

            # Construct updated student record
            updated_student_info = f"{student_id},{full_name},{age},{sex},{email_add},{address},{contact_number},{birthday}\n"

            encrypted_updated_info = caesar_cipher_encrypt(updated_student_info, shift=3)

            # Read existing records, update the required record, and write back to the file
            updated_records = []
            encrypted_filename = encrypt_filename("student_records.txt", shift=3)
            with open(encrypted_filename, "r") as file:
                for line in file:
                    decrypted_student_info = caesar_cipher_decrypt(line.strip(), shift=3)
                    if decrypted_student_info.startswith(student_id):
                        updated_records.append(encrypted_updated_info)
                    else:
                        updated_records.append(line)

            # Write updated records back to the file
            with open(encrypted_filename, "w") as file:
                file.writelines(updated_records)

            messagebox.showinfo("Success", "Student information updated successfully!")
            update_window.destroy()

        name_label = tk.Label(update_window, text="Full Name:", font=("Helvetica", 12))
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        name_entry = tk.Entry(update_window, width=30)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        name_entry.insert(0, student_info[1])

        contact_label = tk.Label(update_window, text="Contact Number:", font=("Helvetica", 12))
        contact_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        contact_entry = tk.Entry(update_window, width=30)
        contact_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        contact_entry.insert(0, student_info[2])

        sex_label = tk.Label(update_window, text="Sex:", font=("Helvetica", 12))
        sex_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        sex_entry = tk.Entry(update_window, width=30)
        sex_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        sex_entry.insert(0, student_info[3])


        address_label = tk.Label(update_window, text="Address:", font=("Helvetica", 12))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        address_entry = tk.Entry(update_window, width=30)
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        address_entry.insert(0, student_info[4])


        birthday_label = tk.Label(update_window, text="Birthday:", font=("Helvetica", 12))
        birthday_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        birthday_entry = tk.Entry(update_window, width=30)
        birthday_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        birthday_entry.insert(0, student_info[5])


         

        # More entry widgets for other fields...

        save_button = tk.Button(update_window, text="Save", command=lambda: save_updated_record(student_info[0], found), font=("Helvetica", 12))
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



def delete_student_record():
    def verify_and_delete():
        student_id = id_entry.get().strip()  # Get the entered student ID and strip any leading/trailing whitespace
        if not student_id:
            messagebox.showerror("Error", "Please enter the Student ID first.")
            return
        
        found = False
        encrypted_filename = encrypt_filename("student_records.txt", shift=3)
        with open(encrypted_filename, "r") as file:
            lines = file.readlines()
        with open(encrypted_filename, "w") as file:
            for line in lines:
                decrypted_student_info = caesar_cipher_decrypt(line.strip(), shift=3)
                if decrypted_student_info.startswith(student_id):
                    found = True
                else:
                    file.write(line)

        if found:
            messagebox.showinfo("Success", "Student information deleted successfully!")
        else:
            messagebox.showerror("Error", "Student ID not found.")

        delete_window.destroy()

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Student Record")

    window_width = 300
    window_height = 150
    screen_width = delete_window.winfo_screenwidth()
    screen_height = delete_window.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    delete_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    delete_label = tk.Label(delete_window, text="Enter Student ID:", font=("Helvetica", 12))
    delete_label.pack(pady=10)

    id_entry = tk.Entry(delete_window, font=("Helvetica", 12))
    id_entry.pack(pady=5)

    delete_button = tk.Button(delete_window, text="Delete", command=verify_and_delete, font=("Helvetica", 12))
    delete_button.pack(pady=5)



root = tk.Tk()
root.title("Student Information System")
root.wm_state("zoom")

canvas = tk.Canvas(root, width=root.winfo_screenwidth() // 2, height=root.winfo_screenheight(), bg="sky blue", highlightthickness=0)
canvas.place(x=0, y=0)  # Ensure it's placed at the back



title_label = tk.Label(root, text="Student Information System", font=("Times New Roman", 45))
title_label.pack(pady=80)



search_frame = tk.Frame(root)
search_frame.pack(pady=(0, 20), padx=(0, 60), anchor='se') 

search_label = tk.Label(search_frame, text="Enter ID:", font=("Helvetica", 12))
search_label.grid(row=0, column=0)

search_entry = tk.Entry(search_frame, width=30)
search_entry.grid(row=0, column=1)

search_button = tk.Button(search_frame, text="Search", command=search_student, font=("Helvetica", 12))
search_button.grid(row=0, column=2, padx=10)


add_button = tk.Button(root, text="Add Student", command=open_add_student_window, font=("Helvetica", 12), width=20, height=2)
add_button.pack(pady=(10, 5))  

view_button = tk.Button(root, text="View Students", command=view_students, font=("Helvetica", 12), width=20, height=2)
view_button.pack(pady=5)

update_button = tk.Button(root, text="Update Student Record", command=update_student_record, font=("Helvetica", 12), width=20, height=2)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Record", command=delete_student_record, font=("Helvetica", 12), width=20, height=2)
delete_button.pack(pady=5)

def on_enter(event):
    event.widget.config(bg="pink")

def on_leave(event):
    event.widget.config(bg="SystemButtonFace")  # Change to the default background color

add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

view_button.bind("<Enter>", on_enter)
view_button.bind("<Leave>", on_leave)

update_button.bind("<Enter>", on_enter)
update_button.bind("<Leave>", on_leave)

delete_button.bind("<Enter>", on_enter)
delete_button.bind("<Leave>", on_leave)

root.mainloop()