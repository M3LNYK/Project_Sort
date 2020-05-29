# import main
from tkinter import *


root = Tk()
root.title("Mvv app")
root.minsize(300, 400)

mylable = Label(root, text = "Hello there!")

button_choose = Button(root, text = "Choose", bg ="red", fg = "white", height = 10, width = 40)
button_modify = Button(root, text = "Modify", bg ="orange", fg = "white", height = 10, width = 40)
button_run = Button(root, text = "GO!", bg ="green", fg = "white", height = 10, width = 38)

# mylable.grid(row = 0, column = 1)
button_choose.grid(row =0, column = 0, pady = 10, padx = 5)
button_modify.grid(row =1, column = 0, pady = 10, padx = 5)
button_run.grid(row =2, column = 0, pady = 10, padx = 5)
# mylable.pack()

root.mainloop()
