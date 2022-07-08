from asyncore import read
from cProfile import label
from distutils.cmd import Command
from importlib.resources import path
import tkinter as tk
import csv
from tkinter import INSERT, ttk, Text
import sys

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
        self.data_window = tk.Tk()
        self.data_window.title("data")
        self.w, self.h = self.data_window.winfo_screenwidth(), self.data_window.winfo_screenheight()
        self.data_window.geometry("%dx%d+0+0" % (0.99 * self.w, 0.9 * self.h))
        self.data_content = []   
        tabControl = ttk.Notebook(self.data_window)

        for file_path in file_name_list:
            tab = ttk.Frame(tabControl)
            tabControl.add(tab, text = file_path)
            tabControl.pack(expand = 1, fill ="both") 
            self.tab_construct(tab, file_path)

        self.data_window.mainloop()

    def tab_construct(self, window, path):
        frame_canvas = tk.Frame(window)
        frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
        frame_canvas.grid_rowconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_propagate(False)

        canvas = tk.Canvas(frame_canvas)
        canvas.grid(row=0, column=0, sticky="news")

        vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
        vsb.grid(row=0, column=1, sticky='ns')
        canvas.configure(yscrollcommand=vsb.set)
        hsb = tk.Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
        hsb.grid(row=1, column=0, sticky='we')
        canvas.configure(xscrollcommand=hsb.set)

        frame_buttons = tk.Frame(canvas, bg="blue")
        canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

        if '.csv' in path:
            with open(path, 'r', newline="") as f:
                            reader = csv.reader(f)
                            data = list(reader)
            while [] in data:
                data.remove([])
        else:
            self.read_txt(frame_canvas, path)
            return

        rows = len(data)
        columns = len(data[0])
        buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
        for i in range(0, rows):
            for j in range(0, columns):
                buttons[i][j] = tk.Button(frame_buttons, text=(data[i][j]))
                buttons[i][j].grid(row=i, column=j, sticky='news')

        frame_buttons.update_idletasks()

        if rows > 20:
            rows = 20
        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, columns)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, rows)])
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height + vsb.winfo_height() + 20)

        canvas.config(scrollregion=canvas.bbox("all"))

    def read_txt(self, window, path):
        text = Text(window, height=50, width=self.w)
        text.pack()

        with open(path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            text.insert(INSERT, str(line))

if __name__ == "__main__":
    DATA_PATH = sys.executable
    DATA_PATH = DATA_PATH[0:DATA_PATH.rfind('\\')] + '\\data'
    data_visualization = DataDisplay()
    data_visualization.create_window()
    data_visualization.mainloop()