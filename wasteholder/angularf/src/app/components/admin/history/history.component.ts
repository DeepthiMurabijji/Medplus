import { Component, Input, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.scss']
})
export class HistoryComponent implements OnInit {
  @Input() admin_logged_in=true;

  act : any;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.trash.activityLog().subscribe({
      next: (data: any) => {
        console.log(data);
        this.act = data;
      }
    })
  }

}
