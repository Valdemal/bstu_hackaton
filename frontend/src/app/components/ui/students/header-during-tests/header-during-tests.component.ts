import { Component } from '@angular/core';

@Component({
  selector: 'app-header-during-tests',
  templateUrl: './header-during-tests.component.html',
  styleUrls: ['./header-during-tests.component.scss'],
})
export class HeaderDuringTestsComponent {
  public date: number = 10;
  getTimeout() {
    const timerId = setInterval(() => this.date - 1, 60000);
    if(this.date === 0) {
      clearTimeout(timerId);
    }
    return this.date;
  }
}
