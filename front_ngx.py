
import sys
import os
from os import mkdir
from os.path import exists, dirname, join
from shutil import copytree
import jinja2
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export
from gen_filters import filters

class SimpleType(object):
    """
    We are registering user SimpleType class to support
    simple types (integer, string) in our entity models
    Thus, user doesn't need to provide integer and string
    types in the model but can reference them in attribute types nevertheless.
    """
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name

class front_ngx:
    this_folder = os.getcwd()   #location user execution
    debug=False
    overwrite=False #knows if projects mode is overwrite
    gen_folder=dirname(__file__)
    type_builtins = {
            'integer': SimpleType(None, 'integer'),
            'string':  SimpleType(None, 'string'),
            'time':  SimpleType(None, 'time'),
            'bool': SimpleType(None, 'bool'),
            'float': SimpleType(None, 'float')
    }
    entity_mm = metamodel_from_file(join(gen_folder , 'entity.tx'),
                                    classes=[SimpleType],
                                    builtins=type_builtins,
                                    debug=debug)

    filter = filters()  #filters methods
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(gen_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    
    def __init__(self,entity_file, project_folder):
        # Build Model from <model>.ent file
        self.entity_model = self.entity_mm.model_from_file(join(self.this_folder, entity_file))        

        # Register filter for mapping Entity type names to angular type names.
        
        self.jinja_env.filters['uppercamelcase'] = self.filter.upper_camel_case
        self.jinja_env.filters['lowercamelcase'] = self.filter.lower_camel_case
        self.jinja_env.filters['kebabcase'] = self.filter.kebab_case
        self.jinja_env.filters['spacecase'] = self.filter.space_case

        self.jinja_env.filters['angulartype'] = self.angulartype
        self.jinja_env.tests['entity'] = self.is_entity
        self.jinja_env.filters['formtype'] = self.formtype        
        self.jinja_env.filters['htmltype'] = self.htmltype

        self.gen_body(project_folder)    
        self.gen_models()
        self.gen_i18n()
        self.gen_conf()
        self.gen_service()
        self.gen_routing()
        self.gen_module()

        print("project generated, find it in "+ self.this_folder)


        
        


    def gen_body(self, project_folder):
        srcgen_folder_project = join(self.this_folder, project_folder)
        if not exists(srcgen_folder_project):
            copytree(self.gen_folder + '/templates/project_template', srcgen_folder_project)
        else:
            print(" ------ the directory already exists, the components are generated within this -----")
            self.overwrite=True
        self.this_folder = self.this_folder + "/" + project_folder  
        
    def gen_models(self):

        if self.overwrite:
            if raw_input("Do you want overwrite models?: \n [y/n]: ").lower() != "y":
                return

        srcgen_folder_frontend_model = self.make_dir('src/app/@core/data/models') 
        # Models
        template = self.jinja_env.get_template('templates/frontend/models/entity.ts.template')
        for entity in self.entity_model.entities:
            with open(join(srcgen_folder_frontend_model, "%s.ts" % entity.name.lower()), 'w') as f:
                f.write(template.render(entity=entity, orderTypeEntity=self.orderTypeEntity))

    def gen_i18n(self):

        if self.overwrite:
            if raw_input("Do you want overwrite i18n?: \n [y/n]: ").lower() != "y":
                return

        srcgen_folder_frontend_translate = self.make_dir('src/assets/i18n')
        template = self.jinja_env.get_template('/templates/frontend/translate/lang.json.template')
        with open(join(srcgen_folder_frontend_translate, "es.json"), 'w') as f:
                f.write(template.render(entity_model=self.entity_model,  listAllAtributes=self.listAllAtributes))
        with open(join(srcgen_folder_frontend_translate, "en.json"), 'w') as f:
                f.write(template.render(entity_model=self.entity_model, listAllAtributes=self.listAllAtributes))
      
    def gen_conf(self):

        if self.overwrite:
            if raw_input("Do you want overwrite conf?: \n [y/n]: ").lower() != "y":
                return

        srcgen_folder_frontend_conf = self.make_dir('src/app')
        template = self.jinja_env.get_template('templates/frontend/conf/app-config.ts.template')
        with open(join(srcgen_folder_frontend_conf, "app-config.ts"), 'w') as f:
                f.write(template.render(entity_model=self.entity_model))

    def gen_service(self):

        if self.overwrite:
            if raw_input("Do you want overwrite service?: \n [y/n]: ").lower() != "y":
                return

        srcgen_folder_frontend_services = self.make_dir('src/app/@core/data')
        template = self.jinja_env.get_template('templates/frontend/services/entity.service.ts.template')
        with open(join(srcgen_folder_frontend_services, "%s.service.ts" % self.entity_model.name.lower()), 'w') as f:
            f.write(template.render(entity=self.entity_model))
    
    def gen_routing(self):

        if self.overwrite:
            if raw_input("Do you want overwrite routing?: \n [y/n]: ").lower() != "y":
                return

        srcgen_folder_frontend_routing = self.make_dir('src/app/pages')
        template = self.jinja_env.get_template('templates/frontend/routing/entity-pages-menu.ts.template')
        with open(join(srcgen_folder_frontend_routing, "pages-menu.ts"), 'w') as f:
                f.write(template.render(entity_model=self.entity_model))
                
        template = self.jinja_env.get_template('templates/frontend/routing/entity-pages-routing.module.ts.template')
        with open(join(srcgen_folder_frontend_routing, "pages-routing.module.ts"), 'w') as f:
                f.write(template.render(entity_model=self.entity_model))
    
    def gen_module(self):

        if self.overwrite:
            if raw_input("Do you want overwrite modules?: \n [y/n]: ").lower() != "y":
                return


        template_module = self.jinja_env.get_template('templates/frontend/module/entity.module.ts.template')
        template_component = self.jinja_env.get_template('templates/frontend/module/entity.component.ts.template')
        template_routing_module = self.jinja_env.get_template('templates/frontend/module/entity-routing.module.ts.template')
        
        template_crud_scss = self.jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.scss.template')
        template_crud_spec = self.jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.spec.ts.template')
        template_crud_html = self.jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.html.template')
        template_crud_component = self.jinja_env.get_template('templates/frontend/module/crud-entity/crud-entity.component.ts.template')
        template_crud_form = self.jinja_env.get_template('templates/frontend/module/crud-entity/form-entity.ts.template')

        template_list_scss = self.jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.scss.template')
        template_list_spec = self.jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.spec.ts.template')
        template_list_html = self.jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.html.template')
        template_list_component = self.jinja_env.get_template('templates/frontend/module/list-entity/list-entity.component.ts.template')

        for entity in self.entity_model.entities:

            #module
            folder_frontend_module = self.make_dir('src/app/pages/%s' % entity.name.lower())
            # entity.module.ts
            with open(join(folder_frontend_module, "%s.module.ts" % entity.name.lower()), 'w') as f:
                f.write(template_module.render(entity=entity,entity_model=self.entity_model))
            # entity.component.ts
            with open(join(folder_frontend_module, "%s.component.ts" % entity.name.lower()), 'w') as f:
                f.write(template_component.render(entity=entity)) 
            # entity.routing.ts
            with open(join(folder_frontend_module, "%s-routing.module.ts" % entity.name.lower()), 'w') as f:
                f.write(template_routing_module.render(entity=entity)) 

            #crud
            folder_frontend_module_crud = self.make_dir('src/app/pages/%s' %entity.name.lower()+'/crud-%s' %  entity.name.lower() )
            #scss crud
            with open(join(folder_frontend_module_crud, "crud-%s.component.scss" % entity.name.lower()), 'w') as f:
                f.write(template_crud_scss.render(entity=entity)) 
            #spec crud
            with open(join(folder_frontend_module_crud, "crud-%s.component.spec.ts" % entity.name.lower()), 'w') as f:
                f.write(template_crud_spec.render(entity=entity)) 
            #html crud
            with open(join(folder_frontend_module_crud, "crud-%s.component.html" % entity.name.lower()), 'w') as f:
                f.write(template_crud_html.render(entity=entity)) 
            #form crud
            with open(join(folder_frontend_module_crud, "form-%s.ts" % entity.name.lower()), 'w') as f:
                f.write(template_crud_form.render(entity=entity))       
            #component crud
            with open(join(folder_frontend_module_crud, "crud-%s.component.ts" % entity.name.lower()), 'w') as f:
                f.write(template_crud_component.render(entity=entity,entity_model=self.entity_model, orderTypeEntity=self.orderTypeEntity))   

            #list            
            folder_frontend_module_list = self.make_dir('src/app/pages/%s' %entity.name.lower()+'/list-%s' %  entity.name.lower() )
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
                f.write(template_list_component.render(entity=entity, entity_model=self.entity_model))


    

    def make_dir(self, dir):
        # Create output folder for backend
        srcgen_folder = join(self.this_folder, dir)
        
        if not exists(srcgen_folder):
            mkdir(srcgen_folder)
        return srcgen_folder        
        
    def is_entity(self,n):
        """
        Test to prove if some type is an entity
        """
        if n.type in self.entity_model.entities:
            return True
        else:
            return False

    def angulartype(self,s):
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

    def formtype(self,s):
        if s.array:
            return 'selectmultiple'
        if self.is_entity(s):
            return 'select'
        return {
                'integer': 'input',
                'string': 'input',
                'bool': 'checkbox',
                'time': 'mat-date',
                'float': 'input'
        }.get(s.type.name, s.type.name)

    def htmltype(self,s):
        return {
                'integer': 'number',
                'string': 'text',
                'bool': 'checkbox',
                'time': 'date',
                'float': 'number'
        }.get(s.name, self.filter.upper_camel_case(s.name))

    def orderTypeEntity(self,properties):
        types=[]
        for p in properties:
            if self.is_entity(p):
                if p.type not in types:
                    types.append(p.type)
        return types

    def listAllAtributes(self,entity_model):
        list=[]
        for entity in entity_model.entities:
            if entity.name not in list:
                    list.append(entity.name)
            for p in entity.properties:
                if p.name not in list:
                    list.append(p.name)
        return list





