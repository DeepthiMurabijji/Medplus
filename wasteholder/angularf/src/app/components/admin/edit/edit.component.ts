import { Component, OnInit ,Input} from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import { state } from '@angular/animations';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  id: any;
  person: any;
  role : string;
  toggle;
  LightNeeded;
  constructor(public trash: TrashService, public router: Router, public auth: AuthService, private activatedRoute: ActivatedRoute) {

    //  this.activatedRoute.queryParams.subscribe(params => {
    //   let id = params['id'];
    //   console.log("params", params['type']);
    //   console.log(`dwd${id}`);
    //   }); 
   }
  //  changeBootstrapSwitchValues() {
  //   let self = this;
  //       $('.light-needed').on('switchChange.bootstrapSwitch', function (event:any, state:any) {
  //           if (state) {  
  //               console.log('true');
  //               //this.LightNeeded= true;
  //               self.LightNeeded= true;
  //           } else {  
  //               console.log('false');
  //               //this.LightNeeded= false;
  //               self.LightNeeded= false;
  //           };
  //       });
  //   }
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

    if(this.toggle === 'Yes')
    {
      console.log("toggle",true);
    }
    else
    {
      console.log("toggle",false);
    }
    

    //   ($('.bootstrap-switch')as any).bootstrapSwitch({
    //     onText: "Yes",
    //     offText: "No"
    // });
    // this.changeBootstrapSwitchValues();
  }

  @Input() onText = 'Yes';
  @Input() offText = 'No';
  
  

}


