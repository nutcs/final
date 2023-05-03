from tkinter import *
import sqlite3
from tkinter import messagebox 


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
    global username,password
    login_frame.grid(row=0,columnspan=2,sticky=N,pady=25,ipady=30,ipadx=30)
    login_frame.rowconfigure(0,weight=1)
    login_frame.columnconfigure((0,1,2,3,4,5),weight=1)

    # img Profile
    Label(login_frame,image=imgLogin,bg='orange').grid(row=0,column=0)

    # username
    Label(login_frame,text='Username',bg='orange').grid(row=0,column=1)
    username = Entry(login_frame,textvariable=amtLogin[0])
    username.grid(row=0,column=2)

    # password
    Label(login_frame,text='Password',bg='orange').grid(row=0,column=3)
    password = Entry(login_frame)
    password.grid(row=0,column=4)
    
    Button(login_frame,text='Login',command=page2).grid(row=0,column=5)
    
def forget_login():
    login_frame.grid_forget()
    print(username.get(),password.get())

def page2():
    global result
    if username.get() == "" or password.get() == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        username.focus_force()
    else :
        sql = "select * from login where username=?;"
        cursor.execute(sql,[username.get()])
        result = cursor.fetchone()
        if result :
            sql = "select * from login where username=? and password=?;"
            cursor.execute(sql,[username.get(),password.get()])
            result = cursor.fetchone()
            if result :
                forget_login()
                messagebox.showinfo("Admin : ","Login Successfully.")
                HomePage_top()
                HomePage_left()
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                username.selection_range(0,END)
                password.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            username.selection_range(0,END)
            password.focus_force()


###########################################################
# page 2
###########################################################

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
    global searchBox,data_find1,data_find2,data_find3,data_find4
    home_right_edit.grid_forget()
    home_right.grid(row=1,column=1,sticky='news')
    home_right.rowconfigure((0,1,2,3,4),weight=1)
    home_right.rowconfigure((5),weight=5)
    home_right.columnconfigure((0,1,2),weight=1)

    # line 1
    Label(home_right,text='Student ID:',bg='white').grid(row=0,column=0)
    searchBox = Entry(home_right,width=30,borderwidth=3, relief="groove")
    searchBox.grid(row=0,column=1)
    Button(home_right,text='Search',command=search).grid(row=0,column=2)
    # line 1+++
    data_find1 = Label(home_right,text=f'ID : {result[0]}',bg='white')
    data_find1.grid(row=1,columnspan=3)
    data_find2 = Label(home_right,text=f'Name : {result[1]}',bg='white')
    data_find2.grid(row=2,columnspan=3)
    data_find3 = Label(home_right,text=f'Year : {result[2]}',bg='white')
    data_find3.grid(row=3,columnspan=3)
    data_find4 = Label(home_right,text=f'GPA : {result[3]}',bg='white')
    data_find4.grid(row=4,columnspan=3)
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
    

    global edit1,edit2,edit3,edit4
    edit1 = Entry(home_right_edit,width=22,borderwidth=3, relief="groove")
    edit1.grid(row=1,column=1,sticky=W,padx=5)
    edit1.insert(0,f'{result[0]}')
    
    edit2 = Entry(home_right_edit,width=22,borderwidth=3, relief="groove")
    edit2.grid(row=2,column=1,sticky=W,padx=5)
    edit2.insert(0,str(result[1]))
    
    edit3 = Entry(home_right_edit,width=22,borderwidth=3, relief="groove")
    edit3.grid(row=3,column=1,sticky=W,padx=5)
    edit3.insert(0,str(result[2]))
    
    edit4 = Entry(home_right_edit,width=22,borderwidth=3, relief="groove")
    edit4.grid(row=4,column=1,sticky=W,padx=5)
    edit4.insert(0,str(result[3]))

            
    Button(home_right_edit,text='Reset Data',width=15).grid(row=5,column=1,sticky=NW,padx=5,ipady=10,ipadx=10)
    Button(home_right_edit,text='Update Student Data').grid(row=5,column=0,sticky=NE,padx=5,ipady=10,ipadx=10)

def search():
    sql = 'select * from login where std_id=?;'
    cursor.execute(sql,[searchBox.get()])
    check = cursor.fetchone()
    if check:
        messagebox.showinfo('Admin','Search Successfully')
        data_find1['text'] = f'ID : {check[0]}'
        data_find2['text'] = f'Name : {check[1]}'
        data_find3['text'] = f'Year : {check[2]}'
        data_find4['text'] = f'GPA : {check[3]}'
        # data_find1.insert(0,f'{check[0]}')
        # data_find2.insert(0,str(check[1]))
        # data_find3.insert(0,str(check[2]))
        # data_find4.insert(0,str(check[3]))
    else:
        messagebox.showinfo('Admin','The student ID not found.')


root = Window()
imgLogin = PhotoImage(file='profilem.png').subsample(3,3)
imgLogin1 = PhotoImage(file='profilem.png').subsample(6,6)
imgLogin2 = PhotoImage(file='profilem.png').subsample(2,2)

# เชื่อม DB
conn = sqlite3.connect('db/ณัฐพล_1650704388.db')
cursor = conn.cursor()

# Login
amtLogin = [StringVar(),StringVar()]
login_frame = Frame(root,bg='orange')
login()

#page2
##############################################################
#top
home_top = Frame(root,bg='lightgreen')
home_top_frame = Frame(home_top,bg='lightgreen')

#left
home_left = Frame(root,bg='pink')
Frame_option = Frame(home_left,bg='pink')

#right
find_data = StringVar()
home_right = Frame(root,bg='white') #find

#Edit
wordEdit = ['Student ID:','Full name:','Year:','GPA:']
home_right_edit = Frame(root,bg='white')

root.mainloop()