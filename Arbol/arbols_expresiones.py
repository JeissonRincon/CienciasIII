import os
from pila import *
from arbol import *

def convertir(lista, pila):
    if lista != []:
        if lista[0] in "+-*/":
            nodo_der = pila.desapilar()
            nodo_izq = pila.desapilar()
            pila.apilar(Nodo(lista[0],nodo_izq,nodo_der))
        else:
            pila.apilar(Nodo(lista[0]))
        return convertir(lista[1:],pila)
            

def evaluar(arbol):
    if arbol.valor == "+":
        return evaluar(arbol.izq) + evaluar(arbol.der)
    if arbol.valor == "-":
        return evaluar(arbol.izq) - evaluar(arbol.der)
    if arbol.valor == "/":
        return evaluar(arbol.izq) / evaluar(arbol.der)
    if arbol.valor == "*":
        return evaluar(arbol.izq) * evaluar(arbol.der)
    return int(arbol.valor)
    



f = open ('expresiones.in.txt','r')
op = f.read().split()
print(op)
f.close()

pila = Pila()

convertir(op, pila)
t = open ('expresiones.out.txt','w')

while (pila.es_vacia() != True):   
    t.write('resultado: '+ str(evaluar(pila.desapilar())) + os.linesep)
  #print(pila.es_vacia())
t.close()




