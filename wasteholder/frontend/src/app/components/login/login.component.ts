import { Component, OnInit } from '@angular/core';

import { TrashService } from 'src/app/services/trash.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.sass']
})
export class LoginComponent implements OnInit {

  constructor(private trashService: TrashService) { }

  ngOnInit(): void {
  }

}
