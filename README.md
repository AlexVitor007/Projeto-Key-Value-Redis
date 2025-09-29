# 🚀 Projeto-Key-Value-Redis  

## 📌 Descrição  
Este projeto explora o uso de **bancos de dados NoSQL (Redis)** aplicando o modelo **Key-Value Pair (KVP)**.  

- Objetivo: modelar, armazenar e consultar informações de usuários e seus rankings de filmes favoritos.  
- Estruturas utilizadas: **Hash** e **Sorted Set** do Redis.  
- Ambiente configurado em **AWS EC2 (Windows 11)** com:  
  - Redis for Windows  
  - Python 3.x  
  - Visual Studio Code  
  - Ambiente virtual (venv)  

---

## 🎯 Missão  
- Modelar informações do cenário usando pares **chave/valor**.  

---

## 🗂️ Modelagem  

- **Perfil do usuário (Hash - HSET)**  
  ```bash
  usuario:1001 = {nome: "Ana", idade: 25, cidade: "Recife"}
Ranking de filmes favoritos (Sorted Set - ZADD)

bash
Copiar código
usuario:1001:ranking = {"O Poderoso Chefão": 1, "Interestelar": 2, "Matrix": 3}
🛠️ Implementação
Configuração no Windows EC2

Criada instância Windows 11 na AWS

Instalação do Redis for Windows

Implementação do Memurai for Redis para cliente

Execução local via redis-server.exe

Teste de funcionamento: redis-cli.exe ping

Desenvolvimento em Python (VS Code)

Instalação do Python 3.x

Criação de ambiente virtual (venv)

Instalação da biblioteca Redis:

bash
Copiar código
pip install redis
Estrutura modularizada:

app.py → código principal

funcoes.py → funções de manipulação dos dados

Usuários cadastrados (exemplo):

Ana (Recife)

Carlos (São Paulo)

Maria (Rio de Janeiro)

🔎 Consultas
Recuperar perfil do usuário

bash
Copiar código
HGETALL usuario:1001
Ou em Python:

python
Copiar código
obter_perfil(user_id)
Listar ranking de filmes

bash
Copiar código
ZRANGE usuario:1001:ranking 0 -1 WITHSCORES
Ou em Python:

python
Copiar código
obter_ranking(user_id)
📂 Estrutura do Projeto
Copiar código
📦 projeto-redis-kvp
 ┣ 📂 venv/      
 ┣ 📜 app.py 
 ┣ 📜 funcoes.py    
 ┗ 📜 README.md        
🚀 Como Executar no Windows EC2
1️⃣ Iniciar o Redis

bash
Copiar código
redis-server.exe
2️⃣ Ativar o ambiente virtual

bash
Copiar código
venv\Scripts\activate
3️⃣ Executar o projeto

bash
Copiar código
python app.py
📌 Exemplo de Saída
yaml
Copiar código
Perfil do usuário 1001:
Nome: Ana
Idade: 25
Cidade: Recife

Ranking de filmes:
1 - O Poderoso Chefão
2 - Interestelar
3 - Matrix
🧑‍💻 Tecnologias Utilizadas
Python 3.17

Redis NoSQL for Windows

AWS EC2 (Windows 11)

Visual Studio Code

📘 O que foi aprendido
✅ Configuração de instância EC2 Windows 11 na AWS

✅ Instalação e execução do Redis no Windows

✅ Uso de venv para gerenciamento de ambientes Python

✅ Modelagem de dados no Redis com Hash e Sorted Set

✅ Criação de funções Python para salvar, recuperar e exibir dados

✅ Consultas chave/valor para perfis e rankings
