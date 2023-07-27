import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/ui/login/login.component';
import { RegisterComponent } from './components/ui/register/register.component';
import { ContantComponent } from './components/ui/contant/contant.component';

const routes: Routes = [
  { path: '',         redirectTo: 'login', pathMatch: 'full' },
  { path: 'login',    component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'app',      component: ContantComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
