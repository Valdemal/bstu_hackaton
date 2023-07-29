import { Component } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  public username: string = '';
  public password: string = '';
  
  public message: string = '';

  public isFlagMessageError: boolean = false;

  constructor(
    private authService: AuthService,
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
      this.authService.authorize(this.username, this.password).subscribe({
        next: (resp) => {
          this.authService.setToken(resp);
        },
        error: (err) => console.log('Error: ', err),
      });
    }
  }
}
