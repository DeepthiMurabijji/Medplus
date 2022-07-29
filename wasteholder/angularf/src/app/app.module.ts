import { NgModule } from '@angular/core';
import { MdbCheckboxModule } from 'mdb-angular-ui-kit/checkbox';
import { BrowserModule } from '@angular/platform-browser';
// import { ChartsModule } from 'ng2-charts';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';

import { FormsModule , ReactiveFormsModule} from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
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
import { HistoryComponent } from './components/admin/history/history.component';
import { PiechartComponent } from './components/admin/piechart/piechart.component';
import { AuthjwtInterceptor } from './authjwt.interceptor';



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
    EditComponent,
    HistoryComponent,
    PiechartComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    NgbModule,
    MdbCheckboxModule,
    // ChartsModule
  ],
  providers: [TrashService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthjwtInterceptor,
      multi: true,
    }],
  bootstrap: [AppComponent]
})
export class AppModule { }
