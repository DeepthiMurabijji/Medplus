import { Injectable } from '@angular/core';
// inclde 
import { HttpClient } from '@angular/common/http';
import { observable } from 'rxjs'; 

const baseUrl = 'http://localhost:8000/api/tutorials';
//# include 
@Injectable({
  providedIn: 'root'
})
export class TrashService {

  constructor(private http: HttpClient) { }

 
}
