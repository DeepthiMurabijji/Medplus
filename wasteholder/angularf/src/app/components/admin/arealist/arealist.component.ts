import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TrashService } from 'src/app/services/trash.service';
import { AuthService } from 'src/app/services/auth.service';



@Component({
  selector: 'app-arealist',
  templateUrl: './arealist.component.html',
  styleUrls: ['./arealist.component.scss']
})
export class ArealistComponent implements OnInit {

  arealist : any;
  houselist : any;
  housenumber : any;

  filterhtml : { areaid: number, areaname: string, houes: string[], houseaddress: string [], status: string[] }[]

  constructor(public trash: TrashService, public router: Router, public auth: AuthService) { }

  // Temp variable 
  tempareaid!: number;
  tempareaname!: string;
  tempareahouses: string[];
  tempareaaddress: string[];
  tempareastatus: string[];

  ngOnInit(): void {

    this.trash.getAreaList().subscribe({
      next: (res: any) => {
        this.arealist = res.areas;
        this.housenumber = res.houseCount;
        this.houselist = res.houses;

        // for (let house of res.houseCount){
        //   this.houselist.push({
        //     housename: house[0],
        //     housecount: house[1]
        //   })
        // }
        // console.log("The house list",res.houseCount.arealist.area.area_name);
        console.log(this.arealist);
        console.log(this.houselist);
        console.log(this.housenumber);
        // console.log("for loop");
        // for (let area of this.arealist){
        //   console.log("hi:",area.area_name);
        // }
        // console.log("for loop");
        
        // for (let area of this.arealist)
        // {
        //   console.log("hi:",area.area_name,this.housenumber[area.area_name]);
        // }
        for (let ar of this.arealist)
        {
          // console.log("area:",ar.area_name);
          this.tempareaid = ar.id
          this.tempareaname = ar.area_name

          for (let house of this.houselist)
          {
            if(ar.id == house.area)
            {
              console.log('area:',ar.id ,"house:", house.house_name);
              this.tempareahouses.push(house.house_name)
              this.tempareaaddress.push(house.house_address)
              this.tempareastatus.push(house.is_completed)
            }
            console.log('area:',ar.id ,"house:", house.area);
          }

          this.filterhtml.push({'areaid': this.tempareaid, 'areaname': this.tempareaname, 'houes': this.tempareahouses, 'houseaddress': this.tempareaaddress, 'status': this.tempareastatus});

          console.log("final:", this.filterhtml);

          this.tempareahouses=[];
          this.tempareaaddress=[];
          this.tempareastatus=[];
          

          


        }

      
        
      
      }
    })
  }

}
