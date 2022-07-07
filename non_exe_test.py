from data_visual_oop import *

if os.path.exists('path.txt'):
    with open('path.txt', 'r') as f:
        DATA_PATH = f.readlines()[0]
        print(DATA_PATH)

data_visualization = DataDisplay()
data_visualization.create_window()
data_visualization.mainloop()