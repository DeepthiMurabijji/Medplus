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
  toggleAdmin: boolean;
  toggleCollector: boolean;
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

    // console.log(this.activatedRoute.snapshot.params);
    this.id = this.activatedRoute.snapshot.params['id'];
    this.trash.getuserInfo(this.id).subscribe({
      next: (details:any) => {
        console.log(details);
        this.person = details;  
        console.log("Here")
        console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
        console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);
        // console.log(this.person.user.username);
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
        this.toggleCollector = this.person.is_real;
        this.toggleAdmin = this.person.is_admin;
        console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
        console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);

        // if(this.toggleCollector !== this.person.is_real || this.toggleAdmin !== this.person.is_admin)
        // {
        //   console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
        //   console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);
        //   if (this.toggleCollector !== this.person.is_real){
        //     this.person.is_real = this.toggleCollector
        //   }
        //   if (this.toggleAdmin !== this.person.is_admin){
        //     this.person.is_admin = this.toggleAdmin
        //   }
        //   console.log("After Changing")
        //   console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
        //   console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);
        //   this.changeCollectorRole();
        // }

        

      }
    });

    // this.toggleCollector = this.person.is_real;
    // this.toggleAdmin = this.person.is_admin;
    

    //   ($('.bootstrap-switch')as any).bootstrapSwitch({
    //     onText: "Yes",
    //     offText: "No"
    // });
    // this.changeBootstrapSwitchValues();
  }

  // @Input() onText = 'Yes';
  // @Input() offText = 'No';

  changeCollectorRole() {
    this.person.is_real = this.toggleCollector;
    this.person.is_admin = this.toggleAdmin;
    console.log("Here also returns");
    console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
    console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);

    this.trash.EditingRole(this.person).subscribe({
      next:(permit) => {
        console.log(permit);
        // this.person.is_real = this.toggleCollector;
        // this.person.is_admin = this.toggleAdmin;
        console.log("Here also");
        // console.log("admin",this.toggleAdmin, "collector", this.toggleCollector);
        // console.log("admin person",this.person.is_admin, "collector person", this.person.is_real);
        console.log(this.person);

      }
    });




  //   console.log("admin", this.toggleAdmin);

  //   if(this.toggleAdmin === false)
  //   {
  //     console.log("admin ");
  //   }
  //   else if(this.toggleAdmin === true)
  //   {
  //     console.log("Not admin");
  //   }
  // }
  // onauth() {
  //   this.trash.EditingRole(this.toggleCollector,this.id).subscribe({
  //     next: (auth) =>{
  //       console.log(auth);
  //     }
  //   });



  //   console.log("collector", this.toggleCollector);
  //   if(this.toggleCollector === false)
  //   {
  //     console.log("Collector ");
  //   }
  //   else if(this.toggleCollector === true)
  //   {
  //     console.log("Not Authenticated");
  //   }
   }
  

}


