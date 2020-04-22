import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./ServiceAccount.json")
default_app=firebase_admin.initialize_app(cred)
db = firestore.client()

def updateSpots(free,notFree,spot01,spot02,spot03,spot04,spot05,spot06,spot07,spot08):
    data = {
    u'availability': spot01,
    u'slot': u'1',
    }
    db.collection(u'parking').document(u'1').set(data)

    data = {
    u'availability': spot02,
    u'slot': u'2',
    }
    db.collection(u'parking').document(u'2').set(data)

    data = {
    u'availability': spot03,
    u'slot': u'3',
    }
    db.collection(u'parking').document(u'3').set(data)

    data = {
    u'availability': spot04,
    u'slot': u'4',
    }
    db.collection(u'parking').document(u'4').set(data)

    data = {
    u'availability': spot05,
    u'slot': u'5',
    }
    db.collection(u'parking').document(u'5').set(data)

    data = {
    u'availability': spot06,
    u'slot': u'6',
    }
    db.collection(u'parking').document(u'6').set(data)

    data = {
    u'availability': spot07,
    u'slot': u'7',
    }
    db.collection(u'parking').document(u'7').set(data)

    data = {
    u'availability': spot08,
    u'slot': u'8',
    }
    db.collection(u'parking').document(u'8').set(data)

    print("updated database")