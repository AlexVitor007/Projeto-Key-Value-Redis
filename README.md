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
```
🎬 Ranking de filmes

O ranking foi modelado usando Sorted Set (ZADD), associando a posição de cada filme ao seu título.

📍 Exemplo:
```txt
usuario:1001:ranking = {"O Poderoso Chefão": 1, "Interestelar": 2, "Matrix": 3}
```
🛠️ Implementação
📌 Instalação do Redis no Windows EC2

1. Criada uma instância EC2 Windows 11 na AWS.
2. Instalado o Redis for Windows.
3. Implementado o Memurai for Redis para utilização do client.
4. Configurado para execução local via:
```cmd
redis-server.exe
```
5. Testado o funcionamento:
```cmd
redis-cli.exe ping
```
✅ Resposta esperada: PONG

📌 Desenvolvimento em Python (VS Code)

- Instalação do Python 3.17

- Criação do ambiente virtual (venv)

- Instalação da biblioteca Redis:
```cmd
pip install redis
```
📂 Estrutura modularizada:

- app.py → código principal

- funcoes.py → funções auxiliares

👥 Inserção de dados de usuários

- Foram cadastrados os seguintes exemplos:
```txt
Ana (Recife)

Carlos (São Paulo)

Maria (Rio de Janeiro)
```

