from tkinter import *
from tkinter import filedialog
import shutil, os

root = Tk()

filename = filedialog.askopenfilename(initialdir="/images", title = "Something")

source = Label(root, text=filename).pack()
print(filename)
shutil.copyfile(filename,"C:\\Users\\ANUSHKA\\PycharmProjects\\Tinder\\images")

root.mainloop()