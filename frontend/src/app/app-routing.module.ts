import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/ui/login/login.component';
import { RegisterComponent } from './components/ui/register/register.component';
import { ContantComponent } from './components/ui/contant/contant.component';
import { CreateTestComponent } from './components/ui/teacher/create-test/create-test.component';
import { TestsComponent } from './components/ui/students/tests/tests.component';

const routeStudents: Routes = [
  { path: '',                   redirectTo: 'login', pathMatch: 'full' },
  { path: 'login',              component: LoginComponent },
  { path: 'register',           component: RegisterComponent },
  { path: 'app',                component: ContantComponent },
  { path: 'create_tests',       component: CreateTestComponent },
  { path: 'test',               component: TestsComponent },
];

// const routeTeacher: Routes = [
//   { path: '',         redirectTo: 'create_tests', pathMatch: 'full' },
//   { path: 'create_tests',    component: CreateTestComponent},

// ]

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
