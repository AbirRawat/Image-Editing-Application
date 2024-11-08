import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk

root = tk.Tk()
root.geometry("1000x600")
root.title("Basic Image Editing Tool")

img = Image.open('./cloud.jpg')
img = img.resize((1000, 600))
img_photo = ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root, image=img_photo)
bg_lbl.place(x=0, y=0, width=1000, height=600)

pen_color = "black"
pen_size = 5
file_path = ""


def add_image():
    global file_path
    file_path = filedialog.askopenfilename(
        initialdir="C:/Users/abirr/OneDrive/Pictures/Saved Pictures")
    #Replace the initialdir with FILE PATH of folder with Images
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.BICUBIC)
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')


def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.BICUBIC)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "Contour":
        image = image.filter(ImageFilter.CONTOUR)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")


frame_one = tk.Frame(root, width=200, height=600, bg="white")
frame_one.pack(side="left", fill="y")

canvas = tk.Canvas(root, width=750, height=600)
canvas.pack()

img_butt = tk.Button(frame_one, text="Add Image", command=add_image, bg="white")
img_butt.pack(pady=15)

color_button = tk.Button(
    frame_one, text="Change Pen Color", command=change_color, bg="white")
color_button.pack(pady=5)

pen_size_frame = tk.Frame(frame_one, bg="white")
pen_size_frame.pack(pady=5)

pen_size_1 = tk.Radiobutton(
    pen_size_frame, text="Small", value=1, command=lambda: change_size(1), bg="white")
pen_size_1.pack(side="left")

pen_size_2 = tk.Radiobutton(
    pen_size_frame, text="Medium", value=5, command=lambda: change_size(5), bg="white")
pen_size_2.pack(side="left")
pen_size_2.select()

pen_size_3 = tk.Radiobutton(
    pen_size_frame, text="Large", value=10, command=lambda: change_size(10), bg="white")
pen_size_3.pack(side="left")

clear_button = tk.Button(frame_one, text="Clear", command=clear_canvas, bg="#FF9797")
clear_button.pack(pady=10)

filter_label = tk.Label(frame_one, text="Select Filter", bg="white")
filter_label.pack()
filter_combobox = ttk.Combobox(
    frame_one, values=["Black and White", "Blur","Emboss", "Sharpen", "Smooth"])
filter_combobox.pack()

filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))

canvas.bind("<B1-Motion>", draw)

root.mainloop()