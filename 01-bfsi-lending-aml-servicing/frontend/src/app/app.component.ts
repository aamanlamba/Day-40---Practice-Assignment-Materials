import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { DashboardComponent } from './dashboard.component';

@Component({selector:'app-root', standalone:true, imports:[CommonModule,FormsModule,DashboardComponent], template:`<main><h1>Operations Console</h1><app-dashboard></app-dashboard></main>`})
export class AppComponent {}
