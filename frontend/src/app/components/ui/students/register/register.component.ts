import { UsersService } from 'src/app/shared/services/users.service';
import { User } from 'src/app/shared/models/user.model';
import { Component } from '@angular/core';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  public username: string = '';
  public email: string = '';
  public password: string = '';
  public message: string = '';
  public isFlagMessageError: boolean = false;
  private user: User = {};

  constructor(private userService: UsersService) {}

  validationOfDataFromTheMailField(email: string): boolean {
    let regular = new RegExp(
      '^([a-zA-Z0-9_.-])+@(([a-zA-Z0-9-])+.)+([a-zA-Z0-9]{2,4})|(^[0-9]{10})+$'
    );
    let testValue: boolean = regular.test(email);
    return testValue;
  }

  validationOfFields(username: string, password: string, email: string): void {
    if (username === '' && password === '' && email === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поля';
    } else if (username === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поле с именем';
    } else if (email === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поле с почтой';
    } else if (this.validationOfDataFromTheMailField(email) === false) {
      this.isFlagMessageError = false;
      this.message = 'Почта введена некорректно';
    } else if (password === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поле с паролем';
    } else {
      this.isFlagMessageError = true;
      this.message = 'Данные успешно отправлены на сервер';
    }
  }

  setDataUser(username: string, password: string, email: string): void {
    this.user.id = 0;
    this.user.username = username;
    this.user.password = password;
    this.user.email = email;
  }

  onSubmit(): void {
    this.validationOfFields(this.username, this.password, this.email);
    if (this.isFlagMessageError === true) {
      this.setDataUser(this.username, this.password, this.email);
      this.userService.createUser(this.user).subscribe({
        next: (user) => (this.user = user),
        error: (err) => console.log('Error: ', err),
      });
    }
  }
}
