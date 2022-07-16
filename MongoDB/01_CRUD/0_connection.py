# print('hello world test123')
from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient


load_dotenv(find_dotenv())
# load_dotenv("/Users/benkaan/Desktop/py_mongoDB/.env")


password= os.environ.get("MONGODB_PWD")
connection_string= f"mongodb+srv://benkaan:{password}@nodejs.xqscs.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connection_string)
# client= MongoClient('mongodb://localhost:27017/')


db_list=client.list_database_names()
print(db_list)

client.close()
print('connection closed')