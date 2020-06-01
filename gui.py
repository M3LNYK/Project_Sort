# import main
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from main import main_one

root = Tk()
root.title("Mvv app")
root.minsize(300, 400)


def opener():
    global task_folder
    # For choosing directory
    task_folder = root.directory = askdirectory()     # return folder location
    # Label(root, text = root.directory).grid(row = 4, column = 0)
    # main_one(root.directory)
    print(task_folder)


def creator():
    global destination_folder
    destination_folder = root.directory = askdirectory()


button_choose = Button(root, text = "Choose", bg ="red", fg = "white", height = 10, command = opener)
button_modify = Button(root, text = "Modify", bg ="orange", fg = "white", height = 10, width = 40, command = creator)
button_run = Button(root, text = "GO!", bg ="green", fg = "white", height = 10, width = 38)

# mylable.grid(row = 0, column = 1)
button_choose.grid(row =0, column = 0, pady = 10, padx = 5, sticky = W+E)
button_modify.grid(row =1, column = 0, pady = 10, padx = 5)
button_run.grid(row =2, column = 0, pady = 10, padx = 5)
# mylable.pack()

root.mainloop()
