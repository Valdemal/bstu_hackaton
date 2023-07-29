import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NotFoundComponent } from '../../shared/components/not-found.component';
import { TeacherComponent } from './teacher.component';
import { CreateTestComponent } from '../create-test/create-test.component';
import { CreatingQuestionsComponent } from '../creating-questions/creating-questions.component';

const routeStudents: Routes = [
  { 
    path: '',
    component: TeacherComponent,
    children: [
      { 
        path: '',
        redirectTo: '', 
        pathMatch: 'full',
      },
      { 
        path: 'create_tests',
        component: CreateTestComponent
      }, 
      { 
        path: 'nextStage',
        component: CreatingQuestionsComponent
      },
      {
        path: '**',
        component: NotFoundComponent,
      }
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class TeacherRoutingModule {}
