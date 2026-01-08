# 🛡️ Sistema de Autenticação Seguro (MySQL + Python)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white)
![Security](https://img.shields.io/badge/Security-Bcrypt_%26_Dotenv-red?style=for-the-badge&logo=security&logoColor=white)

Um sistema de cadastro e login de usuários desenvolvido em Python. O foco principal deste projeto é a **Segurança da Informação**, implementando criptografia de senhas (Hashing), proteção contra SQL Injection e gerenciamento seguro de credenciais via Variáveis de Ambiente.

## 🚀 Funcionalidades de Segurança

Diferente de sistemas básicos, este projeto segue os padrões de mercado:

* **Criptografia de Senha (Hashing):** Utilização da biblioteca `bcrypt` para transformar senhas em hashes irreversíveis com *salt* automático. Nenhuma senha é salva em texto puro.
* **Variáveis de Ambiente (.env):** As credenciais do banco de dados não ficam expostas no código fonte (Hardcoding), prevenindo vazamentos no GitHub.
* **Proteção SQL Injection:** Consultas ao banco utilizam *Prepared Statements* (parâmetros `%s`) para impedir injeção de código malicioso.
* **Verificação de Duplicidade:** O sistema impede que o mesmo e-mail seja cadastrado duas vezes.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **MySQL** (Banco de Dados Relacional)
* **mysql-connector-python** (Driver de conexão)
* **Bcrypt** (Algoritmo de Hashing seguro)
* **Python-Dotenv** (Gerenciamento de variáveis de ambiente)

## 📂 Estrutura do Projeto

O código foi organizado em módulos para facilitar a manutenção:

```bash
auth_system/
│
├── .env                # Arquivo de configuração (NÃO é enviado ao Git)
├── .gitignore          # Bloqueia o envio do .env
├── main.py             # Interface CLI (Menu principal)
├── database.py         # Conexão segura com MySQL
├── auth.py             # Lógica de Login e Registro
└── requirements.txt    # Dependências do projeto
```

## 🧠 O que aprendi com este projeto

Este projeto foi fundamental para solidificar conhecimentos em Backend e Segurança:

* **Hashing vs Encriptação: Entendi que senhas não devem ser descriptografadas, mas sim comparadas via Hash.**

* **MySQL Connector: Aprendi a conectar o Python a um banco de dados real (Server-based) em vez de apenas arquivos locais.**

* **Boas Práticas (Security First): A importância de usar .gitignore e python-dotenv para proteger credenciais sensíveis.**

* **Refatoração: Como transformar um código "spaghetti" em módulos organizados e reutilizáveis.**

---

Desenvolvido por **Pedro Augusto**.
