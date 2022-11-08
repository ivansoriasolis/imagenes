'''
Created on 03/04/2015

@author: ivan
'''

from estego import binario as Binario
from estego.reglas import reglas

class automata:
    def __init__(self, semilla="12345678", reg=[]):
        '''Inicializa el automata con la semilla o clave indicada, si no se pone una semilla se usara una por default
        '''
        self.latice = []
        self.conjReglas = reglas(reg)
        semBinaria = Binario.generaBinario(bytearray(semilla,"ASCII"))
        n = int(pow(len(semBinaria),0.5)+1)    #determina el tamano del automata en base a las semmilla
        semBinaria = semBinaria +  "".join(["0" for i in range(n*n -len(semBinaria))]) #completa ceros para un automata cuadrado
        self.filas = self.columnas = n
        self.latice = [[int(v) for v in list(semBinaria[i:i+n])] for i in range(0,len(semBinaria),n)] #rellena el latice con la semilla
      
    def evolucionar(self, n=1):
        for itera in range(0,n):
            sigLatice = [[0 for i in range(self.filas)] for j in range(self.columnas)]
            for fil in range(self.filas):
                for col in range(self.columnas):
                    if self.conjReglas.buscaRegla(self.obtenerVecinos(fil, col)):
                        sigLatice[fil][col] = 1
                    else:
                        sigLatice[fil][col] = 0
            self.latice = list(sigLatice)
#             print(self.toString())
            yield self.latice[self.filas//2][self.columnas//2]        
    
    def obtenerVecinos(self, f, c):
        vecino1 = self.latice[f][c]
        vecino2 = self.latice[f][(c+1) % self.columnas]
        vecino4 = self.latice[(f+1) % self.filas][(c+1) % self.columnas]
        vecino8 = self.latice[(f+1) % self.filas][c]
        vecino16 = self.latice[(f+1) % self.filas][(c-1) % self.columnas]
        vecino32 = self.latice[f][(c-1) % self.columnas]
        vecino64 = self.latice[(f-1) % self.filas][(c-1) % self.columnas]
        vecino128 = self.latice[(f-1) % self.filas][c]
        vecino256 = self.latice[(f-1) % self.filas][(c+1) % self.columnas]
        vecinos = [vecino1, vecino2, vecino4, vecino8, vecino16, vecino32, vecino64, vecino128, vecino256]
        stringVecinos = "".join([str(v) for v in vecinos])
        return stringVecinos
        
    def toString(self):
        cadena = ""
        for fil in range(self.filas):
            for col in range(self.columnas):
                cadena = cadena + str(self.latice[fil][col]) + " "
            cadena = cadena + "\n"
        return cadena
        
                
# a = automata("Fibonacci_112358",[321])
# print(a.toString())
# print(list(a.evolucionar(128)))

    
    