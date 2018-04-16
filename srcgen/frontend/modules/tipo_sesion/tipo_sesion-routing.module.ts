import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TipoSesionComponent } from './tipo_sesion.component';
import { ListTipoSesionComponent } from './list-tipo_sesion/list-tipo_sesion.component';
import { CrudTipoSesionComponent } from './crud-tipo_sesion/crud-tipo_sesion.component';



const routes: Routes = [{
  path: '',
  component: TipoSesionComponent,
  children: [{
    path: 'list-tipo_sesion',
    component: ListTipoSesionComponent,
  }, {
    path: 'crud-tipo_sesion',
    component: CrudTipoSesionComponent,
  }],
}];

@NgModule({
  imports: [
      RouterModule.forChild(routes),
  ],
  exports: [
      RouterModule,
  ],
})

export class TipoSesionRoutingModule { }

export const routedComponents = [
  TipoSesionComponent,
  ListTipoSesionComponent,
  CrudTipoSesionComponent,
];
