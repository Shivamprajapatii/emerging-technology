from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client.SIES

def delete():
    try:
        name= input("\n Enter name to Delete: ")

        db.TYIT.delete_one(
            {"name":name},
        )

        print("\n Record Deleted Succesfully \n")

    except Exception as e:
        print("error str(e)")

delete()
