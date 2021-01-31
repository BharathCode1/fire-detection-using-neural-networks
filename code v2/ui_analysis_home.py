import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import fucntions_csv_file_operations
import parameters_functions
import functions_image_analyse_report_create
from subprocess import Popen


def create_file_name(image_number):
    raw_image_names = parameters_functions.dwt_image_images


def insertValuesToTree(tree):
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_functions.dwt_analysis_result_csv_path)
    file_list.reverse()
    sno = 0
    for row in file_list:
        sno = row[0]
        tree.insert('', 'end', text=sno, values=(row[2],row[5],row[8],row[11],row[14],row[15],row[16]))


def search_report(date,tree):
    date = date.get()
    file_list = fucntions_csv_file_operations.get_values_from_file(parameters_functions.dwt_analysis_result_csv_path)
    file_list.reverse()
    tree.delete(*tree.get_children())
    sno = 0
    for row in file_list:
        if date == row[11]:
            sno = row[0]
            tree.insert('', 'end', text=sno, values=(row[2], row[4], row[6], row[8], row[10], row[11], row[12]))


def analysis():
    def on_double_click(event):
        item = tree.selection()
        item = tree.selection()[0]
        number = tree.item(item, "text")
        #functions_image_analyse_report_create.open_report(number)
        report_file_name = "D:/fire_detection/result_doc/result_"+str(number)+".docx"
        p = Popen([r"C:/Program Files/Microsoft Office/Office16/WINWORD.EXE", report_file_name], shell=True)

    result_table_window = t.Tk()
    result_table_window.title("Analysis Report")
    result_table_window.resizable(width=0, height=0)

    date_label = t.Label(result_table_window, text="Date : ", font=('Courier', 9)).pack(side='left',pady = 30, padx = 5)


    tree = ttk.Treeview(result_table_window)
    tree["columns"] = ("two","three","four","five","six","seven","eight")
    tree.column("#0",width=50)
    tree.heading("#0",text="Image No",anchor = t.N)
    tree.heading("two",text="Dark Red Fire Region", anchor = t.N)
    tree.column("three",width=150)
    tree.heading("three",text="Red Fire Region", anchor = t.N)
    tree.column("four",width=150)
    tree.heading("four",text="Yellow Fire Region", anchor = t.N)
    tree.column("five",width=150)
    tree.heading("five",text="Orange Fire Region", anchor = t.N)
    tree.column("six",width=150)
    tree.heading("six",text="Smoke Region", anchor = t.N)
    tree.column("seven",width=150)
    tree.heading("seven",text="Date", anchor = t.N)
    tree.column("eight",width=150)
    tree.heading("eight",text="Time", anchor = t.N)


    insertValuesToTree(tree)
    date_entry = t.Entry(result_table_window)
    date_entry.pack(side='left', pady=30, padx=6)
    search_button = t.Button(result_table_window, text='Search', font=('Courier', 9), width=15, state="normal",
                             command=lambda: search_report(date_entry,tree))
    search_button.configure(foreground="blue")
    search_button.pack(side='left', pady=30, padx=5)

    tree.pack(side='left',pady = 5, padx = 14)

    vsb = ttk.Scrollbar(result_table_window, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')

    tree.bind("<<TreeviewSelect>>", on_double_click)

    result_table_window.configure(bg='MediumPurple4')

    result_table_window.mainloop()





