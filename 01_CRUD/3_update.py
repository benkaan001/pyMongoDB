import pprint
from config import get_database
from bson.objectid import ObjectId

printer=pprint.PrettyPrinter()

dbname=get_database()
kitty_collection=dbname["kitty_collection"]

def update_kitty_by_id(kitty_id):
    _id=ObjectId(kitty_id)

    updates= { "$set": { "temp_field" : "I SHALL GET DELETED!"},
               "$inc": { "age" : 1 },
               "$rename": {"isVaccinated": "receivedBooster"}
             }

    kitty_collection.update_one({"_id": _id},updates)
    return printer.pprint(kitty_collection.find_one({"_id": _id}))

# update_kitty_by_id("62c3885f502fed84bfe3d160")

def update_kitty_by_id(kitty_id):
    _id=ObjectId(kitty_id)
    # need to pass an empty string as value to unset/delete the temp_field
    kitty_collection.update_one({"_id": _id}, {"$unset": {"temp_field": ""}})

# update_kitty_by_id("62c3885f502fed84bfe3d160")


def replace_document(kitty_id):
    _id=ObjectId(kitty_id)

    new_doc = {
        "name": "vacant slot",
        "age": 0,
        "isVaccinated": False
    }

    kitty_collection.replace_one({"_id":_id}, new_doc)

# replace_document("62c3885f502fed84bfe3d160")
