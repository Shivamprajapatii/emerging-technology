from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client.SIES

def read():
    try:
        Collection = db.TYIT.find()
        print("\n All data  from SIES DB inside TYIT Collection \n")

        for i in Collection:
            print(i)

    except Exception:
        print(str(e))

read();

