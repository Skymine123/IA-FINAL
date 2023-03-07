import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { FlaskService } from 'src/services/flask.service';
import { Test } from '../models/test';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers:[FlaskService]
})
export class AppComponent implements OnInit{
  title = 'frontia';
  public texto:string;
  public test:Test;
  constructor(
    private _flaskService:FlaskService
  ){
    this.texto='';
    this.test=new Test('1',2,3);
  }
  ngOnInit(): void {
  }
}
