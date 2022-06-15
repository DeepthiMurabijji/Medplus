import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
// import for typescript....
import {FormsModule} from '@angular/forms';
/// end 
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
