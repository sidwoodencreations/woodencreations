import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ContactService {

  private apiUrl = 'http://localhost:8888/contact';
  private http:HttpClient = inject(HttpClient);

  sendContactRequest(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
