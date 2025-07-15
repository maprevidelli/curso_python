import pymongo
import datetime
cliente = pymongo.MongoClient("mongodb://localhost:27017/")
# Criar o database:
db = cliente.funcionarios_db
# Criar a Collection funcionarios:
funcionarios_collect = db.funcionarios

funcionario = {"nome" : "Mike",
               "e-mail" : "mike@gmail.com",
               "dob" : datetime.datetime(1989, 10, 25)
               }
funcionarios_collect.insert_one(funcionario)

