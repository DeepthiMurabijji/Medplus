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

      next: (user) => {
        localStorage.setItem('user',JSON.stringify(user));
        console.log('successfully logged in');
        console.log(user);

        if(user.is_admin){
          this.router.navigate(['/admin']);
        }
        else {
          this.router.navigate(['/member']);
        }
        
      }, error: (res) => {

        console.log(' Bad requests')

      }
      
    }
      
    )
  }

}
