'''
Created on 08/05/2015

@author: ivan
'''
from estego.codec import codec
import argparse

if __name__ == '__main__':
    codificador = codec()
    parser = argparse.ArgumentParser()
    parser.add_argument("-verbose",action='store_true', help="Mostrar informacion de depuracion")
    args = parser.parse_args()
    
    if args.verbose:
        print ("depuracion activada")
        
    pass
