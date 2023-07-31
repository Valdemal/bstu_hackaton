import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UsersService } from './shared/services/users.service';
import { HttpClientModule } from '@angular/common/http';
import { AuthService } from './shared/services/auth.service';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { ContantComponent } from './components/ui/students/contant/contant.component';
import { CreateTestComponent } from './components/ui/teacher/create-test/create-test.component';
import { TestsComponent } from './components/ui/students/tests/tests.component';
import { LayoutComponent } from './components/ui/students/layout/layout.component';
import { HeadersComponent } from './components/ui/students/headers/headers.component';
import { LoginComponent } from './components/ui/students/login/login.component';
import { RegisterComponent } from './components/ui/students/register/register.component';
import { DashboardOfTestsTopicsComponent } from './components/ui/students/dashboard-of-tests-topics/dashboard-of-tests-topics.component';
import { HeaderDuringTestsComponent } from './components/ui/students/header-during-tests/header-during-tests.component';

import { CreatingQuestionsComponent } from './components/ui/teacher/creating-questions/creating-questions.component';
import { MenuComponent } from './components/ui/administrator/menu/menu.component';
import { MenuStudentsComponent } from './components/ui/students/menu-students/menu-students.component';
import { LayoutAdministratorComponent } from './components/ui/administrator/layout-administrator/layout-administrator.component';
import { HeaderAdministratorComponent } from './components/ui/administrator/header-administrator/header-administrator.component';
import { LayoutUsersComponent } from './components/ui/students/layout-users/layout-users.component';
import { MenuUsersComponent } from './components/ui/students/menu-users/menu-users.component';
import { LayoutTestsComponent } from './components/ui/students/layout-tests/layout-tests.component';
import { CreateFormComponent } from './components/ui/administrator/create-form/create-form.component';
import { LayoutTeacherComponent } from './components/ui/teacher/layout-teacher/layout-teacher.component';
import { HeaderTeacherComponent } from './components/ui/teacher/header-teacher/header-teacher.component';
import { MenuTeacherComponent } from './components/ui/teacher/menu-teacher/menu-teacher.component';

@NgModule({
  declarations: [
    AppComponent,
    LayoutComponent,
    HeadersComponent,
    LoginComponent,
    RegisterComponent,
    ContantComponent,
    CreateTestComponent,
    TestsComponent,
    DashboardOfTestsTopicsComponent,
    HeaderDuringTestsComponent,
    CreatingQuestionsComponent,
    MenuComponent,
    MenuStudentsComponent,
    LayoutAdministratorComponent,
    HeaderAdministratorComponent,
    LayoutUsersComponent,
    MenuUsersComponent,
    LayoutTestsComponent,
    CreateFormComponent,
    LayoutTeacherComponent,
    HeaderTeacherComponent,
    MenuTeacherComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [UsersService, AuthService],
  bootstrap: [AppComponent],
})
export class AppModule {}
