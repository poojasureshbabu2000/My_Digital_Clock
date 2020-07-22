import sys
from tkinter import *
import time

def cidClock():
    c_time = time.strftime("%H : %M: %S")
    clock.config(text=c_time)
    clock.after(100,cidClock)

root =Tk ()
root.title("My Digital Clock")

message= Label(root, font=("times new roman",100,"bold"), text="Original Time",fg= "black")
message.grid(row=0,column=0)
clock= Label(root, font=("time",150,"bold"),bg="black",fg="yellow")
clock.grid(row=1,column=0)
cidClock()
mainloop()
