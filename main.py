import cv2 as cv
import numpy as np
import string
import random
from reportlab.pdfgen import canvas
from tqdm import tqdm
from tkinter import filedialog
import webbrowser
image = cv.imread(filedialog.askopenfilename(filetypes=[("Image", [".png", ".jpeg", ".jpg"])]))
image_rgb=cv.cvtColor(image, cv.COLOR_BGR2RGB) 
ascii_image = [['X' for _ in range(len(image_rgb))] for _ in range(len(image_rgb))]
print("Analazing Photo")
for x in tqdm(range(len(image_rgb))):
    for y in range(len(image_rgb)):
         sum = image_rgb[x,y][0] + image_rgb[x,y][1] + image_rgb[x,y][2]
         if sum < 160:
              image_rgb[x,y] = [0,0,0]
              ascii_image[x][y] = random.choice(string.ascii_lowercase)
         else:
              image_rgb[x,y] = [255,255,255]
              ascii_image[x][y] = " "
c = canvas.Canvas("resultado.pdf")
c.setFont("Helvetica", 1)
print("Creating Result")
for x in tqdm(range(len(ascii_image))):
     for y in range(len(ascii_image)):
          try:
           c.drawString(x,y,ascii_image[len(ascii_image) - y][len(ascii_image) - x])
          except Exception:
              c.drawString(x,y," ")
c.save()
webbrowser.open_new("resultado.pdf")