from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient


load_dotenv(find_dotenv())

password= os.environ.get("MONGODB_PWD")
connection_string= f"mongodb+srv://benkaan:{password}@nodejs.xqscs.mongodb.net/?retryWrites=true&w=majority"

client=MongoClient(connection_string)


db_list=client.list_database_names()
print(db_list)

client.close()
print('connection closed')