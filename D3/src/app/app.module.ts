import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BarChartVerticalComponent } from './bar-chart-vertical/bar-chart-vertical.component';
// import { PieChartComponent } from './pie-chart/pie-chart.component';
import { DataService} from './data.service';
import { D3piechartComponent } from './d3piechart/d3piechart.component';

@NgModule({
  declarations: [
    AppComponent,
    BarChartVerticalComponent,
    D3piechartComponent,
    // PieChartComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
