import { CommonModule } from "@angular/common";
import { NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { StudentsRoutingModule } from "./students.routing";
import { ContantComponent } from "../contant/contant.component";
import { DashboardOfTestsTopicsComponent } from "../dashboard-of-tests-topics/dashboard-of-tests-topics.component";
import { TestsComponent } from "../tests/tests.component";
import { StudentsHeaderComponent } from "../students-header/students-header.component";
import { StudentsComponent } from "./students.component";
import { HeaderDuringTestsComponent } from "../header-during-tests/header-during-tests.component";
import { NotFoundModule } from "../../shared/components/not-found.module";

@NgModule({
    declarations: [
      StudentsComponent, StudentsHeaderComponent,
      ContantComponent,
      TestsComponent, HeaderDuringTestsComponent,
      DashboardOfTestsTopicsComponent,
    ],
    imports: [
      CommonModule,
      FormsModule,
      StudentsRoutingModule,
      NotFoundModule,
    ],
    providers: [],
    bootstrap: [],
  })
  export class AppModule {}