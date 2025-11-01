<div align="center">
🛒 Lojinha Local (Flask) 
  
🛍️Um sistema de e-commerce completo (mini-loja) construído com Python, Flask, SQLAlchemy e Flask-Login.
</div>
<p align="center"><img alt="Status do Projeto" src="https://img.shields.io/badge/Status-Completo-brightgreen?style=for-the-badge"><img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white"><img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"><img alt="SQLAlchemy" src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white"></p>

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📖 Sobre o Projeto

  A Lojinha Local é uma aplicação web full-stack que simula um pequeno site de e-commerce. Ela permite que utilizadores se registem, façam login, naveguem por um catálogo de produtos, adicionem itens ao carrinho e finalizem uma compra.

  O projeto também inclui um painel administrativo (implícito) onde utilizadores logados podem adicionar, editar e gerir os produtos do catálogo, incluindo o upload de imagens.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
✨ Funcionalidades Principais

🔐 Autenticação de Utilizadores: Sistema completo de registo (/register) e login (/login), com gestão de sessão usando Flask-Login.

🔑 Segurança de Senhas: As senhas são "hasheadas" usando Bcrypt antes de serem guardadas na base de dados.

🛍️ Catálogo de Produtos: A página inicial (/) exibe todos os produtos disponíveis na base de dados.

⚙️ Gestão de Produtos (CRUD):

Adicionar novos produtos com imagem (/adicionar_produto).

Editar produtos existentes (/editar_produto/<int:produto_id>).

Remover produtos (diretamente do carrinho, neste caso).

🛒 Carrinho de Compras:

Adicionar produtos ao carrinho (/adicionar_carrinho/<int:produto_id>).

Ver o carrinho detalhado (/carrinho).

Remover itens do carrinho (/remover_carrinho/<int:produto_id>).

💳 Checkout Simulado:

Página de finalização de compra (/checkout) que processa o pedido.

Página de sucesso após a compra (/pedido_sucesso).

🖼️ Upload de Imagens: Sistema de upload seguro para as imagens dos produtos, que são guardadas em static/uploads/.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🛠️ Tecnologias Utilizadas

A pilha de tecnologia principal para este projeto é:

Python:Linguagem principal.

Flask: Framework web.

Flask-SQLAlchemy: ORM para interação com a base de dados.

SQLite: Base de dados (em ficheiro).

Flask-Login: Gestão de sessões de utilizador. 

Flask-Bcrypt: Hashing de senhas.

Flask-WTF: Criação e validação de formulários.

Jinja2: Motor de templates (HTML)

HTML5 & CSS: Estrutura e estilização

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📂 Estrutura do RepositórioO projeto segue uma estrutura modular padrão do Flask:

lojinha_local/

│

├── app.py                  # Ficheiro principal: define rotas e lógica da aplicação

├── models.py               # Define os modelos da base de dados (User, Produto)

├── forms.py                # Define os formulários WTForms

├── extensions.py           # Inicializa as extensões do Flask (db, bcrypt, etc.)

├── requirements.txt        # Lista de dependências Python

│

├── instance/

│   └── lojinha.db          # A base de dados SQLite

│

├── static/

│   ├── style.css           # Folha de estilo

│   └── uploads/            # Onde as imagens dos produtos são guardadas

│

├── templates/

│   ├── base.html           # Template mestre

│   ├── index.html          # Página inicial (catálogo)

│   ├── login.html          # Página de login

│   ├── register.html       # Página de registo

│   ├── adicionar_produto.html # Formulário para adicionar produtos

│   ├── editar_produto.html  # Formulário para editar produtos

│   ├── carrinho.html       # Página do carrinho

│   ├── checkout.html       # Página de checkout

│   └── pedido_sucesso.html # Página de sucesso

│

└── test_app.py             # Testes para a aplicação

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
💿 Como Executar o Projeto Localmente

Siga estes passos para executar a aplicação no seu computador.

Pré-requisitos:

Python 3.10 ou superior.

pip (gestor de pacotes do Python).

Guia de Instalação

1. Clone o repositório: git clone https://github.com/victorhjsantiago/lojinha_local.git

cd lojinha_local

2. Crie e ative um ambiente virtual:

# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate

Instale as dependências: O ficheiro requirements.txt contém todas as bibliotecas necessárias.

pip install -r requirements.txt

Crie a Base de Dados:Execute o seguinte comando no terminal (na raiz do projeto) para criar a base de dados lojinha.db e as tabelas User e Produto:
# Este comando executa o bloco db.create_all() dentro do contexto da app
    flask shell -c "from app import db; db.create_all()"

(Alternativamente, pode adicionar db.create_all() em app.py antes de app.run(), mas a forma acima é mais segura).

Execute a Aplicação: flask run --debug

Aceda à Lojinha:

Abra o seu navegador e vá para http://127.0.0.1:5000 ou http://localhost:5000.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🧪 Testes
O projeto inclui um conjunto de testes em test_app.py. Para executá-los, utilize o pytest:pytest
