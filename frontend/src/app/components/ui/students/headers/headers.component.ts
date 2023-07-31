import { Component } from '@angular/core';

@Component({
  selector: 'app-headers',
  templateUrl: './headers.component.html',
  styleUrls: ['./headers.component.scss']
})
export class HeadersComponent {
  public message: string = "Войти"; 
  
  getName() { 
    return localStorage.getItem('user');
  }
}
