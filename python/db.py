import pyrebase

config = {
    "apiKey": "AIzaSyDmqGZvEC5RU_tjwSXqMgDfnpCy3MTjkWg",
    "authDomain": "parklk.firebaseapp.com",
    "databaseURL": "https://parklk.firebaseio.com",
    "projectId": "parklk",
    "storageBucket": "parklk.appspot.com",
    "messagingSenderId": "610767984527",
    "appId": "1:610767984527:web:766af8b0892ba128955dfa"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def updateSpots(free,notFree,spot01,spot02,spot03,spot04,spot05,spot06,spot07,spot08):
    db.child("AllSpots").update({"Free": free, "Occupied":notFree})
    db.child("Spot01").update({"Availability":spot01})
    db.child("Spot02").update({"Availability":spot02})
    db.child("Spot03").update({"Availability":spot03})
    db.child("Spot04").update({"Availability":spot04})
    db.child("Spot05").update({"Availability":spot05})
    db.child("Spot06").update({"Availability":spot06})
    db.child("Spot07").update({"Availability":spot07})
    db.child("Spot08").update({"Availability":spot08})
    return
