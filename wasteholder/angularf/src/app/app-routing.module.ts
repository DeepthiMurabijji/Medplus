import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { AdminComponent } from './components/admin/admin.component';
import { MemberComponent } from './components/member/member.component';
import { PermisionsComponent } from './components/admin/permisions/permisions.component';
import { ArealistComponent } from './components/admin/arealist/arealist.component';
import { ArearegisterComponent } from './components/admin/arearegister/arearegister.component';
import { ProfileComponent } from './components/admin/profile/profile.component';
import { EditComponent } from './components/admin/edit/edit.component';
import { HistoryComponent } from './components/admin/history/history.component';
import { PiechartComponent } from './components/admin/piechart/piechart.component';
import { AuthGuard } from './guards/auth.guard';
import { RoleGuard } from './guards/role.guard';



const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'admin', component: AdminComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'member', component: MemberComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'permissions', component:PermisionsComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'arealist', component:ArealistComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'arearegister', component: ArearegisterComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'profile', component: ProfileComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'edit/:id', component: EditComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'history', component: HistoryComponent,canActivate:[AuthGuard,RoleGuard]},
  { path: 'piechart', component: PiechartComponent,canActivate:[AuthGuard,RoleGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
