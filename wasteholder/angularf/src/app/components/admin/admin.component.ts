import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';



@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {

  admin : any;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.admin = JSON.parse(localStorage.getItem('user'));
    
  }

}
