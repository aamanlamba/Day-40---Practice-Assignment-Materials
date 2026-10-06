import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { LegacyApiService } from './legacy-api.service';

@Component({selector:'app-dashboard', standalone:true, imports:[CommonModule,FormsModule], template:`
  <section><h2>Operational Summary</h2>
  <input [(ngModel)]="q" aria-label="Search text"><button (click)="run()">Search</button>
  <p *ngIf="error" role="alert">{{error}}</p><pre>{{result | json}}</pre></section>`})
export class DashboardComponent implements OnInit {
  q=''; result: unknown; error='';
  constructor(private api: LegacyApiService) {}
  ngOnInit(){ this.api.summary().subscribe({next:x=>this.result=x,error:e=>this.error=String(e)}); }
  run(){ if(this.q.trim().length<2){this.error='Enter at least 2 characters';return;} this.error=''; this.api.search(this.q).subscribe({next:x=>this.result=x,error:e=>this.error=String(e)}); }
}
