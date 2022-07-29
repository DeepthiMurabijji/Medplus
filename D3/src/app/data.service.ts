import { Injectable } from "@angular/core";
import { BehaviorSubject } from "rxjs";
import { IData } from './data.interface';
import * as d3 from "d3";

@Injectable()
export class DataService {
    public d3 = d3;


    public generateId(length): string {
        var result = "";
        var characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        var charactersLength = characters.length;
        for (var i = 0; i < length; i++) {
          result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        return result;
    }
    private mockData: IData[] = [
        {
            label: "data1",
            value: 1,
        },
        {
            label: "data2",
            value: 2,
        },
		{
			label: "data3",
			value: 3,
		},
		{
			label: "data4",
			value: 4,
		}
    ];

    private dataSubject = new BehaviorSubject<IData[]>(this.mockData);
    
    $data = this.dataSubject.asObservable();

    addData(newData: IData) {
        this.mockData.push(newData);
        this.dataSubject.next(this.mockData);
    }
}