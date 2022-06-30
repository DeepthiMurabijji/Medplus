import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ArearegisterComponent } from './arearegister.component';

describe('ArearegisterComponent', () => {
  let component: ArearegisterComponent;
  let fixture: ComponentFixture<ArearegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ArearegisterComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ArearegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
