import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import ui_message_edit_number


def is_empty(number):
    if number == "":
        return True
    else:
        return False


def move_to_next_window(number,window):
    if is_empty(number):
        messagebox.showerror("Data Error", "No Value Found")
        print("Validation Error @ui_message_edit_number_home")
        window.destroy()
    else:
        ui_message_edit_number.edit_number(number)
        window.destroy()


def edit_number_home():
    edit_number_home_window= t.Tk()
    edit_number_home_window.title("Edit Mobile Number Home")
    edit_number_home_window.minsize(300, 90)

    t.Label(edit_number_home_window, text="Mobile Number : ", font=('Courier', 9), bg="MediumPurple4").place(x = 3, y = 23)
    mobile_number_text = t.Entry(edit_number_home_window)
    mobile_number_text.place(x = 150, y = 23)

    fetch_data_button = t.Button(edit_number_home_window, text='Fetch Number Details', font=('Courier', 9), width=25, state = "normal",
                             command= lambda :move_to_next_window(mobile_number_text.get(),edit_number_home_window))
    fetch_data_button.pack(side=t.BOTTOM, pady = 10)
    fetch_data_button.configure(foreground="blue")
    edit_number_home_window.configure(bg='MediumPurple4')
    edit_number_home_window.resizable(False,False)

    edit_number_home_window.mainloop()