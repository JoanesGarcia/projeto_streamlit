import bcrypt

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDB:
    def __init__(self, st) -> None:
        user = st.secrets.banco.USER
        senha = st.secrets.banco.SENHA
        cluster = st.secrets.banco.CLUSTER
        
        uri = f"mongodb+srv://{user}:{senha}@{cluster}/?retryWrites=true&w=majority"
        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def criptografar_senha(self,senha):
        return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    def verificar_senha(self,senha_digitada, senha_armazenada):
        return bcrypt.checkpw(senha_digitada.encode('utf-8'), senha_armazenada.encode("utf-8"))
    
    def get_login(self, login, senha):
        db = self.client['master']
        collection = db['users']

        result = collection.find({"login": login}) 
        for document in result:
            senha_banco = document["password"]
        self.client.close()
        
        return self.verificar_senha(senha, senha_banco)
