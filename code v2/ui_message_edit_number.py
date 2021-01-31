import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import fucntions_csv_file_operations
import parameters_ui

import re

def is_valid(number):
    pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if pattern.match(number):
        return True
    else:
        messagebox.showerror("Error", "Number Format Wrong")
        print("Number Format Wrong")
        return False


def check_empty_values(name,position,number):
    if(name == "" or position == "" or number == ""):
        messagebox.showerror("Error", "Empty fields present")
        print("Empty fields present")
        return False
    else:
        return True

def edit_number_func(number,mobile_number_text,person_name_text,postition_text):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_ui.file_name_mobile_number)
    for row in file_list:
        if row[2] == number:
            print(row)
            displayData(row[2],row[0],row[1],mobile_number_text,person_name_text,postition_text)
            break

def remove_data(number):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_ui.file_name_mobile_number)
    for row in file_list:
        if row[2] == number:
            print(row)
            file_list.remove(row)
            fucntions_csv_file_operations.write_values_to_file(parameters_ui.file_name_mobile_number, file_list, 'w')
            break

def displayData(mobile_number,person_name,position,mobile_number_text,person_name_text,postition_text):
    #mobile_number_text.insert(0,mobile_number)
    person_name_text.insert(0,person_name)
    postition_text.insert(0,position)

def saveChanges(original_number,mobile_number_text,person_name_text,postition_text,window):
    mobile_number = original_number
    name_data = person_name_text.get()
    position_data = postition_text.get()
    if check_empty_values(name_data, position_data,mobile_number) and is_valid(mobile_number):
        remove_data(mobile_number)
        file_list = [[person_name_text.get(),postition_text.get(),original_number]]
        fucntions_csv_file_operations.write_values_to_file(parameters_ui.file_name_mobile_number,file_list,'a')
        print("Changes saved successfully")
        messagebox.showinfo("Success","Details edited")
    else:
        print("Validation error. Changes not persisted")
    window.destroy()


def edit_number(number):

    edit_number_window= t.Tk()
    edit_number_window.title("Edit Mobile Number")
    edit_number_window.minsize(300, 250)

    t.Label(edit_number_window, text="Mobile Number : ", font=('Courier', 9),bg="MediumPurple4").place(x = 3, y = 23)
    t.Label(edit_number_window, text=str(number), font=('Courier', 9), bg="MediumPurple4").place(x = 150, y = 23)
    t.Label(edit_number_window, text="Person Name : ", font=('Courier', 9), bg="MediumPurple4").place(x = 3, y = 63)
    person_name_text = t.Entry(edit_number_window)
    person_name_text.place(x = 150, y = 63)
    t.Label(edit_number_window, text="Position : ", font=('Courier', 9),bg="MediumPurple4").place(x = 3, y = 103)
    postition_text = t.Entry(edit_number_window)
    postition_text.place(x = 150, y = 103)

    #setData(mobile_number_text,person_name_text,postition_text)

    edit_number_func(number,number,person_name_text,postition_text)

    original_number = number

    edit_button = t.Button(edit_number_window, text='Update Details', font=('Courier', 9), width=25, state = "normal",
                             command= lambda : saveChanges(original_number,number,person_name_text,postition_text,edit_number_window))

    edit_button.configure(foreground="blue")
    edit_button.pack(side=t.BOTTOM, pady = 10)
    edit_number_window.configure(bg='MediumPurple4')
    edit_number_window.resizable(False,False)

    edit_number_window.mainloop()

