'''
Created on 04/04/2015

@author: ivan
'''
from estego.automata import automata
from datetime import time
import time

def chiCuadrado(muestra):
    '''Realiza una prueba de uniformidad a una lista de bits seudoaleatoria
    '''
    fo0 = muestra.count(0)
    fo1 = muestra.count(1)
    fe0 = len(muestra)/2
    fe1 = len(muestra)/2
    x2 = (fe0-fo0)**2/fe0 + (fe1-fo1)**2/fe1
    return x2

def varianza(muestra):
    '''Realiza una prueba de varianza a una lista de bits seudoaleatoria
    '''
    med = media(muestra)
    varianza = sum([(r-med)**2 for r in muestra])/(len(muestra)-1)
    return varianza

def media(muestra):
    return sum(muestra)/len(muestra)

def corridas(muestra):
    corr = 1
    actual = muestra[0]
    for n in range(1,len(muestra)):
        if muestra[n] != muestra[n-1]:
            corr +=1
            actual=muestra[n]
    esperado = (2*len(muestra)-1)/3
    varCorrida = (16*len(muestra)-29)/90
    return abs((corr-esperado)/varCorrida)
#generacion de las claves y reglas a ser probadas
claves = ['1','123', '123456789', 'Fibonacci_112358']
reglas = [[i] for i in range(511,512)]

fileResul = open("../repo/resultados1.txt", 'w')

for r in reglas:
    inicio = time.time()
    for c in claves:
        aut = automata(c,r)
        secAleatoria = list(aut.evolucionar(16384))
        resChi = chiCuadrado(secAleatoria)
        resMedia = media(secAleatoria)
        resCorrida = corridas(secAleatoria)
        registro = ",".join([str(r[0]),str(c),str(resMedia),str(resChi),str(resCorrida)])
        print(registro)
        print(time.time()-inicio)
        fileResul.write(registro+"\n")


