import redis
from funcoes import *

r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

usuarios = {
    "1001": {"nome": "Ana", "idade": 25, "cidade": "Recife",
             "ranking_filmes": [("O Poderoso Chefão", 1), ("Interestelar", 2), ("Matrix", 3)]},
    "1002": {"nome": "Carlos", "idade": 30, "cidade": "São Paulo",
             "ranking_filmes": [("Inception", 1), ("Matrix", 2), ("Clube da Luta", 3)]},
    "1003": {"nome": "Maria", "idade": 28, "cidade": "Rio de Janeiro",
             "ranking_filmes": [("Parasita", 1), ("Titanic", 2), ("Interestelar", 3)]}
}

for user_id, dados in usuarios.items():
    salvar_usuario(user_id, dados)

exibir_usuario("1001")  
exibir_usuario("1003")  
