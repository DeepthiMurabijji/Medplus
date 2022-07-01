import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-arearegister',
  templateUrl: './arearegister.component.html',
  styleUrls: ['./arearegister.component.scss']
})
export class ArearegisterComponent implements OnInit {

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }


  areasData: { area_name: string }[];
  arearegister;

  ngOnInit(): void {

    this.arearegister = {
      areaname : '',
      housename: '',
      address:'',
    };


    this.trash.getAllAreas().subscribe({
      next: (res) => {
        this.areasData = res;
        console.log("registration", res);
      }
    })


  }

  onRegister(){

    this.trash.AreaRegistrations(this.arearegister).subscribe({
        next: (reg) => {
          alert("User" + this.arearegister.username + "registered successfully")
        }, error :(reg) =>{
            console.log('error',reg)
          }
    })
  }

}
