import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  admin : any;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {
    this.admin = JSON.parse(localStorage.getItem('user'));
    console.log("hey this is admin", this.admin);
    console.log(this.admin.user.email);
  }

  



}
