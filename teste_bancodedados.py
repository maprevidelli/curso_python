# Conexão com o MongoDB - Pymongo
import pymongo
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
for collection in client.catalogo.list_collection_names():
    print(collection)

#for db in cliente.list_databases():
#print(db)



    