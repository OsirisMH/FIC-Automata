import json 
data = open('configuracionPDA.json')
config = json.load(data) 
with open("cadena.txt", 'r') as f:
    datosEntrada = f.read()

parametros = {}
parametros['estados'] = config['estados']
parametros['alfabeto'] = config['alfabeto']
parametros['simbolosPila'] = config['simbolosPila']
for i in config['transiciones']:
    parametros['transiciones'] = i
parametros['estadoInicial'] = config['estadoInicial']
parametros['estadoAceptacion'] = config['estadoAceptacion']
estadoActual = parametros['estadoInicial'] 
posicionCaracter = 0
pila = []

for i in datosEntrada:
    pop = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][1][0]
    push = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][1][1]
    estadoActual = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][0]
    if(push != 'e'):
        pila.append(push)
    if((pop != 'e') and (len(pila) != 0)):
        pila = pila[:-1]
    posicionCaracter +=1 

print("Posición: " + estadoActual)
if((estadoActual in parametros['estadoAceptacion']) and (len(pila) == 0)):
    print("Aceptado") 
else:
    print("Rechazado")