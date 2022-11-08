'''
Created on 09/04/2015

@author: ivan
'''
from PIL import Image
from estego.binario import completaBits

def imgToBits(archivo):
    original = Image.open(archivo)
    pxO = original.load()
    l = []

    for x in range(original.size[0]):
        for y in range(original.size[1]):
            for chan in range(4):
                for bit in completaBits((bin(pxO[x,y][chan])[2:]), 8):
                    l.append(int(bit)+1)
    return l

def imgToInt(archivo):
    original = Image.open(archivo)
    pxO = original.load()
    l = []

    for x in range(original.size[0]):
        for y in range(original.size[1]):
            for chan in range(4):
                l.append(pxO[x,y][chan])
    return l

def MSE(imgOriginal, imgEstego):
    original = Image.open(imgOriginal)
    estego = Image.open(imgEstego)
    pxO = original.load()
    pxE = estego.load()
    sumatoria = [0,0,0,0]
    MSEcanal = [0,0,0,0]
    M = original.size[0]
    N = original.size[1]
    for x in range(original.size[0]):
        for y in range(original.size[1]):
            sumatoria[0] = sumatoria[0] + (pxO[x,y][0]-pxE[x,y][0])**2 
            sumatoria[1] = sumatoria[1] + (pxO[x,y][1]-pxE[x,y][1])**2 
            sumatoria[2] = sumatoria[2] + (pxO[x,y][2]-pxE[x,y][2])**2  
            sumatoria[3] = sumatoria[3] + (pxO[x,y][3]-pxE[x,y][3])**2 
    MSEcanal[0] = sumatoria[0]/(M*N)
    MSEcanal[1] = sumatoria[1]/(M*N)
    MSEcanal[2] = sumatoria[2]/(M*N)
    MSEcanal[3] = sumatoria[3]/(M*N)
    return sum(MSEcanal)/4
    
    return sumatoria/(original.size[0]*original.size[1])


def PSNR(imagenOriginal, imagenEstego, bits=8):
    from math import log10
    MSERGBA = MSE(imagenOriginal, imagenEstego)
    return 10*log10(((255)**2)/MSERGBA)

def entropia(imagen):
    l = imgToBits(imagen)
                
    from math import log
    
    log2=lambda x:log(x)/log(2)
    total=len(l)
    counts={}
    for item in l:
        counts.setdefault(item,0)
        counts[item]+=1
    ent=0   
    for i in counts:
        p=float(counts[i])/total
        ent-=p*log2(p)
    return ent

def klDistancia(imgp, imgq):
    p = imgToInt(imgp)
    q = imgToInt(imgq)
    import numpy as np
    p = np.asarray(p,dtype=np.float)
    q = np.asarray(q,dtype=np.float)
    return np.sum(np.where(p!=0,p*np.log(p/q),0))

    
# # entropia de una imagen de prueba blanca la entropia es cero
# print(entropia("blanco.png"))

#calcula la entropia de una imagen y devuelve una tupla 
  
nombres = ["lenna", "nieve","bombilla","arguedas","abeja"]
  
for nom in nombres:
    orig = "../img/" + nom + ".png"
    entOrig = entropia(orig)
    for n in range(1,9):
        destino = "../img/" +nom + str(n) + ".png"
        entDest = entropia(destino)
        print(",".join([destino, str(entDest), str(entOrig),str(entropia(destino) - entOrig) ]))
        print(klDistancia(orig, destino))
#print(c.decodificar("eye2_c.png", "12345678",bits=2))

#########################################################################################################

# #codifica todas las imagenes con todos los bits menos significativos en orden creciente
# c = codec()
# 
# mensaje = c.cargarMensaje("mensaje01.txt")
# print(mensaje)
# 
# nombres = ["lenna", "nieve","bombilla","arguedas","abeja"]
# 
# for nom in nombres:
#     for n in range(1,9):
#         origen = nom + ".png"
#         destino = nom + str(n) + ".png"
#         c.codificar(origen, destino, mensaje, "12345678", bits=n)
#         print(",".join([origen, destino, str(PSNR(origen, destino))]))
# #print(c.decodificar("eye2_c.png", "12345678",bits=2))



