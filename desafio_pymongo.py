import pymongo as pyM
import datetime
import pprint

#conectando com Mongodb
cliente = pyM.MongoClient("mongodb+srv://pmariaeduarda987:1MrhEiaiuOMOFcf3@cluster0.nst0y7p.mongodb.net/?retryWrites=true&w=majority")
base = cliente.test

colecao = base.test_collection


post = {
    "cliente":"Maria",
    "tipo conta":"corrente",
    "Documentos": ["RG","CPF","Contrato"],
    "data": datetime.datetime.utcnow()
}

posts = base.posts

#salvando apenas um colecao/tabela
posts_id = posts.insert_one(post).inserted_id

print(posts_id)


new_post = [{
            "cliente":"Maria",
                "tipo conta":"poupança",
                "Documentos": ["RG","CPF","Contrato"],
                "data": datetime.datetime.utcnow()
               },
{
"cliente":"Carlos",
    "tipo conta":"corrente",
    "Documentos": ["RG","CPF","Contrato"],
    "data": datetime.datetime.utcnow()
}]


#salvando varias coleçoes
inserir_posts = posts.insert_many(new_post)

print(inserir_posts.inserted_ids)

print("Recuperando informações")

#recuperando dados baseado em uma condição
pprint.pprint(base.posts.find_one({"cliente":"Maria"}))

print("Recuperando todos documentos")
print("-"*50)
for posts in posts.find():
    pprint.pprint(f"\n {post} ")
    print("-" * 50)

#contagem
print("contagem de todos documentos")
print("-"*50)

print(inserir_posts.inserted_ids)

base.new_posts.drop()

print(inserir_posts.inserted_ids)
