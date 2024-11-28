import pyrebase
import json
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, firestore


# from grandeurs.models import Grandeur, Mesure 

firebase_config = {
  "apiKey": "AIzaSyDfG5PYEClsnK5DA2AKauoHNwzbgdDoUh8",
  "authDomain": "gestiongrandeurs.firebaseapp.com",
  "databaseURL": "https://gestiongrandeurs-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "gestiongrandeurs",
  "storageBucket": "gestiongrandeurs.firebasestorage.app",
  "messagingSenderId": "70857390853",
  "appId": "1:70857390853:web:ac4b722092b59a1cc9156c"
}

firebase=pyrebase.initialize_app(firebase_config)
database=firebase.database()


cred = credentials.Certificate(r"C:/Users/Oussama/Desktop/IOTProjectProgress/key.json")
firebase_admin.initialize_app(cred)

db_firestore = firestore.client()

def persistData(message):
    #Firebase: RealTime DB
    json_object = json.loads(message)
    json_object['time']= str(datetime.now())
    # Firebase Realtime db persist data
    database.child('temperature').push(json_object)
    # Firebase firestore persist data
    doc_ref = db_firestore.collection("temperature").document()
    doc_ref.set(json_object)
