# Projeto-Key-Value-Redis
📌 Descrição

Este projeto tem como objetivo explorar o uso de bancos de dados NoSQL (Redis) aplicando o modelo Key-Value Pair (KVP).

A missão foi modelar, armazenar e consultar informações de usuários e seus rankings de filmes favoritos, utilizando estruturas de dados próprias do Redis como Hash e Sorted Set.
O ambiente foi configurado em uma instância EC2 Windows 11 (AWS Cloud), com as seguintes ferramentas:

Redis for Windows
Python 3.x
Visual Studio Code
Ambiente virtual (venv)

🎯 Missão (extraída da imagem)

Modelar as informações do cenário usando pares de chave/valor.

🗂️ Modelagem

Como modelar o perfil do usuário?
O perfil do usuário foi modelado usando Hash (HSET), contendo atributos como nome, idade e cidade.

Exemplo:

usuario:1001 = {nome: "Ana", idade: 25, cidade: "Recife"}

Como modelar o ranking de filmes favoritos?
O ranking foi modelado usando Sorted Set (ZADD), associando a posição de cada filme ao seu título.

Exemplo:

usuario:1001:ranking = {"O Poderoso Chefão": 1, "Interestelar": 2, "Matrix": 3}

🛠️ Implementação

- Instalação do Redis no Windows EC2
- Criada uma instância EC2 Windows 11 na AWS.
- Instalado o Redis a partir do Redis for Windows
- implementação do memurai for redis para utilização do client
- Configurado para execução local via redis-server.exe.
- Testado o funcionamento com redis-cli.exe ping

  
Desenvolvimento em Python (VS Code)
Instalação do Python 3.x.
Criação de venv para isolamento do ambiente.
Instalação da biblioteca Redis:

pip install redis


Implementação em dois arquivos principais modularizados:

app.py → código principal.

funcoes.py → funções de manipulação dos dados.

Inserção de dados de usuários de exemplo (3–5 usuários)
Foram cadastrados os seguintes usuários:

Ana (Recife)
Carlos (São Paulo)
Maria (Rio de Janeiro)

🔎 Consultas

Recuperar o perfil de um usuário específico
Usando HGETALL no Redis ou a função obter_perfil(user_id) no Python.

Listar o ranking de filmes de um usuário
Usando ZRANGE no Redis ou a função obter_ranking(user_id) no Python.

📂 Estrutura do Projeto
📦 projeto-redis-kvp
 ┣ 📂 venv/      
 ┣ 📜 app.py 
 ┣ 📜 funcoes.py       
 ┗ 📜 README.md        

🚀 Como Executar no Windows EC2
1️⃣ Iniciar o Redis

No prompt de comando:
redis-server.exe

2️⃣ Ativar o ambiente virtual
venv\Scripts\activate

3️⃣ Executar o projeto
python app.py

📌 Exemplo de Saída
Perfil do usuário 1001:
Nome: Ana
Idade: 25
Cidade: Recife

Ranking de filmes:
1 - O Poderoso Chefão
2 - Interestelar
3 - Matrix

🧑‍💻 Tecnologias Utilizadas

- Python 3.17
- Redis NoSql for Windows
- AWS EC2 (Windows 11)
- Visual Studio Code

📘 O que foi aprendido

Durante o desenvolvimento deste projeto, foram absorvidos os seguintes conceitos:

✅ Configuração de uma instância EC2 Windows 11 na AWS.
✅ Instalação e execução do Redis no Windows.
✅ Uso de venv para gerenciar ambientes Python.
✅ Modelagem de dados no Redis usando Hash e Sorted Set.
✅ Criação de funções Python para salvar, recuperar e exibir dados no Redis.
✅ Implementação de consultas chave/valor para perfis e rankings.
