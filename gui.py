# import main
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory

root = Tk()
root.title("Mvv app")
root.minsize(300, 400)

def open():
    global my_file
    # For choosing file
    # root.filename = filedialog.askopenfilename(initialdir = "C:\Personal\pp2_photo\dataBase", title = "Select files:", filetypes = (("JPG files", "*.JPG"), ("All files", "*.*")))
    # Label(root, text = root.filename).pack()
    # For choosing directory
    root.directory = askdirectory() # return folder location
    # Label(root, text = root.directory).grid(row = 3, column = 0)


button_choose = Button(root, text = "Choose", bg ="red", fg = "white", height = 10, command = open)
button_modify = Button(root, text = "Modify", bg ="orange", fg = "white", height = 10, width = 40)
button_run = Button(root, text = "GO!", bg ="green", fg = "white", height = 10, width = 38)

# mylable.grid(row = 0, column = 1)
button_choose.grid(row =0, column = 0, pady = 10, padx = 5, sticky = W+E)
button_modify.grid(row =1, column = 0, pady = 10, padx = 5)
button_run.grid(row =2, column = 0, pady = 10, padx = 5)
# mylable.pack()

root.mainloop()
