
import { Component, OnInit, ViewChild, ElementRef, AfterViewInit} from '@angular/core';
import { NgForm } from '@angular/forms';
import { FormsModule }   from '@angular/forms';
import { FlaskService } from 'src/services/flask.service';
import { Test } from '../../../models/test';
import { Modelo } from 'src/models/modelo';

@Component({
  selector: 'app-enviar-datos',
  templateUrl: './enviar-datos.component.html',
  styleUrls: ['./enviar-datos.component.css'],
  providers:[FlaskService]
})
export class EnviarDatosComponent implements AfterViewInit{
  
  title = 'frontia';
  public texto:string;
  public test:Test;
  public modelo:Modelo;

  public sector_ot:string;
  public ownership_ot:string;
  public job_title_ot:string;

  public messages:any;

  //public cadena_skills:string;
  public skills:any[];
  constructor(
    private _flaskService:FlaskService
  ){
    
    this.sector_ot='';
    this.ownership_ot='';
    this.job_title_ot='';

    this.texto='';
    this.skills=[false,false,false,false,false];
    this.texto='';
    this.test=new Test('1',2,3);
    //this.modelo=new Modelo(0,'Health Care','','Private','Data scientist',0,'','Excel');
    this.modelo=new Modelo(0,'','','',0,'','');
  }
  ngOnInit(): void {
    
  }
  ngAfterViewInit(): void {
  }
  sendForm(form:NgForm){
    this.parseOthers();
    this.getChecks();
    console.log(this.texto);
    this._flaskService.postFlask(this.modelo).subscribe(
      response=>{
        console.log(response);
        this.messages={message:response.message,status:'success'};
      }
      ,error=>{
        console.log(<any>error);
        this.messages={message:"ALGO FALLÓ",status:'failed'};
      }
    );
  }
  getChecks(){
    var skillsT=[
      'Excel',
      'Tableau',
      'Python',
      'SQL',
      'Other'
    ];
    var texto='';
    for (let i = 0; i < 5; i++){
      if (this.skills[i]==true){
        texto+=skillsT[i]+",";
      }
    }
    this.modelo.job_skills=texto;
  }
  parseOthers(){
    if (this.sector_ot!=''){
      this.modelo.sector=this.sector_ot;
    }
    if (this.ownership_ot!=''){
      this.modelo.ownership=this.ownership_ot;
    }
    if (this.job_title_ot!=''){
      this.modelo.job_title=this.job_title_ot;
    }
  }
}

