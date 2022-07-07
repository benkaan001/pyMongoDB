
import pprint

from config import get_database

dbname=get_database()

jeopardy_collection=dbname['jeopardy']

printer = pprint.PrettyPrinter()


def create_documents():
    #sample doc
    docs={"category": "HISTORY", "air_date": "2004-12-31", "question": "'For the last 8 years of his life, Galileo was under house arrest for espousing this man's theory'", "value": "$200", "answer": "Copernicus", "round": "Jeopardy!", "show_number": "4680"}

    jeopardy_collection.insert_one(docs)

# create_documents()