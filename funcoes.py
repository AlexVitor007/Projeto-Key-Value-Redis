import redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


def salvar_usuario(user_id, dados):
    r.hset(f"usuario:{user_id}", mapping={
        "nome": dados["nome"],
        "idade": dados["idade"],
        "cidade": dados["cidade"]
    })


    chave_Ranking = f"usuario:{user_id}:ranking_Filmes"
    r.delete(chave_Ranking) 
    for filme, posicao in dados["ranking_filmes"]:
        r.zadd(chave_Ranking, {filme: posicao})


def obter_perfil(user_id):
    return r.hgetall(f"usuario:{user_id}")


def obter_ranking(user_id):
    return r.zrange(f"usuario:{user_id}:ranking_Filmes", 0, -1, withscores=True)


def exibir_usuario(user_id):
    perfil = obter_perfil(user_id)
    print(f"\nPerfil do usuário {user_id}:")
    for campo, valor in perfil.items():
        print(f"{campo.capitalize()}: {valor}")

    ranking = obter_ranking(user_id)
    print("\nRanking de filmes:")
    for filme, posicao in ranking:
        print(f"{int(posicao)} - {filme}")

