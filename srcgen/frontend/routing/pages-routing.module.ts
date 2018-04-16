import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardComponent } from './dashboard/dashboard.component';

const routes: Routes = [{
  path: '',
  component: PagesComponent,
  children: [
  {
    path: 'dashboard',
    component: DashboardComponent,
  }, 
  {
    path: 'participante_sesion',
    loadChildren: './participante_sesion/participante_sesion.module#ParticipanteSesionModule',
  },
  {
    path: 'sesion',
    loadChildren: './sesion/sesion.module#SesionModule',
  },
  {
    path: 'tipo_sesion',
    loadChildren: './tipo_sesion/tipo_sesion.module#TipoSesionModule',
  },
  {
    path: 'relacion_sesiones',
    loadChildren: './relacion_sesiones/relacion_sesiones.module#RelacionSesionesModule',
  },
  {
    path: 'rol_participante_sesion',
    loadChildren: './rol_participante_sesion/rol_participante_sesion.module#RolParticipanteSesionModule',
  },
 
  {
    path: '',
    redirectTo: 'dashboard',
    pathMatch: 'full',
  }],
}];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule {
}