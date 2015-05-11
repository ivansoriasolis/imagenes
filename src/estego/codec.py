# -*- coding: utf-8 -*-
'''
Created on 06/04/2015

@author: ivan
'''
from PIL import Image
from random import randint, Random
from estego import binario as Binario
from estego.automata import automata

class codec:
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def codificar(self, archivo, archResul, cadena, clave, regla=[341], bits=2):
        if not (bits >=1 and bits <=8):
            raise RuntimeError("Cantidad de bits fuera de rango")
        if len(clave)>16:
            raise RuntimeWarning("La clave tardará mucho en procesarse")
        mensaje = bytearray(cadena, "ascii")
        binario = Binario.generaBinario(mensaje)
        binario = self.cifrar(binario, clave, regla)
        binario = self.agregaEncabezado(binario,bits)
        contador = 0
        i = Image.open(archivo)
        px = i.load()
        for x in range(i.size[0]):
            for y in range(i.size[1]):
                pixel = [0,0,0,0]
                for p in range(4):
                    if contador < len(binario):
                        canalBinario = Binario.completaBits((bin(px[x,y][p])[2:]), 8)
                        bitsBinario = binario[contador:contador+bits]
                        byteCanal = Binario.LSB(canalBinario,bitsBinario)
                        pixel[p] = int("0b"+byteCanal,2)
                        #print(bitsBinario,byteGreen)
                    else:
                        canalBinario = Binario.completaBits((bin(px[x,y][p])[2:]), 8)
                        bitsBinario = Binario.completaBits(bin(randint(0,2**bits-1))[2:],bits)
                        byteCanal = Binario.LSB(canalBinario,bitsBinario)
                        pixel[p] = int("0b"+byteCanal,2)
                        #print(greenBinario,bitsBinario,byteGreen)
                    contador+=bits
                red   = pixel[0]
                green = pixel[1]
                blue  = pixel[2] 
                alfa  = pixel[3] 
                    
                px[x,y]=(red,green,blue,alfa)
                #print(x,y,px[x,y][1])
        i.save(archResul,compress_level=0)
        
    def decodificar(self, archivo, clave, regla = [341], bits = 2):
        mensaje = ""
        contador = 0
        i = Image.open(archivo)
        px = i.load()
        for x in range(i.size[0]):
            for y in range(i.size[1]):
                for p in range(4):
                    byteColor=Binario.completaBits((bin(px[x,y][p])[2:]), 8)
                    mensaje = mensaje+ Binario.extraeLSB(byteColor,bits)
        tamano, mensaje = self.extraeEncabezado(mensaje)
        textoCifrado = mensaje[:tamano]
        textoClaro = self.cifrar(textoCifrado, clave, regla)
        return Binario.obtenerCadena(textoClaro)
        
    
    def agregaEncabezado(self, secBinaria,bits=1):
        '''agrega un encabezado a la secuencia binaria, el encabezado consta de 16 bits que representan 
        el tamano del mensaje codificado en binario
        '''
        tamanoSec = len(secBinaria)
        encabezado = Binario.completaBits(bin(tamanoSec)[2:], 16)
        return encabezado + secBinaria
    
    def extraeEncabezado(self, secBinaria):
        '''Lee el encabezado de la secuencia binaria dada, se toamn los 16 primeros bits como encabezado
        '''
        encabezado = secBinaria[:16]
        return [int("0b"+encabezado,2), secBinaria[16:]]
    
    def cifrar(self, secBinaria, clave, regla):
        '''aplica la operacion XOR a la secuencia de bits secBinario par lo que hace evolucionar el automata
        un numero de veces igual al tamano de la secuencia de bits, la secuencia de bits debe incluir
        el encabezdo, qe tambien se cifra.
        '''
        generador = automata(clave, regla)
        secCifrante = "".join([str(i) for i in list(generador.evolucionar(len(secBinaria)))])
        return Binario.xor(secBinaria, secCifrante)
    
    def cargarMensaje(self, archivo):
        '''Carga un mensaje desde un archivo de texto, el texto debe estar en formato ASCCII, de lo contrario
        se generaran caracteres extraños
        '''
        with open(archivo, mode='rt', encoding='ascii', errors='ignore') as f:
            data= f.read()
        return data
    
    def normalizar(self,archivo):
        '''Uniformiza la compresión de los archivos
        '''
        i = Image.open(archivo)
        i.save(archivo,compress_level=0)               
    
