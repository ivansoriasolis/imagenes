'''
Created on 08/05/2015

@author: ivan
'''
from estego.codec import codec
import argparse

if __name__ == '__main__':
    codificador = codec()
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose",action='store_true', help="Mostrar informacion de depuracion")
    parser.add_argument("-f","--file",help="Archivo a procesar")
    parser.add_argument("-o","--out", help="Archivo de salida")
    parser.add_argument("-l","--lsb", help="Bits por pixel")
    parser.add_argument("-k","--key", help="Semilla")
    parser.add_argument("-m","--mens", help="Mensaje en claro")
    parser.add_argument("-c","--codif",action="store_true")
    parser.add_argument("-d","--decod",action="store_true")
    
    args = parser.parse_args()
    
    cod = codec()
    
    if args.verbose:
        print ("depuracion activada")
    if args.codif:
        texto = cod.cargarMensaje(args.mens)
        cod.codificar(args.file, args.out, texto, args.key, [234], int(args.lsb))
    if args.decod:
        print(cod.decodificar(args.file, args.key, [234], int(args.lsb)))
    pass
