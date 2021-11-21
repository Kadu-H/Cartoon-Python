#Area de importação
import cv2
import numpy as np
from tkinter.filedialog import *

#Selecionar imagem
photo = askopenfilename()
img = cv2.imread(photo)

#Adicionando partes dos efeitos
gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur (gray, 3)
edges = cv2.adaptiveThreshold (gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

#Fazendo o efeito CARTOON
color = cv2.bilateralFilter(img, 9,250,250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

#Mostrar as imagens finais
cv2.imshow("Image", img)
cv2.imshow("Edges", edges)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
