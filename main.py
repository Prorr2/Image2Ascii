import cv2 as cv
import numpy as np
import string
import random
from reportlab.pdfgen import canvas
from tqdm import tqdm
from tkinter import filedialog
import webbrowser
from pdf2image import convert_from_path
option = input("Do you want yo change image size? (y/n)")
aceptableOptionList = ["yes", "y"]
px = 0
if option in aceptableOptionList:
    px = int(input("px in width and heigh: "))
image = cv.imread(filedialog.askopenfilename(filetypes=[("Image", [".png", ".jpeg", ".jpg"])]))
if option in aceptableOptionList:
     image_rgb=cv.cvtColor(cv.resize(image, (px, px)), cv.COLOR_BGR2RGB) 
else:
    image_rgb=cv.cvtColor(image, cv.COLOR_BGR2RGB) 
ascii_image = [['X' for _ in range(len(image_rgb))] for _ in range(len(image_rgb))]
print("-----------------------------------------------------------------------")
print("Analazing Photo")
print("-----------------------------------------------------------------------")
for x in tqdm(range(len(image_rgb))):
    for y in range(len(image_rgb)):
         sum = image_rgb[x,y][0] + image_rgb[x,y][1] + image_rgb[x,y][2]
         if sum < 160:
              image_rgb[x,y] = [0,0,0]
              ascii_image[x][y] = random.choice(string.ascii_lowercase)
         else:
              image_rgb[x,y] = [255,255,255]
              ascii_image[x][y] = " "
c = canvas.Canvas("result.pdf")
c.setFont("Helvetica", 1)
print("-----------------------------------------------------------------------")
print("Creating Image")
print("-----------------------------------------------------------------------")
for x in tqdm(range(len(ascii_image))):
     for y in range(len(ascii_image)):
          try:
           c.drawString(x,y,ascii_image[len(ascii_image) - y][len(ascii_image) - x])
          except Exception:
              c.drawString(x,y," ")
              
c.save()
page = convert_from_path('result.pdf')
page[0].save('result.jpg', 'JPEG')

file = open("result.txt", "w")
print("-----------------------------------------------------------------------")
print("Creating Text")
print("-----------------------------------------------------------------------")
for x in tqdm(range(len(ascii_image))):
     for y in range(len(ascii_image)):
          try:
           file.write(ascii_image[x][y])
          except Exception:
              file.write(" ")
     file.write("\n")
file.close()
webbrowser.open_new_tab("result.jpg")
webbrowser.open_new_tab("result.txt")