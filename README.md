# 🚢 shiptasks

API multi-container de gestão de tarefas — construída pra praticar Docker Compose, MongoDB, autenticação JWT e um pipeline completo de CI/CD, do commit ao servidor em produção.

🌐 **Deploy:** [3.142.92.226:8000/docs](http://3.142.92.226:8000/docs) — hospedado numa instância AWS EC2 configurada manualmente.

## 📋 Funcionalidades

- Cadastro e autenticação de usuários com JWT e senha criptografada (bcrypt)
- CRUD de tarefas: criar, listar, marcar como feita, deletar
- Rotas de escrita protegidas por token; listagem pública
- Documentação interativa automática (Swagger)

## 📁 Estrutura do Projeto

shiptasks/
├── docker-compose.yml
├── .github/
│ └── workflows/
│ └── deploy.yml
└── api/
├── Dockerfile
├── requirements.txt
├── main.py
├── database.py
├── auth.py
├── models/
│ ├── todo.py
│ └── usuario.py
├── schemas/
│ ├── todo.py
│ └── usuario.py
├── services/
│ ├── todo_service.py
│ └── usuario_service.py
└── routes/
├── todo.py
└── usuario.py


## ▶️ Como rodar localmente

1. Crie um arquivo `.env` na raiz do projeto:

MONGO_PASSWORD=sua_senha_aqui
SECRET_KEY=sua_chave_secreta_aqui

2. Suba os containers (API + MongoDB):

docker compose up --build

3. Acesse a documentação interativa em `http://localhost:8000/docs`

## 🚀 Deploy e CI/CD

O deploy acontece automaticamente a cada push na branch `main`, via GitHub Actions:

1. **CI** — builda a imagem Docker da API numa máquina limpa, garantindo que o projeto compila sem erro antes de qualquer publicação
2. **CD** — se o CI passar, conecta via SSH numa instância AWS EC2 (Ubuntu), atualiza o código (`git pull`) e reinicia os containers (`docker compose up --build -d`)

A instância EC2 foi provisionada manualmente pelo console da AWS (sem Terraform/Ansible), usando um usuário IAM com permissões restritas apenas ao EC2 — não a conta raiz.

## 🛠️ Tecnologias

- Python
- FastAPI
- MongoDB (PyMongo)
- JWT (autenticação)
- Passlib/Bcrypt (hash de senha)
- Docker e Docker Compose
- GitHub Actions (CI/CD)
- AWS EC2

## 📚 Conceitos aplicados

- API RESTful com rotas GET, POST, PUT e DELETE
- Banco de dados NoSQL orientado a documentos (MongoDB), com conversão explícita de `ObjectId`
- Schemas de entrada/saída (Pydantic) separados dos models do banco
- Autenticação com JWT e hash de senha com bcrypt; erro 401 genérico no login para evitar enumeração de usuários
- Containerização multi-serviço com Docker Compose, incluindo healthcheck e volumes persistentes
- Orquestração de rede entre containers (resolução de nomes de serviço, sem uso de `localhost`)
- Pipeline de CI/CD com GitHub Actions, incluindo dependência entre jobs (`needs`) e segredos protegidos (`GitHub Secrets`)
- Deploy manual em servidor AWS EC2, com controle de acesso via Security Groups e IAM de privilégio mínimo
