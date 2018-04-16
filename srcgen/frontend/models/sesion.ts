
import { TipoSesion } from './tipo_sesion';

export class Sesion {
  Id:	number;  
  Descripcion:	string;  
  Fechacreacion:	Date;  
  Fechamodificacion:	Date;  
  Fechainicio:	Date;  
  Fechafin:	Date;  
  Periodo:	number;  
  Recurrente:	boolean;  
  NumeroRecurrencias:	number;  
  TipoSesion: TipoSesion;
}