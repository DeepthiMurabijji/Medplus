import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { TrashService } from './trash.service';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private trash: TrashService) { }

  userprofile = new Observable((observer)  => {
    let user : any ;
    if (user = localStorage.getItem('user'))
    {
      observer.next(JSON.parse(user));
      observer.complete();
    }
    observer.next(null);
  })


  loggedIn(): boolean{
    let loggedin:boolean = false;
    this.userprofile.subscribe({
      next: (user:any) => {
        if(user){
          loggedin = true;
        }
        else{
          loggedin = false;
        }
      },
      complete: () => {
      }
    })
    return loggedin;
  }

  username():string{
    let name = ''
      this.userprofile.subscribe({
        next: (user:any) => {
          if(user){
            name = user.user.username;
            
          }
        },
        complete: () => {
        }
      })
      // console.log(name);
      return name;
    }

  
}
