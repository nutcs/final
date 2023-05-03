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

def HomePage_top():
    #Frame color
    home_top.grid(row=0,columnspan=2,sticky='news')
    home_top.rowconfigure(0,weight=1)
    home_top.columnconfigure(0,weight=1)

    #Frame items
    home_top_frame.grid(row=0,column=0)
    home_top_frame.rowconfigure(0,weight=1)
    home_top_frame.columnconfigure(0,weight=1)
    #img
    Label(home_top_frame,image=imgLogin,bg='lightgreen').grid(row=1,column=0,padx=10)
    Label(home_top_frame,text='Login name Administrator',bg='lightgreen').grid(row=1,column=1)

def HomePage_left():
    #Frame color
    home_left.grid(row=1,column=0,sticky='news')
    home_left.rowconfigure(0,weight=1)
    home_left.columnconfigure(0,weight=1)

    #Frame items
    Frame_option.grid(row=0,column=0)
    Frame_option.rowconfigure((0,1,2),weight=1)
    Frame_option.columnconfigure(0,weight=1)

    Button(Frame_option,text='Find Student',image=imgLogin1,command=right_find,compound='left',width=300).grid(row=0,column=0,pady=20,ipady=10)
    Button(Frame_option,text='Edit Student',command=righr_edit,image=imgLogin1,compound='left',width=300).grid(row=1,column=0,pady=20,ipady=10)
    Button(Frame_option,text='Close Student',image=imgLogin1,compound='left',width=300,command=quit).grid(row=2,column=0,pady=20,ipady=10)

def right_find():
    home_right_edit.grid_forget()
    home_right.grid(row=1,column=1,sticky='news')
    home_right.rowconfigure((0,1,2,3,4),weight=1)
    home_right.rowconfigure((5),weight=5)
    home_right.columnconfigure((0,1,2),weight=1)

    # line 1
    Label(home_right,text='Student ID:',bg='white').grid(row=0,column=0)
    Entry(home_right,width=30,borderwidth=3, relief="groove").grid(row=0,column=1)
    Button(home_right,text='Search').grid(row=0,column=2)
    # line 1+++
    Label(home_right,text='ID :',bg='white').grid(row=1,columnspan=3)
    Label(home_right,text='Name :',bg='white').grid(row=2,columnspan=3)
    Label(home_right,text='Year :',bg='white').grid(row=3,columnspan=3)
    Label(home_right,text='GPA :',bg='white').grid(row=4,columnspan=3)
    #img
    Label(home_right,image=imgLogin2).grid(row=5,columnspan=3)

def righr_edit():
    home_right.grid_forget()
    home_right_edit.grid(row=1,column=1,sticky='news')
    home_right_edit.rowconfigure((0),weight=2)
    home_right_edit.rowconfigure((1,2,3,4),weight=1)
    home_right_edit.rowconfigure((5),weight=5)
    home_right_edit.columnconfigure((0,1),weight=1)
    home_right_edit.columnconfigure((2),weight=2)

    #header
    Label(home_right_edit,text='Edit Student Page:',bg='white').grid(row=0,columnspan=2)
    Label(home_right_edit,image=imgLogin1).grid(row=1,column=2,sticky=W)
    
    for i in range(len(wordEdit)):
        Label(home_right_edit,text=wordEdit[i],bg='white').grid(row=i+1,column=0,sticky=E,padx=5)
        Entry(home_right_edit,width=22,textvariable=amt_edit[i],borderwidth=3, relief="groove").grid(row=i+1,column=1,sticky=W,padx=5)

            
    Button(home_right_edit,text='Reset Data',width=15).grid(row=5,column=1,sticky=NW,padx=5,ipady=10,ipadx=10)
    Button(home_right_edit,text='Update Student Data').grid(row=5,column=0,sticky=NE,padx=5,ipady=10,ipadx=10)


root = Window()
imgLogin = PhotoImage(file='profilem.png').subsample(3,3)
imgLogin1 = PhotoImage(file='profilem.png').subsample(6,6)
imgLogin2 = PhotoImage(file='profilem.png').subsample(2,2)

#top
home_top = Frame(root,bg='lightgreen')
home_top_frame = Frame(home_top,bg='lightgreen')
HomePage_top()

#left
home_left = Frame(root,bg='pink')
Frame_option = Frame(home_left,bg='pink')
HomePage_left()

#right
#find
home_right = Frame(root,bg='white')

#Edit
wordEdit = ['Student ID:','Full name:','Year:','GPA:']
amt_edit = [StringVar() for i in range(len(wordEdit))]
home_right_edit = Frame(root,bg='white')

#right_find()

root.mainloop()