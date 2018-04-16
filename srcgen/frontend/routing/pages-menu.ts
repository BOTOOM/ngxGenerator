// import { NbMenuItem } from '@nebular/theme';
import { MenuItem } from './menu-item';

export const MENU_ITEMS: MenuItem[] = [
  {
    title: 'Dashboard',
    icon: 'nb-home',
    link: '/pages/dashboard',
    home: true,
    key: 'dashboard',
  },
  {
    title: 'Participante Sesion',
    icon: 'nb-compose',
    link: '/pages/participante_sesion',
    key: 'participante_sesion',
    children: [
      {
        title: 'Lista Participante Sesion',
        link: '/pages/participante_sesion/list_participante_sesion',
        key: 'lista_participante_sesion',
      },
      {
        title: 'CRUD Participante Sesion',
        link: '/pages/participante_sesion/crud_participante_sesion',
        key: 'crud_participante_sesion',
      },
    ],
  },
  {
    title: 'Sesion',
    icon: 'nb-compose',
    link: '/pages/sesion',
    key: 'sesion',
    children: [
      {
        title: 'Lista Sesion',
        link: '/pages/sesion/list_sesion',
        key: 'lista_sesion',
      },
      {
        title: 'CRUD Sesion',
        link: '/pages/sesion/crud_sesion',
        key: 'crud_sesion',
      },
    ],
  },
  {
    title: 'Tipo Sesion',
    icon: 'nb-compose',
    link: '/pages/tipo_sesion',
    key: 'tipo_sesion',
    children: [
      {
        title: 'Lista Tipo Sesion',
        link: '/pages/tipo_sesion/list_tipo_sesion',
        key: 'lista_tipo_sesion',
      },
      {
        title: 'CRUD Tipo Sesion',
        link: '/pages/tipo_sesion/crud_tipo_sesion',
        key: 'crud_tipo_sesion',
      },
    ],
  },
  {
    title: 'Relacion Sesiones',
    icon: 'nb-compose',
    link: '/pages/relacion_sesiones',
    key: 'relacion_sesiones',
    children: [
      {
        title: 'Lista Relacion Sesiones',
        link: '/pages/relacion_sesiones/list_relacion_sesiones',
        key: 'lista_relacion_sesiones',
      },
      {
        title: 'CRUD Relacion Sesiones',
        link: '/pages/relacion_sesiones/crud_relacion_sesiones',
        key: 'crud_relacion_sesiones',
      },
    ],
  },
  {
    title: 'Rol Participante Sesion',
    icon: 'nb-compose',
    link: '/pages/rol_participante_sesion',
    key: 'rol_participante_sesion',
    children: [
      {
        title: 'Lista Rol Participante Sesion',
        link: '/pages/rol_participante_sesion/list_rol_participante_sesion',
        key: 'lista_rol_participante_sesion',
      },
      {
        title: 'CRUD Rol Participante Sesion',
        link: '/pages/rol_participante_sesion/crud_rol_participante_sesion',
        key: 'crud_rol_participante_sesion',
      },
    ],
  },
];