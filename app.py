import os
import secrets
from flask import Flask, render_template, request, redirect, url_for, flash, session
from functools import wraps
from werkzeug.utils import secure_filename

from extensions import db, bcrypt
from models import User, Produto, CarrinhoItem
from forms import RegistrationForm, LoginForm, ProdutoForm, CheckoutForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'sua_chave_secreta_muito_segura'
app.instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lojinha.db'
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

os.makedirs(app.instance_path, exist_ok=True)
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)
bcrypt.init_app(app)

def save_picture(form_picture):
    """Salva a imagem de upload e retorna o nome do arquivo."""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_fn)
    form_picture.save(picture_path)
    return picture_fn

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Conta criada com sucesso! Faça o login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Bem-vindo, {user.username}!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login falhou. Verifique seu nome de usuário e senha.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('login'))

@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)

@app.route('/adicionar_produto', methods=['GET', 'POST'])
@login_required
def add_produto():
    form = ProdutoForm()
    if form.validate_on_submit():
        imagem_arquivo = None
        if form.imagem.data:
            imagem_arquivo = save_picture(form.imagem.data)
        
        novo_produto = Produto(
            nome=form.nome.data,
            descricao=form.descricao.data,
            preco=float(form.preco.data),
            imagem=imagem_arquivo
        )
        db.session.add(novo_produto)
        db.session.commit()
        flash('Produto adicionado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('adicionar_produto.html', form=form)

@app.route('/editar_produto/<int:id>', methods=['GET', 'POST'])
@login_required
def update_produto(id):
    produto = Produto.query.get_or_404(id)
    form = ProdutoForm(obj=produto)
    if form.validate_on_submit():
        if form.imagem.data:
            if produto.imagem and produto.imagem != 'default.jpg':
                old_image_path = os.path.join(app.config['UPLOAD_FOLDER'], produto.imagem)
                if os.path.exists(old_image_path):
                    os.remove(old_image_path)
            produto.imagem = save_picture(form.imagem.data)

        produto.nome = form.nome.data
        produto.descricao = form.descricao.data
        produto.preco = float(form.preco.data)
        
        db.session.commit()
        flash('Produto atualizado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    return render_template('editar_produto.html', form=form, produto=produto)

@app.route('/excluir_produto/<int:id>')
@login_required
def delete_produto(id):
    produto = Produto.query.get_or_404(id)
    if produto.imagem and produto.imagem != 'default.jpg':
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], produto.imagem)
        if os.path.exists(image_path):
            os.remove(image_path)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/add_carrinho/<int:id>')
@login_required
def add_to_cart(id):
    produto = Produto.query.get_or_404(id)
    user_id = session['user_id']
    item_existente = CarrinhoItem.query.filter_by(user_id=user_id, produto_id=produto.id).first()
    
    if item_existente:
        item_existente.quantidade += 1
    else:
        novo_item = CarrinhoItem(user_id=user_id, produto_id=produto.id, quantidade=1)
        db.session.add(novo_item)
    
    db.session.commit()
    flash(f'{produto.nome} adicionado ao carrinho!', 'success')
    return redirect(url_for('index'))

@app.route('/remover_carrinho/<int:id>')
@login_required
def remove_from_cart(id):
    user_id = session['user_id']
    item_para_remover = CarrinhoItem.query.filter_by(user_id=user_id, produto_id=id).first()
    
    if item_para_remover:
        db.session.delete(item_para_remover)
        db.session.commit()
        flash('Produto removido do carrinho.', 'info')
    else:
        flash('Item não encontrado no carrinho.', 'warning')
        
    return redirect(url_for('ver_carrinho'))

@app.route('/carrinho')
@login_required
def ver_carrinho():
    user_id = session['user_id']
    itens_carrinho = CarrinhoItem.query.filter_by(user_id=user_id).options(db.joinedload(CarrinhoItem.produto)).all()
    
    display_cart = {}
    total = 0
    
    for item in itens_carrinho:
        if item.produto:
            subtotal = item.produto.preco * item.quantidade
            display_cart[item.produto.id] = {
                'nome': item.produto.nome,
                'preco': item.produto.preco,
                'quantidade': item.quantidade,
                'subtotal': subtotal
            }
            total += subtotal
            
    return render_template('carrinho.html', display_cart=display_cart, total=total)

def get_cart_details():
    """[CORREÇÃO] Helper para buscar detalhes do carrinho do banco de dados."""
    user_id = session.get('user_id')
    if not user_id:
        return {}, 0

    itens_carrinho = CarrinhoItem.query.filter_by(user_id=user_id).options(db.joinedload(CarrinhoItem.produto)).all()
    display_order = {}
    total = 0

    for item in itens_carrinho:
        if item.produto:
            display_order[item.produto.id] = {
                'nome': item.produto.nome,
                'quantidade': item.quantidade
            }
            total += item.produto.preco * item.quantidade
            
    return display_order, total

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = CheckoutForm()
    display_order, total = get_cart_details()
    user_id = session['user_id']

    if not display_order:
        flash('Seu carrinho está vazio.', 'warning')
        return redirect(url_for('index'))

    if form.validate_on_submit():
        print(f"Pedido recebido de: {form.nomeCompleto.data} ({form.email.data})")
        CarrinhoItem.query.filter_by(user_id=user_id).delete()
        db.session.commit()

        return redirect(url_for('pedido_sucesso'))
    
    return render_template('checkout.html', form=form, display_order=display_order, total=total)

@app.route('/pedido_sucesso')
@login_required
def pedido_sucesso():
    return render_template('pedido_sucesso.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
