import { Component, OnInit } from '@angular/core';
import { UsersService } from '../../shared/services/users.service';
import { User } from '../../shared/models/user.model';

@Component({
  selector: 'app-contant',
  templateUrl: './contant.component.html',
  styleUrls: ['./contant.component.scss']
})
export class ContantComponent implements OnInit{
  title = 'services';

  columns = ['Id', 'Email', 'Username', 'Password'];

  constructor(private usersService: UsersService){}

  users: User[] = [];

  ngOnInit(){
    this.usersService.getUsersList().subscribe({
      next  : (users) => this.users = users,
      error : (err)  => console.log('Error: '   , err ),
    })
  }
}
