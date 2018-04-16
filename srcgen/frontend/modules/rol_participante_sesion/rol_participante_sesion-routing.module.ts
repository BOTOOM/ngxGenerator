import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { RolParticipanteSesionComponent } from './rol_participante_sesion.component';
import { ListRolParticipanteSesionComponent } from './list-rol_participante_sesion/list-rol_participante_sesion.component';
import { CrudRolParticipanteSesionComponent } from './crud-rol_participante_sesion/crud-rol_participante_sesion.component';



const routes: Routes = [{
  path: '',
  component: RolParticipanteSesionComponent,
  children: [{
    path: 'list-rol_participante_sesion',
    component: ListRolParticipanteSesionComponent,
  }, {
    path: 'crud-rol_participante_sesion',
    component: CrudRolParticipanteSesionComponent,
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

export class RolParticipanteSesionRoutingModule { }

export const routedComponents = [
  RolParticipanteSesionComponent,
  ListRolParticipanteSesionComponent,
  CrudRolParticipanteSesionComponent,
];
