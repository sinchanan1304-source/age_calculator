from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import date

# Function to calculate age
def calculate_age():
    dob = cal.get_date()
    today = date.today()

    if dob > today:
        messagebox.showerror("Invalid Date", "Date of Birth cannot be in the future!")
        return

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days += 30
    if months < 0:
        years -= 1
        months += 12

    result_label.config(text=f"{years} Years, {months} Months, {days} Days")


# Main Window
root = Tk()
root.title("Age Calculator")
root.geometry("500x450")
root.configure(bg="#dfe6e9")
root.resizable(False, False)

# Frame Card
frame = Frame(root, bg="white", bd=2, relief=GROOVE)
frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=380, height=350)

# Title
title = Label(frame, text="AGE CALCULATOR", font=("Calibri", 18, "bold"), fg="#2d3436", bg="white")
title.pack(pady=15)

# DOB Label
dob_label = Label(frame, text="Select Your Date of Birth", font=("Arial", 12), bg="white")
dob_label.pack(pady=5)

# Date Picker
cal = DateEntry(frame, width=18, background="#0984e3", foreground="white", date_pattern="dd/mm/yyyy",
                borderwidth=2, font=("Arial", 11))
cal.pack(pady=8)

# Calculate Button
btn = Button(frame, text="CALCULATE", font=("Arial", 12, "bold"), bg="#00b894", fg="white",
             activebackground="#019874", cursor="hand2", width=15, command=calculate_age)
btn.pack(pady=15)

# Result
result_title = Label(frame, text="Your Age is:", font=("Arial", 12, "bold"), bg="white")
result_title.pack(pady=5)

result_label = Label(frame, text="", font=("Arial", 14, "bold"), fg="#6c5ce7", bg="white")
result_label.pack(pady=5)

# Footer
footer = Label(root, text="Created by Sinchana 💜", font=("Arial", 9), bg="#dfe6e9")
footer.pack(side="bottom", pady=8)

root.mainloop()
