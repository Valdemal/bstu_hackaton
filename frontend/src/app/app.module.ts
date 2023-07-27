import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UsersService } from './shared/services/users.service';
import { HttpClientModule } from '@angular/common/http';
import { AuthService } from './shared/services/auth.service';
import { LayoutComponent } from './components/ui/layout/layout.component';
import { HeadersComponent } from './components/ui/headers/headers.component';
import { LoginComponent } from './components/ui/login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RegisterComponent } from './components/ui/register/register.component';
import { ContantComponent } from './components/ui/contant/contant.component';

@NgModule({
  declarations: [
    AppComponent,
    LayoutComponent,
    HeadersComponent,
    LoginComponent,
    RegisterComponent,
    ContantComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
  ],
  providers: [UsersService, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }
