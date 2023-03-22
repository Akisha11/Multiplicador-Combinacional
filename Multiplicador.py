#importación de bibliotecas python3 Multiplicador.py --bits 8 -a b1010 -b d45

import sys
import argparse

#-----------------------------------------------------------------------------------

#input de datos

parser = argparse.ArgumentParser()
parser.add_argument('--bits', type=int, required=True)
parser.add_argument('-a', type=str, required=True)
parser.add_argument('-b', type=str, required=True)
args = parser.parse_args()

#-----------------------------------------------------------------------------------

#definir argumentos como variables de python

cantidad = args.bits
num1 = args.a
num2 = args.b

#-----------------------------------------------------------------------------------

#función de sorteo de números según su tipo y conversión a binario

def sorteador_conversor(a):
    if a[:1] == "h":
        a = (a[1:])
        a = int(a,base = 16)
        a = bin(a)
        a = a[2:]
    elif a[:1] == "d":
        a = int(a[1:])
        a = bin(a)
        a = a[2:]
    elif a[:1] == "b":
        a = int(a[1:])
    else:
        lista = ["A","B","C","D","E","F","a","b","c","d","e","f"]
        x = list(a)
        y = bool(set(lista).intersection(x))
        
        if(y == True):
            a = int(a,base = 16)
            a = bin(a)
            a = a[2:]
        else:
            a = int(a)
            a = bin(a)
            a = a[2:]
    return(a)

binario1 = sorteador_conversor(num1)
binario2 = sorteador_conversor(num2)

print(binario1,binario2)

#-----------------------------------------------------------------------------------

#verifica que la cantidad de bits de los números ingresados sean los soportados por el multiplicador y en concordancia con el ingresado

def cantidad_de_bits(a,b):
    a = str(a)
    x = len(a)
    
    if x > b:
        print("El número ingresado: ",a," supera la cantidad de bits indicada")
        exit()
    elif x >= 9:
        print("El número ingresado: ",a," supera la cantidad de bits soportada por el multiplicador")
        exit()

test1 = cantidad_de_bits(binario1,cantidad)
test2 = cantidad_de_bits(binario2,cantidad)

#-----------------------------------------------------------------------------------

# Genera las sumas parciales del multiplicador para la impresión 

def multiplicador_parcial(a,b):
    a = str(a)
    b = str(b)

    largo = len(a)

    lista = list(b)
    lista = [int(x) for x in lista]
    
    a = int(a)
    y = "0"
    y = y.zfill(largo)
    
    
    parc = [x*a for x in lista]
    
    for index, value in enumerate(parc):
        if value == 0:
          parc[index] = y
    
    parc = [str(x) for x in parc]
    
    return(parc)

parciales = multiplicador_parcial(binario1, binario2)

#-----------------------------------------------------------------------------------

# Rellena con 0 los resultados de las multiplicaciones para su posterior impresión 

def rellenador(a,b):
    for index, value in enumerate(a):
        if len(value) < b:
             a[index] = a[index].zfill(b)
    return(a)

parciales_rev = rellenador(parciales, cantidad)

print(parciales_rev)

#-----------------------------------------------------------------------------------

# Multiplica los binarios para arrojar el resultado

