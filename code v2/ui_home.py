from tkinter import *
import tkinter as ttk
from PIL import ImageTk, Image
import ui_message_home
import ui_analysis_home
import os



GUI = Tk()
GUI.title("Deflagoration Recognition")
F1=Frame(GUI)
F1=Frame(GUI,width=100,height=100)
F1.place(height=700, width=400, x=0, y=0)
F1.config()

F1.grid(columnspan=10,rowspan=10)

F1.grid_rowconfigure(0,weight=1)
F1.grid_columnconfigure(0,weight=1)

photo = ImageTk.PhotoImage(Image.open("D:/fire_detection/background_image.jpg"))
label = Label(GUI,image = photo)
label.image = photo
label.grid(row=0,column=0,columnspan=30,rowspan=30)



config_message_b = ttk.Button(GUI, text ='Message Module', font=('Courier',10), width=25, command=ui_message_home.messageConfig)
config_message_b.configure(foreground="blue",background="thistle2")
config_message_b.grid(row=2,column=10)

analysis_dwt_b = ttk.Button(GUI, text='Analysis Module', font=('Courier',10), width=25, command=ui_analysis_home.analysis)
analysis_dwt_b.configure(foreground="red",background="thistle2")
analysis_dwt_b.grid(row=5,column=10)

def call_predict():
    os.system("start cmd.exe /k D:/fire_detection/predict_batch_file.bat")

def call_analysis():
    os.system("start cmd.exe /k D:/fire_detection/analysis_batch_file.bat")

predict_b = ttk.Button(GUI, text='Start Monitoring', font=('Courier',10), width=25, command=call_predict)
predict_b.configure(foreground="green",background="thistle2")
predict_b.grid(row=8,column=10)


config_b = ttk.Button(GUI, text='Config Video Path', font=('Courier',10), width=25, command=call_analysis)
config_b.configure(foreground="black",background="thistle2")
config_b.grid(row=11,column=10)
GUI.mainloop()