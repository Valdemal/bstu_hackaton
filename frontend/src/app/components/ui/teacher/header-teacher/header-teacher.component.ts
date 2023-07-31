import { Component } from '@angular/core';

@Component({
  selector: 'app-header-teacher',
  templateUrl: './header-teacher.component.html',
  styleUrls: ['./header-teacher.component.scss']
})
export class HeaderTeacherComponent {
  getName() { 
    return localStorage.getItem('user');
  }
}
