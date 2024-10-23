from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client.SIES

def update():
    try:
        name= input("\n Enter the Name: ")
        age= input("\n Enter age to Update: ")

        #Some time update only some time update_one
        
        db.TYIT.update_one(
            {"name":name},
            {"$set": {"age":age}}
        )

        print("\n Record Updated Succesfully \n")

    except Exception as e:
        print("error str(e)")

update()
    
