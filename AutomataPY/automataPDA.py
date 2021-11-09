"""
Versión que saca el último elemento de la pila solo
si el caracter pop no es 'e' y la pila no es vacía
"""

import json 
data = open('Configuracion.json')
config = json.load(data) 
with open("Cadena.txt", 'r') as f:
    datosEntrada = f.read()
    
parametros = {}
parametros['estados'] = config['estados']
parametros['alfabeto'] = config['alfabeto']
for i in config['transiciones']:    
    parametros['transiciones'] = i
parametros['estadoInicial'] = config['estadoInicial']
parametros['estadoAceptacion'] = config['estadoAceptacion']

estadoActual = parametros['estadoInicial'] 
posicionCaracter = 0
pila = []

for i in datosEntrada:
    pop = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][1]
    push = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][2]
    estadoActual = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][0]
    if(push != 'e'):
        pila.append(push)  
    if((pop != 'e') and (len(pila) != 0)):
        pila.pop(len(pila)-1)
    posicionCaracter +=1 

print("Posición: " + estadoActual)
if((estadoActual in parametros['estadoAceptacion']) and (len(pila) == 0)):
    print("Aceptado") 
else:
    print("Rechazado")