<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/3514/3514491.png" alt="Lojinha Local Logo" width="110" />

# 🛒 Lojinha Local

### Software Engineering Documentation & E-commerce System

A full-stack e-commerce demo built with **Python, Flask, SQLAlchemy and Flask-Bcrypt**, documented end-to-end following classic Software Engineering artifacts (Requirements, UML, Data Modeling, DFD, UX).

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### 🌐 Choose Language / Selecione o idioma / Elija su idioma

[![English](https://img.shields.io/badge/ENGLISH-CURRENT-brightgreen?style=for-the-badge)](./README.md)
[![Português](https://img.shields.io/badge/PORTUGU%C3%8AS-README__PT.MD-blue?style=for-the-badge)](./README_PT.md)
[![Español](https://img.shields.io/badge/ESPAÑOL-README__ES.MD-yellow?style=for-the-badge)](./README_ES.md)

</div>

---

## 📖 About the Project

> **Lojinha Local** is a full-stack web application that simulates a small local store: catalog, shopping cart and checkout, plus an authenticated panel to manage products.

This README is the **engineering documentation hub** of the project. It follows a classic Software Engineering documentation structure — requirements, use cases, UML diagrams, data modeling, data flow, architecture and UX artifacts — built around the real implementation (Flask + SQLAlchemy + SQLite).

> 🚧 **Status:** Sections **1. Requirements** and **2. Use Cases** are fully written. All other sections (3–10) are scaffolded with their final structure and will be filled in incrementally.

---

## 📑 Table of Contents

| # | Section | Status |
|:-:|:--------|:------:|
| 1 | [📋 Requirements](#1--requirements) | ✅ |
| 2 | [🎯 Use Cases](#2--use-cases) | ✅ |
| 3 | [🔗 Requirements Traceability Matrix](#3--requirements-traceability-matrix) | 🚧 |
| 4 | [📄 Software Requirements Specification (SRS)](#4--software-requirements-specification-srs) | 🚧 |
| 5 | [🖼️ UML & Structural Diagrams](#5--uml--structural-diagrams) | 🚧 |
| 6 | [🗄️ Data Model & Data Dictionary](#6--data-model--data-dictionary) | 🚧 |
| 7 | [🌊 Data Flow Diagram (DFD)](#7--data-flow-diagram-dfd) | 🚧 |
| 8 | [🏗️ Architecture Diagram & Flowchart](#8--architecture-diagram--flowchart) | 🚧 |
| 9 | [🧑 Persona & User Journey Map](#9--persona--user-journey-map) | 🚧 |
| 10 | [🎨 Wireframes & Mockups](#10--wireframes--mockups) | 🚧 |
| 11 | [🚀 Installation & Execution](#11--installation--execution) | ✅ |
| 12 | [👨‍💻 Author](#12--author) | ✅ |

---

## 1. 📋 Requirements

<details>
<summary><strong>1.1 Functional Requirements (RF)</strong></summary>

| ID | Requirement | Priority |
|:---|:------------|:--------:|
| RF01 | The system shall allow new users to register with a unique username and password. | High |
| RF02 | The system shall allow registered users to log in with username and password. | High |
| RF03 | The system shall allow authenticated users to log out, ending their session. | High |
| RF04 | The system shall display a catalog of all products on the home page (name, price, description, image). | High |
| RF05 | The system shall allow authenticated users to add new products, including an optional image upload. | High |
| RF06 | The system shall allow authenticated users to edit existing products (name, description, price, image). | High |
| RF07 | The system shall allow authenticated users to delete products, removing the associated image file from storage. | Medium |
| RF08 | The system shall allow authenticated users to add a product to their personal shopping cart. | High |
| RF09 | The system shall increment the quantity of an existing cart item if the same product is added again. | Medium |
| RF10 | The system shall display the cart with item name, unit price, quantity, subtotal and grand total. | High |
| RF11 | The system shall allow authenticated users to remove individual items from the cart. | Medium |
| RF12 | The system shall provide a checkout form requiring the customer's full name and e-mail. | Medium |
| RF13 | The system shall empty the user's cart after a successful checkout and redirect to an order confirmation page. | High |
| RF14 | The system shall persist users, products and cart items in a relational database (SQLite). | High |

</details>

<details>
<summary><strong>1.2 Non-Functional Requirements (RNF)</strong></summary>

| ID | Requirement | Category |
|:---|:------------|:--------:|
| RNF01 | Passwords must be stored using one-way hashing (Bcrypt), never in plain text. | Security |
| RNF02 | All forms must be protected against CSRF attacks via Flask-WTF tokens. | Security |
| RNF03 | Routes that create/modify data (products, cart, checkout) must require an authenticated session. | Security |
| RNF04 | Uploaded images must be limited to 16 MB and stored under a randomized filename to avoid collisions. | Security / Reliability |
| RNF05 | Standard catalog and cart operations must respond in under 1 second under normal local load. | Performance |
| RNF06 | The UI must be legible and usable on both desktop and mobile viewports. | Usability |
| RNF07 | Every state-changing action must give the user clear feedback via flash messages. | Usability |
| RNF08 | Code must be organized into clear modules (models, forms, routes, templates) for maintainability. | Maintainability |
| RNF09 | The application must run on any OS with Python 3.10+, with no extra native dependencies (SQLite is file-based). | Portability |
| RNF10 | Critical flows (auth, catalog, cart) must be covered by automated tests (pytest). | Testability |

</details>

<details>
<summary><strong>1.3 Business Rules (RN)</strong></summary>

| ID | Rule |
|:---|:-----|
| RN01 | A username must be unique across the system; duplicate registrations are rejected. |
| RN02 | A product must have a name and a price greater than zero; description and image are optional. |
| RN03 | If no image is provided for a product, the system uses a default image (`default.jpg`). |
| RN04 | A cart belongs to exactly one user; adding the same product again increments its quantity instead of duplicating the row. |
| RN05 | The cart total equals the sum of (unit price × quantity) for every item. |
| RN06 | Checkout is only allowed when the cart is not empty. |
| RN07 | A successful checkout empties the user's cart completely. |
| RN08 | When a product's image is replaced or the product is deleted, the previous image file is removed from disk (except the default image). |
| RN09 | Only authenticated users can manage the catalog (create/edit/delete products) and their own cart. |
| RN10 | A user can only view and modify their own cart, never another user's. |

</details>

<details>
<summary><strong>1.4 Domain Requirements</strong></summary>

The system models the domain of a **single-vendor local store (B2C)**:

- **Account**: each customer/manager has one account (`User`), identified by a unique `username`.
- **Catalog**: a shared set of `Produto` (product) entities, visible to every visitor regardless of login state.
- **Cart**: each authenticated user owns exactly one cart, represented as a collection of `CarrinhoItem` rows linking `User` ↔ `Produto` with a `quantidade`.
- **Order**: checkout is a one-shot transaction that consumes the cart; no persistent `Order`/`OrderItem` history is kept (current scope).

**Out of scope for this domain** (explicitly not modeled): multi-seller marketplaces, stock/inventory control, payment gateway integration, taxes/shipping calculation, order history and order status tracking. These are candidate areas for future iterations.

</details>

<details>
<summary><strong>1.5 Data Requirements</strong></summary>

| Entity | Field | Type | Constraint |
|:-------|:------|:-----|:-----------|
| `User` | `id` | Integer | Primary Key |
| `User` | `username` | String(150) | Unique, Not Null |
| `User` | `password` | String(150) | Not Null (Bcrypt hash) |
| `Produto` | `id` | Integer | Primary Key |
| `Produto` | `nome` | String(100) | Not Null |
| `Produto` | `descricao` | Text | Nullable |
| `Produto` | `preco` | Float | Not Null |
| `Produto` | `imagem` | String(300) | Nullable, default `'default.jpg'` |
| `CarrinhoItem` | `id` | Integer | Primary Key |
| `CarrinhoItem` | `quantidade` | Integer | Not Null, default `1` |
| `CarrinhoItem` | `user_id` | Integer | Foreign Key → `User.id` |
| `CarrinhoItem` | `produto_id` | Integer | Foreign Key → `Produto.id` |

> 📌 The full conceptual / logical / physical models and the complete data dictionary are detailed in **[6. Data Model & Data Dictionary](#6--data-model--data-dictionary)**.

</details>

<details>
<summary><strong>1.6 Interface Requirements</strong></summary>

| Page / Template | Requirement |
|:-----------------|:------------|
| `base.html` | Must provide a shared layout with navigation bar, flash-message area and login/logout state. |
| `index.html` | Must list every product with image, name, price and an "add to cart" action. |
| `register.html` / `login.html` | Must render a Flask-WTF form with CSRF token and inline validation errors. |
| `adicionar_produto.html` / `editar_produto.html` | Must include a multipart form supporting image upload. |
| `carrinho.html` | Must list cart items with quantity, subtotal and grand total, plus a remove action per item. |
| `checkout.html` | Must show the order summary (items + total) alongside the customer-info form. |
| `pedido_sucesso.html` | Must confirm the order was placed successfully. |
| Global | The layout must be responsive (desktop and mobile) using `static/style.css`. |

</details>

---

## 2. 🎯 Use Cases

<details>
<summary><strong>UC01 — Register Account</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Visitor |
| **Description** | A visitor creates an account to access authenticated features. |
| **Preconditions** | The visitor is not logged in. |
| **Main Flow** | 1. Visitor opens `/register`. 2. Fills username and password. 3. System validates the form (CSRF, required fields). 4. System checks username uniqueness. 5. System hashes the password and creates the `User`. 6. System redirects to `/login` with a success message. |
| **Alternative Flow** | If the username already exists, the system shows a validation error and stays on the form. |
| **Postconditions** | A new `User` row exists with a hashed password. |

</details>

<details>
<summary><strong>UC02 — Log In</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Registered User |
| **Description** | A registered user authenticates to access protected routes. |
| **Preconditions** | The user has a registered account. |
| **Main Flow** | 1. User opens `/login`. 2. Enters username and password. 3. System verifies the hash with Bcrypt. 4. System stores `user_id`/`username` in the session. 5. System redirects to the home page with a welcome message. |
| **Alternative Flow** | If credentials are invalid, the system shows "Login failed" and stays on the form. |
| **Postconditions** | The user has an active session and can access protected routes. |

</details>

<details>
<summary><strong>UC03 — Log Out</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User |
| **Description** | The user ends their session. |
| **Preconditions** | The user is authenticated. |
| **Main Flow** | 1. User clicks "Logout" (`/logout`). 2. System clears `user_id`/`username` from the session. 3. System redirects to `/login` with an info message. |
| **Postconditions** | The session no longer grants access to protected routes. |

</details>

<details>
<summary><strong>UC04 — Browse Product Catalog</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Visitor / Authenticated User |
| **Description** | Anyone can view the list of available products. |
| **Preconditions** | None. |
| **Main Flow** | 1. User opens `/`. 2. System queries all `Produto` rows. 3. System renders `index.html` with name, price, description and image for each product. |
| **Postconditions** | The user can see every product currently in the catalog. |

</details>

<details>
<summary><strong>UC05 — Add Product</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User (manager) |
| **Description** | An authenticated user registers a new product in the catalog. |
| **Preconditions** | The user is authenticated. |
| **Main Flow** | 1. User opens `/adicionar_produto`. 2. Fills name, description, price and (optionally) an image. 3. System validates the form. 4. If an image is sent, the system saves it under `static/uploads/` with a random filename. 5. System creates the `Produto` row and redirects to `/` with a success message. |
| **Alternative Flow** | If no image is provided, `imagem` stays `None`/default. |
| **Postconditions** | A new `Produto` exists and appears in the catalog. |

</details>

<details>
<summary><strong>UC06 — Edit Product</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User (manager) |
| **Description** | An authenticated user updates an existing product's data. |
| **Preconditions** | The user is authenticated and the product exists. |
| **Main Flow** | 1. User opens `/editar_produto/<id>`. 2. Form is pre-filled with current data. 3. User edits fields and/or uploads a new image. 4. If a new image is sent, the old image file is deleted (unless it is `default.jpg`) and replaced. 5. System commits the changes and redirects to `/` with a success message. |
| **Postconditions** | The `Produto` row reflects the updated values. |

</details>

<details>
<summary><strong>UC07 — Delete Product</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User (manager) |
| **Description** | An authenticated user removes a product from the catalog. |
| **Preconditions** | The user is authenticated and the product exists. |
| **Main Flow** | 1. User triggers `/excluir_produto/<id>`. 2. System deletes the associated image file from disk (unless it is `default.jpg`). 3. System deletes the `Produto` row. 4. System redirects to `/` with a success message. |
| **Postconditions** | The product no longer appears in the catalog or in any cart. |

</details>

<details>
<summary><strong>UC08 — Add Product to Cart</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User |
| **Description** | A user adds a product to their personal cart. |
| **Preconditions** | The user is authenticated and the product exists. |
| **Main Flow** | 1. User triggers `/add_carrinho/<id>`. 2. System checks if a `CarrinhoItem` already exists for this user/product. 3a. If it exists, increments `quantidade` by 1. 3b. If not, creates a new `CarrinhoItem` with `quantidade = 1`. 4. System redirects to `/` with a success message. |
| **Postconditions** | The cart contains the product with an updated quantity. |

</details>

<details>
<summary><strong>UC09 — View / Update Cart</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User |
| **Description** | A user views their cart and may remove items. |
| **Preconditions** | The user is authenticated. |
| **Main Flow** | 1. User opens `/carrinho`. 2. System loads all `CarrinhoItem` rows for the user (joined with `Produto`). 3. System computes subtotal per item and the grand total. 4. System renders `carrinho.html`. |
| **Alternative Flow** | The user triggers `/remover_carrinho/<id>`; the system deletes the matching `CarrinhoItem` and redirects back to `/carrinho` with an info message. |
| **Postconditions** | The cart view reflects the current items and total. |

</details>

<details>
<summary><strong>UC10 — Checkout</strong></summary>

| Field | Description |
|:------|:------------|
| **Actor** | Authenticated User |
| **Description** | A user finalizes the purchase of items in their cart. |
| **Preconditions** | The user is authenticated and the cart is not empty. |
| **Main Flow** | 1. User opens `/checkout`. 2. System shows the order summary and a form for full name and e-mail. 3. User submits the form. 4. System validates the form (CSRF + required fields). 5. System deletes all `CarrinhoItem` rows for the user. 6. System redirects to `/pedido_sucesso`. |
| **Alternative Flow** | If the cart is empty when `/checkout` is opened, the system redirects to `/` with a warning message. |
| **Postconditions** | The user's cart is empty and an order confirmation page is shown. |

</details>

---

## 3. 🔗 Requirements Traceability Matrix

> 🚧 **Coming soon.** This section will map each **RF / RNF / RN** from [Section 1](#1--requirements) to the **Use Cases**, source files (routes/models/templates) and test cases that implement and verify them.

<details>
<summary>Planned structure</summary>

| Requirement | Use Case(s) | Implementation | Test(s) |
|:------------|:------------|:----------------|:--------|
| RF01 | UC01 | `app.py::register` | `test_app.py` |
| ... | ... | ... | ... |

</details>

---

## 4. 📄 Software Requirements Specification (SRS)

> 🚧 **Coming soon.** A consolidated SRS document (IEEE 830 / ISO 29148 style) covering scope, overall description, specific requirements, external interfaces and constraints — aggregating Sections 1–3.

---

## 5. 🖼️ UML & Structural Diagrams

> 🚧 **Coming soon.** Diagrams will be provided as Mermaid sources (rendered inline on GitHub):

<details>
<summary>Planned diagrams</summary>

- [ ] Use Case Diagram
- [ ] Class Diagram
- [ ] Object Diagram
- [ ] Sequence Diagram
- [ ] Communication (Collaboration) Diagram
- [ ] Activity Diagram
- [ ] State Machine Diagram
- [ ] Component Diagram
- [ ] Deployment Diagram
- [ ] Package Diagram
- [ ] Composite Structure Diagram
- [ ] Interaction Overview Diagram
- [ ] Timing Diagram

</details>

---

## 6. 🗄️ Data Model & Data Dictionary

> 🚧 **Coming soon.** Builds on [1.5 Data Requirements](#15-data-requirements).

<details>
<summary>Planned content</summary>

- [ ] Entity-Relationship Diagram (ER / DER)
- [ ] Conceptual Data Model
- [ ] Logical Data Model
- [ ] Physical Data Model
- [ ] Full Data Dictionary (table/column, type, constraints, description)

</details>

---

## 7. 🌊 Data Flow Diagram (DFD)

> 🚧 **Coming soon.**

<details>
<summary>Planned content</summary>

- [ ] Data Flow Diagram (Levels 0/1) — User ↔ Flask routes ↔ SQLite ↔ File storage
- [ ] Data Lineage Diagram — from form input to persisted/derived data (e.g., cart total)

</details>

---

## 8. 🏗️ Architecture Diagram & Flowchart

> 🚧 **Coming soon.**

<details>
<summary>Planned content</summary>

- [ ] Architecture Diagram (overview) — Browser ↔ Flask app ↔ SQLAlchemy ↔ SQLite + static/uploads
- [ ] Flowchart — checkout decision flow (empty cart? valid form? success page)

</details>

---

## 9. 🧑 Persona & User Journey Map

> 🚧 **Coming soon.**

<details>
<summary>Planned content</summary>

- [ ] Persona — e.g., "Maria, local shop owner managing her catalog"
- [ ] User Journey Map — from landing on the catalog to completing checkout

</details>

---

## 10. 🎨 Wireframes & Mockups

> 🚧 **Coming soon.**

<details>
<summary>Planned content</summary>

- [ ] Wireframes — low-fidelity layouts for catalog, cart and checkout
- [ ] Mockups — high-fidelity visuals matching `static/style.css`

</details>

---

## 11. 🚀 Installation & Execution

### Prerequisites

| Requirement | Detail |
|:-------------|:-------|
| **Python** | 3.10+ |
| **pip** | bundled with Python |
| **Git** | to clone the repository |

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/VictorHJesusSantiago/lojinha_local.git
cd lojinha_local

# 2. Create and activate a virtual environment
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create the database
flask shell -c "from app import db; db.create_all()"

# 5. Run the application
flask run --debug
```

| Service | URL |
|:--------|:----|
| 🏠 Home (catalog) | `http://localhost:5000` |
| 🔐 Login | `http://localhost:5000/login` |
| 📋 Register | `http://localhost:5000/register` |
| ➕ Add Product | `http://localhost:5000/adicionar_produto` |

---

## 12. 👨‍💻 Author

<div align="center">

**Victor H. J. Santiago**
Full Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/VictorHJesusSantiago)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victor-henrique-de-jesus-santiago/)

</div>

---

<div align="center">

*Made with 🛒 and Flask*

</div>
