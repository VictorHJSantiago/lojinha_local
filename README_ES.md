<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/3514/3514491.png" alt="Lojinha Local Logo" width="110" />

# 🛒 Lojinha Local

### Documentación de Ingeniería de Software & Sistema de E-commerce

Una aplicación full-stack de e-commerce construida con **Python, Flask, SQLAlchemy y Flask-Bcrypt**, documentada de extremo a extremo siguiendo los clásicos artefactos de Ingeniería de Software (Requisitos, UML, Modelado de Datos, DFD, UX).

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20Progreso-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

### 🌐 Choose Language / Selecione o idioma / Elija su idioma

[![English](https://img.shields.io/badge/ENGLISH-README.MD-blue?style=for-the-badge)](./README.md)
[![Português](https://img.shields.io/badge/PORTUGU%C3%8AS-README__PT.MD-green?style=for-the-badge)](./README_PT.md)
[![Español](https://img.shields.io/badge/ESPAÑOL-ACTUAL-yellow?style=for-the-badge)](./README_ES.md)

</div>

---

## 📖 Acerca del Proyecto

> **Lojinha Local** es una aplicación web full-stack que simula una pequeña tienda local: catálogo, carrito de compras y checkout, además de un panel autenticado para gestionar productos.

Este README es el **centro de documentación de ingeniería** del proyecto. Sigue una estructura clásica de documentación de Ingeniería de Software — requisitos, casos de uso, diagramas UML, modelado de datos, flujo de datos, arquitectura y artefactos de UX — construida alrededor de la implementación real (Flask + SQLAlchemy + SQLite).

> 🚧 **Estado:** Las secciones **1. Requisitos** y **2. Casos de Uso** están completamente redactadas. Las demás secciones (3–10) están estructuradas y se completarán de forma incremental.

---

## 📑 Tabla de Contenidos

| # | Sección | Estado |
|:-:|:--------|:------:|
| 1 | [📋 Requisitos](#1--requisitos) | ✅ |
| 2 | [🎯 Casos de Uso](#2--casos-de-uso) | ✅ |
| 3 | [🔗 Matriz de Trazabilidad de Requisitos](#3--matriz-de-trazabilidad-de-requisitos) | 🚧 |
| 4 | [📄 Especificación de Requisitos de Software (SRS)](#4--especificación-de-requisitos-de-software-srs) | 🚧 |
| 5 | [🖼️ Diagramas UML & Estructurales](#5--diagramas-uml--estructurales) | 🚧 |
| 6 | [🗄️ Modelo de Datos & Diccionario de Datos](#6--modelo-de-datos--diccionario-de-datos) | 🚧 |
| 7 | [🌊 Diagrama de Flujo de Datos (DFD)](#7--diagrama-de-flujo-de-datos-dfd) | 🚧 |
| 8 | [🏗️ Diagrama de Arquitectura & Diagrama de Flujo](#8--diagrama-de-arquitectura--diagrama-de-flujo) | 🚧 |
| 9 | [🧑 Persona & Mapa de Viaje del Usuario](#9--persona--mapa-de-viaje-del-usuario) | 🚧 |
| 10 | [🎨 Wireframes & Mockups](#10--wireframes--mockups) | 🚧 |
| 11 | [🚀 Instalación & Ejecución](#11--instalación--ejecución) | ✅ |
| 12 | [👨‍💻 Autor](#12--autor) | ✅ |

---

## 1. 📋 Requisitos

<details>
<summary><strong>1.1 Requisitos Funcionales (RF)</strong></summary>

| ID | Requisito | Prioridad |
|:---|:----------|:---------:|
| RF01 | El sistema debe permitir que nuevos usuarios se registren con un nombre de usuario único y contraseña. | Alta |
| RF02 | El sistema debe permitir que usuarios registrados inicien sesión con usuario y contraseña. | Alta |
| RF03 | El sistema debe permitir que usuarios autenticados cierren sesión, finalizando su sesión. | Alta |
| RF04 | El sistema debe mostrar el catálogo de todos los productos en la página principal (nombre, precio, descripción, imagen). | Alta |
| RF05 | El sistema debe permitir que usuarios autenticados agreguen nuevos productos, incluyendo carga opcional de imagen. | Alta |
| RF06 | El sistema debe permitir que usuarios autenticados editen productos existentes (nombre, descripción, precio, imagen). | Alta |
| RF07 | El sistema debe permitir que usuarios autenticados eliminen productos, removiendo el archivo de imagen asociado del almacenamiento. | Media |
| RF08 | El sistema debe permitir que usuarios autenticados agreguen un producto a su carrito de compras personal. | Alta |
| RF09 | El sistema debe incrementar la cantidad de un ítem existente en el carrito si el mismo producto se agrega de nuevo. | Media |
| RF10 | El sistema debe mostrar el carrito con nombre del ítem, precio unitario, cantidad, subtotal y total general. | Alta |
| RF11 | El sistema debe permitir que usuarios autenticados eliminen ítems individuales del carrito. | Media |
| RF12 | El sistema debe proporcionar un formulario de checkout que requiera el nombre completo y el correo electrónico del cliente. | Media |
| RF13 | El sistema debe vaciar el carrito del usuario después de un checkout exitoso y redirigir a una página de confirmación de pedido. | Alta |
| RF14 | El sistema debe persistir usuarios, productos e ítems del carrito en una base de datos relacional (SQLite). | Alta |

</details>

<details>
<summary><strong>1.2 Requisitos No Funcionales (RNF)</strong></summary>

| ID | Requisito | Categoría |
|:---|:----------|:---------:|
| RNF01 | Las contraseñas deben almacenarse con hash unidireccional (Bcrypt), nunca en texto plano. | Seguridad |
| RNF02 | Todos los formularios deben estar protegidos contra ataques CSRF mediante tokens de Flask-WTF. | Seguridad |
| RNF03 | Las rutas que crean/modifican datos (productos, carrito, checkout) deben requerir una sesión autenticada. | Seguridad |
| RNF04 | Las imágenes cargadas deben limitarse a 16 MB y almacenarse con un nombre de archivo aleatorio para evitar colisiones. | Seguridad / Confiabilidad |
| RNF05 | Las operaciones estándar de catálogo y carrito deben responder en menos de 1 segundo bajo carga local normal. | Rendimiento |
| RNF06 | La interfaz debe ser legible y utilizable tanto en escritorio como en dispositivos móviles. | Usabilidad |
| RNF07 | Cada acción que cambie el estado debe dar al usuario retroalimentación clara mediante mensajes flash. | Usabilidad |
| RNF08 | El código debe estar organizado en módulos claros (models, forms, rutas, templates) para facilitar el mantenimiento. | Mantenibilidad |
| RNF09 | La aplicación debe ejecutarse en cualquier SO con Python 3.10+, sin dependencias nativas adicionales (SQLite se basa en archivos). | Portabilidad |
| RNF10 | Los flujos críticos (autenticación, catálogo, carrito) deben estar cubiertos por pruebas automatizadas (pytest). | Verificabilidad |

</details>

<details>
<summary><strong>1.3 Reglas de Negocio (RN)</strong></summary>

| ID | Regla |
|:---|:------|
| RN01 | Un nombre de usuario debe ser único en todo el sistema; los registros duplicados son rechazados. |
| RN02 | Un producto debe tener nombre y precio mayor que cero; la descripción y la imagen son opcionales. |
| RN03 | Si no se proporciona una imagen para un producto, el sistema utiliza una imagen predeterminada (`default.jpg`). |
| RN04 | Un carrito pertenece exactamente a un usuario; agregar el mismo producto de nuevo incrementa su cantidad en lugar de duplicar el registro. |
| RN05 | El total del carrito es igual a la suma de (precio unitario × cantidad) de todos los ítems. |
| RN06 | El checkout solo se permite cuando el carrito no está vacío. |
| RN07 | Un checkout exitoso vacía completamente el carrito del usuario. |
| RN08 | Cuando se reemplaza la imagen de un producto o se elimina el producto, el archivo de imagen anterior se elimina del disco (excepto la imagen predeterminada). |
| RN09 | Solo los usuarios autenticados pueden gestionar el catálogo (crear/editar/eliminar productos) y su propio carrito. |
| RN10 | Un usuario solo puede ver y modificar su propio carrito, nunca el de otro usuario. |

</details>

<details>
<summary><strong>1.4 Requisitos de Dominio</strong></summary>

El sistema modela el dominio de una **tienda local con un único vendedor (B2C)**:

- **Cuenta**: cada cliente/gestor tiene una cuenta (`User`), identificada por un `username` único.
- **Catálogo**: un conjunto compartido de entidades `Produto`, visible para cualquier visitante, esté o no autenticado.
- **Carrito**: cada usuario autenticado posee exactamente un carrito, representado por una colección de registros `CarrinhoItem` que vinculan `User` ↔ `Produto` con una `quantidade`.
- **Pedido**: el checkout es una transacción única que consume el carrito; no se mantiene un historial persistente de `Pedido`/`ItemPedido` (alcance actual).

**Fuera del alcance de este dominio** (explícitamente no modelado): marketplaces multi-vendedor, control de stock/inventario, integración con pasarela de pago, cálculo de impuestos/envío, historial y seguimiento del estado de pedidos. Son candidatos para futuras iteraciones.

</details>

<details>
<summary><strong>1.5 Requisitos de Datos</strong></summary>

| Entidad | Campo | Tipo | Restricción |
|:--------|:------|:-----|:------------|
| `User` | `id` | Integer | Clave Primaria |
| `User` | `username` | String(150) | Único, No Nulo |
| `User` | `password` | String(150) | No Nulo (hash Bcrypt) |
| `Produto` | `id` | Integer | Clave Primaria |
| `Produto` | `nome` | String(100) | No Nulo |
| `Produto` | `descricao` | Text | Puede ser Nulo |
| `Produto` | `preco` | Float | No Nulo |
| `Produto` | `imagem` | String(300) | Puede ser Nulo, valor predeterminado `'default.jpg'` |
| `CarrinhoItem` | `id` | Integer | Clave Primaria |
| `CarrinhoItem` | `quantidade` | Integer | No Nulo, valor predeterminado `1` |
| `CarrinhoItem` | `user_id` | Integer | Clave Foránea → `User.id` |
| `CarrinhoItem` | `produto_id` | Integer | Clave Foránea → `Produto.id` |

> 📌 Los modelos conceptual / lógico / físico completos y el diccionario de datos completo se detallan en **[6. Modelo de Datos & Diccionario de Datos](#6--modelo-de-datos--diccionario-de-datos)**.

</details>

<details>
<summary><strong>1.6 Requisitos de Interfaz</strong></summary>

| Página / Template | Requisito |
|:-------------------|:----------|
| `base.html` | Debe proporcionar un diseño compartido con barra de navegación, área de mensajes flash y estado de inicio/cierre de sesión. |
| `index.html` | Debe listar todos los productos con imagen, nombre, precio y una acción de "agregar al carrito". |
| `register.html` / `login.html` | Debe renderizar un formulario Flask-WTF con token CSRF y errores de validación en línea. |
| `adicionar_produto.html` / `editar_produto.html` | Debe incluir un formulario multipart con soporte para carga de imágenes. |
| `carrinho.html` | Debe listar los ítems del carrito con cantidad, subtotal y total general, además de una acción de eliminación por ítem. |
| `checkout.html` | Debe mostrar el resumen del pedido (ítems + total) junto al formulario de datos del cliente. |
| `pedido_sucesso.html` | Debe confirmar que el pedido se realizó con éxito. |
| Global | El diseño debe ser responsivo (escritorio y móvil) usando `static/style.css`. |

</details>

---

## 2. 🎯 Casos de Uso

<details>
<summary><strong>UC01 — Registrar Cuenta</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Visitante |
| **Descripción** | Un visitante crea una cuenta para acceder a funcionalidades autenticadas. |
| **Precondiciones** | El visitante no ha iniciado sesión. |
| **Flujo Principal** | 1. El visitante abre `/register`. 2. Completa usuario y contraseña. 3. El sistema valida el formulario (CSRF, campos obligatorios). 4. El sistema verifica la unicidad del nombre de usuario. 5. El sistema genera el hash de la contraseña y crea el `User`. 6. El sistema redirige a `/login` con un mensaje de éxito. |
| **Flujo Alternativo** | Si el nombre de usuario ya existe, el sistema muestra un error de validación y permanece en el formulario. |
| **Postcondiciones** | Existe un nuevo registro `User` con la contraseña en hash. |

</details>

<details>
<summary><strong>UC02 — Iniciar Sesión</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Registrado |
| **Descripción** | Un usuario registrado se autentica para acceder a rutas protegidas. |
| **Precondiciones** | El usuario tiene una cuenta registrada. |
| **Flujo Principal** | 1. El usuario abre `/login`. 2. Ingresa usuario y contraseña. 3. El sistema verifica el hash con Bcrypt. 4. El sistema almacena `user_id`/`username` en la sesión. 5. El sistema redirige a la página principal con un mensaje de bienvenida. |
| **Flujo Alternativo** | Si las credenciales son inválidas, el sistema muestra "Login falhou" y permanece en el formulario. |
| **Postcondiciones** | El usuario tiene una sesión activa y puede acceder a rutas protegidas. |

</details>

<details>
<summary><strong>UC03 — Cerrar Sesión</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado |
| **Descripción** | El usuario finaliza su sesión. |
| **Precondiciones** | El usuario está autenticado. |
| **Flujo Principal** | 1. El usuario hace clic en "Logout" (`/logout`). 2. El sistema elimina `user_id`/`username` de la sesión. 3. El sistema redirige a `/login` con un mensaje informativo. |
| **Postcondiciones** | La sesión ya no otorga acceso a rutas protegidas. |

</details>

<details>
<summary><strong>UC04 — Navegar por el Catálogo de Productos</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Visitante / Usuario Autenticado |
| **Descripción** | Cualquier persona puede ver la lista de productos disponibles. |
| **Precondiciones** | Ninguna. |
| **Flujo Principal** | 1. El usuario abre `/`. 2. El sistema consulta todos los registros `Produto`. 3. El sistema renderiza `index.html` con nombre, precio, descripción e imagen de cada producto. |
| **Postcondiciones** | El usuario puede ver todos los productos actualmente en el catálogo. |

</details>

<details>
<summary><strong>UC05 — Agregar Producto</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado (gestor) |
| **Descripción** | Un usuario autenticado registra un nuevo producto en el catálogo. |
| **Precondiciones** | El usuario está autenticado. |
| **Flujo Principal** | 1. El usuario abre `/adicionar_produto`. 2. Completa nombre, descripción, precio y (opcionalmente) una imagen. 3. El sistema valida el formulario. 4. Si se envía una imagen, el sistema la guarda en `static/uploads/` con un nombre de archivo aleatorio. 5. El sistema crea el registro `Produto` y redirige a `/` con un mensaje de éxito. |
| **Flujo Alternativo** | Si no se proporciona una imagen, `imagem` permanece `None`/predeterminada. |
| **Postcondiciones** | Existe un nuevo `Produto` y aparece en el catálogo. |

</details>

<details>
<summary><strong>UC06 — Editar Producto</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado (gestor) |
| **Descripción** | Un usuario autenticado actualiza los datos de un producto existente. |
| **Precondiciones** | El usuario está autenticado y el producto existe. |
| **Flujo Principal** | 1. El usuario abre `/editar_produto/<id>`. 2. El formulario se precompleta con los datos actuales. 3. El usuario edita los campos y/o sube una nueva imagen. 4. Si se envía una nueva imagen, el archivo de imagen anterior se elimina (a menos que sea `default.jpg`) y se reemplaza. 5. El sistema confirma los cambios y redirige a `/` con un mensaje de éxito. |
| **Postcondiciones** | El registro `Produto` refleja los valores actualizados. |

</details>

<details>
<summary><strong>UC07 — Eliminar Producto</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado (gestor) |
| **Descripción** | Un usuario autenticado elimina un producto del catálogo. |
| **Precondiciones** | El usuario está autenticado y el producto existe. |
| **Flujo Principal** | 1. El usuario activa `/excluir_produto/<id>`. 2. El sistema elimina el archivo de imagen asociado del disco (a menos que sea `default.jpg`). 3. El sistema elimina el registro `Produto`. 4. El sistema redirige a `/` con un mensaje de éxito. |
| **Postcondiciones** | El producto ya no aparece en el catálogo ni en ningún carrito. |

</details>

<details>
<summary><strong>UC08 — Agregar Producto al Carrito</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado |
| **Descripción** | Un usuario agrega un producto a su carrito personal. |
| **Precondiciones** | El usuario está autenticado y el producto existe. |
| **Flujo Principal** | 1. El usuario activa `/add_carrinho/<id>`. 2. El sistema verifica si ya existe un `CarrinhoItem` para ese usuario/producto. 3a. Si existe, incrementa `quantidade` en 1. 3b. Si no existe, crea un nuevo `CarrinhoItem` con `quantidade = 1`. 4. El sistema redirige a `/` con un mensaje de éxito. |
| **Postcondiciones** | El carrito contiene el producto con la cantidad actualizada. |

</details>

<details>
<summary><strong>UC09 — Ver / Actualizar Carrito</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado |
| **Descripción** | Un usuario visualiza su carrito y puede eliminar ítems. |
| **Precondiciones** | El usuario está autenticado. |
| **Flujo Principal** | 1. El usuario abre `/carrinho`. 2. El sistema carga todos los registros `CarrinhoItem` del usuario (con join a `Produto`). 3. El sistema calcula el subtotal por ítem y el total general. 4. El sistema renderiza `carrinho.html`. |
| **Flujo Alternativo** | El usuario activa `/remover_carrinho/<id>`; el sistema elimina el `CarrinhoItem` correspondiente y redirige de nuevo a `/carrinho` con un mensaje informativo. |
| **Postcondiciones** | La vista del carrito refleja los ítems y el total actuales. |

</details>

<details>
<summary><strong>UC10 — Finalizar Compra (Checkout)</strong></summary>

| Campo | Descripción |
|:------|:------------|
| **Actor** | Usuario Autenticado |
| **Descripción** | Un usuario finaliza la compra de los ítems en su carrito. |
| **Precondiciones** | El usuario está autenticado y el carrito no está vacío. |
| **Flujo Principal** | 1. El usuario abre `/checkout`. 2. El sistema muestra el resumen del pedido y un formulario con nombre completo y correo electrónico. 3. El usuario envía el formulario. 4. El sistema valida el formulario (CSRF + campos obligatorios). 5. El sistema elimina todos los registros `CarrinhoItem` del usuario. 6. El sistema redirige a `/pedido_sucesso`. |
| **Flujo Alternativo** | Si el carrito está vacío al abrir `/checkout`, el sistema redirige a `/` con un mensaje de advertencia. |
| **Postcondiciones** | El carrito del usuario está vacío y se muestra una página de confirmación de pedido. |

</details>

---

## 3. 🔗 Matriz de Trazabilidad de Requisitos

> 🚧 **En construcción.** Esta sección mapeará cada **RF / RNF / RN** de la [Sección 1](#1--requisitos) con los **Casos de Uso**, archivos de origen (rutas/models/templates) y casos de prueba que los implementan y verifican.

<details>
<summary>Estructura planificada</summary>

| Requisito | Caso(s) de Uso | Implementación | Prueba(s) |
|:----------|:----------------|:----------------|:----------|
| RF01 | UC01 | `app.py::register` | `test_app.py` |
| ... | ... | ... | ... |

</details>

---

## 4. 📄 Especificación de Requisitos de Software (SRS)

> 🚧 **En construcción.** Un documento SRS consolidado (estilo IEEE 830 / ISO 29148) que cubre alcance, descripción general, requisitos específicos, interfaces externas y restricciones — agregando las Secciones 1–3.

---

## 5. 🖼️ Diagramas UML & Estructurales

> 🚧 **En construcción.** Los diagramas se proporcionarán en Mermaid (renderizados en línea en GitHub):

<details>
<summary>Diagramas planificados</summary>

- [ ] Diagrama de Casos de Uso
- [ ] Diagrama de Clases
- [ ] Diagrama de Objetos
- [ ] Diagrama de Secuencia
- [ ] Diagrama de Comunicación (Colaboración)
- [ ] Diagrama de Actividades
- [ ] Diagrama de Máquina de Estados
- [ ] Diagrama de Componentes
- [ ] Diagrama de Implementación (Deployment)
- [ ] Diagrama de Paquetes
- [ ] Diagrama de Estructura Compuesta
- [ ] Diagrama de Visión General de Interacción
- [ ] Diagrama de Tiempo (Timing)

</details>

---

## 6. 🗄️ Modelo de Datos & Diccionario de Datos

> 🚧 **En construcción.** Amplía los [1.5 Requisitos de Datos](#15-requisitos-de-datos).

<details>
<summary>Contenido planificado</summary>

- [ ] Diagrama Entidad-Relación (DER)
- [ ] Modelo Conceptual de Datos
- [ ] Modelo Lógico de Datos
- [ ] Modelo Físico de Datos
- [ ] Diccionario de Datos completo (tabla/columna, tipo, restricciones, descripción)

</details>

---

## 7. 🌊 Diagrama de Flujo de Datos (DFD)

> 🚧 **En construcción.**

<details>
<summary>Contenido planificado</summary>

- [ ] Diagrama de Flujo de Datos (Niveles 0/1) — Usuario ↔ rutas Flask ↔ SQLite ↔ Almacenamiento de archivos
- [ ] Diagrama de Linaje de Datos — desde la entrada del formulario hasta los datos persistidos/derivados (p. ej., total del carrito)

</details>

---

## 8. 🏗️ Diagrama de Arquitectura & Diagrama de Flujo

> 🚧 **En construcción.**

<details>
<summary>Contenido planificado</summary>

- [ ] Diagrama de Arquitectura (visión general) — Navegador ↔ App Flask ↔ SQLAlchemy ↔ SQLite + static/uploads
- [ ] Diagrama de Flujo — flujo de decisión del checkout (¿carrito vacío? ¿formulario válido? página de éxito)

</details>

---

## 9. 🧑 Persona & Mapa de Viaje del Usuario

> 🚧 **En construcción.**

<details>
<summary>Contenido planificado</summary>

- [ ] Persona — p. ej., "María, dueña de una tienda local que gestiona su catálogo"
- [ ] Mapa de Viaje del Usuario — desde la llegada al catálogo hasta completar el checkout

</details>

---

## 10. 🎨 Wireframes & Mockups

> 🚧 **En construcción.**

<details>
<summary>Contenido planificado</summary>

- [ ] Wireframes — diseños de baja fidelidad para catálogo, carrito y checkout
- [ ] Mockups — visuales de alta fidelidad alineados con `static/style.css`

</details>

---

## 11. 🚀 Instalación & Ejecución

### Requisitos Previos

| Requisito | Detalle |
|:----------|:--------|
| **Python** | 3.10+ |
| **pip** | incluido con Python |
| **Git** | para clonar el repositorio |

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/VictorHJesusSantiago/lojinha_local.git
cd lojinha_local

# 2. Crear y activar el entorno virtual
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear la base de datos
flask shell -c "from app import db; db.create_all()"

# 5. Ejecutar la aplicación
flask run --debug
```

| Servicio | URL |
|:---------|:----|
| 🏠 Inicio (catálogo) | `http://localhost:5000` |
| 🔐 Iniciar sesión | `http://localhost:5000/login` |
| 📋 Registro | `http://localhost:5000/register` |
| ➕ Agregar Producto | `http://localhost:5000/adicionar_produto` |

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

*Hecho con 🛒 y Flask*

</div>
