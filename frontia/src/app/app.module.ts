import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { NgForm } from '@angular/forms';
import { FormsModule }   from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { EnviarDatosComponent } from './components/enviar-datos/enviar-datos.component';

@NgModule({
  declarations: [
    AppComponent,
    EnviarDatosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
