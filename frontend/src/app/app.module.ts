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
import { AboutComponent } from './components/ui/students/about/about.component';
import { CreatingQuestionsComponent } from './components/ui/teacher/creating-questions/creating-questions.component';

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
    AboutComponent,
    CreatingQuestionsComponent,
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
