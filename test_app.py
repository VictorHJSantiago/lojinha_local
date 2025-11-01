import pytest
from app import app
from extensions import db
from models import User, Produto, CarrinhoItem 

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' 
    app.config['WTF_CSRF_ENABLED'] = False 
    app.config['SECRET_KEY'] = 'test_secret_key'

    with app.test_client() as client:
        with app.app_context():
            db.create_all() 
        yield client
        with app.app_context():
            db.drop_all()

def test_index_page(client):
    """Testa se a página inicial carrega."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Nossos Produtos" in response.data

def test_login_page(client):
    """Testa se a página de login carrega."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data

def test_register_page(client):
    """Testa se a página de registro carrega."""
    response = client.get('/register')
    assert response.status_code == 200
    assert b"Cadastro" in response.data

def test_user_registration(client):
    """Testa o registro de um novo usuário."""
    response = client.post('/register', data={
        'username': 'testuser',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Conta criada com sucesso!" in response.data
    
    with app.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user is not None

def test_user_login_logout(client):
    """Testa o login e logout de um usuário."""
    client.post('/register', data={
        'username': 'loginuser',
        'password': 'password123',
        'confirm_password': 'password123'
    })
    
    response = client.post('/login', data={
        'username': 'loginuser',
        'password': 'password123'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Bem-vindo, loginuser!" in response.data
    
    with client.session_transaction() as sess:
        assert sess['user_id'] is not None
        
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Voc\xc3\xaa saiu da sua conta." in response.data
    with client.session_transaction() as sess:
        assert 'user_id' not in sess

def login_test_user(client):
    """Função helper para logar um usuário de teste."""
    client.post('/register', data={
        'username': 'crud_user', 'password': 'password', 'confirm_password': 'password'
    })
    client.post('/login', data={'username': 'crud_user', 'password': 'password'})

def test_add_produto_requires_login(client):
    """Testa se a rota de adicionar produto redireciona se não estiver logado."""
    response = client.get('/adicionar_produto', follow_redirects=True)
    assert response.status_code == 200
    assert b"Por favor, fa\xc3\xa7a login" in response.data

def test_add_produto(client):
    """Testa adicionar um produto (Etapa 2) quando logado."""
    login_test_user(client)
    
    response = client.post('/adicionar_produto', data={
        'nome': 'Produto Teste',
        'descricao': 'Descricao Teste',
        'preco': 10.99
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Produto Teste" in response.data
    
    with app.app_context():
        produto = Produto.query.filter_by(nome='Produto Teste').first()
        assert produto is not None
        assert produto.preco == 10.99

def test_add_to_cart_database(client):
    """[CORREÇÃO] Testa adicionar um item ao carrinho (Etapa 3 - com BD)."""
    login_test_user(client)
    
    product_id = 0
    with app.app_context():
        produto = Produto(nome="Produto Carrinho", preco=50.0)
        db.session.add(produto)
        db.session.commit()
        product_id = produto.id 

    client.get(f'/add_carrinho/{product_id}', follow_redirects=True)
    
    with app.app_context():
        user = User.query.filter_by(username='crud_user').first()
        item = CarrinhoItem.query.filter_by(user_id=user.id, produto_id=product_id).first()
        
        assert item is not None
        assert item.quantidade == 1
        assert item.produto.nome == "Produto Carrinho"