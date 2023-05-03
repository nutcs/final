from tkinter import *


def Window():
    root = Tk()
    root.title("Final : Nutthapon Salangsing 1650704388")
    root.geometry("1000x700")
    root.configure(bg="red")
    root.columnconfigure((0),weight=1)
    root.columnconfigure((1),weight=3)
    root.rowconfigure((0),weight=1)
    root.rowconfigure((1),weight=3)
    root.option_add('*font','Garamond 16 bold')
    return root

def login():
    login_frame.grid(row=0,columnspan=2,sticky=N,pady=25,ipady=30,ipadx=30)
    login_frame.rowconfigure(0,weight=1)
    login_frame.columnconfigure((0,1,2,3,4,5),weight=1)

    # img Profile
    Label(login_frame,image=imgLogin,bg='orange').grid(row=0,column=0)

    # username
    Label(login_frame,text='Username',bg='orange').grid(row=0,column=1)
    Entry(login_frame,textvariable=amtLogin[0]).grid(row=0,column=2)

    # password
    Label(login_frame,text='Password',bg='orange').grid(row=0,column=3)
    Entry(login_frame,textvariable=amtLogin[1]).grid(row=0,column=4)
    
    Button(login_frame,text='Login',command=forget_login).grid(row=0,column=5)
    
def forget_login():
    login_frame.grid_forget()
    print(amtLogin[0].get(),amtLogin[1].get())


root = Window()
# Login
amtLogin = [StringVar(),StringVar()]
login_frame = Frame(root,bg='orange')




imgLogin = PhotoImage(file='final/profilem.png').subsample(3,3)

login()

root.mainloop()