# import main
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from main import main_one

root = Tk()
root.title("Mvv app")
root.minsize(300, 400)

global checker1, checker2
checker1 = FALSE
checker2 = FALSE

def opener():
    # For choosing directory
    global task_folder
    task_folder = root.directory = askdirectory()     # return folder location
    # Label(root, text = root.directory).grid(row = 4, column = 0)
    global checker1
    checker1 = TRUE
    tester()


def creator():
    global destination_folder
    global checker2
    destination_folder = root.directory = askdirectory()
    checker2 = TRUE
    tester()

def tester():
    if checker1 == TRUE and checker2 == TRUE:
        print("GG, WP")
        button_run = Button(root, text = "GO!", bg = "green", fg = "white",
                            height = 10, width = 38, state = NORMAL)
        button_run.grid(row = 2, column = 0, pady = 10, padx = 5)
    elif checker1 == FALSE and checker2 == TRUE:
        print("Choose fies to sort!")
        print(checker1, checker2)
    elif checker1 == TRUE and checker2 == FALSE:
        print("Choose where to drop sorted photos!")
        print(checker1, checker2)
    elif checker1 == FALSE and checker2 == FALSE:
        print("Chose files to choose and where to place them!")


button_choose = Button(root, text = "Choose", bg ="red", fg = "white", height = 10, command = opener)
button_modify = Button(root, text = "Modify", bg ="orange", fg = "white", height = 10, width = 40, command = creator)
button_run = Button(root, text = "GO!", bg ="green", fg = "white",
                    height = 10, width = 38, state = DISABLED, disabledforegroun="red")

# mylable.grid(row = 0, column = 1)
button_choose.grid(row =0, column = 0, pady = 10, padx = 5, sticky = W+E)
button_modify.grid(row =1, column = 0, pady = 10, padx = 5)
button_run.grid(row =2, column = 0, pady = 10, padx = 5)
# mylable.pack()

root.mainloop()
