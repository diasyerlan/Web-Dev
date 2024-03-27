import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { AlbumsComponent } from './albums/albums.component';
import { AlbumDetailsComponent } from './album-details/album-details.component';
import { AlbumPhotosComponent } from './album-photos/album-photos.component';

const routes: Routes = [
  {path: '', redirectTo: '/app-home', pathMatch: 'full'},
  {path: 'app-home', component:HomeComponent},
  {path: 'app-about', component: AboutComponent},
  {path: 'app-albums', component: AlbumsComponent},
  {path: 'app-album-details', component: AlbumDetailsComponent},
  {path: 'app-album-photos', component: AlbumPhotosComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
