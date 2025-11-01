from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DecimalField, EmailField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional, NumberRange
from models import User 

class RegistrationForm(FlaskForm):
    username = StringField('Nome de Usuário', 
                           validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Senha', 
                                     validators=[DataRequired(), EqualTo('password', message='As senhas devem ser iguais.')])
    submit = SubmitField('Criar Conta')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Esse nome de usuário já existe. Por favor, escolha outro.')

class LoginForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')

class ProdutoForm(FlaskForm):
    nome = StringField('Nome do Produto', validators=[DataRequired(), Length(max=100)])
    descricao = TextAreaField('Descrição', validators=[Optional()])
    preco = DecimalField('Preço (R$)', validators=[DataRequired(), NumberRange(min=0.01)], places=2)
    imagem = FileField('Imagem do Produto (Opcional)', 
                       validators=[Optional(), FileAllowed(['jpg', 'png', 'jpeg'], 'Apenas imagens JPG, PNG e JPEG são permitidas!')])
    submit_add = SubmitField('Salvar Produto')
    submit_update = SubmitField('Atualizar Produto')


class CheckoutForm(FlaskForm):
    nomeCompleto = StringField('Nome Completo', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    endereco = StringField('Endereço', validators=[DataRequired(), Length(min=10)])
    submit = SubmitField('Confirmar Pedido')