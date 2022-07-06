import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';

import { FormsModule , ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RegisterComponent } from './components/register/register.component';
import { TrashService } from './services/trash.service';
import { AdminComponent } from './components/admin/admin.component';
import { MemberComponent } from './components/member/member.component';
import { SidebarComponent } from './components/admin/sidebar/sidebar.component';
import { PermisionsComponent } from './components/admin/permisions/permisions.component';
import { ArealistComponent } from './components/admin/arealist/arealist.component';
import { ArearegisterComponent } from './components/admin/arearegister/arearegister.component';
import { ProfileComponent } from './components/admin/profile/profile.component';
import { EditComponent } from './components/admin/edit/edit.component';



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    AdminComponent,
    MemberComponent,
    SidebarComponent,
    PermisionsComponent,
    ArealistComponent,
    ArearegisterComponent,
    ProfileComponent,
    EditComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [TrashService],
  bootstrap: [AppComponent]
})
export class AppModule { }
