import { Component } from '@angular/core';
import { SharedService } from '../../shared/services/shared.service';

@Component({
  selector: 'students-header',
  templateUrl: './students-header.component.html',
  styleUrls: ['./students-header.component.scss']
})
export class StudentsHeaderComponent {
  public message: string = "Войти"; 
  
  isVisible: boolean = true;

  show = () => this.isVisible = true;
  hide = () => this.isVisible = false;

  ngOnInit(){
    SharedService.showStudnetHeader = this.show;
    SharedService.hideStudentHeader = this.hide;
  }
}
