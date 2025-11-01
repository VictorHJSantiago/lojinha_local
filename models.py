from extensions import db

class CarrinhoItem(db.Model):
    """ Novo Modelo para os Itens do Carrinho """
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)

    produto = db.relationship('Produto')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    carrinho_itens = db.relationship('CarrinhoItem', backref='user', lazy=True, cascade="all, delete-orphan")

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    preco = db.Column(db.Float, nullable=False)
    imagem = db.Column(db.String(300), nullable=True, default='default.jpg')