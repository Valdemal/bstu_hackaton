import { NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { AuthRoutingModule } from "./auth.routing";
import { LoginComponent } from "../login/login.component";
import { CommonModule } from "@angular/common";
import { NotFoundModule } from "../../shared/components/not-found.module";
import { AuthComponent } from "./auth.component";
import { RegisterComponent } from "../register/register.component";

@NgModule({
    declarations: [
      AuthComponent,
      LoginComponent,
      RegisterComponent,
    ],
    imports: [
      CommonModule,
      FormsModule,
      AuthRoutingModule,
      NotFoundModule,
    ],
    providers: [],
    bootstrap: [],
  })
  export class AuthModule {}