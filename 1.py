from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("my window")
root.geometry("500x300+100+200")

btn01 = Button(root)
btn01["text"] = "hit me"

btn01.pack()

def songhua(e):
    messagebox.showinfo("Message", "you hit me")
    print("give you flower")


btn01.bind('<Button-1>', thumb)

root.mainloop()
