import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import fucntions_csv_file_operations
import parameters_ui

print("importing success")


def delete_number_func(number,window):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_ui.file_name_mobile_number)
    delete_flag = 0
    for row in file_list:
        print(row[2])
        if row[2] == number.get():
            file_list.remove(row)
            delete_flag = 1
    if delete_flag == 1:
        fucntions_csv_file_operations.write_values_to_file(parameters_ui.file_name_mobile_number, file_list, 'w')
        messagebox.showerror("Entry","Entry deleted")
        print("Entry deleted")
        window.destroy()
    else:
        messagebox.showerror("Data Error", "No entry found")
        print("No entry found")
        window.destroy()

def delete_number_main():
    delete_number_window= t.Tk()
    delete_number_window.title("Delete Mobile Number")
    delete_number_window.minsize(300, 90)

    t.Label(delete_number_window, text="Mobile Number : ", font=('Courier', 9),bg="MediumPurple4").place(x = 3, y = 23)
    mobile_number_text = t.Entry(delete_number_window)
    mobile_number_text.place(x = 150, y = 23)

    delete_button = t.Button(delete_number_window, text='Delete Number', font=('Courier', 9), width=15, state = "normal",
                             command= lambda : delete_number_func(mobile_number_text,delete_number_window))
    delete_button.configure(foreground="red")
    delete_button.pack(side=t.BOTTOM, pady = 10)

    delete_number_window.configure(bg='MediumPurple4')

    delete_number_window.resizable(False,False)
    delete_number_window.mainloop()
