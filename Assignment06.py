from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText 

def load(): 
    with open(filename.get()) as file: 
        contents.delete('1.0', END) 
        contents.insert(INSERT, file.read()) 

def save(): 
    with open(filename.get(), 'w') as file: 
        file.write(contents.get('1.0', END)) 

def saveAs():
    filePath = filedialog.asksaveasfilename(initialdir='.', title='Save As', filetypes=(('Text Files', '*.txt'), ('All Files', '*.*')))
    if filePath:
        with open(filePath, "w", encoding="utf-8") as file:
            file.write(contents.get(1.0, END))

def updateStatusBar(event = None):
    currentLine = contents.index(INSERT).split('.')[0]
    currentColumn = contents.index(INSERT).split('.')[1]
    totalLines = contents.index('end-1c').split('.')[0]
    statusBar.config(text=f"Line {currentLine}, Column {currentColumn}(Total Lines: {totalLines})")

top = Tk() 
top.title("Simple Editor") 

statusBar = Label(text="Be Ready", bd=1, relief=SUNKEN, anchor=W) 
statusBar.pack(side=BOTTOM, fill=X) 

contents = ScrolledText() 
contents.pack(side=BOTTOM, expand=True, fill=BOTH) 

contents.bind('<KeyRelease>', updateStatusBar) 
contents.bind('<ButtonRelease-1>', updateStatusBar) 

filename = Entry() 
filename.pack(side=LEFT, expand=True, fill=X) 

Button(text='Open', command=load).pack(side=LEFT) 
Button(text='Save', command=save).pack(side=LEFT) 
Button(text='SaveAs', command=saveAs).pack(side=LEFT) 

mainloop()