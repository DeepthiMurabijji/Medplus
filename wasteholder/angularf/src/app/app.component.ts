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

  title = 'angularf';

  constructor(public trash:TrashService,public auth:AuthService,private router:Router) { }

  ngOnInit(): void {
  }

  logout(){
    localStorage.clear()
    sessionStorage.clear()
    this.router.navigate([''])
  }
}
