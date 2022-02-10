import numpy as np
import cv2
from PIL import Image

# Carregando a imagem
imagem = Image.open('God2-Sistine_Chapel.png')

# Formato da imagem
print(imagem.format)

# Passando altura e largura para variavel
image = cv2.imread('God2-Sistine_Chapel.png')
a = np.size(image, 0)
l = np.size(image, 1)

#Multiplicando largura e altura para achar os pixels
print('Pixels:', l * a)
