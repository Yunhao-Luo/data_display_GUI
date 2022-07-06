# #Import tkinter library
# from tkinter import *
# from tkinter import ttk
# #Create an instance of tkinter frame or window
# win= Tk()
# #Set the geometry of tkinter frame
# win.geometry("750x250")
# def get_value():
#    e_text=entry.get()
#    Label(win, text=e_text, font= ('Century 15 bold')).pack(pady=20)
# #Create an Entry Widget
# entry= ttk.Entry(win,font=('Century 12'),width=40)
# entry.pack(pady= 30)
# #Create a button to display the text of entry widget
# button= ttk.Button(win, text="Enter", command= get_value)
# button.pack()
# win.mainloop()

""" from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B90C')

def display_selected(choice):
    choice = variable.get()
    print(choice)

countries = ['Bahamas','Canada', 'Cuba','United States']

# setting variable for Integers
variable = StringVar()
variable.set(countries[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *countries,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

# infinite loop 
ws.mainloop() """


""" import tkinter as tk                    
from tkinter import ttk
  
  
root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.pack(expand = 1, fill ="both")
  
ttk.Label(tab1, 
          text ="Welcome to \
          GeeksForGeeks").grid(column = 0, 
                               row = 0,
                               padx = 30,
                               pady = 30)  
ttk.Label(tab2,
          text ="Lets dive into the\
          world of computers").grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
  
root.mainloop()  
 """

""" import csv
from tkinter import *
from tkinter import ttk
import tkinter

root = tkinter.Tk()
root.title("Double scrollbar with tkinter")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (0.99 * w, 0.9 * h))


def displayontowindow():
    #frame = Frame(root, width=600, height=310, bg="light grey")

    frame = ttk.Frame(root, width=300, height=250)

    # Canvas creation with double scrollbar
    hscrollbar = ttk.Scrollbar(frame, orient=tkinter.HORIZONTAL)
    vscrollbar = ttk.Scrollbar(frame, orient=tkinter.VERTICAL)
    sizegrip = ttk.Sizegrip(frame)
    canvas = tkinter.Canvas(frame, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set,
                            xscrollcommand=hscrollbar.set)
    vscrollbar.config(command=canvas.yview)
    hscrollbar.config(command=canvas.xview)

    # Add controls here
    subframe = ttk.Frame(canvas)

    # open file
    path = "/Users/Luo/Internship/data_display_GUI/data"
    path += "/" + "6666_06-27-2022-17-18-37_English_Session1_FrogPR_MushNP_RadiCT_stim_file.csv"
    with open(path, newline="") as file:
        reader = csv.reader(file)

        # r and c tell us where to grid the labels
        r = 0
        for col in reader:
            c = 0
            for row in col:
                # i've added some styling
                label = tkinter.Label(subframe, width=10, height=2,
                                      text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1

    # Packing everything
    subframe.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)
    hscrollbar.pack(fill=tkinter.X, side=tkinter.BOTTOM, expand=tkinter.FALSE)
    vscrollbar.pack(fill=tkinter.Y, side=tkinter.RIGHT, expand=tkinter.FALSE)
    sizegrip.pack(in_=hscrollbar, side=BOTTOM, anchor="se")
    canvas.pack(side=tkinter.LEFT, padx=5, pady=5, fill=tkinter.BOTH, expand=tkinter.TRUE)
    frame.pack(padx=5, pady=5, expand=True, fill=tkinter.BOTH)

    canvas.create_window(0, 0, window=subframe)
    root.update_idletasks()  # update geometry
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.xview_moveto(0)
    canvas.yview_moveto(0)

displayontowindow()

root.mainloop() """


""" from tkinter import *  
  
top = Tk()  
sb = Scrollbar(top)  
sb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(top, yscrollcommand = sb.set )  
  
for line in range(30):  
    mylist.insert(END, "Number " + str(line))  
  
mylist.pack( side = LEFT )  
sb.config( command = mylist.yview )  
  
mainloop() """

import tkinter as tk
import csv

root = tk.Tk()
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

path = "/Users/Luo/Internship/data_display_GUI/data"
path += "/" + "asdf_06-29-2022-15-23-16_structured summary.csv"
with open(path, 'r', newline="") as f:
                reader = csv.reader(f)
                data = list(reader)

# Add 9-by-5 buttons to the frame
rows = len(data)
columns = len(data[0])
print(rows)
print(columns)
buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
for i in range(0, rows):
    for j in range(0, columns):
        buttons[i][j] = tk.Button(frame_buttons, text=(data[i][j]))
        buttons[i][j].grid(row=i, column=j, sticky='news')

# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
if rows > 10:
    rows = 10
first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, rows)])
first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, columns)])
frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
                    height=first5rows_height)

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
root.mainloop()