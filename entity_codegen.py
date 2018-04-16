"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
import sys
import os
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export


def main(entity,debug=False):

    this_folder = dirname(__file__)

    entity_mm = metamodel_from_file(join(this_folder, 'entity.tx'),
                                     debug=debug)

    # Build Model from <model>.ent file
    entity_model = entity_mm.model_from_file(join(this_folder, entity))

    #print entity_model.entities
    def space_case(n):
        x=n.name.split("_")
        temp = ""
        for t in x :
            temp += t.capitalize()+" "
        return temp[0:-1]

    def upper_camel_case(n):
        x=n.name.split("_")
        temp = ""
        for t in x :
            temp += t.capitalize()
        return temp

    def lower_camel_case(n):
        x=n.name.split("_")
        temp = ""
        temp += x[0].lower()
        for t in x[1:] :
            print temp
            temp += t.capitalize()
        return temp

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in entity_model.entities:
            return True
        else:
            return False

    def beegotype(s):
        """
        Maps type names from PrimitiveType to beego.
        """
        return {
                'integer': 'number',
                'string': 'string',
                'bool': 'bool',
                'boolean':'bool',
                'time': 'Date'
        }.get(s.name, s.name)

    def angulartype(s):
        """
        Maps type names from PrimitiveType to angular.
        """
        return {
                'integer': 'number',
                'string': 'string',
                'bool': 'boolean',
                'time': 'Date',
                'float': 'number'
        }.get(s.name, s.name)

    def orderTypeEntity(properties):
        types=[]
        for p in properties:
            if is_entity(p):
                if p.type not in types:
                    types.append(p.type)
        return types

    
    # Create output folder for backend
    srcgen_folder = join(this_folder, 'srcgen')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    srcgen_folder_backend = join(this_folder, 'srcgen/backend')
    if not exists(srcgen_folder_backend):
        mkdir(srcgen_folder_backend)

    srcgen_folder_controler = join(this_folder, 'srcgen/backend/controllers')
    if not exists(srcgen_folder_controler):
        mkdir(srcgen_folder_controler)

    srcgen_folder_model = join(this_folder, 'srcgen/backend/models')
    if not exists(srcgen_folder_model):
        mkdir(srcgen_folder_model)

    srcgen_folder_router = join(this_folder, 'srcgen/backend/routers')
    if not exists(srcgen_folder_router):
        mkdir(srcgen_folder_router)

    # Create output folder for frontend
    srcgen_folder_frontend = join(this_folder, 'srcgen/frontend')
    if not exists(srcgen_folder_frontend):
        mkdir(srcgen_folder_frontend)

    srcgen_folder_frontend_model = join(this_folder, 'srcgen/frontend/models')
    if not exists(srcgen_folder_frontend_model):
        mkdir(srcgen_folder_frontend_model)

    srcgen_folder_frontend_services = join(this_folder, 'srcgen/frontend/services')
    if not exists(srcgen_folder_frontend_services):
        mkdir(srcgen_folder_frontend_services)

    srcgen_folder_frontend_routing = join(this_folder, 'srcgen/frontend/routing')
    if not exists(srcgen_folder_frontend_routing):
        mkdir(srcgen_folder_frontend_routing)

    srcgen_folder_frontend_modules = join(this_folder, 'srcgen/frontend/modules')
    if not exists(srcgen_folder_frontend_modules):
        mkdir(srcgen_folder_frontend_modules)    

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to beego type names.
    jinja_env.filters['beegotype'] = angulartype
    # Register filter for mapping Entity type names to angular type names.
    jinja_env.filters['angulartype'] = angulartype

    jinja_env.filters['uppercamelcase'] = upper_camel_case

    jinja_env.filters['lowercamelcase'] = lower_camel_case

    jinja_env.filters['spacecase'] = space_case

    jinja_env.tests['entity'] = is_entity

    
    """
    # Load Backend Controllers
    template = jinja_env.get_template('templates/backend/controller.template')

    for entity in entity_model.entities:
        # For each entity generate java file
        with open(jon(srcgen_folder_controler, "%s.go" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load Backend models
    template = jinja_env.get_template('templates/backend/model.template')

    for entity in entity_model.entities:
        with open(join(srcgen_folder_model, "%s.go" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))

    # Load Backend Router
    template = jinja_env.get_template('templates/backend/router.template')
    with open(join(srcgen_folder_router, "router.go"), 'w') as f:
        f.write(template.render(entities=entity_model.entities))

    

    templates = ['edit','new','view']
    for template in templates:
        for entity in entity_model.entities:
            template_ts = jinja_env.get_template("templates/frontend/entity/{template}/entity-{template}.component.ts.template".format(**{'template':template}))
            template_html = jinja_env.get_template("templates/frontend/entity/{template}/entity-{template}.component.html.template".format(**{'template':template}))
            srcgen_folder_frontend_entity = join(this_folder, "srcgen/frontend/{entity}/{entity}-{template}".format(**{'entity':entity.name.lower(),'template':template}))
            if not os.path.exists(srcgen_folder_frontend_entity):
                print "Creando carpeta: {}".format(srcgen_folder_frontend_entity)
                os.makedirs(srcgen_folder_frontend_entity)
            with open(join(srcgen_folder_frontend_entity, "{entity}-{template}.component.ts".format(**{'entity':entity.name.lower(),'template':template})), 'w') as f:
                f.write(template_ts.render(entity=entity))
            with open(join(srcgen_folder_frontend_entity, "{entity}-{template}.component.html".format(**{'entity':entity.name.lower(),'template':template})), 'w') as f:
                f.write(template_html.render(entity=entity))
    """
    # Routing Template
    template = jinja_env.get_template('templates/frontend/routing/entity-pages-menu.ts.template')
    with open(join(srcgen_folder_frontend_routing, "pages-menu.ts"), 'w') as f:
            f.write(template.render(entity_model=entity_model))
    template = jinja_env.get_template('templates/frontend/routing/entity-pages-routing.module.ts.template')
    with open(join(srcgen_folder_frontend_routing, "pages-routing.module.ts"), 'w') as f:
            f.write(template.render(entity_model=entity_model))

    

    # Models
    template = jinja_env.get_template('templates/frontend/models/entity.ts.template')
    for entity in entity_model.entities:
        with open(join(srcgen_folder_frontend_model, "%s.ts" % entity.name.lower()), 'w') as f:
            f.write(template.render(entity=entity, orderTypeEntity=orderTypeEntity))

    #Services Template
    template = jinja_env.get_template('templates/frontend/services/entity.service.ts.template')
    #for entity in entity_model.entities:
    with open(join(srcgen_folder_frontend_services, "%s.service.ts" % entity_model.name.lower()), 'w') as f:
        f.write(template.render(entity=entity_model))


    #modules
    template_module = jinja_env.get_template('templates/frontend/module/entity.module.ts.template')
    template_component = jinja_env.get_template('templates/frontend/module/entity.component.ts.template')
    template_routing_module = jinja_env.get_template('templates/frontend/module/entity-routing.module.ts.template')
    template_crud_scss = jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.scss.template')
    template_crud_spec = jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.spec.ts.template')
    template_crud_html = jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.html.template')

    template_list_scss = jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.scss.template')
    template_list_spec = jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.spec.ts.template')
    template_list_html = jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.html.template')
    template_list_component = jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.ts.template')

    for entity in entity_model.entities:
        folder_frontend_module = join(this_folder, 'srcgen/frontend/modules/%s' % entity.name.lower())
        if not exists(folder_frontend_module):
            mkdir(folder_frontend_module)  
        # entity.module.ts
        with open(join(folder_frontend_module, "%s.module.ts" % entity.name.lower()), 'w') as f:
            f.write(template_module.render(entity=entity,entity_model=entity_model))
        # entity.component.ts
        with open(join(folder_frontend_module, "%s.component.ts" % entity.name.lower()), 'w') as f:
            f.write(template_component.render(entity=entity)) 
        # entity.routing.ts
        with open(join(folder_frontend_module, "%s-routing.module.ts" % entity.name.lower()), 'w') as f:
            f.write(template_routing_module.render(entity=entity)) 
        #crud
        folder_frontend_module_crud = join(this_folder, 'srcgen/frontend/modules/%s' %entity.name.lower()+'/crud-%s' %  entity.name.lower() )
        if not exists(folder_frontend_module_crud):
            mkdir(folder_frontend_module_crud)  
        #scss crud
        with open(join(folder_frontend_module_crud, "crud-%s.component.scss" % entity.name.lower()), 'w') as f:
            f.write(template_crud_scss.render(entity=entity)) 
        #spec crud
        with open(join(folder_frontend_module_crud, "crud-%s.component.spec.ts" % entity.name.lower()), 'w') as f:
            f.write(template_crud_spec.render(entity=entity)) 
        #html crud
        with open(join(folder_frontend_module_crud, "crud-%s.component.html" % entity.name.lower()), 'w') as f:
            f.write(template_crud_html.render(entity=entity)) 
        

        #list
        folder_frontend_module_list = join(this_folder, 'srcgen/frontend/modules/%s' %entity.name.lower()+'/list-%s' %  entity.name.lower() )
        if not exists(folder_frontend_module_list):
            mkdir(folder_frontend_module_list)  
        #scss list
        with open(join(folder_frontend_module_list, "list-%s.component.scss" % entity.name.lower()), 'w') as f:
            f.write(template_list_scss.render(entity=entity)) 
        #spec list
        with open(join(folder_frontend_module_list, "list-%s.component.spec.ts" % entity.name.lower()), 'w') as f:
            f.write(template_list_spec.render(entity=entity)) 
        #html list
        with open(join(folder_frontend_module_list, "list-%s.component.html" % entity.name.lower()), 'w') as f:
            f.write(template_list_html.render(entity=entity))  
        #component list
        with open(join(folder_frontend_module_list, "list-%s.component.ts" % entity.name.lower()), 'w') as f:
            f.write(template_list_component.render(entity=entity, entity_model=entity_model))  

if __name__ == "__main__":
    entity = None
    if len(sys.argv) > 1:
        print "Creando codigo ..."
        entity = sys.argv[1]
        main(entity)
    else:
        print "Debe ingresar el nombre de la entidad con la cual quiere generar el codigo"
        exit(1)
