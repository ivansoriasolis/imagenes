'''
Created on 03/04/2015

@author: ivan
'''
class reglas(list):
    '''Almacena un conjunto de reglas que seran consultadas por un automata,
    si existe la regla en la lista de reglas, debera interpretarse como regla activa
    si no existe esta inactiva
    ''' 
    def __init__(self, reglasDecimal=[]):
        reglasBinario = [self.completaBits(bin(i)[2:],9) for i in reglasDecimal]
        self.extend(reglasBinario)
        pass
    def agregarReglas(self, numDecimal):
        ''' Carga una lista con las reglas que se le dan en base 10,
        esto solamente funciona si se esta trabajando con varias reglas a la vez
        '''
        reglaBinario = self.completaBits(bin(numDecimal)[2:],9)
        if not self.buscaRegla(reglaBinario):
            self.append(reglaBinario)

    def completaBits(self, secIncompleta, numBits=9):
        '''completa una cadena que representa un binario con ceros a la izquierda
        completaBits(sIncompleta[, numBits]) ---> string
        retorna una cadena de tamano numBits
        Ejm.
        completaBits('101',7)   ---->  '0000101'
        '''
        secCompleta = "".join(["0" for i in range(numBits-len(secIncompleta))])+secIncompleta
        return secCompleta
    
    def buscaRegla(self, binario):
        '''busca una regla en binario y devuelve verdadero si esta presente.
        la secuencia binaria se le debe presentar como un string de 0s y 1s
        '''
        vecinosActivos = [0 for i in range(len(binario))]
        cantCeros = 0 #lleva la cuenta de los ceros
        cantUnos = 0 #lleva la cuenta de los unos
        for n in range(len(binario)):   
            vecinosActivos[n] = int(binario[n]) and int(self[0][n])  #realiza un and logico para combinar las reglas
            if vecinosActivos[n] == 0:
                cantCeros = cantCeros + 1
            else:
                cantUnos = cantUnos + 1
        if cantUnos % 2 == 0:   #si la cantidad de unos es par, entonces se actualiza la celula central
            return True
        else:
            return False
        