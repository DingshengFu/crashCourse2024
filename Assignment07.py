import tkinter as tk 
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def openImage():
    global originalImage, tkOriginalImage
    filePath = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.gif *.bmp")])
    if filePath:
        originalImage = Image.open(filePath)
        originalImage.thumbnail((500, 500))  # 缩放图片
        # originalImage = originalImage.resize((500, 500))
        tkOriginalImage = ImageTk.PhotoImage(originalImage)

        imageLabel1.config(image=tkOriginalImage)
        imageLabel1.image = tkOriginalImage

def flipImage():
    global flippedImage, tkFlippedImage
    flippedImage = originalImage.transpose(Image.FLIP_LEFT_RIGHT)
    tkFlippedImage = ImageTk.PhotoImage(flippedImage)

    imageLabel2.config(image=tkFlippedImage)
    imageLabel2.image = tkFlippedImage

def saveImage():
    filePath = filedialog.asksaveasfilename(defaultextension=".jpg",filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"),("All files", "*.*")])
    if filePath:
        flipImage.save(filePath)

    

root = tk.Tk() 
root.title("Picture Flip Tool") 
root.geometry("1000x505") 

# 图像框
imageFrame = tk.Frame(root,borderwidth=2,relief=GROOVE) 
imageFrame.place(x= 0,y=5,width=1000,height=500) 

imageLabel1 = tk.Label(imageFrame, text='Original Image',borderwidth=2,relief=GROOVE)
imageLabel1.place(x=0,y=5,width=500,height=500) 
imageLabel2 = tk.Label(imageFrame, text='Flipped Image')
imageLabel2.place(x=500,y=5,width=500,height=500) 

# 按钮框
buttonFrame = tk.Frame(root,borderwidth=2,relief=GROOVE) 
buttonFrame.pack(fill=X)  

tk.Button(buttonFrame, text='Open Image', command=openImage).grid(row=0, column=0, padx=200, pady=5) 
tk.Button(buttonFrame, text='Flip Image', command=flipImage,bg='yellow').grid(row=0, column=1,pady=5) 
tk.Button(buttonFrame, text='Save Image', command=saveImage).grid(row=0, column=2,padx=200, pady=5) 

root.mainloop()