from asyncore import read
from cProfile import label
from distutils.cmd import Command
import tkinter as tk
import csv

from file_finder import *
from configuration import *

class DataDisplay(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Dashboard")
        self.geometry("400x250")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.var = tk.StringVar(self)
        self.dropdown_list = ['']
        self.var.set(self.dropdown_list[0])
        self.option_menu = tk.OptionMenu(self, self.var, *self.dropdown_list)
        self.option_menu.config(width=18)

        self.create_window()

    def create_window(self):

        tk.Label(self, text="Participant id").grid(row=1)
        self.participant_name = tk.Entry(self)
        self.participant_name.grid(row=1, column=1)
        tk.Button(self, text="Confirm", width=10, command=self.update_menu_options).grid(row=1, column=2)
        tk.Label(self, text="Trial session").grid(row=2)
        self.option_menu.grid(row=2, column=1)
        tk.Button(self, text="Search", width=10, command=self.display_data).grid(row=4, column=1)

    def update_menu_options(self):

        self.sessions = FileFinder(DATA_PATH)
        new_options = self.sessions.find_id_sessions(self.participant_name.get())
        if len(new_options) == 0:
            new_options.append("No such participant!")
        
        self.var.set(new_options[0])
        self.option_menu['menu'].delete(0, 'end')
        for option in new_options:
            self.option_menu['menu'].add_command(label=option, command=tk._setit(self.var, option))

    def display_data(self):
        date = self.var.get()
        file_name_list = self.sessions.find_all_files_date(self.participant_name.get(), date)
        print(file_name_list)
        """data_window = tk.Tk()
        data_window.title(file_name)
        file_path = DATA_PATH + '/' + file_name + '*'
        data_content = []

        if 'csv' in file_name:
            with open(file_path, 'r', newline="") as f:
                reader = csv.reader(f)
                data = list(reader)

            entrieslist = []
            for i , row in enumerate(data, start=4):
                entrieslist.append(row[0])
                for col in range(0, 10):
                    tk.Label(data_window, text = row[col]).grid(row=i, column=col)
        else:
            with open(file_path, 'r', ) as f:
                content = f.readlines()

            for line in content:
                data_content.append(line)

            tk.Label(data_window, text=data_content).pack()

        data_window.mainloop()
"""



if __name__ == "__main__":
    data_visualization = DataDisplay()
    data_visualization.mainloop()