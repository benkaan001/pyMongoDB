
import pprint

from config import get_database

dbname=get_database()

kitty_collection=dbname['kitty_collection']

printer = pprint.PrettyPrinter()


def create_documents():
    names=['Maple','Fuzzy','CheakPea','Fussy','Butter Ball']
    ages=[6,2,1,1,4]
    isVaccinated=[True,True,False,False,True]

    docs=[]

    for name,age,vaccine_status in zip(names,ages,isVaccinated):
        doc={'name':name, 'age':age, 'isVaccinated': vaccine_status}
        docs.append(doc)

    kitty_collection.insert_many(docs)

# create_documents()

