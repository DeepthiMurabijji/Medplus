import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TrashService {

  readonly APIUrl = "http://127.0.0.1:8000/";

  constructor(private http: HttpClient) { }

  // getCollectorList(): Observable<any[]> {
  //   return this.http.get<any[]>(this.APIUrl + 'collector/');
  // }

  getAllAreas(): Observable<any> {
    return this.http.get(this.APIUrl + 'apiRegister')
  }

  RegistrationSaving(data: any): Observable<any[]> {
    return this.http.post<any>(this.APIUrl + 'apiRegister', data)
  }

}
