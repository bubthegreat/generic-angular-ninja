import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { GlobalStateService } from '../../services/global-state.service';
import { MatSnackBar } from '@angular/material';


@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {

  constructor(
    private router: Router,
    private state: GlobalStateService,
    private _snackBar: MatSnackBar
    ) { }

  ngOnInit() {
  }


}
