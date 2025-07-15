# Conexão com o MongoDB - Pymongo
import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
for collection in cliente.catalago.list_collection_names():
    print(collection)

for livros in cliente.catalago.list_collections():
    print(livros)