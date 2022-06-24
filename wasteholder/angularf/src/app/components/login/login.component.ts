import { Component, OnInit } from '@angular/core';
import { TrashService } from 'src/app/services/trash.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [ TrashService]
})
export class LoginComponent implements OnInit {

  constructor(private trash: TrashService) { }

  login;


  ngOnInit(): void {

    this.login = {

      username: '',
      password: '',
    }
  }

  onLogin() {

    this.trash.Loginaccess(this.login).subscribe(
      res => {
        console.log('successfully logged in')
      },
      
    )
  }

}
