// ? Importaciones externas
const fs = require('fs');
require('colors');

// ? Importaciones internas
const { q: estadoInicial, 
        d: funcionTransicion,
        F: estadoAceptacion
} = require('./config-pila.json');
const [ ...cadena ] = fs.readFileSync('./cadena.txt', 'utf8');

// * Agregar principio y final a la cadena
cadena.unshift(null);
cadena.push(null);

// * Pila 
let pila = [];
let estado = estadoInicial;

const getDefinition = ( input ) => {
    let definition = []; 
    
    if ( input ){
        definition = funcionTransicion?.[estado]?.[input];
    }
    else {
        definition = funcionTransicion?.[estado]?.e;
    }

    if ( definition ){
        return definition
    }
    else{
        throw new Error('Transición no definida | No aceptado');
    }
}

const stackActions = ( definition ) => {
    // * Pop
    if ( definition[0] !== 'e' ){
        if ( definition[0] === pila[pila.length - 1] ) {
            pila.pop();
        }
        else {
            throw new Error('Transición no definida | No aceptado');
        }
    }
    // * Push
    else if ( definition[1] !== 'e' ){
        pila.push(definition[1]);
    }

    return definition[2];
}

const isAccepted = ( state ) => {
    if ( estadoAceptacion.includes(state) ){
        console.log('Aceptado'.brightGreen);
    }
}

try {    

    cadena.forEach( input => {
        const definition = getDefinition(input);
        estado = stackActions( definition );
    });

    isAccepted( estado );
}
catch(error) {
    console.log(error.message.red);
};