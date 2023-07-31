import { LayoutTestsComponent } from './components/ui/students/layout-tests/layout-tests.component';
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContantComponent } from './components/ui/students/contant/contant.component';
import { CreateTestComponent } from './components/ui/teacher/create-test/create-test.component';
import { TestsComponent } from './components/ui/students/tests/tests.component';
import { LoginComponent } from './components/ui/students/login/login.component';
import { RegisterComponent } from './components/ui/students/register/register.component';
import { DashboardOfTestsTopicsComponent } from './components/ui/students/dashboard-of-tests-topics/dashboard-of-tests-topics.component';
import { CreatingQuestionsComponent } from './components/ui/teacher/creating-questions/creating-questions.component';
import { LayoutAdministratorComponent } from './components/ui/administrator/layout-administrator/layout-administrator.component';
import { LayoutUsersComponent } from './components/ui/students/layout-users/layout-users.component';
import { CreateFormComponent } from './components/ui/administrator/create-form/create-form.component';
import { LayoutTeacherComponent } from './components/ui/teacher/layout-teacher/layout-teacher.component';

const routeStudents: Routes = [
  { path: '',                   redirectTo: 'login', pathMatch: 'full' },
  { path: 'login',              component: LoginComponent },  
  { path: 'create_tests',       component: LayoutTeacherComponent }, 
  { path: 'nextStage',          component: CreatingQuestionsComponent},
  { path: 'test',               component: LayoutTestsComponent},
  { path: 'administrator',      component: LayoutAdministratorComponent},
  { path: 'user',               component: LayoutUsersComponent},
  { path: 'create',             component: CreateFormComponent},
  { path: 'teacher',            component: LayoutTeacherComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
