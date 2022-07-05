import tkinter as tk

master = tk.Tk()

var = tk.StringVar(master)
var.set('apple')

master.title("Data Dashboard")
master.geometry("400x250")
master.grid_rowconfigure(0, weight=1)
master.grid_columnconfigure(0, weight=1)
master.grid_rowconfigure(4, weight=1)
master.grid_columnconfigure(2, weight=1)
tk.Label(master, text=" ").grid(row=0)
tk.Label(master, text="trial number").grid(row=1)
# trial_num = tk.Entry(master).grid(row=1, column=1)
tk.OptionMenu(master, var, 'apple', 'banana').grid(row=1, column=1)
tk.Label(master, text="column name").grid(row=2)
col_name = tk.Entry(master).grid(row=2, column=1)
button = tk.Button(master, text="Search", width=10).grid(row=4, column=1)

master.mainloop()