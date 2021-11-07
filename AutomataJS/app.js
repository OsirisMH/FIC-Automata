const fs = require('fs');
const { q: estadoInicial, 
        d: funcionTransicion,
        F: estadoAceptacion
} = require('./config.json');
const [ ...cadena ] = fs.readFileSync('./cadena.txt', 'utf8');

try {
    let estado = estadoInicial;

    cadena.forEach( valor => {            
        estado = funcionTransicion?.[estado]?.[valor];
        if ( !estado ) throw new Error('Cadena no compatible');
    });

    let resultado = ( estadoAceptacion.includes(estado) ) ? 'Aceptado' : 'No aceptado';
    console.log(resultado);
}
catch(error) {
    console.log(error.message);
};