from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)  #Delete all text in the TextArea (from line 1, character 0 to the end of the text).

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file #Global lets you update outside the function variable, inside the function.
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt"
        , filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            #Save as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        #Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy() #This will close the application when the user clicks on Exit in the File menu.

def cut():
    TextArea.event_generate("<<Cut>>")

def copy():
    TextArea.event_generate("<<Copy>>")

def paste():
    TextArea.event_generate("<<Paste>>") #It takes whatever is in the clipboard (like copied text) and inserts it into TextArea at the current cursor position.

def about():
    showinfo("Notepad", "Notepad by Code With Harry")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13") #Text() → Tkinter Text widget (a big multi-line text editor box, like Notepad’s typing area).
    file = None #None means no file is currently open (a new untitled document).
    TextArea.pack(expand=True, fill=BOTH) #pack() is used to add the TextArea to the root window. expand=True allows the TextArea to expand and fill the available space, and fill=BOTH allows it to fill both horizontally and vertically.


    # Lets create a menubar
    MenuBar = Menu(root) #A MenuBar attaches directly to the window (using root.config(menu=MenuBar)), so it doesn’t need pack() or grid().
    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label = "New", command = newFile) #In Notepad’s File menu, Items like New, Open, Save, Exit are created using add_command
    #To open already existing file
    FileMenu.add_command(label = "Open", command = openFile)
    #To save current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu = FileMenu) #add_cascade() is used to add a menu to the menubar.It work as a dropdown menu.
    #File Menu Ends

    #Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0) #By default, Tkinter menus can be “torn off” (a dashed line at the top lets you open the menu in a separate window).
    #TO GIVE A FEATURE OF CUT, COPY AND PASTE
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)    
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    #Edit Menu Ends
    #Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command= about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)


    #Help Menu Ends
    root.config(menu = MenuBar) #config() is used to set the menu bar for the root window.

    #Adding Scrollbar using rules from Tkinter 
    Scroll = Scrollbar(TextArea) #Scrollbar is attached inside the text area widget.
    Scroll.pack(side = RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview) #This connects the scrollbar to the TextArea.
    TextArea.config(yscrollcommand=Scroll.set) #Whenever the text moves (typing, arrow keys, page up/down), update the scrollbar’s position.

    root.mainloop()