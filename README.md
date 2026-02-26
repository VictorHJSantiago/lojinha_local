<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/3514/3514491.png" alt="Lojinha Local Logo" width="110" />

# 🛒 Lojinha Local — E-commerce com Flask

**Um sistema de e-commerce completo (mini-loja) construído com**
**Python, Flask, SQLAlchemy e Flask-Login.**

<br>

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completo-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## 📚 Tabela de Conteúdos

> Navegue rapidamente pelas seções do projeto.

| # | Seção |
|:-:|:------|
| 1 | [📖 Sobre o Projeto](#-sobre-o-projeto) |
| 2 | [✨ Funcionalidades Principais](#-funcionalidades-principais) |
| 3 | [🛠️ Pilha de Tecnologias](#️-pilha-de-tecnologias) |
| 4 | [🗺️ Mapa de Rotas da Aplicação](#️-mapa-de-rotas-da-aplicação) |
| 5 | [📂 Estrutura do Repositório](#-estrutura-do-repositório) |
| 6 | [🚀 Como Executar Localmente](#-como-executar-localmente) |
| 7 | [🧪 Testes](#-testes) |
| 8 | [🤝 Como Contribuir](#-como-contribuir) |
| 9 | [👨‍💻 Autor](#-autor) |
| 10 | [📄 Licença](#-licença) |

---

## 📖 Sobre o Projeto

> **Lojinha Local** é uma aplicação web **full-stack** que simula um pequeno site de e-commerce completo, do catálogo ao checkout.

A aplicação permite que usuários se registrem, façam login, naveguem por um catálogo de produtos, adicionem itens ao carrinho e finalizem uma compra. O projeto também conta com um **painel de gestão de produtos** onde usuários autenticados podem adicionar, editar e gerenciar o catálogo com upload de imagens.

---

## ✨ Funcionalidades Principais

| Ícone | Funcionalidade | Descrição |
|:-----:|:---------------|:----------|
| 🔐 | **Autenticação de Usuários** | Registro (`/register`) e login (`/login`) completos com gestão de sessão via `Flask-Login`. |
| 🔑 | **Segurança de Senhas** | Senhas armazenadas com hash seguro usando `Flask-Bcrypt` — nunca salvas em texto puro. |
| 🛍️ | **Catálogo de Produtos** | Página inicial (`/`) exibe todos os produtos disponíveis com imagem e preço. |
| ➕ | **Adicionar Produto** | Upload de novo produto com imagem via `/adicionar_produto`. |
| ✏️ | **Editar Produto** | Edição de produtos existentes via `/editar_produto/<int:produto_id>`. |
| 🛒 | **Carrinho de Compras** | Adicionar, visualizar e remover itens do carrinho de forma dinâmica. |
| 💳 | **Checkout Simulado** | Página de finalização (`/checkout`) com processamento do pedido e página de sucesso. |
| 🖼️ | **Upload de Imagens** | Sistema de upload seguro — imagens dos produtos salvas em `static/uploads/`. |

---

## 🛠️ Pilha de Tecnologias

| Tecnologia | Função no Projeto |
|:-----------|:------------------|
| **Python 3.11+** | Linguagem principal de toda a lógica da aplicação. |
| **Flask** | Framework web que gerencia rotas, requisições e respostas. |
| **Flask-SQLAlchemy** | ORM para modelagem e interação com o banco de dados SQLite. |
| **SQLite** | Banco de dados relacional em arquivo (`instance/lojinha.db`). |
| **Flask-Login** | Gerenciamento de sessões de usuário e proteção de rotas autenticadas. |
| **Flask-Bcrypt** | Hashing seguro de senhas antes do armazenamento. |
| **Flask-WTF** | Criação e validação de formulários com proteção CSRF integrada. |
| **Jinja2** | Motor de templates para renderização dinâmica do HTML. |
| **HTML5 & CSS3** | Estrutura e estilização das páginas da aplicação. |

---

## 🗺️ Mapa de Rotas da Aplicação

| Método | Rota | Autenticação | Descrição |
|:------:|:-----|:------------:|:----------|
| `GET` | `/` | — | Página inicial com o catálogo completo de produtos. |
| `GET/POST` | `/register` | — | Formulário de cadastro de novo usuário. |
| `GET/POST` | `/login` | — | Formulário de login. |
| `GET` | `/logout` | ✅ | Encerramento da sessão do usuário. |
| `GET/POST` | `/adicionar_produto` | ✅ | Formulário para adicionar novo produto com imagem. |
| `GET/POST` | `/editar_produto/<int:id>` | ✅ | Formulário para editar produto existente. |
| `GET` | `/adicionar_carrinho/<int:id>` | ✅ | Adiciona um produto ao carrinho. |
| `GET` | `/carrinho` | ✅ | Visualização detalhada do carrinho. |
| `GET` | `/remover_carrinho/<int:id>` | ✅ | Remove um item do carrinho. |
| `GET/POST` | `/checkout` | ✅ | Página de finalização e processamento do pedido. |
| `GET` | `/pedido_sucesso` | ✅ | Confirmação de pedido realizado com sucesso. |

---

## 📂 Estrutura do Repositório

```plaintext
lojinha_local/
│
├── 📄 app.py                        # 🧠 Arquivo principal — rotas e lógica da aplicação ← CORE
├── 📄 models.py                     # 🏛️  Modelos do banco de dados (User, Produto)
├── 📄 forms.py                      # 📝 Formulários WTForms (login, registro, produto)
├── 📄 extensions.py                 # 🔌 Inicialização das extensões Flask (db, bcrypt, login)
├── 📄 requirements.txt              # 📦 Lista de dependências Python
├── 📄 test_app.py                   # 🧪 Suite de testes da aplicação
│
├── 📁 instance/
│   └── 📄 lojinha.db                # 🗃️  Banco de dados SQLite (gerado automaticamente)
│
├── 📁 static/
│   ├── 📄 style.css                 # 🎨 Folha de estilos global
│   └── 📁 uploads/                  # 🖼️  Imagens dos produtos (gerado no upload)
│
└── 📁 templates/
    ├── 📄 base.html                 # 🏗️  Template mestre (herança de todos os outros)
    ├── 📄 index.html                # 🏠 Página inicial — catálogo de produtos
    ├── 📄 login.html                # 🔐 Página de login
    ├── 📄 register.html             # 📋 Página de registro
    ├── 📄 adicionar_produto.html    # ➕ Formulário de novo produto
    ├── 📄 editar_produto.html       # ✏️  Formulário de edição de produto
    ├── 📄 carrinho.html             # 🛒 Visualização do carrinho
    ├── 📄 checkout.html             # 💳 Página de finalização de compra
    └── 📄 pedido_sucesso.html       # ✅ Confirmação de pedido
```

---

## 🚀 Como Executar Localmente

### 📋 Pré-requisitos

| Requisito | Detalhe |
|:----------|:--------|
| **Python** | Versão **3.10 ou superior** instalada e configurada no `PATH`. |
| **pip** | Gerenciador de pacotes do Python (incluso na instalação padrão). |
| **Git** | Para clonar o repositório. |

---

### 🔧 Passo a Passo

**1. Clone o repositório:**

```bash
git clone https://github.com/VictorHJesusSantiago/lojinha_local.git
cd lojinha_local
```

**2. Crie e ative o ambiente virtual:**

```bash
# Criar o ambiente
python -m venv venv

# Ativar no Windows
.\venv\Scripts\activate

# Ativar no macOS / Linux
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Crie o banco de dados:**

```bash
# Forma recomendada — via Flask shell
flask shell -c "from app import db; db.create_all()"
```

> 💡 Este comando cria o arquivo `instance/lojinha.db` com as tabelas `User` e `Produto`.

**5. Execute a aplicação:**

```bash
flask run --debug
```

---

### 🛰️ Acesso à Aplicação

| Serviço | URL |
|:--------|:----|
| 🏠 **Loja (Página Inicial)** | `http://localhost:5000` |
| 🔐 **Login** | `http://localhost:5000/login` |
| 📋 **Registro** | `http://localhost:5000/register` |
| ➕ **Adicionar Produto** | `http://localhost:5000/adicionar_produto` |

---

## 🧪 Testes

> O projeto inclui uma suite de testes em `test_app.py`.

```bash
# Executar todos os testes
pytest

# Executar com saída detalhada
pytest -v
```

---

## 🤝 Como Contribuir

> Contribuições são muito bem-vindas! Siga as etapas abaixo para colaborar de forma organizada.

| Passo | Ação | Comando |
|:-----:|:-----|:--------|
| 1️⃣ | **Fork** | Crie um fork do repositório para a sua conta. | — |
| 2️⃣ | **Branch** | Crie sua feature branch a partir da `main`. | `git checkout -b feature/NovaFeature` |
| 3️⃣ | **Commit** | Salve as alterações com mensagem clara e semântica. | `git commit -m 'feat: Adiciona NovaFeature'` |
| 4️⃣ | **Push** | Envie a branch para o repositório remoto. | `git push origin feature/NovaFeature` |
| 5️⃣ | **Pull Request** | Abra um PR detalhando as mudanças realizadas. | — |

<div align="center">

<br>

**Se este projeto foi útil para os seus estudos, deixe uma estrela ⭐️ no repositório!**

</div>

---

## 👨‍💻 Autor

<div align="center">

<br>

**Victor H. J. Santiago**

<br>

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VictorHJesusSantiago)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-henrique-de-jesus-santiago/)

</div>

---

## 📄 Licença

<div align="center">

Este projeto está distribuído sob a **Licença MIT**.
Consulte o arquivo [`LICENSE`](./LICENSE) no repositório para mais informações.

![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

<div align="center">

*Feito com 🛒 e Flask por **Victor H. J. Santiago***

</div>
