import tkinter as tk
import csv
from tkinter import INSERT, ttk, Text
import sys

from file_finder import *
from configuration import *
from azure_test import *

class DataDisplay(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Dashboard")
        self.geometry("400x250")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.dropdown_list = ['']

    def create_window(self):
        tk.Label(self, text="Participant id").grid(row=1)
        self.participant_name = tk.Entry(self)
        self.participant_name.grid(row=1, column=1)
        tk.Button(self, text="Confirm", width=10, command=self.show_summary).grid(row=1, column=2)

    def update_menu_options(self):
        self.sessions = FileFinder(DATA_PATH)
        new_options = self.sessions.find_id_sessions(self.participant_name.get())
        if len(new_options) == 0:
            new_options.append("No such participant!")
        
        self.var.set(new_options[0])
        self.menu['menu'].delete(0, 'end')
        for option in new_options:
            self.menu['menu'].add_command(label=option, command=tk._setit(self.var, option))

    def create_summary(self):
        id = self.participant_name.get()
        path = self.sessions.find_result_file(id)
        with open(path, 'r', newline="") as f:
                            reader = csv.reader(f)
                            data = list(reader)

        summary_file = id + "_summary.csv"
        session_num = path[path.rfind('\\'):]
        session_num = session_num[session_num.find("_")+1:]
        session_start = session_num[session_num.find("_")+1:session_num.rfind("_")]
        session_num = session_num[0:session_num.find("_")]

        num_corrrect_list = {}
        task_names = []
        for i in data:
            if i[0] not in task_names:
                task_names.append(i[0])
            if 'key' not in i[4] and i[4] != "":
                if i[0] not in num_corrrect_list:
                    key_list = []
                    num_corrrect_list[i[0]] = key_list
                    key_list.append(i[4])
                else:
                    num_corrrect_list[i[0]].append(i[4])
        print(num_corrrect_list)

        with open(summary_file, 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['ID #', id])
            filewriter.writerow(['Training session #', session_num])
            filewriter.writerow(['Task name', ""])
            for i in task_names:
                filewriter.writerow(['', i])
            filewriter.writerow(['# of problems completed ', len(data)-1])
            filewriter.writerow(['# of problems correct ', ""])
            for i in num_corrrect_list:
                filewriter.writerow(['', i + " " + "attempts: " + str(len(num_corrrect_list[i])) + " successes: " + str(num_corrrect_list[i].count('UP'))])
            filewriter.writerow(['Timestamp of session start & end ', session_start])
            filewriter.writerow(['Duration of the training session', data[-1][2]])
            
        return summary_file

    def show_summary(self):
        self.sessions = FileFinder(DATA_PATH)
        self.data_window = tk.Tk()
        test = tk.Label(self.data_window, text="Select a session")
        test.pack()
        self.var = tk.StringVar(self.data_window)
        self.var.set(self.dropdown_list[0])
        self.menu = tk.OptionMenu(self.data_window, self.var, *self.dropdown_list)
        self.menu.config(width=18)
        self.menu.pack()
        com_btn = tk.Button(self.data_window, text="Search", command=self.display_data)
        com_btn.pack()
        self.data_window.title("data")
        self.w, self.h = self.data_window.winfo_screenwidth(), self.data_window.winfo_screenheight()
        self.data_window.geometry("%dx%d+0+0" % (0.99 * self.w, 0.9 * self.h))
        self.data_content = []   
        self.tabControl = ttk.Notebook(self.data_window)
        self.tabControl.pack(fill='x')

        self.update_menu_options()

        self.tab_list = []
        file_path = self.create_summary()
        tab = "tab" + str(0)
        tab = ttk.Frame(self.tabControl)
        self.tabControl.add(tab, text = file_path[file_path.rfind("\\")+1:])
        self.tabControl.pack(expand = 1, fill ="both") 
        self.tab_construct(tab, file_path)
        self.tab_list.append(tab)

    def display_data(self):
        if len(self.tab_list) > 1:
            for i in range(1, len(self.tab_list)):
                self.tabControl.forget(self.tab_list[i])
            self.tab_list = self.tab_list[0:1]
        date = self.var.get()
        file_name_list = self.sessions.find_all_files_date(self.participant_name.get(), date)
        count = 2
        for file_path in file_name_list:
            tab = "tab" + str(count)
            tab = ttk.Frame(self.tabControl)
            self.tabControl.add(tab, text = file_path[file_path.rfind("\\")+1:])
            self.tabControl.pack(expand = 1, fill ="both") 
            self.tab_construct(tab, file_path)
            self.tab_list.append(tab)
            count+=1

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

        first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, columns)])
        first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, rows)])
        if first5columns_width > self.w:
            first5columns_width = self.w - 50
        if first5rows_height > self.h:
            first5rows_height = self.h - 200
        frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                            height=first5rows_height + vsb.winfo_height() + 20)
        
        if first5columns_width + vsb.winfo_width() > self.w * 0.9:
            hsb = tk.Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
            hsb.grid(row=1, column=0, sticky='we')
            canvas.configure(xscrollcommand=hsb.set)

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