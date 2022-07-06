import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  id: any;
  person: any;
  role : string;
  constructor(public trash: TrashService, public router: Router, public auth: AuthService, private activatedRoute: ActivatedRoute) {

    //  this.activatedRoute.queryParams.subscribe(params => {
    //   let id = params['id'];
    //   console.log("params", params['type']);
    //   console.log(`dwd${id}`);
    //   }); 
   }

  ngOnInit(): void {

  console.log(this.activatedRoute.snapshot.params);
  this.id = this.activatedRoute.snapshot.params['id'];
  this.trash.getuserInfo(this.id).subscribe({
    next: (details:any) => {
      //console.log(details);
      this.person = details;  

      console.log(this.person.user.username);
      if(this.person.is_real === true)
      {
        if(this.person.is_admin === true)
        {
          this.role = 'Administrator';
        }
        else
        {
          this.role = ' Trash Collector';
        }
      }
      else{
        this.role = 'None';
      }
     
      
    }
  });


  }

}
