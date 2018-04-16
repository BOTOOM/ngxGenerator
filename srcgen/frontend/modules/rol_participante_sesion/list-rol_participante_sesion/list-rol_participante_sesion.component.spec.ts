/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { CrudRolParticipanteSesionComponent } from './crud-rol_participante_sesion.component';

describe('CrudRolParticipanteSesionComponent', () => {
  let component: CrudRolParticipanteSesionComponent;
  let fixture: ComponentFixture<CrudRolParticipanteSesionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CrudRolParticipanteSesionComponent ],
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CrudRolParticipanteSesionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});