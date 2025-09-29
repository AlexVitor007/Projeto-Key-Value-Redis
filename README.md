# 🔑 Projeto Key-Value Redis

## 📌 Descrição
Este projeto tem como objetivo explorar o uso de bancos de dados **NoSQL (Redis)** aplicando o modelo **Key-Value Pair (KVP)**.  

A missão foi **modelar, armazenar e consultar informações de usuários e seus rankings de filmes favoritos**, utilizando estruturas de dados próprias do Redis como **Hash** e **Sorted Set**.  

O ambiente foi configurado em uma instância **EC2 Windows 11 (AWS Cloud)**, com as seguintes ferramentas:  
- 🗄️ Redis for Windows (com **Memurai for Redis** para client)  
- 🐍 Python 3.17  
- 💻 Visual Studio Code  
- 🌱 Ambiente virtual (venv)  

---

## 🎯 Missão
> Modelar as informações do cenário usando pares de chave/valor.

---

## 🗂️ Modelagem

### 👤 Perfil do usuário
O perfil foi modelado usando **Hash (HSET)**, contendo atributos como `nome`, `idade` e `cidade`.

📍 Exemplo:
```txt
usuario:1001 = {nome: "Ana", idade: 25, cidade: "Recife"}

🎬 Ranking de filmes

O ranking foi modelado usando Sorted Set (ZADD), associando a posição de cada filme ao seu título.

📍 Exemplo:

usuario:1001:ranking = {"O Poderoso Chefão": 1, "Interestelar": 2, "Matrix": 3}

🛠️ Implementação
📌 Instalação do Redis no Windows EC2

Criada uma instância EC2 Windows 11 na AWS.

Instalado o Redis for Windows.

Implementado o Memurai for Redis para utilização do client.

Configurado para execução local via:

redis-server.exe


Testado o funcionamento:

redis-cli.exe ping


✅ Resposta esperada: PONG

📌 Desenvolvimento em Python (VS Code)

Instalação do Python 3.17

Criação do ambiente virtual (venv)

Instalação da biblioteca Redis:

pip install redis


📂 Estrutura modularizada:

app.py → código principal

funcoes.py → funções auxiliares

👥 Inserção de dados de usuários

Foram cadastrados os seguintes exemplos:

Ana (Recife)

Carlos (São Paulo)

Maria (Rio de Janeiro)

🔎 Consultas

Recuperar o perfil de um usuário específico

Redis:

HGETALL usuario:1001


Python:

obter_perfil("1001")


Listar o ranking de filmes de um usuário

Redis:

ZRANGE usuario:1001:ranking 0 -1 WITHSCORES


Python:

obter_ranking("1001")

📂 Estrutura do Projeto
📦 projeto-redis-kvp
 ┣ 📂 venv/          # Ambiente virtual Python
 ┣ 📜 app.py         # Código principal
 ┣ 📜 funcoes.py     # Funções auxiliares para Redis
 ┗ 📜 README.md      # Documentação

🚀 Como Executar no Windows EC2
1️⃣ Iniciar o Redis
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

🐍 Python 3.17

🗄️ Redis NoSQL for Windows

☁️ AWS EC2 (Windows 11)

💻 Visual Studio Code

📘 O que foi aprendido

Durante o desenvolvimento deste projeto, foram absorvidos os seguintes conceitos:

✅ Configuração de uma instância EC2 Windows 11 na AWS
✅ Instalação e execução do Redis no Windows
✅ Uso de venv para gerenciar ambientes Python
✅ Modelagem de dados no Redis usando Hash e Sorted Set
✅ Criação de funções Python para salvar, recuperar e exibir dados
✅ Implementação de consultas chave/valor para perfis e rankings
