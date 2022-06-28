import { Component, OnInit } from '@angular/core';
import { TrashService } from 'src/app/services/trash.service';
import { Router }  from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [ TrashService]
})
export class LoginComponent implements OnInit {

  constructor(private trash: TrashService, private router: Router ) { }

  login;


  ngOnInit(): void {

    this.login = {

      username: '',
      password: '',
    }
  }

  onLogin() {

    this.trash.Loginaccess(this.login).subscribe({

      next: (res) => {
        console.log('successfully logged in');
        this.router.navigate(['/admin']);
      }, error: (res) => {

        console.log(' Bad requests')

      }
      
    }
      
    )
  }

}
