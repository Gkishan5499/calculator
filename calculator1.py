from tkinter import Tk
from tkinter import Entry
from tkinter import Button
from tkinter import StringVar
root=Tk()
root.title("Kishan Kumar Gautam Calculator*")
root.geometry("425x280")
root.resizable(0,0)
root.configure(background="black")
a=StringVar()
def show(c):
      a.set(a.get()+c)

def equ():
      ex=a.get()
      a.set(eval(ex))

def clear():
     a.set("")
e1=Entry(root,font=("",30),justify="right",bg="light blue",bd=4,textvariable=a)
e1.place(x=0,y=0,width=425,height=50)

      

      
      
b1=Button(root,text="1",font=("",25),bg="gray")
b1.place(x=5,y=55,width=100,height=50)
b1.configure(command=lambda:show("1"))
b2=Button(root,text="2",font=("",25),bg="gray")
b2.place(x=110,y=55,width=100,height=50)
b2.configure(command=lambda:show("2"))
b3=Button(root,text="3",font=("",25),bg="gray")
b3.place(x=215,y=55,width=100,height=50)
b3.configure(command=lambda:show("3"))
b4=Button(root,text="+",font=("",25),bg="pink")
b4.place(x=320,y=55,width=100,height=50)
b4.configure(command=lambda:show("+"))



b5=Button(root,text="4",font=("",25),bg="gray")
b5.place(x=5,y=110,width=100,height=50)
b5.configure(command=lambda:show("4"))
b6=Button(root,text="5",font=("",25),bg="gray")
b6.place(x=110,y=110,width=100,height=50)
b6.configure(command=lambda:show("5"))
b7=Button(root,text="6",font=("",25),bg="gray")
b7.place(x=215,y=110,width=100,height=50)
b7.configure(command=lambda:show("6"))
b8=Button(root,text="-",font=("",25),bg="pink")
b8.place(x=320,y=110,width=100,height=50)
b8.configure(command=lambda:show("-"))




b9=Button(root,text="7",font=("",25),bg="gray")
b9.place(x=5,y=165,width=100,height=50)
b9.configure(command=lambda:show("7"))


b10=Button(root,text="8",font=("",25),bg="gray")
b10.place(x=110,y=165,width=100,height=50)
b10.configure(command=lambda:show("8"))

b11=Button(root,text="9",font=("",25),bg="gray")
b11.place(x=215,y=165,width=100,height=50)
b11.configure(command=lambda:show("9"))

b12=Button(root,text="*",font=("",25),bg="pink")
b12.place(x=320,y=165,width=100,height=50)
b12.configure(command=lambda:show("*"))



b13=Button(root,text="0",font=("",25),bg="gray")
b13.place(x=5,y=220,width=100,height=50)
b13.configure(command=lambda:show("0"))
b14=Button(root,text="C",font=("",25),bg="pink")
b14.place(x=110,y=220,width=100,height=50)
b14.configure(command=clear)
b15=Button(root,text="=",font=("",25),bg="pink")
b15.place(x=215,y=220,width=100,height=50)
b15.configure(command=lambda:show("="))
b15.configure(command=equ)

b16=Button(root,text="/",font=("",25),bg="pink")
b16.place(x=320,y=220,width=100,height=50)
b16.configure(command=lambda:show("/"))





root.mainloop()
