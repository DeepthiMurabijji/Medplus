import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { TrashService } from 'src/app/services/trash.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
  providers: [ TrashService]
})
export class RegisterComponent implements OnInit {

  constructor(private trash: TrashService) { }

  areasData: { area_name: string }[];
  register;

  // username!: string;
  // emailId!: string;
  // password!: string;

  ngOnInit(): void {

    this.register = {
      username : '',
      email: '',
      areas:'',
      password: '',
    };

    this.trash.getAllAreas().subscribe({
      next: (res) => {
        console.log('fasdfsa');
        console.log(res);
        this.areasData = res
      }
    })
    console.log(this.register);
  }

  

  onRegister(){

    this.trash.RegistrationSaving(this.register).subscribe(
      res => {
        alert("User" + this.register.username + "registered successfully")
      },
      error => console.log('error',error)
    )
  }

  // onUsername(event: any){

  //   this.username = (event.target as HTMLInputElement).value;

  // }


  // onEmailId(event: any){

  //   this.emailId = (event.target as HTMLInputElement).value;

  // }

  // onPassword(event: any){

  //   this.username = (event.target as HTMLInputElement).value;

  // }

  // // @ViewChild('username') username: ElementRef;
  // // @ViewChild('emailId') emailId: ElementRef;
  // // @ViewChild('password') password: ElementRef;
  // // @ViewChild('repeatPassword') repeatPassword: ElementRef;
  @ViewChild('areas') areas: ElementRef;

  // onRegister() {


  //   const collectorData = {

  //     // username: this.username.nativeElement.value,
  //     // emailId: this.emailId.nativeElement.value,
  //     // password: this.password.nativeElement.value,
  //     username: this.username,
  //     emailId: this.emailId,
  //     password: this.password,
  //     areas: this.areas.nativeElement.value

  //   }

  //   console.log(collectorData)

  //   this.trash.RegistrationSaving(collectorData).subscribe({
  //     next: (res) => {
  //       console.log(res)
  //     }
  //   })

  // }


}
