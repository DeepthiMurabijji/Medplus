import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';


@Component({
  selector: 'app-permisions',
  templateUrl: './permisions.component.html',
  styleUrls: ['./permisions.component.scss']
})
export class PermisionsComponent implements OnInit {

  collectors : any;
  houselist : any;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.trash.Administration().subscribe({ 
      next: (details:any) => { 

        // console.log(details); 
        this.collectors= details.collector_serializer;
        this.houselist = details.home;

        console.log("user", this.collectors); 
        console.log("houses:", this.houselist);   

        
        // for (let col of this.collectors)
        // {
        //   for (let house of this.houselist)
        //   {
        //     if(col.area.id === house.area)
        //     {
        //       console.log("area: ",col.area.area_name)
        //       console.log("houes: ",house.house_name)
        //     }
        //   }
        // }


        for (let col of this.collectors)
        {
          console.log(col.user.username, col.is_real);
        }
      }
    })

  }

}
