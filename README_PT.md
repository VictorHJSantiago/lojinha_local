<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/3514/3514491.png" alt="Lojinha Local Logo" width="110" />

# 🛒 Lojinha Local

### Documentação de Engenharia de Software & Sistema de E-commerce

Uma aplicação full-stack de e-commerce construída com **Python, Flask, SQLAlchemy e Flask-Bcrypt**, documentada de ponta a ponta seguindo os clássicos artefatos de Engenharia de Software (Requisitos, UML, Modelagem de Dados, DFD, UX).

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20Andamento-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### 🌐 Choose Language / Selecione o idioma / Elija su idioma

[![English](https://img.shields.io/badge/ENGLISH-README.MD-blue?style=for-the-badge)](./README.md)
[![Português](https://img.shields.io/badge/PORTUGU%C3%8AS-ATUAL-brightgreen?style=for-the-badge)](./README_PT.md)
[![Español](https://img.shields.io/badge/ESPAÑOL-README__ES.MD-yellow?style=for-the-badge)](./README_ES.md)

</div>

---

## 📖 Sobre o Projeto

> **Lojinha Local** é uma aplicação web full-stack que simula uma pequena loja local: catálogo, carrinho de compras e checkout, além de um painel autenticado para gerenciar produtos.

Este README é o **hub de documentação de engenharia** do projeto. Ele segue uma estrutura clássica de documentação de Engenharia de Software — requisitos, casos de uso, diagramas UML, modelagem de dados, fluxo de dados, arquitetura e artefatos de UX — construída em torno da implementação real (Flask + SQLAlchemy + SQLite).

> 🚧 **Status:** As seções **1. Requisitos** e **2. Casos de Uso** estão totalmente escritas. As demais seções (3–10) estão estruturadas e serão preenchidas de forma incremental.

---

## 📑 Sumário

| # | Seção | Status |
|:-:|:------|:------:|
| 1 | [📋 Requisitos](#1--requisitos) | ✅ |
| 2 | [🎯 Casos de Uso](#2--casos-de-uso) | ✅ |
| 3 | [🔗 Matriz de Rastreabilidade de Requisitos](#3--matriz-de-rastreabilidade-de-requisitos) | 🚧 |
| 4 | [📄 Documento de Especificação de Requisitos (SRS)](#4--documento-de-especificação-de-requisitos-srs) | 🚧 |
| 5 | [🖼️ Diagramas UML & Estruturais](#5--diagramas-uml--estruturais) | 🚧 |
| 6 | [🗄️ Modelo de Dados & Dicionário de Dados](#6--modelo-de-dados--dicionário-de-dados) | 🚧 |
| 7 | [🌊 Diagrama de Fluxo de Dados (DFD)](#7--diagrama-de-fluxo-de-dados-dfd) | 🚧 |
| 8 | [🏗️ Diagrama de Arquitetura & Fluxograma](#8--diagrama-de-arquitetura--fluxograma) | 🚧 |
| 9 | [🧑 Persona & Mapa de Jornada do Usuário](#9--persona--mapa-de-jornada-do-usuário) | 🚧 |
| 10 | [🎨 Wireframes & Mockups](#10--wireframes--mockups) | 🚧 |
| 11 | [🚀 Instalação & Execução](#11--instalação--execução) | ✅ |
| 12 | [👨‍💻 Autor](#12--autor) | ✅ |

---

## 1. 📋 Requisitos

<details>
<summary><strong>1.1 Requisitos Funcionais (RF)</strong></summary>

| ID | Requisito | Prioridade |
|:---|:----------|:----------:|
| RF01 | O sistema deve permitir que novos usuários se cadastrem com um nome de usuário único e senha. | Alta |
| RF02 | O sistema deve permitir que usuários cadastrados façam login com usuário e senha. | Alta |
| RF03 | O sistema deve permitir que usuários autenticados façam logout, encerrando a sessão. | Alta |
| RF04 | O sistema deve exibir o catálogo de todos os produtos na página inicial (nome, preço, descrição, imagem). | Alta |
| RF05 | O sistema deve permitir que usuários autenticados adicionem novos produtos, incluindo upload opcional de imagem. | Alta |
| RF06 | O sistema deve permitir que usuários autenticados editem produtos existentes (nome, descrição, preço, imagem). | Alta |
| RF07 | O sistema deve permitir que usuários autenticados excluam produtos, removendo o arquivo de imagem associado do armazenamento. | Média |
| RF08 | O sistema deve permitir que usuários autenticados adicionem um produto ao seu carrinho de compras pessoal. | Alta |
| RF09 | O sistema deve incrementar a quantidade de um item já existente no carrinho caso o mesmo produto seja adicionado novamente. | Média |
| RF10 | O sistema deve exibir o carrinho com nome do item, preço unitário, quantidade, subtotal e total geral. | Alta |
| RF11 | O sistema deve permitir que usuários autenticados removam itens individuais do carrinho. | Média |
| RF12 | O sistema deve fornecer um formulário de checkout exigindo nome completo e e-mail do cliente. | Média |
| RF13 | O sistema deve esvaziar o carrinho do usuário após um checkout bem-sucedido e redirecionar para uma página de confirmação de pedido. | Alta |
| RF14 | O sistema deve persistir usuários, produtos e itens de carrinho em um banco de dados relacional (SQLite). | Alta |

</details>

<details>
<summary><strong>1.2 Requisitos Não Funcionais (RNF)</strong></summary>

| ID | Requisito | Categoria |
|:---|:----------|:---------:|
| RNF01 | As senhas devem ser armazenadas com hash unidirecional (Bcrypt), nunca em texto puro. | Segurança |
| RNF02 | Todos os formulários devem ser protegidos contra ataques CSRF via tokens do Flask-WTF. | Segurança |
| RNF03 | Rotas que criam/modificam dados (produtos, carrinho, checkout) devem exigir sessão autenticada. | Segurança |
| RNF04 | Imagens enviadas devem ser limitadas a 16 MB e armazenadas com nome de arquivo aleatório para evitar colisões. | Segurança / Confiabilidade |
| RNF05 | Operações padrão de catálogo e carrinho devem responder em menos de 1 segundo sob carga local normal. | Desempenho |
| RNF06 | A interface deve ser legível e utilizável tanto em desktop quanto em dispositivos móveis. | Usabilidade |
| RNF07 | Toda ação que altere o estado deve fornecer feedback claro ao usuário via mensagens flash. | Usabilidade |
| RNF08 | O código deve estar organizado em módulos claros (models, forms, rotas, templates) para facilitar a manutenção. | Manutenibilidade |
| RNF09 | A aplicação deve rodar em qualquer SO com Python 3.10+, sem dependências nativas extras (SQLite é baseado em arquivo). | Portabilidade |
| RNF10 | Os fluxos críticos (autenticação, catálogo, carrinho) devem ser cobertos por testes automatizados (pytest). | Testabilidade |

</details>

<details>
<summary><strong>1.3 Regras de Negócio (RN)</strong></summary>

| ID | Regra |
|:---|:------|
| RN01 | Um nome de usuário deve ser único em todo o sistema; cadastros duplicados são rejeitados. |
| RN02 | Um produto deve ter nome e preço maior que zero; descrição e imagem são opcionais. |
| RN03 | Se nenhuma imagem for fornecida para um produto, o sistema utiliza uma imagem padrão (`default.jpg`). |
| RN04 | Um carrinho pertence a exatamente um usuário; adicionar o mesmo produto novamente incrementa sua quantidade em vez de duplicar o registro. |
| RN05 | O total do carrinho é igual à soma de (preço unitário × quantidade) de todos os itens. |
| RN06 | O checkout só é permitido quando o carrinho não está vazio. |
| RN07 | Um checkout bem-sucedido esvazia completamente o carrinho do usuário. |
| RN08 | Quando a imagem de um produto é substituída ou o produto é excluído, o arquivo de imagem anterior é removido do disco (exceto a imagem padrão). |
| RN09 | Apenas usuários autenticados podem gerenciar o catálogo (criar/editar/excluir produtos) e seu próprio carrinho. |
| RN10 | Um usuário só pode visualizar e modificar seu próprio carrinho, nunca o de outro usuário. |

</details>

<details>
<summary><strong>1.4 Requisitos de Domínio</strong></summary>

O sistema modela o domínio de uma **loja local com um único vendedor (B2C)**:

- **Conta**: cada cliente/gestor possui uma conta (`User`), identificada por um `username` único.
- **Catálogo**: um conjunto compartilhado de entidades `Produto`, visível a qualquer visitante, independentemente de estar autenticado.
- **Carrinho**: cada usuário autenticado possui exatamente um carrinho, representado por uma coleção de registros `CarrinhoItem` que ligam `User` ↔ `Produto` com uma `quantidade`.
- **Pedido**: o checkout é uma transação única que consome o carrinho; não há histórico persistente de `Pedido`/`ItemPedido` (escopo atual).

**Fora do escopo deste domínio** (explicitamente não modelado): marketplaces com múltiplos vendedores, controle de estoque/inventário, integração com gateway de pagamento, cálculo de impostos/frete, histórico e acompanhamento de status de pedidos. São candidatos para iterações futuras.

</details>

<details>
<summary><strong>1.5 Requisitos de Dados</strong></summary>

| Entidade | Campo | Tipo | Restrição |
|:---------|:------|:-----|:----------|
| `User` | `id` | Integer | Chave Primária |
| `User` | `username` | String(150) | Único, Não Nulo |
| `User` | `password` | String(150) | Não Nulo (hash Bcrypt) |
| `Produto` | `id` | Integer | Chave Primária |
| `Produto` | `nome` | String(100) | Não Nulo |
| `Produto` | `descricao` | Text | Pode ser Nulo |
| `Produto` | `preco` | Float | Não Nulo |
| `Produto` | `imagem` | String(300) | Pode ser Nulo, padrão `'default.jpg'` |
| `CarrinhoItem` | `id` | Integer | Chave Primária |
| `CarrinhoItem` | `quantidade` | Integer | Não Nulo, padrão `1` |
| `CarrinhoItem` | `user_id` | Integer | Chave Estrangeira → `User.id` |
| `CarrinhoItem` | `produto_id` | Integer | Chave Estrangeira → `Produto.id` |

> 📌 Os modelos conceitual / lógico / físico completos e o dicionário de dados completo estão detalhados em **[6. Modelo de Dados & Dicionário de Dados](#6--modelo-de-dados--dicionário-de-dados)**.

</details>

<details>
<summary><strong>1.6 Requisitos de Interface</strong></summary>

| Página / Template | Requisito |
|:-------------------|:----------|
| `base.html` | Deve fornecer um layout compartilhado com barra de navegação, área de mensagens flash e estado de login/logout. |
| `index.html` | Deve listar todos os produtos com imagem, nome, preço e ação de "adicionar ao carrinho". |
| `register.html` / `login.html` | Deve renderizar um formulário Flask-WTF com token CSRF e erros de validação inline. |
| `adicionar_produto.html` / `editar_produto.html` | Deve incluir um formulário multipart com suporte a upload de imagem. |
| `carrinho.html` | Deve listar os itens do carrinho com quantidade, subtotal e total geral, além de uma ação de remoção por item. |
| `checkout.html` | Deve exibir o resumo do pedido (itens + total) junto ao formulário de dados do cliente. |
| `pedido_sucesso.html` | Deve confirmar que o pedido foi realizado com sucesso. |
| Global | O layout deve ser responsivo (desktop e mobile) usando `static/style.css`. |

</details>

---

## 2. 🎯 Casos de Uso

<details>
<summary><strong>UC01 — Cadastrar Conta</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Visitante |
| **Descrição** | Um visitante cria uma conta para acessar funcionalidades autenticadas. |
| **Pré-condições** | O visitante não está logado. |
| **Fluxo Principal** | 1. Visitante acessa `/register`. 2. Preenche usuário e senha. 3. Sistema valida o formulário (CSRF, campos obrigatórios). 4. Sistema verifica a unicidade do usuário. 5. Sistema gera o hash da senha e cria o `User`. 6. Sistema redireciona para `/login` com mensagem de sucesso. |
| **Fluxo Alternativo** | Se o usuário já existir, o sistema exibe um erro de validação e permanece no formulário. |
| **Pós-condições** | Um novo registro `User` existe com a senha em hash. |

</details>

<details>
<summary><strong>UC02 — Fazer Login</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Cadastrado |
| **Descrição** | Um usuário cadastrado se autentica para acessar rotas protegidas. |
| **Pré-condições** | O usuário possui uma conta cadastrada. |
| **Fluxo Principal** | 1. Usuário acessa `/login`. 2. Informa usuário e senha. 3. Sistema verifica o hash com Bcrypt. 4. Sistema armazena `user_id`/`username` na sessão. 5. Sistema redireciona para a página inicial com mensagem de boas-vindas. |
| **Fluxo Alternativo** | Se as credenciais forem inválidas, o sistema exibe "Login falhou" e permanece no formulário. |
| **Pós-condições** | O usuário possui uma sessão ativa e pode acessar rotas protegidas. |

</details>

<details>
<summary><strong>UC03 — Sair (Logout)</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado |
| **Descrição** | O usuário encerra sua sessão. |
| **Pré-condições** | O usuário está autenticado. |
| **Fluxo Principal** | 1. Usuário clica em "Logout" (`/logout`). 2. Sistema remove `user_id`/`username` da sessão. 3. Sistema redireciona para `/login` com mensagem informativa. |
| **Pós-condições** | A sessão não concede mais acesso a rotas protegidas. |

</details>

<details>
<summary><strong>UC04 — Navegar pelo Catálogo de Produtos</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Visitante / Usuário Autenticado |
| **Descrição** | Qualquer pessoa pode visualizar a lista de produtos disponíveis. |
| **Pré-condições** | Nenhuma. |
| **Fluxo Principal** | 1. Usuário acessa `/`. 2. Sistema consulta todos os registros `Produto`. 3. Sistema renderiza `index.html` com nome, preço, descrição e imagem de cada produto. |
| **Pós-condições** | O usuário visualiza todos os produtos atualmente no catálogo. |

</details>

<details>
<summary><strong>UC05 — Adicionar Produto</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado (gestor) |
| **Descrição** | Um usuário autenticado cadastra um novo produto no catálogo. |
| **Pré-condições** | O usuário está autenticado. |
| **Fluxo Principal** | 1. Usuário acessa `/adicionar_produto`. 2. Preenche nome, descrição, preço e (opcionalmente) uma imagem. 3. Sistema valida o formulário. 4. Se uma imagem for enviada, o sistema a salva em `static/uploads/` com um nome de arquivo aleatório. 5. Sistema cria o registro `Produto` e redireciona para `/` com mensagem de sucesso. |
| **Fluxo Alternativo** | Se nenhuma imagem for enviada, `imagem` permanece `None`/padrão. |
| **Pós-condições** | Um novo `Produto` existe e aparece no catálogo. |

</details>

<details>
<summary><strong>UC06 — Editar Produto</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado (gestor) |
| **Descrição** | Um usuário autenticado atualiza os dados de um produto existente. |
| **Pré-condições** | O usuário está autenticado e o produto existe. |
| **Fluxo Principal** | 1. Usuário acessa `/editar_produto/<id>`. 2. O formulário é pré-preenchido com os dados atuais. 3. Usuário edita os campos e/ou envia uma nova imagem. 4. Se uma nova imagem for enviada, o arquivo de imagem anterior é excluído (exceto se for `default.jpg`) e substituído. 5. Sistema confirma as alterações e redireciona para `/` com mensagem de sucesso. |
| **Pós-condições** | O registro `Produto` reflete os valores atualizados. |

</details>

<details>
<summary><strong>UC07 — Excluir Produto</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado (gestor) |
| **Descrição** | Um usuário autenticado remove um produto do catálogo. |
| **Pré-condições** | O usuário está autenticado e o produto existe. |
| **Fluxo Principal** | 1. Usuário acessa `/excluir_produto/<id>`. 2. Sistema exclui o arquivo de imagem associado do disco (exceto se for `default.jpg`). 3. Sistema exclui o registro `Produto`. 4. Sistema redireciona para `/` com mensagem de sucesso. |
| **Pós-condições** | O produto não aparece mais no catálogo nem em nenhum carrinho. |

</details>

<details>
<summary><strong>UC08 — Adicionar Produto ao Carrinho</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado |
| **Descrição** | Um usuário adiciona um produto ao seu carrinho pessoal. |
| **Pré-condições** | O usuário está autenticado e o produto existe. |
| **Fluxo Principal** | 1. Usuário acessa `/add_carrinho/<id>`. 2. Sistema verifica se já existe um `CarrinhoItem` para esse usuário/produto. 3a. Se existir, incrementa `quantidade` em 1. 3b. Se não existir, cria um novo `CarrinhoItem` com `quantidade = 1`. 4. Sistema redireciona para `/` com mensagem de sucesso. |
| **Pós-condições** | O carrinho contém o produto com a quantidade atualizada. |

</details>

<details>
<summary><strong>UC09 — Visualizar / Atualizar Carrinho</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado |
| **Descrição** | Um usuário visualiza seu carrinho e pode remover itens. |
| **Pré-condições** | O usuário está autenticado. |
| **Fluxo Principal** | 1. Usuário acessa `/carrinho`. 2. Sistema carrega todos os registros `CarrinhoItem` do usuário (com join em `Produto`). 3. Sistema calcula o subtotal por item e o total geral. 4. Sistema renderiza `carrinho.html`. |
| **Fluxo Alternativo** | O usuário acessa `/remover_carrinho/<id>`; o sistema exclui o `CarrinhoItem` correspondente e redireciona de volta para `/carrinho` com mensagem informativa. |
| **Pós-condições** | A visualização do carrinho reflete os itens e o total atuais. |

</details>

<details>
<summary><strong>UC10 — Finalizar Compra (Checkout)</strong></summary>

| Campo | Descrição |
|:------|:----------|
| **Ator** | Usuário Autenticado |
| **Descrição** | Um usuário finaliza a compra dos itens em seu carrinho. |
| **Pré-condições** | O usuário está autenticado e o carrinho não está vazio. |
| **Fluxo Principal** | 1. Usuário acessa `/checkout`. 2. Sistema exibe o resumo do pedido e um formulário com nome completo e e-mail. 3. Usuário envia o formulário. 4. Sistema valida o formulário (CSRF + campos obrigatórios). 5. Sistema exclui todos os registros `CarrinhoItem` do usuário. 6. Sistema redireciona para `/pedido_sucesso`. |
| **Fluxo Alternativo** | Se o carrinho estiver vazio ao acessar `/checkout`, o sistema redireciona para `/` com mensagem de aviso. |
| **Pós-condições** | O carrinho do usuário está vazio e uma página de confirmação de pedido é exibida. |

</details>

---

## 3. 🔗 Matriz de Rastreabilidade de Requisitos

> 🚧 **Em construção.** Esta seção irá mapear cada **RF / RNF / RN** da [Seção 1](#1--requisitos) para os **Casos de Uso**, arquivos de origem (rotas/models/templates) e casos de teste que os implementam e verificam.

<details>
<summary>Estrutura planejada</summary>

| Requisito | Caso(s) de Uso | Implementação | Teste(s) |
|:----------|:----------------|:----------------|:---------|
| RF01 | UC01 | `app.py::register` | `test_app.py` |
| ... | ... | ... | ... |

</details>

---

## 4. 📄 Documento de Especificação de Requisitos (SRS)

> 🚧 **Em construção.** Um documento SRS consolidado (estilo IEEE 830 / ISO 29148) cobrindo escopo, descrição geral, requisitos específicos, interfaces externas e restrições — agregando as Seções 1–3.

---

## 5. 🖼️ Diagramas UML & Estruturais

> 🚧 **Em construção.** Os diagramas serão fornecidos em Mermaid (renderizados inline no GitHub):

<details>
<summary>Diagramas planejados</summary>

- [ ] Diagrama de Casos de Uso
- [ ] Diagrama de Classes
- [ ] Diagrama de Objetos
- [ ] Diagrama de Sequência
- [ ] Diagrama de Comunicação (Colaboração)
- [ ] Diagrama de Atividades
- [ ] Diagrama de Máquina de Estados
- [ ] Diagrama de Componentes
- [ ] Diagrama de Implantação (Deployment)
- [ ] Diagrama de Pacotes
- [ ] Diagrama de Estrutura Composta
- [ ] Diagrama de Visão Geral de Interação
- [ ] Diagrama de Tempo (Timing)

</details>

---

## 6. 🗄️ Modelo de Dados & Dicionário de Dados

> 🚧 **Em construção.** Expande os [1.5 Requisitos de Dados](#15-requisitos-de-dados).

<details>
<summary>Conteúdo planejado</summary>

- [ ] Diagrama Entidade-Relacionamento (DER)
- [ ] Modelo Conceitual de Dados
- [ ] Modelo Lógico de Dados
- [ ] Modelo Físico de Dados
- [ ] Dicionário de Dados completo (tabela/coluna, tipo, restrições, descrição)

</details>

---

## 7. 🌊 Diagrama de Fluxo de Dados (DFD)

> 🚧 **Em construção.**

<details>
<summary>Conteúdo planejado</summary>

- [ ] Diagrama de Fluxo de Dados (Níveis 0/1) — Usuário ↔ rotas Flask ↔ SQLite ↔ Armazenamento de arquivos
- [ ] Diagrama de Linhagem de Dados — do input do formulário até os dados persistidos/derivados (ex.: total do carrinho)

</details>

---

## 8. 🏗️ Diagrama de Arquitetura & Fluxograma

> 🚧 **Em construção.**

<details>
<summary>Conteúdo planejado</summary>

- [ ] Diagrama de Arquitetura (visão geral) — Navegador ↔ App Flask ↔ SQLAlchemy ↔ SQLite + static/uploads
- [ ] Fluxograma — fluxo de decisão do checkout (carrinho vazio? formulário válido? página de sucesso)

</details>

---

## 9. 🧑 Persona & Mapa de Jornada do Usuário

> 🚧 **Em construção.**

<details>
<summary>Conteúdo planejado</summary>

- [ ] Persona — ex.: "Maria, dona de loja local gerenciando seu catálogo"
- [ ] Mapa de Jornada do Usuário — desde a chegada ao catálogo até a finalização do checkout

</details>

---

## 10. 🎨 Wireframes & Mockups

> 🚧 **Em construção.**

<details>
<summary>Conteúdo planejado</summary>

- [ ] Wireframes — layouts de baixa fidelidade para catálogo, carrinho e checkout
- [ ] Mockups — visuais de alta fidelidade alinhados ao `static/style.css`

</details>

---

## 11. 🚀 Instalação & Execução

### Pré-requisitos

| Requisito | Detalhe |
|:----------|:--------|
| **Python** | 3.10+ |
| **pip** | incluso na instalação do Python |
| **Git** | para clonar o repositório |

### Passo a Passo

```bash
# 1. Clone o repositório
git clone https://github.com/VictorHJesusSantiago/lojinha_local.git
cd lojinha_local

# 2. Crie e ative o ambiente virtual
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Crie o banco de dados
flask shell -c "from app import db; db.create_all()"

# 5. Execute a aplicação
flask run --debug
```

| Serviço | URL |
|:--------|:----|
| 🏠 Início (catálogo) | `http://localhost:5000` |
| 🔐 Login | `http://localhost:5000/login` |
| 📋 Cadastro | `http://localhost:5000/register` |
| ➕ Adicionar Produto | `http://localhost:5000/adicionar_produto` |

---

## 12. 👨‍💻 Autor

<div align="center">

**Victor H. J. Santiago**
Full Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VictorHJesusSantiago)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-henrique-de-jesus-santiago/)

</div>

---

<div align="center">

*Feito com 🛒 e Flask*

</div>
