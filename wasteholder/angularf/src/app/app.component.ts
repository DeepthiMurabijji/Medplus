import { Component , OnInit} from '@angular/core';
import { TrashService } from './services/trash.service';
import { AuthService } from './services/auth.service';
import { Router } from '@angular/router';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  username : string;
  title = 'angularf';
  id : any;

  constructor(public trash:TrashService,public auth:AuthService,private router:Router) { }

  ngOnInit(): void {
  }

  role ()
  {
    this.id = JSON.parse(localStorage.getItem('user'));
    // console.log(this.id);
    this.username = this.id.user.username;
    if (this.id.is_admin){
      this.router.navigate(['/admin']);
    }
    else{
      this.router.navigate(['/member']);
    }
  }



  logout(){
    localStorage.clear()
    sessionStorage.clear()
    this.router.navigate([''])
  }
  
 
}


