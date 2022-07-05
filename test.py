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

from tkinter import *

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
ws.mainloop()
