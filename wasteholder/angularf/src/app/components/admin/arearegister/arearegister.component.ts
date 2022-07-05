import { Component, OnInit } from '@angular/core';
import { Router ,  ActivatedRoute} from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import { FormBuilder, FormGroup, FormControl} from '@angular/forms';


@Component({
  selector: 'app-arearegister',
  templateUrl: './arearegister.component.html',
  styleUrls: ['./arearegister.component.scss']
})
export class ArearegisterComponent implements OnInit {

  form: FormGroup;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService, private formBuilder: FormBuilder,
    private route: ActivatedRoute,) { }


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

  areaform = new FormGroup({
    areaname : new FormControl(''),
    housename: new FormControl(''),
    address:new FormControl(''),
  });

  onRegister(){

    console.log(this.areaform.value);

    this.trash.AreaRegistrations(this.areaform.value).subscribe({
        next: (reg) => {
          console.log(reg);
          alert("registered successfully")
        }, error :(reg) =>{
            console.log('error',reg)
          }
    })
  }

}
