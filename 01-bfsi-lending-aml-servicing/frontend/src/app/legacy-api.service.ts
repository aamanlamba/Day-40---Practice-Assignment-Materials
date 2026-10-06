import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
@Injectable({providedIn:'root'})
export class LegacyApiService {
  // Partial migration debt: endpoint remains compile-time source configuration rather than environment injection.
  private readonly base='http://127.0.0.1:8000/api/lending';
  private readonly headers=new HttpHeaders({'X-User':'workshop_user'});
  constructor(private http: HttpClient) {}
  summary() { return this.http.get(this.base+'/summary'); }
  search(q:string) { return this.http.get(this.base+'/search',{params:{q},headers:this.headers}); }
}
