import { Component, OnInit } from '@angular/core';
import { LocalDataSource } from 'ng2-smart-table';
import { SesionesService } from '../../../@core/data/sesiones.service';
import { ToasterService, ToasterConfig, Toast, BodyOutputType } from 'angular2-toaster';
import Swal from 'sweetalert2';
import 'style-loader!angular2-toaster/toaster.css';

@Component({
  selector: 'ngx-list-sesion',
  templateUrl: './list-sesion.component.html',
  styleUrls: ['./list-sesion.component.scss'],
  })
export class ListSesionComponent implements OnInit {
  uid: number;
  cambiotab: boolean = false;
  config: ToasterConfig;
  settings = {
    add: {
      addButtonContent: '<i class="nb-plus"></i>',
      createButtonContent: '<i class="nb-checkmark"></i>',
      cancelButtonContent: '<i class="nb-close"></i>',
    },
    edit: {
      editButtonContent: '<i class="nb-edit"></i>',
      saveButtonContent: '<i class="nb-checkmark"></i>',
      cancelButtonContent: '<i class="nb-close"></i>',
    },
    delete: {
      deleteButtonContent: '<i class="nb-trash"></i>',
      confirmDelete: true,
    },
    mode: 'external',
    columns: {
      Id: {
        title: 'Id',
        // type: 'number;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Descripcion: {
        title: 'Descripcion',
        // type: 'string;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Fechacreacion: {
        title: 'Fechacreacion',
        // type: 'Date;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Fechamodificacion: {
        title: 'Fechamodificacion',
        // type: 'Date;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Fechainicio: {
        title: 'Fechainicio',
        // type: 'Date;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Fechafin: {
        title: 'Fechafin',
        // type: 'Date;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Periodo: {
        title: 'Periodo',
        // type: 'number;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      Recurrente: {
        title: 'Recurrente',
        // type: 'boolean;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      NumeroRecurrencias: {
        title: 'NumeroRecurrencias',
        // type: 'number;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
      TipoSesion: {
        title: 'TipoSesion',
        // type: 'tipo_sesion;',
        valuePrepareFunction: (value) => {
          return value;
        },
      },
    },
  };

  source: LocalDataSource = new LocalDataSource();

  constructor(private sesionesService: SesionesService, private toasterService: ToasterService) {
    this.loadData();
  }

  loadData(): void {
    this.sesionesService.get('sesion/?limit=0').subscribe(res => {
      if (res !== null) {
        const data = <Array<any>>res;
        this.source.load(data);
          }
    });
  }

  ngOnInit() {
  }

  onEdit(event): void {
    this.uid = event.data.Id;
    this.activetab();
  }

  onCreate(event): void {
    this.uid = 0;
    this.activetab();
  }

  onDelete(event): void {
    const opt: any = {
      title: 'Deleting?',
      text: 'Delete Sesion!',
      icon: 'warning',
      buttons: true,
      dangerMode: true,
      showCancelButton: true,
    };
    Swal(opt)
    .then((willDelete) => {

      if (willDelete.value) {
        this.sesionesService.delete('sesion/', event.data).subscribe(res => {
          if (res !== null) {
            this.loadData();
            this.showToast('info', 'deleted', 'Sesion deleted');
            }
         });
      }
    });
  }

  activetab(): void {
    this.cambiotab = !this.cambiotab;
  }

  selectTab(event): void {
    if (event.tabTitle === 'Lista') {
      this.cambiotab = false;
    } else {
      this.cambiotab = true;
    }
  }

  onChange(event) {
    if (event) {
      this.loadData();
      this.cambiotab = !this.cambiotab;
    }
  }


  itemselec(event): void {
    // console.log("afssaf");
  }

  private showToast(type: string, title: string, body: string) {
    this.config = new ToasterConfig({
      // 'toast-top-full-width', 'toast-bottom-full-width', 'toast-top-left', 'toast-top-center'
      positionClass: 'toast-top-center',
      timeout: 5000,  // ms
      newestOnTop: true,
      tapToDismiss: false, // hide on click
      preventDuplicates: true,
      animation: 'slideDown', // 'fade', 'flyLeft', 'flyRight', 'slideDown', 'slideUp'
      limit: 5,
    });
    const toast: Toast = {
      type: type, // 'default', 'info', 'success', 'warning', 'error'
      title: title,
      body: body,
      showCloseButton: true,
      bodyOutputType: BodyOutputType.TrustedHtml,
    };
    this.toasterService.popAsync(toast);
  }

}