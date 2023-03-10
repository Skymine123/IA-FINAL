#!/usr/bin/env python
# coding: utf-8
##Permite leer el archivo .ipynb
# In[1]:
from flask import Flask
from flask import json
import numpy as np
import pickle
import os
import joblib
# In[2]:
app = Flask(__name__)
# In[2]:
##Crea funcion para llamar al modelo

def predecir_Salario(rating, sector, ownership, job_title, job_in_headquarters, job_seniority, job_skills):
 
 absolutepath = os.path.abspath(__file__)
 fileDirectory = os.path.dirname(absolutepath)
  
 prediction_input = list()
 print(fileDirectory)

 with open(fileDirectory+"/sc_rating.pkl", "rb") as file:
  sc_rating = pickle.load(file) 



 prediction_input.append(sc_rating.transform(np.array(rating).reshape(1, -1)))


 sector_columns = ['sector_Health Care','sector_Business Services','sector_Information Technology']
 temp = list(map(int, np.zeros(shape=(1, len(sector_columns)))[0]))
 for index in range(0, len(sector_columns)):
    if sector_columns[index] == 'sector_' + sector:
      temp[index] = 1
      break
 prediction_input = prediction_input + temp


 if ownership == 'Private':
    prediction_input.append(1)
 else:
    prediction_input.append(0)
  

 job_title_columns = ['job_title_data scientist', 'job_title_data analyst']
 temp = list(map(int, np.zeros(shape=(1, len(job_title_columns)))[0]))
 for index in range(0, len(job_title_columns)):
    if job_title_columns[index] == 'job_title_' + job_title:
      temp[index] = 1
      break
 prediction_input = prediction_input + temp


 prediction_input.append(job_in_headquarters)


 job_seniority_map = {'other': 0, 'jr': 1, 'sr': 2}
 prediction_input.append(job_seniority_map[job_seniority])


 temp = list(map(int, np.zeros(shape=(1, 4))[0]))
 if 'excel' in job_skills:
    temp[0] = 1
 if 'python' in job_skills:
    temp[1] = 1
 if 'tableau' in job_skills:
    temp[2] = 1
 if 'sql' in job_skills:
    temp[3] = 1
 prediction_input = prediction_input + temp
 

 modelo = joblib.load(fileDirectory+'/random_forest.joblib') 
 return modelo.predict([prediction_input])

######


def predecir_Salario1(rating, sector, ownership, job_title, job_in_headquarters, job_seniority, job_skills):
 
 absolutepath = os.path.abspath(__file__)
 fileDirectory = os.path.dirname(absolutepath)
  
 prediction_input = list()
 print(fileDirectory)

 with open(fileDirectory+"/sc_rating.pkl", "rb") as file:
  sc_rating = pickle.load(file) 



 prediction_input.append(sc_rating.transform(np.array(rating).reshape(1, -1)))


 sector_columns = ['sector_Health Care','sector_Business Services','sector_Information Technology']
 temp = list(map(int, np.zeros(shape=(1, len(sector_columns)))[0]))
 for index in range(0, len(sector_columns)):
    if sector_columns[index] == 'sector_' + sector:
      temp[index] = 1
      break
 prediction_input = prediction_input + temp


 if ownership == 'Private':
    prediction_input.append(1)
 else:
    prediction_input.append(0)
  

 job_title_columns = ['job_title_data scientist', 'job_title_data analyst']
 temp = list(map(int, np.zeros(shape=(1, len(job_title_columns)))[0]))
 for index in range(0, len(job_title_columns)):
    if job_title_columns[index] == 'job_title_' + job_title:
      temp[index] = 1
      break
 prediction_input = prediction_input + temp


 prediction_input.append(job_in_headquarters)


 job_seniority_map = {'other': 0, 'jr': 1, 'sr': 2}
 prediction_input.append(job_seniority_map[job_seniority])


 temp = list(map(int, np.zeros(shape=(1, 4))[0]))
 if 'excel' in job_skills:
    temp[0] = 1
 if 'python' in job_skills:
    temp[1] = 1
 if 'tableau' in job_skills:
    temp[2] = 1
 if 'sql' in job_skills:
    temp[3] = 1
 prediction_input = prediction_input + temp
 

 modelo = joblib.load(fileDirectory+'/voting_regressor.joblib') 
 return modelo.predict([prediction_input])[0]
 
from flask import Flask,request
#from flask_mandrill import Mandrill
try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS
 
app.config['MANDRILL_API_KEY'] = '...'
app.config['MANDRILL_DEFAULT_FROM']= '...'
app.config['QOLD_SUPPORT_EMAIL']='...'
app.config['CORS_HEADERS'] = 'Content-Type'

#mandrill = Mandrill(app)
cors = CORS(app)
# In[ ]:
@app.route('/', methods=['GET', 'POST']) 
def obtener_datos():
   
   data = request.get_json()
   
   rating=data.get('rating')
   sector=data.get('sector')
   ownership=data.get('ownership')
   job_title=data.get('job_title')
   job_in_headquarters=data.get('job_in_headquarters')
   job_seniority=data.get('job_seniority')
   job_skills=data.get('job_skills')
   job_skills=job_skills.split(',')
   job_skills.pop()

   print(job_skills)   
   salary=predecir_Salario(rating,sector,ownership,job_title,job_in_headquarters,job_seniority,job_skills)
   salary1=predecir_Salario1(rating,sector,ownership,job_title,job_in_headquarters,job_seniority,job_skills)
   texto='Salario Estimado FOREST REGRESSOR (rango): {}(USD) a {}(USD) por año.'.format((int(salary*1000)-9000), (int(salary*1000)+9000))
   texto1='Salario Estimado VOTING REGRESSOR (rango): {}(USD) a {}(USD) por año.'.format((int(salary1*1000)-9000), (int(salary1*1000)+9000))
   texto2=texto+"\n"+texto1
   print(texto2)
   return json.dumps({"message":texto2})



#salary=predecir_Salario(3.8, 1893, 'Health Care', 'Nonprofit Organization', 'Data Analyst', 1, 'sr', ['python', 'sql', 'tableau'])
#texto='Salario Estimado (rango): {}(USD) a {}(USD) por año.'.format((int(salary*1000)-9000), (int(salary*1000)+9000))
#print(texto)
#return str(texto)aZ
#In[ ]:
if __name__ == '__main__':
    app.run()


#In[ ]:
