from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Grilled Cheese")
root.geometry("400x400")
upload = Image.open("download.jpeg")
image = ImageTk.PhotoImage(upload)
Label = Label(root, image=image, height = 350, width = 300)
Label.place(x=50, y =0)
Label2 = Label(root, text="It's delectable!")
Label2.place(x=50, y=360)
root.mainloop()