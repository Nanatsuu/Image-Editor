from PIL import Image, ImageEnhance, ImageFilter
import tkinter as tk
from tkinter import filedialog

class SimpleImageEditor:
    def __init__(self):
        self.image = None;
        self.root = tk.Tk();
        self.root.title("Simple Image Editor")

        # Create buttons for the editor functions
        self.open_button = tk.Button(self.root, text="Open Image", command=self.open_image);
        self.open_button.pack()

        self.resize_button = tk.Button(self.root, text="Resize Image", command=self.resize_image)
        self.resize_button.pack()

        self.rotate_button = tk.Button(self.root, text="Rotate", command=self.rotate_image)
        self.rotate_button.pack()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_image)
        self.save_button.pack()
