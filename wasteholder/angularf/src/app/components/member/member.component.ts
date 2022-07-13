import { Component, Input, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import { FormBuilder, FormGroup, FormControl} from '@angular/forms';

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
    public auth: AuthService, private activatedRoute: ActivatedRoute) { }

  ngOnInit(): void {
    this.usr = JSON.parse(localStorage.getItem('user'));
    console.log("hey this is user", this.usr);

    this.member = this.usr.user.username;

    this.trash.getMemberInfo(this.member).subscribe({
      next: (result: any) => {
        console.log(result);
        this.houses = result;
      }
    })

    
  }

  memberform = new FormGroup({
    housesChecked : new FormControl(''),
  })

  onUpdate(): void {
  }
}
