import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { InscriptionPageRoutingModule } from './inscription-routing.module';

import { InscriptionPage } from './inscription.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    InscriptionPageRoutingModule
  ],
  declarations: [InscriptionPage]
})
export class InscriptionPageModule {
  // email: string;
  // motDePasse: string;
  // telephone: string;

  // soumettre() {
  //   console.log('E-mail:', this.email);
  //   console.log('Mot de passe:', this.motDePasse);
  //   console.log('Téléphone:', this.telephone);
    // Ajoutez votre logique de traitement d'inscription ici
  
}
