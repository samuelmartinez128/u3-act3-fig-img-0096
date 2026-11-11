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
print("+-+-+- Cuadro en la imagen +-+-+-")
imagenol= cv2.imread('oliveira.jpg')
plt.imshow(imagenol)
x = [210, 467, 467, 210, 210]
y = [10, 10, 300, 300, 10]
plt.plot(x,y,c='blue')
plt.show()

print("+-+-+- circulo verde a la imagen +-+-+-")
imagenol = cv2.imread('oliveira.jpg')
plt.imshow(imagenol)
N = 30 #lados del poligono
x= np.zeros((N+1,))
y= np.zeros((N+1,))
(xc,yc) = (350,340)
r= 150 #radio
for i in range(N+1):
 t = 2*np.pi/N*i
 x[i]= xc + r*np.cos(t)
 y[i]= yc + r*np.sin(t)

plt.plot(x,y, c='green')
plt.show()