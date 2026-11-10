import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Samuel Martinez NC 0096 
print("Samuel Martinez NC 0096")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen = cv2.imread('oliveira.jpg')
plt.imshow(mi_imagen)
plt.title('Oliveira, Samy 0096')
plt.show()
print("+-+-+- Puntos es la imagen +-+-+-")
plt.imshow(mi_imagen)
x = [100,100,300,350]
y = [100,400,500,300]
plt.scatter(x,y, s=20, c='red')
plt.show()