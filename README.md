# Generardor de proyectos en Base una definición gramatical simple

se nececitan las siguientes librerias de python:
- tkinter
- textx
- jinja2

_**es necesario python 3**_

/*
  Entity DSL grammar.
*/

EntityModel:


    'project name' name = ID

    types*=SimpleType       // At the beginning of model we can define
                            // zero or more simple types.
    entities+=Entity        // Each model has one or more entities.
;

Entity:


    'entity' name=ID '{'
        properties+=Property // Each entity has one or more properties.
    '}'
;

Property:


    name=ID ':' type=[Type] (array=Array)?  // type is a reference to Type instance.
                                // There are two built-in simple types
                                // registered on meta-model in entity_test.py
;


Type:


    SimpleType | Entity  // Type can be SimpleType or Entity
;

Array:


    '[]' 
;

SimpleType:


    'type' name=ID  // Define types recomended.
                    //type integer
                    //type string   
                    //type bool
                    //type time
;


// Special rule for comments. Comments start with //
Comment:
    /\/\/.*$/
;


#Example

Sesiones project in file "entity.ent":

    project name sesiones

    entity info_basica  {
      id                :integer
      Nombres            :string[]
      Descripcion       :string
      Codigo_Abreviacion :string
      tipo_sesion       :tipo_sesion[]
    }

    entity tipo_sesion  {
      id                :integer
      Nombre            :string
      Descripcion       :string
      Codigo_Abreviacion :string
      Activo            :bool
      Numero_Orden       :integer
    }
    
    
Usage:

Pass file in command

      python main.py entity.ent

pass file selecting folder

      python main.py

