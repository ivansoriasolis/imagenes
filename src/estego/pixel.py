'''
Created on 30/12/2014

@author: ivan
'''
from PIL import Image
from random import randint
from estego import binario as Binario

mensaje = bytearray("MENSAJE SECRETO","ASCII")
binario = Binario.generaBinario(mensaje)

print(binario)

contador = 0

i = Image.open('pyton.png')
px = i.load()

for x in range(i.size[0]):
    for y in range(i.size[1]):
        red = px[x,y][0]
        if contador < len(binario):
            green = int(binario[contador])*100
        else:
            green = px[x,y][1]
        blue = px[x,y][2] 
        alfa = px[x,y][3] 
        px[x,y]=(red,green,blue,alfa)
        contador+=1
        
i.save('pyton1.jpg')
