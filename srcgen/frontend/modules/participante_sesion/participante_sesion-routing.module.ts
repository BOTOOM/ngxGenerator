import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ParticipanteSesionComponent } from './participante_sesion.component';
import { ListParticipanteSesionComponent } from './list-participante_sesion/list-participante_sesion.component';
import { CrudParticipanteSesionComponent } from './crud-participante_sesion/crud-participante_sesion.component';



const routes: Routes = [{
  path: '',
  component: ParticipanteSesionComponent,
  children: [{
    path: 'list-participante_sesion',
    component: ListParticipanteSesionComponent,
  }, {
    path: 'crud-participante_sesion',
    component: CrudParticipanteSesionComponent,
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

export class ParticipanteSesionRoutingModule { }

export const routedComponents = [
  ParticipanteSesionComponent,
  ListParticipanteSesionComponent,
  CrudParticipanteSesionComponent,
];
