import { Component, OnInit } from '@angular/core';
import { Router , ActivatedRoute} from '@angular/router';
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
  id : string;  

  constructor(public trash: TrashService, public router: Router, public auth: AuthService , private activatedRoute: ActivatedRoute) { 


    // this.activatedRoute.queryParams.subscribe(params => {
    //   console.log("params", params['type'])
    //   });  

  }

  ngOnInit(): void {


    

    this.trash.Administration().subscribe({ 
      next: (details:any) => { 

        // console.log(details); 
        this.collectors= details.collector_serializer;
        this.houselist = details.home;
        console.log("user", this.collectors); 
        console.log("houses:", this.houselist);   

        
        for (let col of this.collectors)
        {
          for (let house of this.houselist)
          {
            if(col.id === house.collector)
            {
              console.log("Name: ",col.user.username);
              console.log("houes: ",house.house_name);
            }
          }
        }


        // for (let col of this.collectors)
        // {
        //   console.log(col.id, );
        // }
      }
    })

  }

}
