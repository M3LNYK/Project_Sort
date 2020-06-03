from tkinter import *
from tkinter.filedialog import askdirectory
from draft import main_one


root = Tk()
root.title("Photo Sorting app")
root.minsize(300, 400)

global checker1, checker2
checker2 = FALSE
checker1 = FALSE


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
    # Label(root, text = root.directory).grid(row = 4, column = 0)
    checker2 = TRUE
    tester()


def greenButton():
    main_one(task_folder, destination_folder)


def tester():
    if checker1 == TRUE and checker2 == TRUE:
        print("GG, WP")
        button_run = Button(root,
                            text = "GO!",
                            bg = "Green", fg = "white",
                            height = 10, width = 38,
                            state = NORMAL,
                            command = greenButton)
        button_run.grid(row = 2, column = 0, pady = 10, padx = 5)
    elif checker1 == FALSE and checker2 == TRUE:
        print("Choose fies to sort!")
        print(checker1, checker2)
    elif checker1 == TRUE and checker2 == FALSE:
        print("Choose where to drop sorted photos!")
        print(checker1, checker2)
    elif checker1 == FALSE and checker2 == FALSE:
        print("Chose files to choose and where to place them!")


def reseter():
    global checker1
    checker1 = FALSE
    global checker2
    checker2 = FALSE
    global task_folder
    task_folder = None
    global destination_folder
    destination_folder = None
    button_choose = Button(root,
                           text = "Choose folder with files to sort",
                           bg = "red", fg = "white",
                           height = 10, command = opener)
    button_modify = Button(root,
                           text = "Choose folder where sorted files should be sorted",
                           bg = "orange", fg = "white",
                           height = 10, width = 40,
                           command = creator)
    button_run = Button(root,
                        text = "Not ready to start",
                        bg = "Grey", fg = "white",
                        height = 10, width = 38,
                        state = DISABLED,
                        disabledforegroun = "Black")
    button_restart = Button(root,
                            text = "Res",
                            height = 5, width = 5,
                            pady = 5, padx = 5,
                            command = reseter)
    button_choose.grid(row = 0, column = 0, pady = 10, padx = 5, sticky = W + E)
    button_modify.grid(row = 1, column = 0, pady = 10, padx = 5)
    button_run.grid(row = 2, column = 0, pady = 10, padx = 5)
    button_restart.grid(row = 3, column = 0, pady = 0, padx = 0)


button_choose = Button(root,
                       text = "Choose folder with files to sort",
                       bg ="red", fg = "white",
                       height = 10, command = opener)
button_modify = Button(root,
                       text = "Choose folder where sorted files should be sorted",
                       bg ="orange", fg = "white",
                       height = 10, width = 40,
                       command = creator)
button_run = Button(root,
                    text = "Not ready to start",
                    bg="Grey", fg = "white",
                    height = 10, width = 38,
                    state = DISABLED,
                    disabledforegroun="Black")
button_restart = Button(root,
                        text = "Res",
                        height = 5, width = 5,
                        pady = 5, padx = 5,
                        command = reseter)


# mylable.grid(row = 0, column = 1)
button_choose.grid(row = 0, column = 0, pady = 10, padx = 5, sticky = W + E)
button_modify.grid(row = 1, column = 0, pady = 10, padx = 5)
button_run.grid(row = 2, column = 0, pady = 10, padx = 5)
button_restart.grid(row = 3, column = 0, pady = 0, padx = 0)
# mylable.pack()

root.mainloop()
