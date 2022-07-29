import { Component, Input, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';
import * as FileSaver from 'file-saver';
import { ngxCsv } from 'ngx-csv/ngx-csv';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.scss']
})
export class HistoryComponent implements OnInit {
  // @Input() admin_logged_in=true;
  title = 'mdb-angular-ui-kit-free';

  Dfile : boolean = false;
  act : any;
  del : any;

  items = ['Action', 'Another action', 'Something else here'];
  filteredItems = this.items;

  searchItems(event: any) {
    const value = event.target.value;

    this.filterItems(value);
  }

  filterItems(value: string) {
    const filterValue = value.toLowerCase();
    this.filteredItems = this.items.filter((item: string) =>
      item.toLowerCase().includes(filterValue)
    );
  }
  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  ngOnInit(): void {

    this.trash.activityLog().subscribe({
      next: (data: any) => {
        // console.log(data);
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
