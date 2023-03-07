import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnviarDatosComponent } from './enviar-datos.component';

describe('EnviarDatosComponent', () => {
  let component: EnviarDatosComponent;
  let fixture: ComponentFixture<EnviarDatosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EnviarDatosComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EnviarDatosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
