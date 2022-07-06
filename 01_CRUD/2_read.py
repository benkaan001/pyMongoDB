
from config import get_database

import pprint

from bson.objectid import ObjectId


printer = pprint.PrettyPrinter()

dbname=get_database()
kitty_collection=dbname['kitty_collection']




def find_kitties():
    kitties=kitty_collection.find({})
    for kitty in kitties:
        printer.pprint(kitty)


# find_kitties()

def find_fuzzy():
    fuzzy=kitty_collection.find_one({'name':'Fuzzy'})
    printer.pprint(fuzzy)

# find_fuzzy()

def count_kities():
    count= kitty_collection.count_documents(filter={})
    return print('Number of kitties:',count)

# count_kities()

def get_kitty_by_id(kitty_id):
    _id=ObjectId(kitty_id)
    kitty=kitty_collection.find_one({'_id': _id})
    printer.pprint(kitty)

# get_kitty_by_id('62c3885f502fed84bfe3d161')

def get_vaccine_status_by_name(kitty):
    # case-sensitive search ---> MAple.lower() = maple.title() = Maple
    name=kitty.lower().title()
    vaccine_status=kitty_collection.find_one({"name":{"$eq":name}})
    return printer.pprint(vaccine_status)

# get_vaccine_status_by_name('MAple')



def get_age_range(min_age, max_age):
    query =  { "$and": [
            {"age": {"$gte": min_age}},
            {"age": {"$lte": max_age}}
            ]}
    kitty_list=kitty_collection.find(query).sort("age")

    for kitty in kitty_list:
        printer.pprint(kitty['age'])


# get_age_range(1,5)

def project_columns():
    columns ={"_id": 0, "name":1, "age":1}
    kitties= kitty_collection.find({},columns).sort("name")

    for kitty in kitties:
        printer.pprint(kitty)
'''
{'age': 4, 'name': 'Butter Ball'}
{'age': 1, 'name': 'CheakPea'}
{'age': 1, 'name': 'Fussy'}
{'age': 2, 'name': 'Fuzzy'}
{'age': 6, 'name': 'Maple'}
'''
project_columns()