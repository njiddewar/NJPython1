from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("GinelHUB")
root.resizable(width=False, height=False)
root.geometry("390x300+750+300")
root.configure(background='#1a1a1a')

fundoFoda = PhotoImage(file="C:/Users/JIDDENIL/Desktop/Python Programs/cascade.gif", format="gif")

bg = Label(image=fundoFoda)
bg.place(x=0, y=0, relwidth=1, relheight=1)

root.mainloop()