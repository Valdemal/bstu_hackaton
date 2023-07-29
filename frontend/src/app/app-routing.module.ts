import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContantComponent } from './components/ui/students/contant/contant.component';
import { CreateTestComponent } from './components/ui/teacher/create-test/create-test.component';
import { TestsComponent } from './components/ui/students/tests/tests.component';
import { LoginComponent } from './components/ui/students/login/login.component';
import { RegisterComponent } from './components/ui/students/register/register.component';
import { DashboardOfTestsTopicsComponent } from './components/ui/students/dashboard-of-tests-topics/dashboard-of-tests-topics.component';
import { CreatingQuestionsComponent } from './components/ui/teacher/creating-questions/creating-questions.component';

const routeStudents: Routes = [
  { path: '',                   redirectTo: 'login', pathMatch: 'full' },
  { path: 'login',              component: LoginComponent },
  { path: 'register',           component: RegisterComponent },
  { path: 'app',                component: ContantComponent },
  { path: 'test',               component: TestsComponent }, // authorization
  { path: 'dashboard',          component: DashboardOfTestsTopicsComponent },
  { path: 'create_tests',       component: CreateTestComponent }, 
  { path: 'nextStage',          component: CreatingQuestionsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
