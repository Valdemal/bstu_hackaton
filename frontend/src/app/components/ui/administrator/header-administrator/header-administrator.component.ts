import { Component } from '@angular/core';

@Component({
  selector: 'app-header-administrator',
  templateUrl: './header-administrator.component.html',
  styleUrls: ['./header-administrator.component.scss']
})
export class HeaderAdministratorComponent {
  getName() { 
    return localStorage.getItem('user');
  }
}
