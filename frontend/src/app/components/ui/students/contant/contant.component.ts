import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/shared/models/user.model';
import { AuthService } from 'src/app/shared/services/auth.service';
import { UsersService } from 'src/app/shared/services/users.service';

@Component({
  selector: 'app-contant',
  templateUrl: './contant.component.html',
  styleUrls: ['./contant.component.scss']
})
export class ContantComponent implements OnInit{
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
