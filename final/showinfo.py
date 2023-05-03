from tkinter import *
from tkinter import messagebox


def loginclick(user,pwd) :
    global result
    if user == "" or pwd == "" :
        messagebox.showwarning("Admin : ","Please enter a username or password")
        userentry.focus_force()
    else :
        sql = "select * from student where username=?;"
        cursor.execute(sql,[user])
        result = cursor.fetchone()
        if result :
            sql = "select * from student where username=? and password=?;"
            cursor.execute(sql,[user,pwd])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin : ","Login Successfully.")
                welcomepage(result)
            else :
                messagebox.showwarning("Admin : ","Incorrect Password \nPlease try again")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin : ","The username not found.")
            userentry.selection_range(0,END)
            userentry.focus_force()



def updateclick() :
    if codebox.get() == "" or namebox.get() == "" or daybox.get() == "" or roombox.get() == "" :
        messagebox.showwarning("Admin: ","Please fullfill all of course data")
        codebox.focus_force()
    else :
        #define sql select command to checking course code exist or not
        sql = "select * from course where course_code=?;"
        #execute step
        cursor.execute(sql,[codebox.get()])
        result = cursor.fetchone() #fetch result

        if result :
            #define sql select command of course name for duplicating
            sql = "select * from course where course_name=?;"
            #execute step
            cursor.execute(sql,[namebox.get()])
            #fetch result
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin : ","Duplicated course name.")
                #define sql for updating of day,room fields
                sql = """
                update course
                set day=?, room=?
                where course_code=?;
                """
                #execute step
                cursor.execute(sql,[daybox.get(), roombox.get(), codebox.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update day/room successfully")
                #refresh treeview 
                refreshTreeview()
            else :
                #define sql update command for updating course name, day, room
                sql = """
                update course
                set course_name=?, day=?, room=?
                where course_code=?;
                """
                #execute step
                cursor.execute(sql,[namebox.get(), daybox.get(), roombox.get(), codebox.get()])
                #commit step
                conn.commit()
                messagebox.showinfo("Admin:","Update course successfully")
                #refresh treeview 
        else :
            messagebox.showwarning("Admin: ","Course code not found\n Try again.")
            codebox.select_range(0,END)
            codebox.focus_force()