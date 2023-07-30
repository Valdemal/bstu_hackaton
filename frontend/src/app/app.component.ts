import { Component, OnInit } from '@angular/core';
import { UsersService } from './shared/services/users.service';
import { AuthService } from './shared/services/auth.service';
import { User } from './shared/models/user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'services';

  columns = ['Id', 'Email', 'Username', 'Password'];

  constructor(private usersService: UsersService, private authService: AuthService){}

  users: User[] = [];

  ngOnInit(){
    this.authService.authorize('%%%LOGIN%%%', '%%%PASSWORD%%%').subscribe({
      next: (resp) => {
        this.authService.setToken(resp);
        this.pingService();
      },
      error: console.log
    })
  }

  pingService(){
    this.usersService.getUsersList().subscribe({
      next  : (users) => this.users = users,
      error : (err)  => console.log('Error: '   , err ),
    })
  }
}
