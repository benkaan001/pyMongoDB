import pprint

from config import get_database

client=get_database()
dbname=client.jeopardy_db
jeopardy_collection=dbname["jeopardy"]

printer=pprint.PrettyPrinter()

def fuzzy_matching():
    # searh category that has like%computer%
    result=jeopardy_collection.aggregate([
        {"$search": {
            "index": "language_search",
            "text": {
                "query": "computer",
                "path": "category",
                "fuzzy": {}
            }
        }}
    ])

    printer.pprint(list(result))

fuzzy_matching()

