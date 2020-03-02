from math import sin, cos, sqrt, atan2, radians
from tinydb import TinyDB, where
from tinydb import Query

mapdb = TinyDB('db/strmap.json')
storedb = TinyDB('db/stores.json')
productdb = TinyDB('db/product.json')
Map = Query()
# mapdb.insert({"name":"DEL007","latitude": 28.459593, "longitude": 76.4569593, "fence": 30})

R = 6373.0
#helper functions
def proxy(longi1, lati1, longi2, lati2, thresh):
    lati1 = radians(float(lati1))
    longi1 = radians(float(longi1))
    lati2 = radians(float(lati2))
    longi2 = radians(float(longi2))
    dlon = longi2 - longi1
    dlat = lati2 - lati1

    a = sin(dlat / 2)**2 + cos(float(lati1)) * cos(float(lati2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    if(distance<= float(thresh)):
        return True
    else :
        return False

#active functions    
def match(longi,lati):
    data = mapdb.all()
    for i in data:
        if proxy(i['longitude'], i['latitude'], longi,lati,i['fence']):
            return i['name']
    return 'DEF002'

def storedata(strcode):
    print(strcode)
    return storedb.search(Map.srtid == strcode)

def getobj(id):
    print("Fetching object {}".format(id))
    print(productdb.get(doc_id=id))
    return productdb.get(doc_id=id)

