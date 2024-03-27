import { Component } from '@angular/core';
import { JSONPlacesholderService } from '../services/jsonplacesholder.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrl: './album-photos.component.css'
})
export class AlbumPhotosComponent {
  data: any
  id: number = 0;
  constructor(private jsonPlaceholder: JSONPlacesholderService, private route: ActivatedRoute, private location: Location) {  }
  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.id = params['id'];
    })
    this.getDataFromAPI()
}
  getDataFromAPI() {
    this.jsonPlaceholder.getImages(this.id).subscribe((data) => {
      console.log(data)
      this.data = data
    })
  }
  goBack(): void {
    this.location.back();
  }
}
