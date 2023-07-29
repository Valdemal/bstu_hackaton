import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from '../login/login.component';
import { RegisterComponent } from '../register/register.component';
import { NotFoundComponent } from '../../shared/components/not-found.component';
import { UsersService } from '../../shared/services/users.service';
import { AuthService } from '../../shared/services/auth.service';
import { AuthComponent } from './auth.component';

const routeStudents: Routes = [
  { 
    path: '',
    component: AuthComponent,
    children: [
      { 
        path: '',
        redirectTo: 'login', 
        pathMatch: 'full',
      },
      { 
        path: 'login',              
        component: LoginComponent,
        providers: [AuthService],
      },
      { 
        path: 'register',
        component: RegisterComponent,
        providers: [UsersService],
      },
      {
        path: '**',
        component: NotFoundComponent,
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class AuthRoutingModule {}
