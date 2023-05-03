from tkinter import *

#slip = PhotoImage(file="image/slip.png").subsample(2,2)
amt = [StringVar() for i in range(10)]
amt[0] = 'df'

for i in amt:
    print(type(i))
    