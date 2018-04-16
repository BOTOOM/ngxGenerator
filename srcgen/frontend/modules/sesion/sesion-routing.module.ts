import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SesionComponent } from './sesion.component';
import { ListSesionComponent } from './list-sesion/list-sesion.component';
import { CrudSesionComponent } from './crud-sesion/crud-sesion.component';



const routes: Routes = [{
  path: '',
  component: SesionComponent,
  children: [{
    path: 'list-sesion',
    component: ListSesionComponent,
  }, {
    path: 'crud-sesion',
    component: CrudSesionComponent,
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

export class SesionRoutingModule { }

export const routedComponents = [
  SesionComponent,
  ListSesionComponent,
  CrudSesionComponent,
];
