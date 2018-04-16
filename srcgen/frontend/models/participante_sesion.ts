
import { Sesion } from './sesion';
import { RolParticipanteSesion } from './rol_participante_sesion';

export class ParticipanteSesion {
  Id:	number;  
  Sesion: Sesion;
  RolParticipanteSesion: RolParticipanteSesion;
  Ente:	number;  
}