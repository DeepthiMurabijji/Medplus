import { Injectable } from '@angular/core';

import { Observable } from 'rxjs';
import { HttpClient, HttpParams } from '@angular/common/http';
const APIUrl1 = "http://127.0.0.1:8001/apiLogin";
@Injectable({
  providedIn: 'root'
})
export class TrashService {

  readonly APIUrl = "http://127.0.0.1:8000/";
  

  constructor(private http: HttpClient) {

  }

  // getCollectorList(): Observable<any[]> {
  //   return this.http.get<any[]>(this.APIUrl + 'collector/');
  // }

  getAllAreas(): Observable<any> {
    return this.http.get(this.APIUrl + 'apiRegister')
  }

  RegistrationSaving(data: any): Observable<any[]> {
    return this.http.post<any>(this.APIUrl + 'apiRegister', data)
  }

  Loginaccess(data: any): Observable<any> {
    // console.log("enytetr",this.APIUrl + 'apiLogin', data);
    return this.http.post<any>(this.APIUrl + 'apiLogin', data)
  }

  getAreaList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + 'apiarealist')
  }

  AreaRegistrations(data: any): Observable<any[]> {
    // console.log("enytetr", data);
    return this.http.post<any>(this.APIUrl + 'apiarearegistration',data)
  }

  Administration(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + 'apiAdministration')
  }

  getuserInfo(id:any): Observable<any[]> {
    let params = new HttpParams().set('id',id);
    // console.log(id);
    return this.http.get<any[]>(this.APIUrl + 'apiEditing/',{params:params})
  }

  EditingRole(data: any): Observable<any[]> {
    return this.http.post<any>(this.APIUrl + 'apiEditing/', data)
  }

  getMemberInfo(member:any): Observable<any[]> {
    let params = new HttpParams().set('member',member);
    return this.http.get<any[]>(this.APIUrl + 'apiMember',{params:params})
  }

  postMemberHouses(data :any, member:any): Observable<any[]> {
    let params = new HttpParams().set('member',member);
    return this.http.post<any>(this.APIUrl + 'apiMember',data, {params:params})
  }

  resetService(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + 'apiResetButton')
  }

  activityLog(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + 'apiHistory')
  }

  deleteActivityLog(id:any): Observable<any> {
    console.log('deleteActivityLog',id);
    let params = new HttpParams().set('id',id);
    return this.http.delete(this.APIUrl + 'apiHistory', {params:params})
  }

  deleteAllHistory(): Observable<any[]> {
    return this.http.delete<any[]>(this.APIUrl + 'apiDeleteAll')
  }

  downloadHistory(): Observable<any> {  
    return this.http.get(this.APIUrl + 'apiCsvfile', {responseType: "arraybuffer"})
  }

  getPiechartdetails(): Observable<any[]> { 
    return this.http.get<any[]>(this.APIUrl + 'apiPieChart')
  }

  fetchToken(Credentials):Observable<any> {
    return this.http.post(this.APIUrl + 'api/token/',Credentials);
  }

  SearchByDate(date: any): Observable<any[]> {
    // console.log("date:",date);
    return this.http.post<any>(this.APIUrl + 'apiSearchbyDate',date)
  }
}
