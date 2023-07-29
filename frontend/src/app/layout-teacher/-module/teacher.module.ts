import { NgModule } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { CommonModule } from "@angular/common";
import { NotFoundModule } from "../../shared/components/not-found.module";
import { TeacherComponent } from "./teacher.component";
import { TeacherRoutingModule } from "./teacher.routing";
import { CreatingQuestionsComponent } from "../creating-questions/creating-questions.component";
import { CreateTestComponent } from "../create-test/create-test.component";
import { TeachersHeaderComponent } from "../teacher-header/teachers-header.component";

@NgModule({
    declarations: [
      TeacherComponent, TeachersHeaderComponent,
      CreateTestComponent,
      CreatingQuestionsComponent,
    ],
    imports: [
      CommonModule,
      FormsModule,
      TeacherRoutingModule,
      NotFoundModule,
    ],
    providers: [],
    bootstrap: [],
  })
  export class AuthModule {}