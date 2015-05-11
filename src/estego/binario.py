'''
Created on 03/04/2015

@author: ivan
'''
def completaBits(sIncompleta, numBits=8):
    '''Recibe una secuencia de digitos binarios y completa ceros hasta la longitud dada por numBits
    Ejm.    completaBits('101',8) ------> '00000101'
    '''
    sCompleta = "".join(["0" for i in range(numBits-len(sIncompleta))])+sIncompleta
    return sCompleta

def generaBinario(cadena):
    ''' Recibe un numero binario y lo convierte en una cadena de texto que contiene un binario
    con los ceros completados a la izquierda hasta 8 bits.
    ejemplo:
        obtenerCadena('0b101') ----->>  '00000101'
    '''
    cadBinario = ""
    for n in cadena:
        cadBinario = cadBinario + completaBits(bin(n)[2:],8)
    return cadBinario

def obtenerCadena(numBinario):
    '''convierte una secuencia de ditigos binario numBinario a ascci y retorna una cadena de caracteres
    '''
    cadena = ""
    for i in range(0,len(numBinario),8):
        cadena = cadena+chr(int("0b"+numBinario[i:i+8],2))
    return cadena

def xor(binario1, binario2):
    '''Realiza una operacion de XOR entre dos secuencias de bit binarias de la misma longitud
    Ejm. xor('00010001','00010011') -----> '00000010'
    '''
    resultado =""
    for i in range(len(binario1)):
        if binario1[i] == binario2[i]:
            resultado = resultado + "0"
        else:
            resultado = resultado + "1"
    return resultado

def LSB(binario1, binario2):
    '''Inserta los bits de binario2 en la secuencia de bits mas larga binario1
    '''
    binarioLSB = binario1[:len(binario1)-len(binario2)]+binario2
    return binarioLSB

def extraeLSB(binario, numBits=2):
    '''Estra una cantidad numBits de bits de la secuencia binaria dada por binario
    '''
    bitsLSB = binario[len(binario)-numBits:]
    return bitsLSB

