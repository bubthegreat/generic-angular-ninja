import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable, Subscription, switchMap, timer } from 'rxjs';
import { IStatus } from 'src/app/interfaces/istatus';

const baseAPIURL = 'http://app.localhost/api/'
const statusURL = baseAPIURL + 'status'
const employeeURL = baseAPIURL + 'employees/?page=1'

export interface IEmployees {
  items: IEmployee[],
  count: number
}
export interface IEmployee {
  id: number,
  first_name: string,
  last_name: string,
  department: number,
  birthdate: string
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  status: IStatus = {'uptime': 0, 'mysql_connected': false};
  employeeList!: IEmployees;
  subscription: Subscription = new Subscription;

  constructor(private http: HttpClient) { }


  getStatus() {
    this.subscription = this.http.get<IStatus>(statusURL)
        .subscribe(
          resp => {
            this.status = resp; 
            console.log('resp', resp);
            return resp;
          }
        )
  }
  getEmployees() {
    this.subscription = this.http.get<IEmployees>(employeeURL)
        .subscribe(
          resp => {
            this.employeeList = resp; 
            console.log('employees', resp);
            return resp;
          }
        )
  }

}
