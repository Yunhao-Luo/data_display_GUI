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


import tkinter as tk                    
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
