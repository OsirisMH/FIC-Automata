const fs = require('fs');

// Importación del archivo de configuración
const config = require('./config.json');

// Lectura y desestructuración de la cadena
const [ ...cadena ] = fs.readFileSync('./cadena.txt', 'utf8');

// Declaración e inicialización de los estado(s) de aceptación
const estadoAceptacion = config.F;

// Declaración e inicialización del estado inicial
let estado = config.q[0];

// Declaración e inicialización de la función de transición
const funcion = config.d;

// Ciclo de lectura de la cadena
cadena.forEach((valor) => {
    // Declaración e inicialización de los posibles estados de acuerdo al valor
    const posibilidades = funcion[estado];
    // Cambio del estado
    estado = posibilidades[valor];
});

// Guardar resultado de acuerdo al estado de aceptación
let resultado = ( estadoAceptacion.includes(estado) ) ? 'Aceptado' : 'No aceptado';

// Impresión de resultados
console.log(resultado)