from tkinter import *


def Window():
    root = Tk()
    root.title("Final : Nutthapon Salangsing 1650704388")
    root.geometry("1000x700")
    root.configure(bg="red")
    root.columnconfigure((0,1),weight=1)
    root.rowconfigure((0,1),weight=1)
    root.option_add('*font','Garamond 16 bold')
    return root

root = Window()
# Login
amtLogin = [StringVar(),StringVar()]

imgLogin = PhotoImage(file='final/profilem.png').subsample(3,3)

root.mainloop()