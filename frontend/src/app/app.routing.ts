import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routeStudents: Routes = [
  { 
    path: '',
    redirectTo: 'auth',
    pathMatch: 'full'
  },
  { 
    path: 'login',
    loadChildren:  () => import('./auth/-module/auth.module').then((m) => m.AuthModule),
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routeStudents)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
