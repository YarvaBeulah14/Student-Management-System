import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("600x400")

# ----- Title -----
title_label = tk.Label(root, text="Student Management System",
                       font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# ----- Form Frame -----
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

# Name
tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(form_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Age
tk.Label(form_frame, text="Age:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
age_entry = tk.Entry(form_frame)
age_entry.grid(row=1, column=1, padx=5, pady=5)

# Course
tk.Label(form_frame, text="Course:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
course_entry = tk.Entry(form_frame)
course_entry.grid(row=2, column=1, padx=5, pady=5)

# Gender
tk.Label(form_frame, text="Gender:").grid(row=3, column=0, padx=5, pady=5, sticky="w")

gender_var = tk.StringVar()

tk.Radiobutton(form_frame, text="Male", variable=gender_var,
               value="Male").grid(row=3, column=1, sticky="w")

tk.Radiobutton(form_frame, text="Female", variable=gender_var,
               value="Female").grid(row=3, column=1, sticky="e")

# ----- Listbox -----
student_listbox = tk.Listbox(root, width=70)
student_listbox.pack(pady=15)

# ----- Functions -----
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    gender = gender_var.get()

    # Validation
    if name == "" or age == "" or course == "" or gender == "":
        messagebox.showerror("Error", "Please fill all fields!")
        return

    student_info = f"Name: {name} | Age: {age} | Course: {course} | Gender: {gender}"
    student_listbox.insert(tk.END, student_info)

    # Clear fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    gender_var.set("")

# Delete when row is selected
def delete_selected(event):
    selected = student_listbox.curselection()
    if selected:
        student_listbox.delete(selected[0])

# Bind selection event
student_listbox.bind("<ButtonRelease-1>", delete_selected)

# ----- Add Button -----
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack()

# Run
root.mainloop()
