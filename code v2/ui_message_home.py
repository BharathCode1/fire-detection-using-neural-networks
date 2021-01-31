import tkinter as t
import ui_message_add_number
import ui_message_delete_number
import ui_message_edit_number_home
import ui_message_browse
def messageConfig():
    messageConfiguration = t.Tk()
    messageConfiguration.title("Message Module Configuration")
    messageConfiguration.minsize(300,500)
    config_message_b = t.Button(messageConfiguration, text ='Add Number', font = ('Courier',8), width=25, command=ui_message_add_number.add_message_number)
    config_message_b.pack(pady = 10)

    config_message_b = t.Button(messageConfiguration, text='Delete Number', font=('Courier', 8), width=25,
                                command=ui_message_delete_number.delete_number_main)
    config_message_b.pack(pady=10)

    config_message_b = t.Button(messageConfiguration, text='Edit Number', font=('Courier', 8), width=25,
                                command=ui_message_edit_number_home.edit_number_home)
    config_message_b.pack(pady=10)

    config_message_b = t.Button(messageConfiguration, text='Search Deatils', font=('Courier', 8), width=25,
                                command=ui_message_browse.message_table)
    config_message_b.pack(pady=10)

    messageConfiguration.configure(bg='MediumPurple4')

    messageConfiguration.mainloop()









