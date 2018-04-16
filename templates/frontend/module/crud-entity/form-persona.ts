
export let FORM_{{entity.name | upper}} = {
    titulo: '{{entity | uppercamelcase}}',
    tipo_formulario: 'mini',
    btn: 'Guardar',
    alertas: true,
    modelo: '{{entity | uppercamelcase}}',
    campos: [{
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'PrimerNombre',
        label: 'Primer nombre*:',
        placeholder: 'Ej. Jose',
        requerido: true,
        tipo: 'text',
    }, {
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'SegundoNombre',
        label: 'Segundo nombre:',
        placeholder: 'Ej. Steven',
        requerido: false,
        tipo: 'text',
    }, {
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'PrimerApellido',
        label: 'Primer apellido*:',
        placeholder: 'Ej. Rodriguez',
        requerido: true,
        tipo: 'text',
    }, {
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'SegundoApellido',
        label: 'Segundo apellido:',
        placeholder: 'Ej. Perez',
        requerido: false,
        tipo: 'text',
    }, {
        etiqueta: 'mat-date',
        claseGrid: 'col-6',
        valor: new Date('Tue Mar 13 2018 00:00:00 GMT-0500 (-05)'),
        nombre: 'FechaNacimiento',
        label: 'Fecha de nacimiento*:',
        placeholder: 'Ej. 01/01/2010',
        requerido: true,
        tipo: 'date',
    }, {
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'Usuario',
        label: 'Usuario:',
        placeholder: 'Ej. Steven',
        requerido: false,
        tipo: 'text',
    }, {
        etiqueta: 'input',
        claseGrid: 'col-6',
        nombre: 'Foto',
        label: 'Foto:',
        placeholder: 'Ej. Steven',
        requerido: false,
        tipo: 'text',
    }, {
        claseGrid: 'col-6',
        etiqueta: 'select',
        nombre: 'Genero',
        label: 'Genero*:',
        requerido: true,
        entrelazado: false,
        opciones: [],
    },
],
}
