import { Component, Input, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import * as FileSaver from 'file-saver';
import { ngxCsv } from 'ngx-csv/ngx-csv';
import {MatInputModule} from '@angular/material/input';
import { FormBuilder, FormGroup, FormControl} from '@angular/forms';


@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.scss']
})
export class HistoryComponent implements OnInit {
  // @Input() admin_logged_in=true;
  title = 'mdb-angular-ui-kit-free';
  form: FormGroup;
  Dfile : boolean = false;
  act : any;
  del : any;
  username : string;
  historyList : any

  
  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.trash.activityLog().subscribe({
      next: (data: any) => {
        // console.log(data);
        this.act = data;
    
      }
    })  
  }
  searchform = new FormGroup({
    findout : new FormControl(''),
  });

  onSearch() {
    // console.log(this.searchform.value);

    this.trash.SearchByDate(this.searchform.value).subscribe({
        next: (reg) => {
          console.log("serach:",reg);

        }, error :(reg) =>{
            console.log('error',reg)
        }
    })

  }
  onDelete(id: any) {
    this.del = id;
    console.log(this.del);
    this.trash.deleteActivityLog(this.del).subscribe({
      next: (data: any) => {
        // console.log(data);
        window.location.reload();
      },error : (err : any) =>{
        // console.log(err);
      }
    })
  }

  onClearAll() {
    this.trash.deleteAllHistory().subscribe({
      next: (data: any ) =>{
        console.log(data);
        window.location.reload();
      },error : (err : any) =>{
        console.log(err);
      }
    });
  }

  onDownload() {
    this.trash.downloadHistory().subscribe({
      next: (data: any ) =>{
        console.log("Here is your Download History",data);
        let blob = new Blob([data], {type: "text/csv;charset=utf-8;" });
        FileSaver.saveAs(blob, "work.csv")
        // let blob = new Blob([data._body.toString()], {type: 'text/csv' });
        // FileSaver.saveAs(blob, "work.csv")
        // var options = { 
        //   fieldSeparator: ',',
        //   quoteStrings: '"',
        //   decimalseparator: '.',
        //   showLabels: true, 
        //   showTitle: true,
        //   title: 'Your title',
        //   useBom: true,
        //   noDownload: false,
        //   // headers: ["First Name", "Last Name", "ID"]
        // };
       
        // new ngxCsv(data, "work", options);

        console.log("DD:",data);
      },error : (err : any) =>{
        console.log("So, the error is:", err);
      }
    })
  }

  


}
