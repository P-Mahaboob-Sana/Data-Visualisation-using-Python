from tkinter import *
from PIL import ImageTk, Image

root = Tk()  #creates a main window (here root is name of the main doc , you can name it anything)
root.title("Day4")
root.geometry("300x400")

def clicked():
    name = e.get()
    newtext = "Hello " + name
    Label2 = Label(root, text=newtext)
    Label2.pack()

 #  Adding widget
Label1 = Label(root, text ="Hello World!",background="red", font=20)   # defining a 
# Label1.grid(row=0,column=0)  #organizes widgets(here,Label1) in form of blocks and send it to the parent(here root) window 
Label1.pack()

Button1 = Button(root, text="Click Me!", background="pink", command=clicked)  # creating a button
# # Button1.grid(row=3,column=0) # grid method aligns all the widgets in form of grid and ignores spaces in b/n
# Button1.place(x=100, y=100)
Button1.pack()

img = PhotoImage(file="calculator.png")
root.iconphoto(False, img)

#creating a imageframe
imageFrame = Frame(root, width=100, height=100)
imageFrame.pack()

calculatorimg = ImageTk.PhotoImage(Image.open("calculator.png"))
imageLabel = Label(calculatorimg, image = calculatorimg)
imageLabel.pack()

# Entry widget is used to give a input field
e = Entry(root,width=100,borderwidth=5)
e.pack()
# e.grid(row=2, column=0)
# text = e.get()
# e.insert(0, "Enter name")


root.mainloop() #looping the application to run 
