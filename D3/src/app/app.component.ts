import { Component, OnInit  } from '@angular/core';
import { IData } from './data.interface';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'D3';

  bardata: {name: string, series: { name: string, value: number }[] }[];
  barColor = ['#a9ce97', '#a5b5de'];
  domain = [100, 1000];



  constructor() {
    this.bardata = [
      {
        name: 'Row1',
        series: [
          {name: 'Bar1', value: 150},
          {name: 'Bar2', value: 200}
        ],
      },
      {
        name: 'Row2',
        series: [
          {name: 'Bar1', value: 300},
          {name: 'Bar2', value: 400}
        ],
      },
      {
        name: 'Row3',
        series: [
          {name: 'Bar1', value: 500},
          {name: 'Bar2', value: 1000}
        ],
      }
    ];
  }
  data: SimpleDataModel[] = [
    {
      name: "text1",
      value: "95"
    },
    {
      name: "text1",
      value: "4"
    },
    {
      name: "text3",
      value: "1"
    }
  ];



}

export interface SimpleDataModel {
  name: string;
  value: string;
  color?: string;
}

