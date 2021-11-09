import json #Módulo para trabajar con archivos json
data = open('configuracion.json') #Importar configuracion.json el cual queda almacenado en la variable config
config = json.load(data) 
with open("cadena.txt", 'r') as f: #Importar cadena.txt la cual queda almacenada en la variable datosEntrada
    datosEntrada = f.read()
    
parametros = {} #Se asignan los datos del archivo json al diccionario parametros
parametros['estados'] = config['estados']
parametros['alfabeto'] = config['alfabeto']
for i in config['transiciones']:    
    parametros['transiciones'] = i
parametros['estadoInicial'] = config['estadoInicial']
parametros['estadoAceptacion'] = config['estadoAceptacion']

estadoActual = parametros['estadoInicial'] #estadoActual se inicializa con el estado inicial
posicionCaracter = 0 #Se va incrementando con cada vuelta y se usa en vez de i porque i no deja trabajar con caracteres que no sean números a la hora de asignar un nuevo estado

for i in datosEntrada: #Recorrer datosEntrada la cual contiene la cadena
    
    """
    ASIGNACIÓN DE NUEVO ESTADO ACTUAL:
    Asignar un nuevo estado eligiendo posicion del diccionario parametros['transiciones'] en donde los parametros son:
    [estadoActual]: Elige la llave para ver en cual fila va a escoger posición(si el estado actual es q1 entonces va a ir a la fila q1)
    [str(datosEntrada[posicionCaracter])]: Este parametro da un caracter de la variable que contiene la cadena datosEntrada en la posicion posicionCaracter para escoger un estado de la fila indicada en el parametro anterior
    """
    estadoActual = parametros['transiciones'][estadoActual][str(datosEntrada[posicionCaracter])] 
    posicionCaracter +=1 #Se suma una posición para elegir el siguiente caracter de datosEntrada en la siguiente vuelta 
            
if(estadoActual in parametros['estadoAceptacion']): #Si al final estadoActual existe dentro de los estados de aceptación se dice si la cadena es aceptada o no
    print("Aceptado") 
else:
    print("Rechazado")