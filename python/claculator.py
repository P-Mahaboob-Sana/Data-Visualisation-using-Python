from tkinter import *

import executing

def click(number):
    prevnum = e.get()
    e.delete(0,END)
    newnumber = str(prevnum)+str(number)
    e.insert(0,newnumber)

def clear():
        e.delete(0,END)

def add():
     global f_num
     global operation
     operation = "add"
     f_num = e.get()
     e.delete(0,END)

def sub():
      global f_num
      global operation
      operation = "sub"
      f_num = e.get()
      e.delete(0,END)


def mul():
     global f_num
     global operation
     operation = "mul"
     f_num = e.get()
     e.delete(0,END)

def div():
     global f_num
     global operation
     operation = "mul"
     f_num = e.get()
     e.delete(0,END)
         
     
def equal():
    global s_num
    s_num= e.get()
    e.delete(0,END)
    if(operation=="add"):
         result = int(f_num)+ int(s_num)
    elif(operation=="sub"):
           result = int(f_num)- int(s_num)
    elif(operation=="mul"):
         result = int(f_num)* int(s_num) 
    elif(operation=="div"):
         result = int(f_num)/int(s_num)      
    newresult = str(result)
    e.insert(0,newresult)






root = Tk()
root.title("Calculator")


img = PhotoImage(file="calculatorimg.png")
root.iconphoto(False, img)

e = Entry(root, width=40,borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

Button0 = Button(root,text="0", padx=40, pady=20, command=lambda: click(0))
Button1 = Button(root,text="1", padx=40, pady=20, command=lambda: click(1))
Button2 = Button(root,text="2", padx=40, pady=20, command=lambda: click(2))
Button3 = Button(root,text="3", padx=40, pady=20, command=lambda:click(3))
Button4 = Button(root,text="4", padx=40, pady=20, command=lambda:click(4))
Button5 = Button(root,text="5", padx=40, pady=20, command=lambda:click(5))
Button6 = Button(root,text="6", padx=40, pady=20, command=lambda:click(6))
Button7 = Button(root,text="7", padx=40, pady=20, command=lambda:click(7))
Button8 = Button(root,text="8", padx=40, pady=20, command=lambda:click(8))
Button9 = Button(root,text="9", padx=40, pady=20, command=lambda:click(9))

Button_clear = Button(root, text="clear", padx=79, pady=20, command=clear)
Button_add = Button(root, text="+", padx=40, pady=40 , command=add)
Button_sub = Button(root, text="-", padx=40, pady=40 , command=sub)
Button_mul = Button(root, text="*", padx=40, pady=40 , command=mul)
Button_div = Button(root, text="/", padx=40, pady=40 , command=div)
Button_equal = Button(root, text="=", padx=40, pady=40, command=equal)


Button0.grid(row=4, column=0)

Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Button_clear.grid(row=4, column=1, columnspan=2)
Button_add.grid(row=5,column=0)
Button_sub.grid(row=5,column=1)
Button_mul.grid(row=5,column=2)
Button_div.grid(row=5,column=3)
Button_equal.grid(row=6, column=4)




root.mainloop()
