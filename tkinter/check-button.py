from tkinter import *

glavni = Tk()
check1 = IntVar()
Checkbutton(glavni, text='check 1', bg="lightgrey", variable=check1).grid(row=0, sticky=W)
check2 = IntVar()
Checkbutton(glavni, text='check 2', bg="lightgrey", variable=check2).grid(row=1, sticky=W)
check3 = IntVar()
Checkbutton(glavni, text='check 3', bg="lightgrey", variable=check3).grid(row=2, sticky=W)

glavni.mainloop()
