from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Denominator Calculator")
root.geometry("650x400")
root.config(bg="light blue")
label1 = Label(root, text="Welcome to the Denominator Calculator", font=("Arial", 12), bg="light blue")
label1.place(relx=0.5, y=150, anchor=CENTER)
def msg():
    msgbox = messagebox.showinfo("Do you want to use the Denominator Calculator?")
    if msgbox == "ok":
        topwin()
button1 = Button(root, command=msg, bg="brown", fg="white")
button1.place(x=160, y=205)
def topwin():
    top = Toplevel(root)
    top.title("Currency Dennominator Calculator")
    top.config(bg="grey")
    label1 = Label(top, text='Enter amount', bg="grey")
    label1.place(x=230, y=50)
    entry = Entry(top)
    entry.place(x=200, y=80)
    lb1 = Label(top, text="Denominations", bg="grey")
    lb1.place(x=140, y=170)
    l1 = Label(top, text="2000", bg="grey")
    l2 = Label(top, text="500", bg="grey")
    l3 = Label(top, text="100", bg="grey")
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1 = Label(top, text="")
    t2 = Label(top, text="")
    t3 = Label(top, text="")
    t1.place(x=300,y=200)
    t2.place(x=300,y=230)
    t3.place(x=300,y=260)
    def calculate():
        amount = int(entry.get())
        d2000 = amount // 2000
        amount = amount % 2000
        d500 = amount // 500
        amount = amount % 500
        d100 = amount // 100
        t1.config(text=str(d2000))
        t2.config(text=str(d500))
        t3.config(text=str(d100))
    btn=Button(top, text="Calculate", command=calculate)
    btn.place(x=240, y=120)
root.mainloop()