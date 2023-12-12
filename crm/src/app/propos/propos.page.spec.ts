import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ProposPage } from './propos.page';

describe('ProposPage', () => {
  let component: ProposPage;
  let fixture: ComponentFixture<ProposPage>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(ProposPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
