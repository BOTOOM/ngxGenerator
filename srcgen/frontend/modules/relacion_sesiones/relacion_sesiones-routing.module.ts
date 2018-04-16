import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RelacionSesionesComponent } from './relacion_sesiones.component';
import { ListRelacionSesionesComponent } from './list-relacion_sesiones/list-relacion_sesiones.component';
import { CrudRelacionSesionesComponent } from './crud-relacion_sesiones/crud-relacion_sesiones.component';



const routes: Routes = [{
  path: '',
  component: RelacionSesionesComponent,
  children: [{
    path: 'list-relacion_sesiones',
    component: ListRelacionSesionesComponent,
  }, {
    path: 'crud-relacion_sesiones',
    component: CrudRelacionSesionesComponent,
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

export class RelacionSesionesRoutingModule { }

export const routedComponents = [
  RelacionSesionesComponent,
  ListRelacionSesionesComponent,
  CrudRelacionSesionesComponent,
];
