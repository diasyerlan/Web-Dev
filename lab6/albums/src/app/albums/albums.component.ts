import { Component, Input } from '@angular/core';
import { JSONPlacesholderService } from '../services/jsonplacesholder.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrl: './albums.component.css'
})
export class AlbumsComponent {
  newItemText: string = '';
  num: number = 100;
  data: Array<any>
  constructor(private JSONPlaceholder: JSONPlacesholderService, private router: Router) {
    this.data = new Array<any>()
  }
  getDataFromAPI() {
    this.JSONPlaceholder.getData().subscribe((data) => {
      console.log(data)
      this.data = data
    })
  }
ngOnInit() {
  this.getDataFromAPI()
}
goToAlbum(id: number, title: string) {
  this.router.navigate(['/app-album-details'], {queryParams: {id: id, title: title}});
}
deleteItem(index: number) {
  this.data.splice(index, 1);
}
addItem() {
  if(this.newItemText.trim() !== '') {
    const newItem = {
      id: this.num + 1,
      title: this.newItemText
    }
    this.num += 1;
    this.data.push(newItem);
    this.newItemText = '';
  }
}
}
