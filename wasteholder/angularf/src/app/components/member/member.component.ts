import { Component, Input, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import { FormBuilder, FormGroup, FormControl,FormArray, Validators} from '@angular/forms';

@Component({
  selector: 'app-member',
  templateUrl: './member.component.html',
  styleUrls: ['./member.component.scss']
})
export class MemberComponent implements OnInit {
  // @Input()
  usr :any;
  member : any;
  houses :any;
  form: FormGroup;
  constructor(public trash: TrashService, public router: Router, 
    public auth: AuthService, private activatedRoute: ActivatedRoute, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.usr = JSON.parse(localStorage.getItem('user'));
    // console.log("hey this is user", this.usr);

    this.member = this.usr.user.username;

    this.trash.getMemberInfo(this.member).subscribe({
      next: (result: any) => {
        // console.log(result);
        this.houses = result;
      }
    })

    this.form = this.formBuilder.group({
      checkArray: this.formBuilder.array([], [Validators.required]),
    })


   
    
  }

  onCheckboxChange(e) {
    const checkArray: FormArray = this.form.get('checkArray') as FormArray;
    if (e.target.checked) {
      checkArray.push(new FormControl(e.target.value));
    } else {
      let i: number = 0;
      checkArray.controls.forEach((item: FormControl) => {
        if (item.value == e.target.value) {
          checkArray.removeAt(i);
          return;
        }
        i++;
      });
    }
  }

  onUpdate() {
    let length = this.form.value.checkArray.length;
    let array = this.form.value.checkArray;
    if (length < 1) {
      alert('Please select atleast one checkbox');
    }
    // else if(length ===3)
    // {
    //   alert('Cleaning of all houses is done for today');
    // }
    else{
      // console.log("length: ",this.form.value.checkArray.length )
      // console.log(array);
      alert('Cleaning of all houses is done for today');
    
      this.trash.postMemberHouses(array , this.member).subscribe({
        next: (housename) => {
          // console.log(housename);
          alert("changes are saved");
          window.location.reload();
        }, error :(err) =>{
            console.log('error',err)
          }
      })
    }
  }
}
