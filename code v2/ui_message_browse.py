import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import fucntions_csv_file_operations
import parameters_ui

def insertValuesToTree(tree):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_ui.file_name_mobile_number)
    sno = 0
    for row in file_list:
        sno+=1
        tree.insert('', 'end', text=sno, values=(row[0],row[1],row[2]))

def search(name,position,number,tree):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_ui.file_name_mobile_number)
    tree.delete(*tree.get_children())
    sno = 0
    for row in file_list:
        if name == row[0] or position == row[1] or number == row[2]:
            sno+=1
            tree.insert('', 'end', text=sno, values=(row[0], row[1], row[2]))
    if sno ==  0:
        messagebox.showerror("Empty Data","No data found")

def message_table():

    message_table_window = t.Tk()
    message_table_window.title("Add Mobile Number")
    message_table_window.minsize(670, 450)

    t.Label(message_table_window, text="Mobile Number : ", font=('Courier', 9),bg="MediumPurple4").place(x=3, y=23)
    mobileNumber = t.Entry(message_table_window)
    mobileNumber.place(x=150, y=23)
    t.Label(message_table_window, text="Person Name : ", font=('Courier', 9),bg="MediumPurple4").place(x=3, y=63)
    personName = t.Entry(message_table_window)
    personName.place(x=150, y=63)
    t.Label(message_table_window, text="Position : ", font=('Courier', 9),bg="MediumPurple4").place(x=3, y=103)
    position = t.Entry(message_table_window)
    position.place(x=150, y=103)

    button = t.Button(message_table_window, text='Search', font=('Courier', 9), width=15, state = "normal",
                          command=lambda : search(personName.get(),position.get(),mobileNumber.get(),tree))
    button.configure(foreground="blue")
    button.place(x=150, y=129)

    tree = ttk.Treeview(message_table_window)
    tree["columns"] = ("two","three","four")
    tree.column("#0",width=50)
    tree.heading("#0",text="SNO",anchor = t.N)
    tree.heading("two",text="Name", anchor = t.N)
    tree.heading("three",text="Position", anchor = t.N)
    tree.heading("four",text="Mobile Number", anchor = t.N)

    insertValuesToTree(tree)

    tree.place(x = 3, y = 170)

    message_table_window.configure(bg='MediumPurple4')

    message_table_window.mainloop()




