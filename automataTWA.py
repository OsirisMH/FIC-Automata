import json 
data = open('ConfiguracionTWA.json')
config = json.load(data) 
with open("CadenaTWA.txt", 'r') as f:
    datosEntrada = f.read()

parametros = {}
parametros['estados'] = config['estados']
parametros['alfabeto'] = config['alfabeto']
for i in config['transiciones']:
    parametros['transiciones'] = i
parametros['estadoInicial'] = config['estadoInicial']
parametros['estadoAceptacion'] = config['estadoAceptacion']

estadoActual = parametros['estadoInicial']
direccion=""
posicionCaracter = 0
vueltas=0
contador=len(parametros['alfabeto'])-1
longitudDatosEntrada = len(datosEntrada)-1

while vueltas <(longitudDatosEntrada*2)-1:
    
    direccion = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][1]
    estadoActual = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])][0]
    
    if(direccion == parametros['alfabeto'][contador]):
        posicionCaracter = posicionCaracter-1

    print("Posicion Caracter: " + str(posicionCaracter))
    print("Vuelta: ",vueltas)
    print("Direccion: " + direccion)
    print("Cadena: " + datosEntrada)
    print("Caracter: " + datosEntrada[posicionCaracter])
    print("Estado: " + estadoActual + "\n")
    
    if(direccion == parametros['alfabeto'][contador-1]):
        posicionCaracter +=1

    vueltas+=1
  

print("Vueltas totales ",vueltas)
print("Longitud de la cadena ",len(datosEntrada))
if((estadoActual in parametros['estadoAceptacion']) and (vueltas > longitudDatosEntrada)):
    print("Aceptado") 
else:
    print("Rechazado")