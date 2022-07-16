def get_database():
    from pymongo import MongoClient
    from dotenv import load_dotenv, find_dotenv
    import os

    # instead of indicating the absolute path for the .env file, we can use find_dotenv() mehtod
    load_dotenv(find_dotenv())

    password= os.environ.get("MONGODB_PWD")

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f"mongodb+srv://benkaan:{password}@nodejs.xqscs.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    # alternatively ---> client=MongoClient("mongodb://localhost:27017")

    # Create the database for our example (we will use the same database throughout the tutorial
    return client["jeopardy_db"]

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

    # Get the database
    dbname = get_database()