import bcrypt
from app import db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):  # Herda UserMixin para ter métodos de login padrão
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)  

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')  # Esta é uma propriedade que não pode ser lida, é usada apenas para definir a senha.

    @password.setter
    def password(self, senha_texto):
        self.password_hash = bcrypt.hashpw(senha_texto.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verificar_senha(self, senha_texto):
        return bcrypt.checkpw(senha_texto.encode('utf-8'), self.password_hash.encode('utf-8'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))