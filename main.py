import cv2 as cv
import numpy as np
import string
import random
from reportlab.pdfgen import canvas
from tqdm import tqdm
from tkinter import filedialog
import webbrowser
image = cv.imread(filedialog.askopenfilename(filetypes=[("Image", [".png", ".jpeg", ".jpg"])]))
imageRgb=cv.cvtColor(image, cv.COLOR_BGR2RGB) 
asciiMatrix = [['X' for _ in range(len(imageRgb))] for _ in range(len(imageRgb))]
print("Analazing Photo")
for x in tqdm(range(len(imageRgb))):
    for y in range(len(imageRgb)):
         totalColor = imageRgb[x,y][0] + imageRgb[x,y][1] + imageRgb[x,y][2]
         if totalColor < 160:
              imageRgb[x,y] = [0,0,0]
              asciiMatrix[x][y] = random.choice(string.ascii_lowercase)
         else:
              imageRgb[x,y] = [255,255,255]
              asciiMatrix[x][y] = " "
c = canvas.Canvas("result.pdf")
c.setFont("Helvetica", 1)
print("Creating Result")
for x in tqdm(range(len(asciiMatrix))):
     for y in range(len(asciiMatrix)):
          try:
           c.drawString(x,y,asciiMatrix[len(asciiMatrix) - y][len(asciiMatrix) - x])
          except Exception:
              c.drawString(x,y," ")
c.save()
webbrowser.open_new("result.pdf")