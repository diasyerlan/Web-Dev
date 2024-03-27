import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { JSONPlacesholderService } from '../services/jsonplacesholder.service';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-details',
  templateUrl: './album-details.component.html',
  styleUrls: ['./album-details.component.css']
})
export class AlbumDetailsComponent implements OnInit {
  newTitleText: string = '';
  id: number = 0;
  title: string | undefined;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private location: Location,
    private dataService: JSONPlacesholderService // Inject your data service
  ) { }

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      this.id = params['id'];
      this.title = params['title'];
    })
}
changeTitle() {
  this.title = this.newTitleText;
  this.newTitleText = '';
}
goBack() {
  this.location.back();
}
goToPhotos(id: number) {
  this.router.navigate(['/app-album-photos'], {queryParams: {id: id}})
}
}