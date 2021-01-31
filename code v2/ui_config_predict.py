import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import csv
import parameters_ui
import fucntions_csv_file_operations
import parameters_functions
import os.path
from os import path

def check_data(ip_data):
    return path.exists(ip_data)


def get_video_path():
    raw_values = fucntions_csv_file_operations.get_values_from_file(parameters_functions.csv_video_path)
    input = raw_values[0][0]
    output = raw_values[1][0]
    flag = raw_values[2][0]
    return input, output, flag

def save_data(ip,op,a_ip,a_op,add_number,flag):
    ip_data = ip.get()
    op_data = op.get()
    flag_data = flag.get()
    print(flag_data)
    if flag_data == 1:
        flag_data = "True"
    else:
        flag_data = "False"
    if check_data(ip_data):
        write_data(ip_data,op_data,flag_data)
        messagebox.showinfo("Success","Path Updated")
        add_number.destroy()
    else:
        print("Video file doesn't exists")
        messagebox.showerror("Error", "Video file doesn't exists")
        ip.delete(0,'end')
        op.delete(0, 'end')
        ip.insert(0,a_ip)
        op.insert(0,a_op)

def write_data(ip_data,op_data,flag_data):
    with open(parameters_functions.csv_video_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip_data])
        writer.writerow([op_data])
        writer.writerow([flag_data])
    print("data saved")

def print_data(flag):
    print(flag.get())

def config_predict():
    ip, op, a_flag = get_video_path()
    add_number = t.Tk()
    add_number.title("Video Path Configuration")
    add_number.minsize(500,200)

    t.Label(add_number, text="Input video path : ", bg="MediumPurple4", font=('Courier', 11)).place(x = 3, y = 23)
    input_video_path = t.Entry(add_number, width = 40)
    input_video_path.insert(0,ip)
    input_video_path.place(x = 170, y = 23)

    t.Label(add_number, text="Output video path: ",bg="MediumPurple4", font=('Courier',11)).place(x = 3, y = 63)
    output_video_path = t.Entry(add_number, width = 40)
    output_video_path.insert(0,op)
    output_video_path.place(x = 170, y = 63)
    flag = t.IntVar()
    chk = t.Checkbutton(add_number, text="Record image with less accuracy",variable=flag)
    chk.place(x = 170, y = 103)
    print(a_flag)
    if a_flag == "True":
        chk.select()

    button = t.Button(add_number, text='Save changes', font=('Courier', 9), width=15, state = "normal",
                      command=lambda : save_data(input_video_path,output_video_path,ip,op,add_number,flag))
    button.configure(foreground="blue")
    button.pack(side=t.BOTTOM, anchor = t.E, pady = 5)



    add_number.configure(bg='MediumPurple4')

    add_number.mainloop()


config_predict()