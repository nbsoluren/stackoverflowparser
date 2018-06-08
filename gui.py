import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import parse as b

def render():
    def donothing():
       b. stackParser(url)

    def file_save():
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        url = 'https://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python'
        text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0
        f.write(str(b.stackParser(url)))
        f.close() # `()` was missing.

    def OpenFile():
        name = askopenfilename(initialdir="~/Desktop/",
                               filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                               title = "Choose a file."
                               )
        print (name)
        #Using try in case user types in unknown file or closes without choosing a file.
        try:
            with open(name,'r') as UseFile:
                print(UseFile.read())
        except:
            msg = "No file exists"

    root = Tk()
    root.geometry("500x250")

    Title = root.title( "Stack Overflow Parser")

    label = Label(root, text ="PUT URL HERE!!!!!!",foreground="red",font=("Helvetica", 16))
    label.pack()

    menubar=Menu(root)
    text=Text(root)
    text.pack()
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    #filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=file_save)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)



    root.config(menu=menubar)
    root.mainloop()
