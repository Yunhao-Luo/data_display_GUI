from asyncore import read
from cProfile import label
from distutils.cmd import Command
from importlib.resources import path
import tkinter as tk
import csv
from tkinter import ttk

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
        self.data_window = tk.Tk()
        self.data_window.title("data")
        w, h = self.data_window.winfo_screenwidth(), self.data_window.winfo_screenheight()
        self.data_window.geometry("%dx%d+0+0" % (0.99 * w, 0.9 * h))
        self.data_content = []   
        tabControl = ttk.Notebook(self.data_window)
        count = 0

        for file in file_name_list:
            count+=1
            tab = ttk.Frame(tabControl)
            tabControl.add(tab, text = file)
            tabControl.pack(expand = 1, fill ="both") 
            path = DATA_PATH
            path += "/" + file
            self.read_file(path, tab)

        # show window
        self.data_window.mainloop()

    def read_file(self, path, display_window):
        if 'csv' in path:
            with open(path, 'r', newline="") as f:
                reader = csv.reader(f)
                data = list(reader)

            """ for row in range(0, len(data)):
                for col in range(0, len(data[row])):
                    tk.Label(display_window, text = data[row][col]).grid(row=row, column=col) """
            
            canvas = tk.Canvas(display_window)
            canvas.grid(row=0, column=0, sticky="news")

            # Link a scrollbar to the canvas
            vsb = tk.Scrollbar(display_window, orient="vertical", command=canvas.yview)
            vsb.grid(row=0, column=1, sticky='ns')
            canvas.configure(yscrollcommand=vsb.set)

            # Create a frame to contain the buttons
            frame_buttons = tk.Frame(canvas, bg="blue")
            canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

            # Add 9-by-5 buttons to the frame
            for row in range(0, len(data)):
                for col in range(0, len(data[row])):
                    tk.Label(canvas, text = data[row][col]).grid(row=row, column=col)
            
            # Update buttons frames idle tasks to let tkinter calculate buttons sizes
            frame_buttons.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))


        else:
            with open(path, 'r', ) as f:
                content = f.readlines()

            for line in content:
                self.data_content.append(line)

            # tk.Label(self.data_window, text=self.data_content).grid()

    def display_file(self, path):
        frame = ttk.Frame(self.data_window, width=300, height=250)

        # Canvas creation with double scrollbar
        hscrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL)
        vscrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
        sizegrip = ttk.Sizegrip(frame)
        canvas = tk.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set,
                                    xscrollcommand=hscrollbar.set)
        vscrollbar.config(command=canvas.yview)
        hscrollbar.config(command=canvas.xview)

        # Add controls here
        subframe = ttk.Frame(canvas)

        # open file
        path = "/Users/Luo/Internship/data_display_GUI/data"
        path += "/" + file
        with open(path, newline="") as file:
            reader = csv.reader(file)

            # r and c tell us where to grid the labels
            r = 0
            for col in reader:
                c = 0
                for row in col:
                    # i've added some styling
                    label = tk.Label(subframe, width=10, height=2,
                                            text=row, relief=tk.RIDGE)
                    label.grid(row=r, column=c)
                    c += 1
                r += 1

        # Packing everything
        subframe.pack(fill=tk.BOTH, expand=tk.TRUE)
        hscrollbar.pack(fill=tk.X, side=tk.BOTTOM, expand=tk.FALSE)
        vscrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        sizegrip.pack(in_=hscrollbar, side=tk.BOTTOM, anchor="se")
        canvas.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=tk.TRUE)
        frame.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

        canvas.create_window(0, 0, window=subframe)
        self.data_window.update_idletasks()  # update geometry
        canvas.config(scrollregion=canvas.bbox("all"))
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)



if __name__ == "__main__":
    data_visualization = DataDisplay()
    data_visualization.mainloop()