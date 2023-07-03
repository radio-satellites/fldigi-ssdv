import tkinter as tk
from PIL import Image, ImageTk
import os


root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("decoded.jpg"))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def update_image():
    os.system("ssdv -d decoded.bin decoded.jpg")
    print("SSDV UPDATE")
    try:
        img2 = ImageTk.PhotoImage(Image.open("decoded.jpg"))
        panel.configure(image=img2)
        panel.image = img2
    except Exception as e:
        print(e)
    root.after(3000, update_image)

update_image()
root.mainloop()
