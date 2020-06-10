import exifread
import glob
import os
import cv2
from tkinter import *
from tkinter.filedialog import askdirectory


def get_photo_date(file_name):
    file = open(file_name, 'rb')
    tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal")
    time_n_date = tags["EXIF DateTimeOriginal"]
    new_time_n_date = str(time_n_date)
    date = new_time_n_date.split(" ")[0]
    new_date = date.split(":")
    return new_date


def get_year(new_list):
    res = new_list[0]
    return res


def get_month(new_list):
    res = new_list[1]
    return res


def get_day(new_list):
    res = new_list[2]
    return res


def create_dirs(fisrPart, year_loc, month_loc):
    n_path = str(fisrPart+"/" + year_loc + "/" + month_loc)
    try:
        os.makedirs(n_path, exist_ok = True)
        print("Directory '%s' created successfully" % n_path)
    except OSError as error:
        print("Directory '%s' can not be created")


def process_all(file, destination_folder):
    file_name = file.split("\\")[1]
    photo = get_photo_date(file)
    month = get_month(photo)
    year = get_year(photo)
    image = cv2.imread(file)
    create_dirs(destination_folder, str(year), str(month))
    name = str(destination_folder + '/' + year + '/' + month + '/' + file_name)
    cv2.imwrite(name, image)


def main_one(string_path_to_folder, destination_folder):
    photos = glob.glob(string_path_to_folder+"/*.JPG")
    print("Number of files: ", len(photos))
    for k in photos:
        process_all(k, destination_folder)


root = Tk()
root.title("Photo Sorting app")
root.geometry('300x600+50+20')
root.minsize(300, 600)

global checker1, checker2
checker2 = FALSE
checker1 = FALSE


def opener():
    global task_folder
    task_folder = root.directory = askdirectory(initialdir = "C:/")
    global checker1
    checker1 = TRUE
    tester()


def creator():
    global destination_folder
    global checker2
    destination_folder = root.directory = askdirectory(initialdir = "C:/")
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
                           text = "CHOOSE FOLDER WITH FILES TO SORT",
                           bg = "red", fg = "white",
                           height = 10, width = 40,
                           relief = GROOVE,
                           command = opener)
    button_modify = Button(root,
                           text = "CHOOSE FOLDER WHERE TO SAVE FILES ",
                           bg = "orange", fg = "white",
                           height = 10, width = 40,
                           relief = GROOVE,
                           command = creator)
    button_run = Button(root,
                        text = "Not ready to start",
                        bg = "Grey", fg = "white",
                        height = 10, width = 38,
                        state = DISABLED,
                        relief = GROOVE,
                        disabledforegroun = "Black")
    button_restart = Button(root,
                            text = "Reset",
                            height = 3, width = 10,
                            relief = GROOVE,
                            command = reseter)
    button_choose.grid(row = 0, column = 0, pady = 10, padx = 5, columnspan = 2)
    button_modify.grid(row = 1, column = 0, pady = 10, padx = 5, columnspan = 2)
    button_run.grid(row = 2, column = 0, pady = 10, padx = 5, columnspan = 2)
    button_restart.grid(row = 3, column = 1, pady = 0, padx = '9px', sticky = NE)


button_choose = Button(root,
                       text = "CHOOSE FOLDER WITH FILES TO SORT",
                       bg = "red", fg = "white",
                       height = 10, width = 40,
                       relief = GROOVE,
                       command = opener)
button_modify = Button(root,
                       text = "CHOOSE FOLDER WHERE TO SAVE FILES ",
                       bg = "orange", fg = "white",
                       height = 10, width = 40,
                       relief = GROOVE,
                       command = creator)
button_run = Button(root,
                    text = "Not ready to start",
                    bg = "Grey", fg = "white",
                    height = 10, width = 38,
                    relief = GROOVE,
                    state = DISABLED,
                    disabledforegroun = "Black")
button_restart = Button(root,
                        text = "Reset",
                        height = 3, width = 10,
                        relief = GROOVE,
                        command = reseter)

button_choose.grid(row = 0, column = 0, pady = 10, padx = 5, columnspan = 2)
button_modify.grid(row = 1, column = 0, pady = 10, padx = 5, columnspan = 2)
button_run.grid(row = 2, column = 0, pady = 10, padx = 5, columnspan = 2)
button_restart.grid(row = 3, column = 1, pady = 0, padx = '9px', sticky = NE)

root.mainloop()
