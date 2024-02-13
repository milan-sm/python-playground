import tkinter as tk

glavni = tk.Tk()
glavni.title('Default')
button = tk.Button(glavni, text='Stop', bg="orangered", width=30, height=30, command=glavni.destroy)
button.pack()

glavni.mainloop()
