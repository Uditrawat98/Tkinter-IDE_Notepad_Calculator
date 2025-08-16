from tkinter import *

def click(event):#This function is called whenever a button is clicked. Event contains information about the click (which widget, which button, etc.).
    global scvalue #global is needed because I want to modify its value inside this function.
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
        
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x900")
root.wm_iconbitmap("manager.ico")
root.title("Calculator by Udit")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font= "lucida 40 bold", border=3)
screen.pack(fill=X, ipadx=8, pady=3, padx=3)
f = Frame(root, bg="grey")

b=Button(f, text="9", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="8", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="7", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")

b=Button(f, text="6", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="5", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="4", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")

b=Button(f, text="3", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="2", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="1", padx=28, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")

b=Button(f, text="C", padx=26, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="0", padx=27, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="=", padx=27, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")

b=Button(f, text="/", padx=29, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="%", padx=29, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

b=Button(f, text="-", padx=29, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")

b=Button(f, text="*", padx=26, pady=3, font="lucida 35 bold")
b.pack(side=LEFT, padx=3, pady=5)
b.bind("<Button-1>", click)

f.pack()



root.mainloop()