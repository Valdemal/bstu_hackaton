import { Component } from '@angular/core';
import { AuthService } from 'src/app/shared/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  public username: string = '';
  public password: string = '';
  public isFlagMessageError: boolean = false;
  public message: string = '';

  constructor(
    private userService: AuthService,
    private authService: AuthService
  ) {}

  validationOfFields(username: string, password: string): void {
    if (username === '' && password === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поля';
    } else if (password === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поле с паролем';
    } else if (username === '') {
      this.isFlagMessageError = false;
      this.message = 'Данные не введены в поле с именем';
    } else {
      this.isFlagMessageError = true;
      this.message = 'Данные успешно отправлены на сервер';
    }
  }

  onSubmit(): void {
    this.validationOfFields(this.username, this.password);
    if (this.isFlagMessageError === true) {
      this.userService.authorize(this.username, this.password).subscribe({
        next: (resp) => {
          this.authService.setToken(resp);
        },
        error: (err) => console.log('Error: ', err),
      });
    }
  }
}
