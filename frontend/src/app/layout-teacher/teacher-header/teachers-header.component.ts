import { Component } from '@angular/core';
import { SharedService } from '../../shared/services/shared.service';

@Component({
  selector: 'teachers-header',
  templateUrl: './teachers-header.component.html',
  styleUrls: ['./teachers-header.component.scss']
})
export class TeachersHeaderComponent {
  public message: string = "Войти";
}
