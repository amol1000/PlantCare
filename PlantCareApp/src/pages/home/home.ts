import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})
export class HomePage {
  moistureValue = null;
  constructor(public navCtrl: NavController, public httpClient: HttpClient) {

    this.moistureValue = 25;
  }

  getData() {
    var url = 'http://localhost:8000/get_data/';
    this.httpClient.get(url).subscribe(data => {
      this.moistureValue = data;
    });
  }

}
