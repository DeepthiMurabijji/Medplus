import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse,
  HttpClient
} from '@angular/common/http';
import { catchError, Observable, switchMap, throwError } from 'rxjs';
import { AuthService } from './services/auth.service';

@Injectable()
export class AuthjwtInterceptor implements HttpInterceptor {
  refresh: boolean= false;

  constructor(private http: HttpClient,private auth:AuthService) {}

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    let token = JSON.parse(localStorage.getItem('token'));
    if (this.auth.loggedIn())    
    request = request.clone({
      setHeaders:{
        Authorization: `Bearer ${token.access}`
      }
    })
    return next.handle(request).pipe(
      catchError((err: HttpErrorResponse) => {
        if(err.status === 401 && !this.refresh){
        this.refresh = true;        
        return this.http.post('http://localhost:8000/api/token/refresh/', {'refresh':token.refresh}).pipe(
          switchMap((res:any) => {
            token.access = res['access'];
            localStorage.setItem('token', JSON.stringify(token));
            return next.handle(request.clone({
              setHeaders: {
                Authorization: `Bearer ${token.access}`
              }
            }));
          })
        ).pipe(catchError((err:HttpErrorResponse)=> {
          if(err.status === 401)
          localStorage.clear();
          return throwError(() => err);
        }));
      }
      this.refresh = false;
      return throwError(() => err);
    }));;;
  }
}
