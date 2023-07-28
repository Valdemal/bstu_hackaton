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
import { HeaderComponent } from './components/ui/teacher/header/header.component';
import { DashboardOfTestsTopicsComponent } from './components/ui/students/dashboard-of-tests-topics/dashboard-of-tests-topics.component';

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
    HeaderComponent,
    DashboardOfTestsTopicsComponent,
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
