import { Component, OnInit } from '@angular/core';
import {Chart, registerables} from 'chart.js'
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';


@Component({
  selector: 'app-piechart',
  templateUrl: './piechart.component.html',
  styleUrls: ['./piechart.component.scss']
})
export class PiechartComponent implements OnInit {

  constructor(public trash: TrashService,public auth: AuthService ) { }

  chart : any;
  values : any;
  piedata : any;
  dictionary!:any
  completed : any;
  notcompleted : any;
xValues!:any;
yValues!:any;
maxVal!:any;
  ngOnInit(): void {
    this.chart = document.getElementById('myChart'),
    Chart.register(...registerables)

    this.trash.getPiechartdetails().subscribe({
      next: (data: any) => {  
        console.log("piechart data:", data);
        this.piedata = data;
        this.dictionary = this.piedata.dict
        // console.log(this.dictionary)
        this.xValues = Object.keys(this.dictionary)
        // console.log(this.xValues)
        this.yValues = Object.values(this.dictionary)
        // console.log(this.yValues)
        this.completed = this.piedata.completed
        this.notcompleted = this.piedata.notCompleted
        // console.log(this.notcompleted)





        // console.log("length:",this.xValues.length)
        // FIXME: Trying out n different colcors 
        // let maxVal = 0xFFFFFF; // 16777215
        // let randomNumber = Math.random() * maxVal; 
        // randomNumber = Math.floor(randomNumber);
        // var barColors[i] = randomNumber.toString(16);
        // var barColors = [
        //   // "#b91d47",
        //   // "#00aba9",
        //   // "#2b5797",
        //   // "#e8c3b9",
        //   // Math.floor(Math.random()*16777225).toString(16),
        //   // Math.floor(Math.random()*16777235).toString(4),
        //   // Math.floor(Math.random()*16777215).toString(23),
        //   maxVal = 0xFFFFFF; // 16777215
        //   let randomNumber = Math.random() * maxVal; 
        //   randomNumber = Math.floor(randomNumber);
        //   let randColor = randomNumber.toString(16);
        // ]
        const randColor = () =>  {
          return "#" + Math.floor(Math.random()*16777215).toString(16).padStart(6, '0').toUpperCase();
      }
      var pieColors=[]
      for(var i=0;i<this.xValues.length;i++){
        let x= randColor();
        pieColors[i]=x;
      }
      // console.log("barcolors",barColors);
      const myChart=new Chart("myChart", {
        type: "pie",
        data: {
          labels: this.xValues,
          datasets: [{
            label:"Total no.of Houses",
            backgroundColor: pieColors,
            data: this.yValues
          }]
        },
        options: {
          maintainAspectRatio:false,
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
      
      })


      var barColors = [
        "#990033",
      ]
    
    const barchart=new Chart("barchart", {
      type: "bar",
      data: {
        labels: this.xValues,
        
        datasets: [
          
          {
            label: "Houses Not Completed",
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor:'rgb(255, 99, 132)',
            borderWidth: 1,
            data : this.notcompleted
          },
          {
            label:"Houses Completed",
            backgroundColor: 'rgba(255, 205, 86, 0.2)',
            borderColor:'rgb(255, 205, 86)',
            borderWidth: 1,
            data: this.completed,
          },
          {
            label: "Total no.of Houses",
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgb(153, 102, 255)',
            borderWidth: 1,
            data : this.yValues
          }
        ]
      },
      options: {
        maintainAspectRatio:false,
          responsive: true,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
    
    }
    )
      },error : (err) =>{
        console.log('piechart unsuccessfull',err);
      }
    })

  }

}
