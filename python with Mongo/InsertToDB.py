from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.SIES
def insert():
    try:
        name =input("Enter the Name: ")
        age=input("Enter the Age: ")

        db.TYIT.insert_one(
            {
                "name" : name,
                "age" : age,
            }
        )

        print("Inserted Data Successfully")
    except Exception:
        print(str("Eroor"))

insert()
