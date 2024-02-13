from tkinter import *
main = Tk() 
ourMessage ='This is our Message\nThis is our Message\nThis is our Message\n'
messageVar = Message(main, text = ourMessage) 
messageVar.config(bg='lightgreen') 
messageVar.pack( ) 
main.mainloop( ) 
