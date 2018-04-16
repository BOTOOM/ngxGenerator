import { RelacionSesionesRoutingModule, routedComponents } from './relacion_sesiones-routing.module';
import { NgModule } from '@angular/core';
import { ThemeModule } from '../../@theme/theme.module';
import { SesionesService } from '../../@core/data/sesiones.service';
import { SmartTableService } from '../../@core/data/smart-table.service';
import { Ng2SmartTableModule } from 'ng2-smart-table';
import { ToasterModule } from 'angular2-toaster';

@NgModule({
  imports: [
    ThemeModule,
    RelacionSesionesRoutingModule,
    Ng2SmartTableModule,
    ToasterModule,
  ],
  declarations: [
    ...routedComponents,
  ],
  providers: [
    SesionesService,
    SmartTableService,
  ],
})
export class RelacionSesionesModule { }
