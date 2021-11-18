import json 
data = open('Config.json')
config = json.load(data) 
with open("Cadena.txt", 'r') as f:
    datosEntrada = f.read()
    
parametros = {}
parametros['estados'] = config['estados']
parametros['alfabeto'] = config['alfabeto']
for i in config['transiciones']:    
    parametros['transiciones'] = i
parametros['estadoInicial'] = config['estadoInicial']
parametros['direccionInicial'] = config['direccionInicial']
parametros['direccionAceptacion'] = config['direccionAceptacion']
parametros['estadoAceptacion'] = config['estadoAceptacion']

estadoActual = parametros['estadoInicial'] 
direccionAnterior = parametros['direccionInicial']
posicionCaracter = 0

if(parametros['direccionInicial'] == 'L'):
    datosEntrada = datosEntrada[::-1]
    
print("CADENA INICIAL: " + datosEntrada)
print("ESTADO INCIAL: " +  estadoActual + "\n")

for i in datosEntrada:
    direccion = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][1]
    if(direccion != direccionAnterior):
        datosEntrada = datosEntrada[::-1]
    direccionAnterior = direccion
    estadoActual = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][0]
     
    print("Posicion Caracter: " + str(posicionCaracter))   
    print("Direccion: " + direccion)
    print("Cadena: " + datosEntrada)
    print("Caracter: " + datosEntrada[posicionCaracter])
    print("Estado: " + estadoActual + "\n")
    
    posicionCaracter +=1 
    if(posicionCaracter > len(datosEntrada)):
        break
        
print("Posicion: " + estadoActual)
if((estadoActual in parametros['estadoAceptacion']) and (direccion in parametros['direccionAceptacion'])):
    print("Aceptado") 
else:
    print("Rechazado")