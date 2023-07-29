import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ContantComponent } from '../contant/contant.component';
import { DashboardOfTestsTopicsComponent } from '../dashboard-of-tests-topics/dashboard-of-tests-topics.component';
import { TestsComponent } from '../tests/tests.component';
import { StudentsComponent } from './students.component';
import { NotFoundComponent } from '../../shared/components/not-found.component';

const routeStudents: Routes = [
  {
    path: '',
    component: StudentsComponent,
    children: [
      { 
        path: '',
        redirectTo: 'app',
        pathMatch: 'full' 
      },
      { 
        path: 'app',     
        component: ContantComponent 
      },
      { 
        path: 'test',               
        component: TestsComponent 
      },
      { 
        path: 'dashboard',
        component: DashboardOfTestsTopicsComponent
      },
      {
        path: '**',
        component: NotFoundComponent,
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class StudentsRoutingModule {}
