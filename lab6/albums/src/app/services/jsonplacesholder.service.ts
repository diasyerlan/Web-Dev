import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class JSONPlacesholderService {

  constructor(private http: HttpClient) { }
  getData(): Observable<any> {
    const url = "https://jsonplaceholder.typicode.com/albums"
    return this.http.get(url)
  }
  getImages(id: number) {
    const url = `https://jsonplaceholder.typicode.com/albums/${id}/photos`
    return this.http.get(url);
  }

}
