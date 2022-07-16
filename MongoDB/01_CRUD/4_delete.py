import pprint
from config import get_database
from bson.objectid import ObjectId

printer=pprint.PrettyPrinter()

dbname=get_database()
kitty_collection=dbname["kitty_collection"]

def delete_doc_by_id(kitty_id):
    _id=ObjectId(kitty_id)
    kitty_collection.delete_one({"_id":_id})

# delete_doc_by_id("62c3885f502fed84bfe3d161")

def delete_many_by_name(name):
    kitty_collection.delete_many({"name": name})

# since there are duplicate records, this will remove all Fussy's
# delete_many_by_name("Fussy")

