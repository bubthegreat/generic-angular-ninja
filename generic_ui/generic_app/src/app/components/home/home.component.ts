import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable, Subscription, switchMap, timer } from 'rxjs';
import { IStatus } from 'src/app/interfaces/istatus';

const baseAPIURL = 'http://app.localhost/api/'
const statusURL = baseAPIURL + 'status'
const busyURL = baseAPIURL + 'load'



@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  status: IStatus = {'uptime': 0, 'mysql_connected': false};
  loadCount: number = 0;
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

  createLoad() {
    this.subscription = this.http.get<number>(busyURL)
        .subscribe(
          resp => {
            this.loadCount += resp; 
            console.log('resp', this.loadCount);
            return resp;
          }
        )
  }

  makeBusy() {
    this.createLoad();
    this.createLoad();
    this.createLoad();
    this.createLoad();
    this.createLoad();
    this.createLoad();
  }



}
