import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import parameters_ui
import functions_message
import re

def is_valid(number):
    pattern = re.compile("(0/91)?[6-9][0-9]{9}")
    if pattern.match(number):
        return True
    else:
        messagebox.showerror("Error", "Number Format Wrong")
        print("Number Format Wrong")
        return False

def check_duplicate(new_number):
    with open(parameters_ui.file_name_mobile_number, 'r') as file:
        reader = csv.reader(file)
        mobile_number = list()
        for row in reader:
            mobile_number.append(row[2])
        if(mobile_number.__contains__(new_number)):
            messagebox.showerror("Error","Details Already Exit")
            print("Details Already Exit")
            return False
        else:
            return True


def check_empty_values(name,position,number):
    if name == "" or position == "" or number == "":
        messagebox.showerror("Error", "Empty fields present")
        print("Empty fields present")
        return False
    else:
        return True

def save_data(name,position,number,tree):
    number_data = number.get()
    position_data = position.get()
    name_data = name.get()
    if check_duplicate(number_data) and check_empty_values(name_data,position_data,number_data) and is_valid(number_data):
        write_data(name_data,position_data,number_data,tree)
    number.delete(0,'end')
    position.delete(0,'end')
    name.delete(0,'end')

def write_data(name,position,number,tree):
    with open(parameters_ui.file_name_mobile_number, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name,position,number])
    print("data saved")
    insert_values_to_tree(tree, 0)

def insert_values_to_tree(tree,Flag):
    if(Flag == 1):
        with open(parameters_ui.file_name_mobile_number, 'r') as file:
            reader = csv.reader(file)
            sno = 0
            for row in reader:
                if(row[0]==""):
                    print("File is empty")
                    break
                sno+=1
                tree.insert('', 'end', text=sno, values=(row[0],row[1],row[2]))
    if(Flag == 0):
        with open(parameters_ui.file_name_mobile_number, 'r') as file:
            reader = csv.reader(file)
            sno = 0
            row_data = list()
            for row in reader:
                sno+=1
                row_data = row
        tree.insert('', 'end', text=sno, values=(row_data[0], row_data[1], row_data[2]))

def add_message_number():
    add_number = t.Tk()
    add_number.title("Add Mobile Number")
    add_number.minsize(670, 480)

    t.Label(add_number, text="Mobile Number : ", bg="MediumPurple4", font=('Courier', 11)).place(x = 3, y = 23)
    mobileNumber = t.Entry(add_number)
    mobileNumber.place(x = 150, y = 23)
    t.Label(add_number, text="Person Name : ",bg="MediumPurple4", font=('Courier',11)).place(x = 3, y = 63)
    personName = t.Entry(add_number)
    personName.place(x = 150, y = 63)
    t.Label(add_number, text="Position : ",bg="MediumPurple4", font=('Courier',11)).place(x = 3, y = 103)
    position = t.Entry(add_number)
    position.place(x = 150, y = 103)

    t.Label(add_number, text="Existing registered numbers : ",bg="MediumPurple4", font=('Courier',11)).place(x = 3, y = 170)

    #table creation
    tree = ttk.Treeview(add_number)
    tree["columns"] = ("two","three","four")
    tree.column("#0",width=50)
    tree.heading("#0",text="SNO",anchor = t.N)
    tree.heading("two",text="Name", anchor = t.N)
    tree.heading("three",text="Position", anchor = t.N)
    tree.heading("four",text="Mobile Number", anchor = t.N)

    insert_values_to_tree(tree,1)

    tree.place(x = 3, y = 200)

    button = t.Button(add_number, text='Save changes', font=('Courier', 9), width=15, state = "normal",
                      command=lambda : save_data(personName,position,mobileNumber,tree))
    button.configure(foreground="blue")
    button.pack(side=t.BOTTOM, anchor = t.E, pady = 5)

    add_number.configure(bg='MediumPurple4')

    add_number.mainloop()


