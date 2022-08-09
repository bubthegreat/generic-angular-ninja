import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Observable, Subscription, switchMap, timer } from 'rxjs';
import { IStatus } from 'src/app/interfaces/istatus';

const baseAPIURL = 'http://app.localhost/api/'
const statusURL = baseAPIURL + 'status'
const busyURL = baseAPIURL + 'load'
const stringConfigURL = baseAPIURL + 'string_configs/?page=1'
const intConfigURL = baseAPIURL + 'int_configs/?page=1'

export interface IStringConfigs {
  items: IStringConfig[],
  count: number
}
export interface IStringConfig {
  id: number,
  title: string,
  value: string,
}

export interface IIntConfigs {
  items: IIntConfig[],
  count: number
}
export interface IIntConfig {
  id: number,
  title: string,
  value: BigInteger,
}

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {

  status: IStatus = {'uptime': 0, 'mysql_connected': false};
  loadCount: number = 0;
  stringConfigList!: IStringConfigs;
  intConfigList!: IIntConfigs;
  subscription: Subscription = new Subscription;
  displayedColumns: string[] = ['title', 'value'];

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

  getStringConfigs() {
    this.subscription = this.http.get<IStringConfigs>(stringConfigURL)
        .subscribe(
          resp => {
            this.stringConfigList = resp; 
            console.log('string_configs', resp);
            return resp;
          }
        )
  }

  getIntConfigs() {
    this.subscription = this.http.get<IIntConfigs>(intConfigURL)
        .subscribe(
          resp => {
            this.intConfigList = resp; 
            console.log('int_configs', resp);
            return resp;
          }
        )
  }

}
