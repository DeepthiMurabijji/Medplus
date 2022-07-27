import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BarChartVerticalComponent } from './bar-chart-vertical/bar-chart-vertical.component';

@NgModule({
  declarations: [
    AppComponent,
    BarChartVerticalComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
