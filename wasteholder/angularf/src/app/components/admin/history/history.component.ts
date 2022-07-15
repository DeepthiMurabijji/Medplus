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
  // @Input() admin_logged_in=true;
  Dfile : boolean = false;
  act : any;
  del : any;

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.trash.activityLog().subscribe({
      next: (data: any) => {
        console.log(data);
        this.act = data;
      }
    })  
  }

  onDelete(id: any) {
    this.del = id;
    console.log(this.del);
    this.trash.deleteActivityLog(this.del).subscribe({
      next: (data: any) => {
        console.log(data);
        window.location.reload();
      },error : (err : any) =>{
        console.log(err);
      }
    })
  }
}
